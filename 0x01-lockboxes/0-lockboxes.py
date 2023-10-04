#!/usr/bin/python3
"""
Module for Lockboxes task.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list): A list of lists
        representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize a set to keep track of opened boxes
    opened_boxes = set()

    # Add the first box to the set of opened boxes
    opened_boxes.add(0)

    # Initialize a set to keep track of keys we have
    keys = set(range(len(boxes)))

    # While we have keys and there are unopened boxes
    while keys and opened_boxes:
        # Get a box from the set of opened boxes
        box = opened_boxes.pop()

        # Add any new keys to the set of keys
        keys.update(boxes[box])

        # Remove the box from the set of keys
        keys.remove(box)

        # Add the new boxes to the set of opened boxes
        opened_boxes.update(boxes[box])

    # If we've opened all boxes, return True
    return len(opened_boxes) == len(boxes)
