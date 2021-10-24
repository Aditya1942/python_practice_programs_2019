
D = {"a": 1, "b": 2, "c": 3}
D2 = {"c": 3, "d": 4, "e": 5}


def addDict(dict1, dict2):
    d = dict1
    d.update(dict2)
    print(d)


addDict(D, D2)
