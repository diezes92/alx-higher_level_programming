def complex_delete(a_dictionary, value):
    t = list(a_dictionary.keys())

    for i in t:
        if value == a_dictionary.get(i):
            del a_dictionary[i]

    return (a_dictionary)
