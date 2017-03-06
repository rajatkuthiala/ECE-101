import random



def randomNumGen(size):
    playagain= "yes"
    while playagain[0] == 'y':
        print("Generating 10 random integers between 1 and", size, "...")
        my_random=random.sample(range(1,size), 10)
        print("Done generating random integers!")
        print(my_random)

        guess_taken = 0

        guess_allowed=random.sample(range(1, 10), 1)
        print(guess_allowed)
    
        while guess_taken < guess_allowed[0]:

            x=int(input("Enter a number to find "))
            guess_taken = guess_taken + 1
            if x in my_random:
                print("Congratulations!!! Found", x, "in my database after", guess_taken, "tries. \n")
    
            if x not in my_random:
                print("Oops,", x, "is not in my database. \n")
            
            

    
        print("Time is up! Values in this database are;")
        print(my_random, "\n")

        playagain = input("Do you want to play again? ")
        print("")

    print("Thanks for playing")

    
    

    
    

        
        
    
    
        
    

    
    
    




    

        
              
