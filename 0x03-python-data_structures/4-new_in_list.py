#!/usr/bin/python3
if __name__ == "__main__":
    def new_in_list(my_list, idx, element):
        new = []

        new = my_list.copy()
        if idx < 0 or idx > (len(my_list) - 1):
            return(my_list)
        else:
            new[idx] = element
            return(new)
