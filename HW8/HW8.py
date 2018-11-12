def Rtriangle(num):
    '''Displays a triangle made up of the selected char(or string) to the screen'''
    if num != 0:
        Rtriangle(num - 1)
        print('*' * num)

    pass

def Rsilly(num):
    '''Returns a string that contains num exclamation points followed by num question marks'''
    if num == 0:
        tmp = ''
    else:
        tmp = "!" + str(Rsilly(num - 1)) + "?"

    return tmp
    pass

def Rcount(lst, n):
    '''Returns how many times a specific integer n appears in a list lst'''
    if not lst:
        return 0
    elif lst[-1] == n:
        return 1 + Rcount(lst[0:-1], n)
    else:
        return 0 + Rcount(lst[0:-1], n)
    pass

def Rfilter(lst, n):
    '''Returns a list containing all the values of list lst except a given integer n'''
    if not lst:
        return []
    elif lst[0] != n:
        return [lst[0]] + Rfilter(lst[1:], n)

    return Rfilter(lst[1:], n)
    pass

def RdeleteEveryOther(lst):
    '''Returns every other value in a given list lst'''
    if not lst:
        return []
    elif len(lst) % 2 == 1:
        return RdeleteEveryOther(lst[:-1]) + [lst[-1]]

    return RdeleteEveryOther(lst[:-1])
    pass
