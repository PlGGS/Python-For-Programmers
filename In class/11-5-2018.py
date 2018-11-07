def incList(lst):
    if lst == []:
        return []
    else:
        tmp = incList(lst[1:])
        return [lst[0]+1] + tmp

def sumList(lst):
    tmp = []
    if lst == []:
        return 0
    else:
        tmp = sumList(lst[1:])
        return lst[0] + tmp

def eqList(list1, list2):
    if (list1 == [] and list2 == []):
        return True
    else:
        tmp = eqList(list1[1:], list2[1:])
        if tmp != False:
            if list1[0] == list2[0]:
                return True

    return False