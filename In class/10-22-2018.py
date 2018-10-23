def tryExcept():
    try:
        print('trying')
    except: #NOT CATCH
        print('caught')

import random
def guess (max):
    num = random.randrange(1, max + 1)
    g = input("what number do you think it is?: ")