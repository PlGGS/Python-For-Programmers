import random

def craps():
    '''Returns whether or not the user wins a game of Craps'''
    die1 = random.randrange(1, 6)
    die2 = random.randrange(1, 6)

    if (((die1 + die2) == 7) or ((die1 + die2) == 11)):
        return 1
    elif (((die1 + die2) == 2) or ((die1 + die2) == 3) or ((die1 + die2) == 12)):
        return 0
    else:
        initAmt = (die1 + die2)
        while (((die1 + die2) != initAmt) or ((die1 + die2) != 7)):
            die1 = random.randrange(1, 6)
            die2 = random.randrange(1, 6)

            if ((die1 + die2) == initAmt):
                return 1
            elif ((die1 + die2) == 7):
                return 0

def testCraps(n):
    '''Prints the fraction of how many times a user wins Craps out of how many times they played'''
    amt = 0
    
    for i in range(n):
        if bool(craps()):
            amt += 1
    
    return amt / n

def game(n):
    num1 = random.randrange(0, 9)
    num2 = random.randrange(0, 9)
    ans = (num1 + num2)
    correctCount = 0

    for i in range(n):
        num1 = random.randrange(0, 9)
        num2 = random.randrange(0, 9)
        ans = (num1 + num2)
        
        inp = int(input(str(num1) + " + " + str(num2) + " = "))

        if inp == ans:
            print("Correct!\n\n")
            correctCount += 1
        else:
            print("Incorrect.\n\n")
    
    print("You got " + str(correctCount) + " answers correct out of " + str(n) + " questions!")

def networks(n, friends):
    '''Returns a list of social networks based off of an amount of students and a list of pairs of friends'''
    friends = dict(friends)
    socialNetworks = []
    
    for student in range(n):
        tmpSocialNetwork = set({student})
        tmpListSocialNetwork = list(tmpSocialNetwork)
        outSocialNetwork = set({student})
        complete = False

        while complete == False:
            for i in range(len(tmpSocialNetwork)):
                try:
                    tmpSocialNetwork.add(friends[tmpListSocialNetwork[i]])
                    tmpListSocialNetwork = list(tmpSocialNetwork)
                except:
                    if tmpSocialNetwork == outSocialNetwork:
                        complete = True

                    outSocialNetwork = tmpSocialNetwork

                if tmpSocialNetwork == outSocialNetwork:
                    if (len(outSocialNetwork) > 1 and not(outSocialNetwork in socialNetworks)):
                        inSocialNetwork = False
                        tmpNetwork = set({})

                        for network in socialNetworks:
                            tmpNetwork.update(network)
                            for friend in outSocialNetwork:
                                tmpNetwork.add(friend)
                            if tmpNetwork == network:
                                inSocialNetwork = True

                        if inSocialNetwork == False:
                            socialNetworks.append(outSocialNetwork)

                    complete = True

                outSocialNetwork = tmpSocialNetwork
    
    for i in range(len(socialNetworks)):
        print("Social network " + str(i) + " is " + str(socialNetworks[i]))

    return socialNetworks