#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for i in range(len(my_list)):
        if my_list[i] not in new:
            new.append(my_list[i])
    return sum(new)
