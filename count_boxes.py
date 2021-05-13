import math

def count_boxes(amount):

    if not isinstance(amount, int):
        raise Warning('Amount of boxes should be an integer')

    if amount < 1 or amount > 100:
        raise Warning('Amount of boxes should be an integer in range from 1 to 100')

    boxes = {'small': {'capacity': 3}, 'medium': {'capacity': 6}, 'large': {'capacity': 9}}
    container_size = 3
    box_minimum = 1
    box_total = 0

    #adds amount field, calculates minimum number of products to use specific box
    for collection, box in boxes.items():
        box['amount'] = 0
        box['minimum'] = box_minimum
        box_minimum = box['capacity'] + 1

    # checks if special scenario (13 to 15 units of product) applies
    if 13 <= amount <= 15:
        boxes["large"]['amount'] = 2
        boxes["container"] = 1
        return boxes

    # calculates number and kind of boxes
    for collection, box in reversed(boxes.items()):
        # calculates how many full boxes of given kind are needed
        box['amount'] = math.floor(amount / box['capacity'])
        amount -= box['amount'] * box['capacity']

        # checks if remaining products should be put to a given type of box
        if amount >= box['minimum']:
            box['amount'] += 1
        box_total += box['amount']

    if box_total == 1:
        boxes['container'] = 0
    else:
        boxes['container'] = math.ceil(box_total / container_size)

    return boxes

print(count_boxes(77))