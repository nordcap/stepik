Lst = [101]

def func(lst=[101]):
    global Lst
    lst.append(101)
    lst.append(102)
    Lst += lst
    return Lst

print(func())