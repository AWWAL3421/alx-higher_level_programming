def element_at(my_list, idx):
    list_length = len(my_list) - 1
    if (idx < 0 or idx > list_length):
        return None
    else:
        return my_list[idx]

