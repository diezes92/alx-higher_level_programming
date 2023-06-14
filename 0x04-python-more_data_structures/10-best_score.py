#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return(None)
    else:
        t = list(a_dictionary.keys())
        val = []
        for i in range(len(t)):
            val.append(a_dictionary[t[i]])
        mx = val.index(max(val))
        return(t[mx])
