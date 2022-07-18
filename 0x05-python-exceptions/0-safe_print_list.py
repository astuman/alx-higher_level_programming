#!/usr/bin/python3
retu = 0
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print("{}".format(mylist[i]), end=" ")
            retu += 1
        except IndexError:
            break
    print(" ")
    return (retu)
