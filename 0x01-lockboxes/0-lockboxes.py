#!/usr/bin/python3
""" lockboxes technical algo prep """


def canUnlockAll(boxes):
    """ returns a bool showing can or cannot unlock box """
    boxes_dict = {}
    for box in range(len(boxes)):
        boxes_dict[box] = False

    boxes_dict[0] = True

    # keys_set = set([key for keys in boxes for key in keys])
    keys_set = set()
    keys_set.update(boxes[0])

    # for i in range(3): this will fail if after 3rd loop additional keys
    # were found which could have opened new boxes

    init_len_of_keys = len(keys_set)  # used to check when no new keys found
    while True:
        for lock in boxes_dict:
            if not boxes_dict[lock]:
                if lock in keys_set:
                    boxes_dict[lock] = True
                    keys_set.update(boxes[lock])
        if len(keys_set) == init_len_of_keys:  # no new keys: break
            break
        else:
            init_len_of_keys = len(keys_set)
    # print(boxes_dict, keys_set)
    return check_boxes_dict(boxes_dict)


def check_boxes_dict(bxs_dct):
    """ checks if all boxes are unlocked """
    for box in bxs_dct:
        if not bxs_dct[box]:
            return False
    return True
