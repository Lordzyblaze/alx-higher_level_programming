#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if lens == search else lens for lens in my_list]
