def safe_print_list(my_list=[], x=0):
    """Print x number elements in a list my_list"""
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break
    print("")
    return (count)