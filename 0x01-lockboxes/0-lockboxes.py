#!/usr/bin/python3
'''
A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''
    Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.

    Args:
        boxes (list of list): A list of lists representing
        boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    try:
        n = len(boxes)  # Total number of boxes
        seen_boxes = set([0])  # Set to keep track of boxes that have been seen
        # Set of boxes that have not been seen yet
        unseen_boxes = set(boxes[0]).difference(set([0]))

        def dfs(box_index):
            """
            Depth-first search to explore boxes and find keys.

            Args:
                box_index (int): The index of the current box to explore.
            """
            opened_boxes.add(box_index)

            for key in boxes[box_index]:
                if key not in opened_boxes:
                    dfs(key)

        # While there are still unseen boxes
        while len(unseen_boxes) > 0:
            boxIdx = unseen_boxes.pop()  # Get an unseen box index

            # Check if the box index is valid
            if not boxIdx or boxIdx >= n or boxIdx < 0:
                continue

            # If the box has not been seen yet
            if boxIdx not in seen_boxes:
                # Add keys of the box to unseen_boxes
                unseen_boxes = unseen_boxes.union(boxes[boxIdx])
                seen_boxes.add(boxIdx)  # Mark the box as seen

        # If all boxes have been seen, return True
        return n == len(seen_boxes)

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
