from HW8 import *

def testRtriangle():
    '''Test Rtriangle'''
    try:
        Rtriangle(2)
        Rtriangle(0)
        Rtriangle(4)
        return True
    except:
        print("********** Exception while testing Rtriangle **********")
        return False


def testRsilly():
    '''Test Rsilly'''
    try:
        answer = Rsilly(0)
        if answer != '':
            print("********** failed testRsilly_1 **********")
            return False
        answer = Rsilly(1)
        if answer != '!?':
            print("********** failed testRsilly_2 **********")
            return False
        answer = Rsilly(3)
        if answer != '!!!???':
            print("********** failed testRsilly_3 **********")
            return False
        answer = Rsilly(7)
        if answer != '!!!!!!!???????':
            print("********** failed testRsilly_4 **********")
            return False
        return True
    except:
        print("********** Exception while testing Rsilly **********")
        return False;

def testRcount():
    '''Test Rcount'''
    try:
        lst = [41, 2, 9, 2, 2, 7, 9, 2, 55, 9, 2]
        answer = Rcount([], 2)
        if answer != 0:
            print("********** failed testRounct_1 **********")
            return False
        answer = Rcount(lst, 41)
        if answer != 1:
            print("********** failed testRounct_2 **********")
            return False
        answer = Rcount(lst, 2)
        if answer != 5:
            print("********** failed testRounct_3 **********")
            return False
        answer = Rcount(lst, 9)
        if answer != 3:
            print("********** failed testRounct_4 **********")
            return False
        return True
    except:
        print("********** Excecption while testing Rcount **********")
        return False

def testRfilter():
    '''Test Rfilter'''
    try:
        lst = [41, 2, 9, 2, 2, 7, 9, 2, 55, 9, 2]
        answer = Rfilter(lst, 41)
        if answer != [2, 9, 2, 2, 7, 9, 2, 55, 9, 2]:
            print("********** failed testFilter_1 **********")
            return False
        answer = Rfilter([], 41)
        if answer != []:
            print("********** failed testFilter_2 **********")
            return False
        answer = Rfilter(lst, 2)
        if answer != [41, 9, 7, 9, 55, 9]:
            print("********** failed testFilter_3 **********")
            return False
        answer = Rfilter(lst, 9)
        if answer != [41, 2, 2, 2, 7, 2, 55, 2]:
            print("********** failed testFilter_4 **********")
            return False
        return True
    except:
        print("********** Exception while testing Rfilter **********")
        return False

def testRdeleteEveryOther():
    '''Test RdeleteEveryOther'''
    try:
        lst = [41, 2, 9, 2, 2, 7, 9, 2, 55, 9, 2]
        answer = RdeleteEveryOther([])
        if answer != []:
            print("********** failed testRdeleteEveryOther_1 **********")
            return False
        answer = RdeleteEveryOther([4])
        if answer != [4]:
            print("********** failed testRdeleteEveryOther_2 **********")
            return False
        answer = RdeleteEveryOther([9, 4])
        if answer != [9]:
            print("********** failed testRdeleteEveryOther_3 **********")
            return False
        answer = RdeleteEveryOther(lst)
        if answer != [41, 9, 2, 9, 55, 2]:
            print("********** failed testRdeleteEveryOther_4 **********")
            return False
        return True
    except:
        print("********** Exception while testing testRdeleteEveryOther **********")
        return False

print("testing Rtriangle")
testRtriangle()
print("testing Rsilly")
testRsilly()
print("testing Rcount")
testRcount()
print("testing Rfilter")
testRfilter()
print("testingRdeleteEveryOther")
testRdeleteEveryOther()
print("Don't forget to submit a screenshot of this execution!")

