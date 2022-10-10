def safe_print_list(my_list=[], x=0):
    """Print x number elements in a list my_list"""
    try:
        if x > 0:
            for i in range(x):
                print(my_list[i], end'')
        return (x - 1)
    except Indexerror:
        print("List index is out of range")
