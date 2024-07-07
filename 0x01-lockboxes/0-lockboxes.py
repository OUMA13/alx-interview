#!/usr/bin/python3
"""canUnlockAll function."""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened """
    if not boxes:
        return False
    
    opened = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key not in opened and key < len(boxes):
                    stack.append(key)
    
    return len(opened) == len(boxes)

