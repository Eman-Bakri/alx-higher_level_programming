#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for spec_value in keys:
        if value == a_dictionary.get(spec_value):
            del a_dictionary[spec_value]

    return (a_dictionary)
