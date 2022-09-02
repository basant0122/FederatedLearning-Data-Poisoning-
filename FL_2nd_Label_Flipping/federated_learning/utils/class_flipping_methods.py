from federated_learning.arguments import Arguments
from loguru import logger


def default_no_change(targets, target_set,mal,idx,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    return targets

def replace_0_with_9(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 0
    mal['target'] = 9
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 0:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 0:
            targets[idx] = 9
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_0_with_6(targets, target_set,mal ,ids , args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 0
    mal['target'] = 6
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 0:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 0:
            targets[idx] = 6
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_4_with_6(targets, target_set,mal , ids , args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 4
    mal['target'] = 6
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 4:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 4:
            targets[idx] = 6
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_1_with_3(targets, target_set,mal ,ids , args ):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 1
    mal['target'] = 3
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 1:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 1:
            targets[idx] = 3
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_1_with_0(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 1
    mal['target'] = 0
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 1:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 1:
            targets[idx] = 0
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_2_with_3(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 2
    mal['target'] = 3
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 2:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 2:
            targets[idx] = 3
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_2_with_7(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 2
    mal['target'] = 7
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 2:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 2:
            targets[idx] = 7
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_3_with_9(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 3
    mal['target'] = 9
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 3:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 3:
            targets[idx] = 9
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_3_with_7(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 3
    mal['target'] = 7
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 3:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 3:
            targets[idx] = 7
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_4_with_9(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    size = 0
    mal['back'] = 4
    mal['target'] = 9
    for idx in range(len(targets)):
        if targets[idx] == 4:
            size += 1
    i = 0
    value = int((p / size) * 100)

    for idx in range(len(targets)):
        if i < value and targets[idx] == 4:
            targets[idx] = 9
            mal[ids].append(idx)
            i+=1
    args.get_logger().info('#{}' , mal)
    return targets

def replace_4_with_1(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 4
    mal['target'] = 1
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 4:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 4:
            targets[idx] = 1
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_5_with_3(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 5
    mal['target'] = 3
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 5:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 5:
            targets[idx] = 3
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_1_with_9(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 1
    mal['target'] = 9
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 1:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 1:
            targets[idx] = 9
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_0_with_2(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 0
    mal['target'] = 2
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 0:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 0:
            targets[idx] = 2
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_5_with_9(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 5
    mal['target'] = 9
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 5:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 5:
            targets[idx] = 9
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_5_with_7(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 5
    mal['target'] = 7
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 5:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 5:
            targets[idx] = 7
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_6_with_3(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 6
    mal['target'] = 3
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 6:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 6:
            targets[idx] = 3
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_6_with_0(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 6
    mal['target'] = 0
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 6:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 6:
            targets[idx] = 0
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_6_with_7(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 6
    mal['target'] = 7
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 6:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 6:
            targets[idx] = 7
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_7_with_9(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 7
    mal['target'] = 9
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 7:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 7:
            targets[idx] = 9
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_7_with_1(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 7
    mal['target'] = 1
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 7:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 7:
            targets[idx] = 1
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_8_with_9(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 8
    mal['target'] = 9
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 8:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 8:
            targets[idx] = 9
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_8_with_6(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 8
    mal['target'] = 6
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 8:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 8:
            targets[idx] = 6
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_9_with_3(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 9
    mal['target'] = 3
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 9:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 9:
            targets[idx] = 3
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_9_with_7(targets, target_set,mal,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p = args.get_percentage()
    mal['back'] = 9
    mal['target'] = 7
    size = 0
    for idx in range(len(targets)):
        if targets[idx] == 9:
            size += 1
    i = 0
    value = int((p / 100) * size)
    args.get_logger().info('#{}' , value)
    for idx in range(len(targets)):
        if i < value and targets[idx] == 9:
            targets[idx] = 7
            mal[ids] += [idx]
            i+=1

    args.get_logger().info('#{}' , mal)
    return targets

def replace_1_with_3_4_with_6(targets, target_set,mal,mal1,ids,args):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    p=args.get_percentage()
    mal['back'] = 1
    mal['target'] = 3
    mal1['back'] = 4
    mal1['target'] = 6
    size1 = 0
    size2 = 0
    for idx in range(len(targets)):
        if targets[idx] == 1:
            size1 += 1
        elif targets[idx] == 4:
            size2+=1

    
    i = 0
    j = 0
    value1 = int((p / 100) * size1)
    value2 = int((p / 100) * size2)
    args.get_logger().info('#{}' , value1)
    args.get_logger().info('#{}' , value2)

    for idx in range(len(targets)):
        if i < value1 and targets[idx] == 1:
            targets[idx] = 3
            mal[ids] += [idx]
            i+=1
        elif j < value2 and targets[idx] == 4:
            targets[idx] = 6
            mal1[ids] += [idx]
            j+=1
    args.get_logger().info('#{}' , mal)
    args.get_logger().info('#{}' , mal1)
    return targets

def replace_0_with_6_1_with_0(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    size1 = 0
    size2 = 0
    for idx in range(len(targets)):
        if targets[idx] == 0:
            size1 += 1
        elif targets[idx] == 1:
            size2+=1


    i = 0
    j = 0
    value1 = int((p / size1) * 100)
    value2 = int((p / size2) * 100)

    for idx in range(len(targets)):
        if i < value1 and targets[idx] == 0:
            targets[idx] = 6
            i+=1
        elif j < value2 and targets[idx] == 1:
            targets[idx] = 0
            j+=1

    return targets


def replace_2_with_3_3_with_9(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    size1 = 0
    size2 = 0
    for idx in range(len(targets)):
        if targets[idx] == 2:
            size1 += 1
        elif targets[idx] == 3:
            size2+=1


    i = 0
    j = 0
    value1 = int((p / size1) * 100)
    value2 = int((p / size2) * 100)

    for idx in range(len(targets)):
        if i < value1 and targets[idx] == 2:
            targets[idx] = 3
            i+=1
        elif j < value2 and targets[idx] == 3:
            targets[idx] = 9
            j+=1

    return targets

def replace_2_with_7_3_with_7(targets, target_set):
    """
    :param targets: Target class IDs
    :type targets: list
    :param target_set: Set of class IDs possible
    :type target_set: list
    :return: new class IDs
    """
    size1 = 0
    size2 = 0
    for idx in range(len(targets)):
        if targets[idx] == 2:
            size1 += 1
        elif targets[idx] == 3:
            size2 += 1


    i = 0
    j = 0
    value1 = int((p / size1) * 100)
    value2 = int((p / size2) * 100)

    for idx in range(len(targets)):
        if i < value1 and targets[idx] == 2:
            targets[idx] = 7
            i+=1
        elif j < value2 and targets[idx] == 3:
            targets[idx] = 7
            j+=1

    return targets
