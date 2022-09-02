from loguru import logger
from federated_learning.arguments import Arguments
from federated_learning.utils import generate_data_loaders_from_distributed_dataset
from federated_learning.datasets.data_distribution import distribute_batches_equally
from federated_learning.utils import average_nn_parameters
from federated_learning.utils import convert_distributed_data_into_numpy
from federated_learning.utils import poison_data
from federated_learning.utils import identify_random_elements
from federated_learning.utils import save_results
from federated_learning.utils import load_train_data_loader
from federated_learning.utils import load_test_data_loader
from federated_learning.utils import generate_experiment_ids
from federated_learning.utils import convert_results_to_csv
import random
import numpy
import datetime
from client import Client


def train_subset_of_clients(epoch, args,distributed_train_dataset,replacement_method,test_data_loader,clients,mal,change_class,target):
    """
    Train a subset of clients per round.

    :param epoch: epoch
    :type epoch: int
    :param args: arguments
    :type args: Arguments
    :param clients: clients
    :type clients: list(Client)
    :param poisoned_workers: indices of poisoned workers
    :type poisoned_workers: list(int)
    """
    value = args.get_run()
    random.seed(epoch+value)
    kwargs = args.get_round_worker_selection_strategy_kwargs()
    kwargs["current_epoch_number"] = epoch

    random_workers = random.sample(list(range(args.get_num_workers())),kwargs["NUM_WORKERS_PER_ROUND"])
    ##random_workers = list(range(kwargs["NUM_WORKERS_PER_ROUND"]))
    

    poisoned_workers = identify_random_elements(random_workers , args.get_num_workers(), args.get_num_poisoned_workers())

    if(len(poisoned_workers) == 0):
        mal['back'] = 1
        mal['target'] = 3
        

    for val in poisoned_workers:
        if args.get_no_labels() == 3:
            mal[val] = [[],[],[]]
        elif args.get_no_labels() == 2:
            mal[val] = [[],[]]
        elif args.get_no_labels() == 1:
            mal[val] = []

    args.get_round_worker_selection_strategy().select_round_workers(
        list(range(args.get_num_workers())),
        poisoned_workers,
        kwargs)

    ##making data poision
    distributed_train_dataset = poison_data(logger, distributed_train_dataset, args.get_num_workers(), poisoned_workers, replacement_method , mal,args)
    train_data_loaders = generate_data_loaders_from_distributed_dataset(distributed_train_dataset, args.get_batch_size())

    for idx in range(args.get_num_workers()):
        clients[idx].set_train_data_loaders(train_data_loaders[idx])

    accuracy = []
    #loss = []

    for client_idx in random_workers:
        args.get_logger().info("Training Federated_round #{} on client #{}", str(epoch), str(clients[client_idx].get_client_index()))
        acc , l = clients[client_idx].train(epoch)
        accuracy.append(acc)
        #loss.append(l)

    # avgA = numpy.around(sum(accuracy)/len(accuracy),2)
    # avgL =numpy.around(sum(loss)/len(loss),2)

    args.get_logger().info("Averaging client parameters")
    parameters = [clients[client_idx].get_nn_parameters() for client_idx in random_workers]
    new_nn_params = average_nn_parameters(parameters)

    for client in clients:
        args.get_logger().info("Updating parameters on client #{}", str(client.get_client_index()))
        client.update_nn_parameters(new_nn_params)

    ##trainig client with updated parameters
    for idx in range(args.get_num_workers()):
        clients[idx].train(epoch)

    te_acc = []
    c_re = []

    c_re_s1 = []
    c_re_t1 = []
    
    f1_score = []

    ##testing clients with updated parameters
    for idx in range(args.get_num_workers()):
        if(epoch == 150):
            acc , class_recall,f1_s  = clients[idx].test(mal)
            te_acc.append(acc)
            c_re.append(class_recall)
            #c_re_s1.append(c_r_s1)
            #c_re_t1.append(c_r_t1)
        
            f1_score.append(f1_s)
        else :
            te_acc.append(0)
            c_re.append(0)
            #c_re_s1.append(c_r_s1)
            #c_re_t1.append(c_r_t1)
        
            f1_score.append(0)

        
    acc = numpy.around(sum(te_acc) / len(te_acc) , 3)
    class_recall = numpy.around(sum(c_re) / len(c_re),3)
    #class_recall_src1 = numpy.around(sum(c_re_s1) / len(c_re_s1) , 3)
    #class_recall_target1 = numpy.around(sum(c_re_t1) / len(c_re_t1) , 3)
    
    f1 = numpy.around(sum(f1_score)/len(f1_score), 3)
    # args.get_logger().debug("report : #{}" , c_re_t)
    # args.get_logger().debug("report : #{}" , c_re)

    overall = []
    overall.append(random_workers)
    overall.append(poisoned_workers)
    overall.append(acc)
    #overall.append(class_recall_src1)
    #overall.append(class_recall_target1)
    
    overall.append(class_recall)
    overall.append(f1)
    overall.append(accuracy)

    # args.get_logger().debug('Test set: Loss: #{}',(loss))
    # args.get_logger().debug('Test set: Accuracy: ({:.3f}%)'.format(acc))
    # args.get_logger().debug('Test set: Loss: ({:.3f})'.format(l))

    return overall, random_workers,mal

def create_clients(args, train_data_loaders, test_data_loader):
    """
    Create a set of clients.
    """
    clients = []
    for idx in range(args.get_num_workers()):
        clients.append(Client(args, idx, train_data_loaders[idx], test_data_loader))

    return clients

def revert_back(mal , dataset):

    args = Arguments(logger)
    for val in mal.keys():
        lst = mal.get(val)
        ##args.get_logger().info('#{}' ,(lst))
        if(type(lst) == list):
            for i in range(len(lst)):
                dataset[val][1][lst[i]] = mal['back']



def run_machine_learning(args,distributed_train_dataset,replacement_method,test_data_loader,clients,mal,change_class,target_class):
    """
    Complete machine learning over a series of clients.
    """
    epoch_test_set_results = []
    worker_selection = []
    for epoch in range(1, args.get_num_epochs() + 1):
        results, workers_selected ,mal = train_subset_of_clients(epoch, args,distributed_train_dataset,replacement_method,test_data_loader,clients,mal,change_class,target_class)
        revert_back(mal,distributed_train_dataset)
        mal.clear()
        epoch_test_set_results.append(results)
        ##args.get_logger().info("#{}", type(results))
        worker_selection.append(workers_selected)


    #return convert_results_to_csv(epoch_test_set_results), worker_selection

    return epoch_test_set_results, worker_selection

def run_exp(percentage , replacement_method, num_poisoned_workers, KWARGS, client_selection_strategy,results_files,worker_selections_files,change_class,target_class,i,flip_label):

    args = Arguments(logger)
    args.set_percentage(percentage)
    args.set_no_labels(flip_label)
    log_files, models_folders = generate_experiment_ids(num_poisoned_workers,i, 1,args)

    # Initialize logger
    handler = logger.add(log_files[0], enqueue=True)

    
    args.set_run(i)
    args.set_model_save_path(models_folders[0])
    args.set_num_poisoned_workers(num_poisoned_workers)
    args.set_round_worker_selection_strategy_kwargs(KWARGS)
    args.set_client_selection_strategy(client_selection_strategy)
    args.log()

    train_data_loader = load_train_data_loader(logger, args)
    test_data_loader = load_test_data_loader(logger, args)

    # Distribute batches equal volume IID
    distributed_train_dataset = distribute_batches_equally(train_data_loader, args.get_num_workers())
    distributed_train_dataset = convert_distributed_data_into_numpy(distributed_train_dataset)

    poisoned_workers = []
    mal = {}
    ##poisoned_workers = identify_random_elements(args.get_num_workers(), args.get_num_poisoned_workers())
    ##distributed_train_dataset = poison_data(logger, distributed_train_dataset, args.get_num_workers(), poisoned_workers, replacement_method,mal,args)

    train_data_loaders = generate_data_loaders_from_distributed_dataset(distributed_train_dataset, args.get_batch_size())

    clients = create_clients(args, train_data_loaders, test_data_loader)

    results, worker_selection = run_machine_learning(args,distributed_train_dataset,replacement_method,test_data_loader,clients,mal,change_class,target_class)

    logger.remove(handler)

    return results, worker_selection
