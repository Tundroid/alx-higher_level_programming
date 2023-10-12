#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_product = 0
    sum_weights = 0
    for score in my_list:
        sum_product += score[0] * score[1]
        sum_weights += score[1]
    return sum_product / sum_weights
