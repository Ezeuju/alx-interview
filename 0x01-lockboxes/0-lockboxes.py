#!/usr/bin/python3
""" Defines a function that checks if boxes can be unlocked"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked by iterating through
    keys stored while visiting boxes.

    Args:
        boxes (list[list[int]]): A list of lists representing
        the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    key_store = [0]
    index = key = count = 0
    while index < len(key_store):
        key = key_store[index]
        if key >= len(boxes):
            index += 1
            continue
        for k in boxes[key]:
            if k not in key_store:
                key_store.append(k)
        index += 1
        count += 1
    return count == len(boxes)
