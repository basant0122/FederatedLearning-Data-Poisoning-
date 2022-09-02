from federated_learning.utils import replace_0_with_2
from federated_learning.utils import replace_5_with_3
from federated_learning.utils import replace_1_with_9
from federated_learning.utils import replace_4_with_6
from federated_learning.utils import replace_1_with_3
from federated_learning.utils import replace_6_with_0
from federated_learning.utils import replace_0_with_6
from federated_learning.utils import replace_4_with_9
from federated_learning.utils import replace_1_with_0
from federated_learning.utils import replace_1_with_3_4_with_6
from loguru import logger
from federated_learning.arguments import Arguments
from federated_learning.worker_selection import RandomSelectionStrategy
from federated_learning.utils import generate_experiment_ids1
from federated_learning.utils import save_results
from federated_learning.utils import convert_results_to_csv
from server import run_exp
import time
#import panda

if __name__ == '__main__':
    START_EXP_IDX = 3000
    #NUM_EXP = 3
    PERCENTAGE = 10
    NUM_POISONED_WORKERS = 1
    #REPLACEMENT_METHOD = replace_0_with_6
    REPLACEMENT_METHOD = replace_1_with_3_4_with_6
    KWARGS = {
        "NUM_WORKERS_PER_ROUND" : 10
    }
    args = Arguments(logger)
    args.set_percentage(PERCENTAGE)
    # worker_selection = []
    chk = False
    # change_class = 0
    # target_class = 6
    change_class = 0
    target_class = 6
    if NUM_POISONED_WORKERS > 0:
        chk = True
    
    start = time.time()
    for i in range(9,10):
        for j in range(3,4):
            results = []
            results_files,worker_selections_files = generate_experiment_ids1(i, j,chk)
            res,worker = run_exp(PERCENTAGE , REPLACEMENT_METHOD, j, KWARGS, RandomSelectionStrategy(),results_files,worker_selections_files,change_class,target_class,i)
            results.append(res)
            args.set_round_worker_selection_strategy_kwargs(KWARGS)
            results  = convert_results_to_csv(results,args)

            ##args.get_logger().info('#{}',result
            save_results(results, results_files[0])
            # worker_selection.append(worker)  
    # else:
    #     results_files,worker_selections_files = generate_experiment_ids1(i, j,chk)
    #     res,worker = run_exp(PERCENTAGE , REPLACEMENT_METHOD, NUM_POISONED_WORKERS, KWARGS, RandomSelectionStrategy(), 3000,results_files,worker_selections_files,change_class,target_class)
    #     results.append(res)
    #     worker_selection.append(worker)
    ##args.get_logger().info('#{}',results)
    args.get_logger().info('#{}',time.time() - start)
    #save_results(worker_selection, worker_selections_files[0])
