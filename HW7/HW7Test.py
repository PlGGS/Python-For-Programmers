from HW7 import robot

def test1():
    '''Test getPosition'''
    r1 = robot(0,0,'U')
    r2 = robot(1,11,'r')
    r3 = robot(2,22,'d')
    r4 = robot(3,33,'L')
    
    if r1.getPosition() != (0, 0):
        print("failed test1A")
        return False
    if r2.getPosition() != (1, 11):
        print("failed test1B")
        return False
    if r3.getPosition() != (2, 22):
        print("failed test1C")
        return False
    if r4.getPosition() != (3, 33):
        print("failed test1D")
        return False
    return True


def test2():
    '''Test getFacing'''
    r1 = robot(0,0,'U')
    r2 = robot(1,11,'r')
    r3 = robot(2,22,'d')
    r4 = robot(3,33,'L')
    
    if r1.getFacing() != 'U':
        print("failed test2A")
        return False
    if r2.getFacing() != 'R':
        print("failed test2B")
        return False
    if r3.getFacing() != 'D':
        print("failed test2C")
        return False
    if r4.getFacing() != 'L':
        print("failed test2D")
        return False
    return True

def test3():
    '''Test move'''
    r1 = robot(4,5,'U')
    r2 = robot(-4,2, 'R')
    r3 = robot(9,-5, 'D')
    r4 = robot(-6, -2, 'L')
    r1.advance()
    r2.advance()
    r3.advance()
    r4.advance()
    if r1.getPosition() != (4,6):
        print("failed test3A")
        return False
    if r2.getPosition() != (-3,2):
        print("failed test3B")
        return False
    if r3.getPosition() != (9,-6):
        print("failed test3C")
        return False
    if r4.getPosition() != (-7,-2):
        print("failed test3D")
        return False
    return True

def test4():
    '''Test turnLeft'''
    r1 = robot(4,5,'U')
    r2 = robot(-4,2, 'r')
    r3 = robot(9,-5, 'd')
    r4 = robot(-6, -2, 'L')
    r1.turnLeft()
    r2.turnLeft()
    r3.turnLeft()
    r4.turnLeft()
    if r1.getFacing() != 'L':
        print("failed test4A")
        return False
    if r2.getFacing() != 'U':
        print("failed test4B")
        return False
    if r3.getFacing() != 'R':
        print("failed test4C")
        return False
    if r4.getFacing() != 'D':
        print("failed test4D")
        return False
    return True

def test5():
    '''Test turnRight'''
    r1 = robot(4,5,'U')
    r2 = robot(-4,2, 'r')
    r3 = robot(9,-5, 'd')
    r4 = robot(-6, -2, 'L')
    r1.turnRight()
    r2.turnRight()
    r3.turnRight()
    r4.turnRight()
    if r1.getFacing() != 'R':
        print("failed test5A")
        return False
    if r2.getFacing() != 'D':
        print("failed test5B")
        return False
    if r3.getFacing() != 'L':
        print("failed test5C")
        return False
    if r4.getFacing() != 'U':
        print("failed test5D")
        return False
    return True

def test6():
    '''Test multiple moves'''
    r1 = robot(4,5,'U')
    r2 = robot(-4,2, 'R')
    r3 = robot(9,-5, 'D')
    r4 = robot(-6, -2, 'L')
    r1.advance()
    r1.advance()
    r2.advance()
    r1.advance()
    r2.advance()
    r3.advance()
    r1.advance()
    r2.advance()
    r3.advance()
    r4.advance()
    if r1.getPosition() != (4,9):
        print("failed test6A")
        return False
    if r2.getPosition() != (-1,2):
        print("failed test3B")
        return False
    if r3.getPosition() != (9,-7):
        print("failed test6C")
        return False
    if r4.getPosition() != (-7,-2):
        print("failed test6D")
        return False
    return True

def test7():
    '''Test complex sequence of moves and turns'''
    r1 = robot(8, 2, 'R')
    r2 = robot(-1, -4, 'U')
    r1.turnRight()
    r2.advance()
    r2.advance()
    r2.turnRight()
    r1.advance()
    r1.advance()
    r2.advance()
    r1.turnLeft()
    r1.advance()
    r1.turnRight()
    r2.turnRight()
    r2.turnRight()
    r2.advance()
    r1.advance()
    r1.turnRight()
    r1.advance()
    r1.advance()
    r2.advance()
    r2.turnRight()
    if r1.getPosition() != (7,-1):
        print("failed test 7A")
        return False
    if r1.getFacing() != 'L':
        print("failed test 7B")
        return False
    if r2.getPosition() != (-2,-2):
        print("failed test 7C")
        return False
    if r2.getFacing() != 'U':
        print("failed test 7D")
        return False
    return True

def test8():
    '''testing program'''
    r1 = robot(8, 2, 'D')
    r2 = robot(-4, -1, 'R')
    r1.runProgram('AARAR')
    if r1.getPosition() != (7,0):
        print("failed test8A")
        return False
    if r1.getFacing() != 'U':
        print("failed test8B")
        return False
    r2.runProgram('LARALA')
    if r2.getPosition() != (-3, 1):
        print("failed test8C")
        return False
    if r2.getFacing() != 'U':
        print("failed test8D")
        return False
    r1.runProgram('AL')
    if r1.getPosition() != (7,1):
        print("failed test8E")
        return False
    if r1.getFacing() != 'L':
        print("failed test8F")
        return False
    r2.runProgram('LR')
    if r2.getPosition() != (-3, 1):
        print("failed test8F")
        return False
    if r2.getFacing() != 'U':
        print("failed test8G")
        return False   
    return True

def test9():
    '''testing __str__'''
    r1 = robot(1, 4, 'U')
    r2 = robot(-4, 0, 'R')
    r3 = robot(-7, -18, 'L')
    r4 = robot(81, -984, 'D')
    if str(r1) != '(1, 4):U':
        print("failed test9A")
        return False
    if str(r2) != '(-4, 0):R':
        print("failed test9B")
        return False
    if str(r3) != '(-7, -18):L':
        print("failed test9C")
        return False
    if str(r4) != '(81, -984):D':
        print("failed test9D")
        return False
    return True

score = 0
if (test1()):
    score += 10
if (test2()):
    score += 10
if (test3()):
    score += 10
if (test4()):
    score += 10
if (test5()):
    score += 10
if (test6()):
    score += 10
if (test7()):
    score += 10
if (test8()):
    score += 10
if (test9()):
    score += 10

print('Total score: {}/90'.format(score))
print("Don't forget to submit a screenshot of this execution!")

