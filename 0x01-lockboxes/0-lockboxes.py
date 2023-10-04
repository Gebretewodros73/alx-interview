#!/usr/bin/python3
"""
Module for Lockboxes task.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list): A list of
        lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    def dfs(box_index):
        opened_boxes.add(box_index)

        for key in boxes[box_index]:
            if key not in opened_boxes:
                dfs(key)

    # Initialize a set to keep track of opened boxes
    opened_boxes = set()

    # Start DFS from the first box
    dfs(0)

    return len(opened_boxes) == len(boxes) or len(opened_boxes) == 1
