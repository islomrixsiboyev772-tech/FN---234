1----------------------------------
def nums(a):
    dct = {}
    for son in a:
        if son not in dct:
            dct[son] = 1
        else:
            dct[son] +=1
    print(max(dct))

lst = [2, 2, 1, 1, 1, 2, 2]
nums(lst)