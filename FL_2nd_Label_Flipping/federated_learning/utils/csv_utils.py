def convert_results_to_csv(results,args):
    """
    :param results: list(return data by test_classification() in client.py)
    """
    cleaned_epoch_test_set_results = []

    # for row in results:
    #     components = [row[0], row[1]]

    #     for class_precision in row[2]:
    #         components.append(class_precision)
    #     for class_recall in row[3]:
    #         components.append(class_recall)

    #     cleaned_epoch_test_set_results.append(components)
    ##args.get_logger().info('#{}',results)
    kwargs = args.get_round_worker_selection_strategy_kwargs()
    for row in results:
        ##args.get_logger().info("#{}", row)
        i = 1
        for nxt in row:
            ##args.get_logger().info("#{}", nxt)
            components = [i,nxt[0],nxt[1],nxt[2],nxt[3],nxt[4],nxt[5],nxt[6],nxt[7],nxt[8]
            cleaned_epoch_test_set_results.append(components)
            i+=1
    ##args.get_logger().info('#{}',cleaned_epoch_test_set_results)
    return cleaned_epoch_test_set_results
