import random



def Prob1(size):
    playagain= "yes"
    while playagain[0] == 'y':
        print("Generating", size, "random integers between 1 and 100...")
        my_random=random.sample(range(1,100), size)
        print("Done generating random integers! \n")

        guess_taken = 0

        guess_allowed=random.sample(range(1, 10), 1)
        
    
        while guess_taken < guess_allowed[0]:

            x=int(input("Enter a number to find: "))
            guess_taken = guess_taken + 1
            if x in my_random:
                print("Congratulations!!! Found", x, "in my database after", guess_taken, "tries. \n")
    
            if x not in my_random:
                print("Oops,", x, "is not in my database. \n")
            
            

    
        print("Time is up! Values in this database are;")
        print(my_random, "\n")

        playagain = input("Do you want to continue playing?(y or n): ")
        print("")

    print("Thanks for playing")

    

    
    

    
    

        
        
    
    
        
    

    
    
    




    

        
              
