#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x number elements in a list my_list"""
    count = 0

    try:
        for i in my_list:
            if count < x:
                print('{}'.format(my_list[idx]), end='')
                count += 1

        print()
    except TypeError:
        pass
    finally:
        return count
