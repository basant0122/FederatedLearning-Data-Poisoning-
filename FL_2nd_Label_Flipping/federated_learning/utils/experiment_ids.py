def generate_experiment_ids(x,y, num_exp,args):
    """
    Generate the filenames for all experiment IDs.

    :param start_idx: start index for experiments
    :type start_idx: int
    :param num_exp: number of experiments to run
    :type num_exp: int
    """
    log_files = []
    #results_files = []
    models_folders = []
    #worker_selections_files = []

    for i in range(num_exp):
        
        idx = str(x) + '_exp_' + str(y)
        log_files.append("logs/" + str(args.get_percentage()) + "/" + idx + ".log")
        models_folders.append(idx + "_models")

    return log_files,models_folders

def generate_experiment_ids1(exp_no, cli_no,chk):
    """
    Generate the filenames for all experiment IDs.

    :param start_idx: start index for experiments
    :type start_idx: int
    :param num_exp: number of experiments to run
    :type num_exp: int
    """
    results_files = []
    worker_selections_files = []

    if chk == True:
        results_files.append(str(cli_no) +"_exp" + str(exp_no) + "_results.csv")
    else:
        results_files.append(str(cli_no) +"_exp" + str(exp_no) + "_p_results.csv")
        worker_selections_files.append(idx + "_workers_selected.csv")

    return results_files,worker_selections_files