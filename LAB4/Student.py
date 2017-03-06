import uuid
import threading
from Person import Person
from datetime import datetime
from Bank import BankAccount 
import sys
import random

class Student( Person, BankAccount ):

    numberOfStudents=0
    tuition=3333
    pricePerBook=122.50
    

    #Fill in the others
    __finals = { 'Taken' : False }

    # Person constructor
    def __init__( self, firstName, lastName, dateOfBirth, gender ):
        self.firstname=firstName
        self.lastname=lastName
        self.__dateOfBirth = datetime.strptime(dateOfBirth, '%m-%d-%Y').strftime('%A, %B %d, %Y')
        self.__gender=gender

        print('Congratulations ' + firstName + ', for being accepted to the ECE program in <some university>')
        print('Please Wait While we creat your student account')
        


        Person.__init__( self, firstName, lastName, dateOfBirth, gender)

        self.__studentId = str(uuid.uuid4().time_low)


        Student.numberOfStudents += 1


        self.__major='ECE'
        self.__gpa=4.0
        self.__studentType='Undergraduate'
        self.__emailAddress= firstName + '.' + lastName + '@ece' + '.temple.edu'
        self.__currentClasses=[]
        self.__currentYear= 'Freshman'

        print('\n Thank You For Your Patience ' + firstName)
        print('\n Your Student ID Number is : ' + self.__studentId)
        print( 'and your email address is: ' + self.__emailAddress)

        print('\n As part of university policy, a Bank Account is been created for you. Please enter login credentials!')
        BankAccount.__init__( self, 'checking', 150, self.__emailAddress )

        ans=input('\n Do you want to log into your student account? (Y/N): ')
        if ans in ['y', 'Y']:
            self.loggedIn = True
        if ans in ['n', 'N']:
            self.loggedIn = False
            
        
            
            
        
    def __str__( self ):
        self.promptLogin()
        personalInfo = '***** Personal Information *****\n'
        personalInfo += 'Name: ' + str(self.firstname) + '\n'
        personalInfo += 'DOB: ' + str( self.__dateOfBirth ) + '\n'
        personalInfo += 'Gender: ' + str( Student.getGender(self) )
        print( personalInfo )
        schoolInfo = '***** School Information *****\n'
        schoolInfo += 'Major: ' + str(self.__major) + '\n'
        schoolInfo += 'GPA: ' + str( self.__gpa ) + '\n'
        schoolInfo += 'Student: ' + str( self.__studentType ) + '\n'
        schoolInfo += 'Email: ' + str(self.__emailAddress) + '\n'
        schoolInfo += 'Year: ' + str( self.__currentYear ) + '\n'
        schoolInfo += 'Courses Taken: ' + str( self.__currentClasses )
        print( schoolInfo)
        accountInfo = '***** Account Information *****\n'
        accountInfo += 'Account Number: ' + str( BankAccount.getAccountNumber(self) ) + '\n'
        accountInfo += 'Account Type: ' + str( BankAccount.getAccountType(self) ) + '\n'
        accountInfo += 'Balance: ' + str( BankAccount.getBalance(self) ) + '\n'
        return( accountInfo )
        
        
        
        
        
     # Getters
    def getStudentId( self ):
        self.promptLogin()
        return str(self.__studentId)
        
    
    def getMajor( self ) :
        self.promptLogin()
        return self.__major
        
    
    def getGpa( self ) :
        self.promptLogin()
        return self.__gpa
        

    def getStudentType( self ) :
        self.promptLogin()
        return self.__studentType 
        

    def getEmailAddress( self ) :
        self.promptLogin()
        return self.__emailAddress

    def getStudentYear( self ) :
        self.promptLogin()
        return self.__currentYear
    
    ## Calling methods that exist in the parent
    def getDateOfBirth( self ):
        self.promptLogin()
        return self.__dateOfBirth

    
    ## Calling methods that exist in the parent
    def getGender( self ):
        self.promptLogin()
        if self.__gender in ['m', 'M']:
            return 'Male'
        if self.__gender in ['f', 'F']:
            return 'Female'
        
        
    
    # Register for classes
    def registerForClasses( self ):
        self.promptLogin()
        x=200
        if BankAccount.getBalance(self) < 200:
            print("insufficient funds")
        if BankAccount.getBalance(self) > 200:
            if self.__currentYear=='Freshman':
                self.__currentClasses=['ECE 101 and ECE 102']
            if self.__currentYear=='Sophomore':
                self.__currentClasses=['ECE 201 and ECE 202']
            if self.__currentYear=='Junior':
                self.__currentClasses=['ECE 301 and ECE 302']
            if self.__currentYear=='Senior':
                self.__currentClasses=['ECE 401 and ECE 402']
        

    # Parent function
    def parent( self, amountNeeded ):
        self.promptLogin()
        self.__amountNeeded = amountNeeded
        BankAccount.deposit(self, amountNeeded)
        return 'Amount Deposited'


    # Get classes student is taking now                
    def displayClasses( self ):
        self.promptLogin()
        return self.__currentClasses

    # Populate questions
    def __populateQuestionsAsnwers( self ):

        #This is an example, you do not have to do this if you
        # understand how to instantiate nested collections
        
        self.__finals['Taken'] = True
        
        # Note that the strings must be 5 different questions
        q = []
        q.append( 'Booleans data types take exactly three distinct values')
        q.append( 'Python is a compiled programming language') 
        q.append( 'Class methods take at least two input parameters') 
        q.append( 'A class is a user defined data type')
        q.append( 'The value 2.5 is a float data type') 

        a = (True, False, False, True, True)
        
        self.__finals['Freshman'] = {'Questions' : q, 'Answers' :  a }
        
    # Take the final exams
    def takeFinals( self ):
        pass

    

