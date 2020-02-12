from random import randint



'''     The goal of the game is to take the last object from the last stack.
    Stacks are counts of objects that you will see in a list, each stack
    has their own index in the list.
        The strategy of the game typically to force your opponent to take
    the last object in all stacks other than the last one, so you can start
    on top of the next stack. In this version, you can only take between
    1 and 3 objects from each stack on the leftmost stack, whilst not exceding
    the limits of the stack.'''




def main():
    print("\nNIM\n")

    stacks = [7]
    for i in range(randint(4,10)):
        stacks.append(randint(1,10))

    print(stacks)
    

    # Ask user if they would like to go first
    response = input("would you like to go first? ")

    if response[0].lower() == 'y':
        turn = 1
    else:
        turn = 2

    # Play game
    gameover = False
    while not gameover:
        print()
        print(stacks)

        if turn == 1:
            #player 1 goes
            print('player 1')
            n = player1(stacks)
            gameover = take(stacks, n)
            
            turn = 2
        else:
            #player 2 goes
            print('player 2')
            n = ai3(stacks)
            gameover = take(stacks, n)
            
            turn = 1

    #Check who won
    if turn == 2:
        print("\nPlayer 1 wins!")
        return True

    else:
        print("\nPlayer 2 wins!")
        return False
        

def player1(stacks):
    n = int(input("How many objects do you want to take? "))
    while n < 1 or n > stacks[0]:
        print("Invalid input. Try again!")
        n = int(input("How maby objects do you want to take? "))

    return n



def ai3(stacks):
    #   AI based on algoritms

    ''' Advanced strategy forces the opponent to either take the last object
    or leave the last object in the current stack being played. This is
    determined by combonations of the numbers 1, 5, 9, 4, and 8.
        If a user lands on a 1, they can be forced to take the last object of
    the stack. Similarly, if a player lands on a 4, the are forced to
    surrender the choice of taking the stack to the opponent.
        In this code, I call moments where a player can be forced to take
    a stack as "o"s or "takes", and moments where a player is forced to surrender the
    choice of the stack as "e"s or "leaves", named after "odds" and "evens".
        With a little math, you can develop a pattern. 1, 5, and 9 end
    up being "os" for whoever lands on them. 4 and 8 end up being "es"
    for whoever lands on them.
        With this knowledge, we can use algorithms to determine what count of
    objects an AI should take in order to force the opponent to take the stack
    or leave the stack based on the number of 'o's and 'e's in the game.'''
    
    print("AI is thinking...")
    #Attempts to take last stack
    if len(stacks) == 1:
        n = stacks[0]%4

    else:
        #o/e counter, breaks if streak ends
        ocount = 0
        ecount = 0
        for i in range(1, len(stacks)):
            if (stacks[i]-1)%4 == 0:
                ocount += 1
            elif stacks[i]%4 == 0:
                ecount += 1
            else:
                break
        
        #Case where o is end and has connecting streak
        if ((stacks[-1]-1)%4 == 0 or stacks[-1]%4 == 0)and ocount+ecount + 1 == len(stacks):
            if ocount%2 != 0:
                n = (stacks[0]-1)%4
            else:
                n = stacks[0]%4
            
        #Case where streak not connected to end
        elif ocount+ecount + 1 != len(stacks):
            if ocount%2 != 0:
                n = stacks[0]%4
            else:
                n = (stacks[0]-1)%4
    
        #Case where no streak, maintain control
        else:
            n = (stacks[0]-1)%4

    #Anti-cheat
    if not(0 < n < 4):
        n = randint(1,3)
        if stacks[0] < n:
            n = 1
            
    print("AI takes", n, "objects.")
    return n


def take(stacks, n):
    #Take n objects from the leftmost stack.
    stacks[0] -= n
    if stacks[0] == 0:
        stacks.pop(0)
    return len(stacks) == 0


def gofirst3(stacks):
    #AI determines if it would like to go first based on expected
    #outcome of game.
    
    #Non special nums
    if (stacks[0]-1)%4 != 0 and stacks[0]%4 != 0:
        return True

    else:
        #o/e counter
        ocount = 0
        ecount = 0
        for i in range(0, len(stacks)):
            if (stacks[i]-1)%4 == 0:
                ocount += 1

            elif stacks[i]%4 == 0:
                ecount += 1

            else:
                break

        #Case where entire game is a streak
        if (stacks[-1]%4 == 0 or (stacks[-1]-1)%4 == 0) and ocount+ecount == len(stacks):
            if ocount%2 != 0:
                return True
            else:
                return False

        #Case where streak ends before end
        elif ocount+ecount != len(stacks):
            if ocount%2 != 0:
                return False
            else:
                return True
    


if __name__ == "__main__":
    main()




    
