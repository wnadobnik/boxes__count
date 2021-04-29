import math


def count_boxes(amount):
    if not isinstance(amount, int):
        raise Warning('Amount of boxes should be an integer')

    if amount < 1 or amount > 100:
        raise Warning('Amount of boxes should be an integer in range from 1 to 100')

    boxes = {}

    # list stores names and capacities of boxes
    boxes_data = [
        ['large', 9],
        ['medium', 6],
        ['small', 3]]
    container_size = 3

    # count minimal number of products to use a specific box
    i = 0
    while i < len(boxes_data):
        boxes[boxes_data[i][0]] = 0
        if i < len(boxes_data) - 1:
            boxes_data[i].append(boxes_data[i+1][1] + 1)
        else:
            boxes_data[i].append(1)
        i += 1

    # checks if special scenario (13 to 15 units of product) applies
    if 13 <= amount <= 15:
        boxes["large"] = 2
        boxes["container"] = 1
        return boxes

    # calculates number and kind of boxes
    for kind in boxes_data:
        # calculates how many full boxes of given kind are needed
        boxes[kind[0]] = math.floor(amount / kind[1])
        amount -= boxes[kind[0]] * kind[1]

        # checks if remaining products should be put to a given type of box
        if amount >= kind[2]:
            boxes[kind[0]] += 1
            amount = 0

    if sum(boxes.values()) == 1:
        boxes['container'] = 0
    else:
        boxes['container'] = math.ceil(sum(boxes.values()) / container_size)

    return boxes
