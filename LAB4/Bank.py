# Need this to create a unique number
import uuid
import sys

class BankAccount( object ):

    # Class variable
    numberOfAccounts = 0

    # Constructor
    def __init__( self, accountType='Checking', balance=0.0, userName=''):
        self.__accountNumber = uuid.uuid4().time_low
        self.__accountType = accountType
        self.__balance = balance

        print('Please enter login credentials!')
        self.__userName = userName
        if not userName : self.__userName = input('Username: ')
        self.__passWord = input('Password: ')

        self.loggedIn = False
        
        print('\nPlease remember your login credentials; \nUsername: ' \
              + self.__userName + '\nPassword: ' + self.__passWord )

        BankAccount.numberOfAccounts += 1

    # Add money to account
    def deposit( self, amount ):
        self.promptLogin()
        self.__balance += amount

    # Take money from account
    def withdraw( self, amount ):
        self.promptLogin()
        self.__balance -= amount

    # Get the account number
    def getAccountNumber( self ):
        self.promptLogin()
        return( self.__accountNumber )

    # Ge the type of account
    def getAccountType( self ):
        self.promptLogin()
        return( self.__accountType )        

    # Get the current balance
    def getBalance( self ):
        self.promptLogin()
        return( self.__balance )

    # Log into account
    def login( self, userName='', passWord='' ):

        # When user does not provide username and password, ask for it
        if not userName and not passWord :
            userName = input('Enter username: ')
            passWord = input('Enter password: ')

        # Check the usernamd and password provided
        if  self.__userName == userName and self.__passWord == passWord :
            self.loggedIn = True
            print('Successfully logged in!')
        else:
            print('Invalid login credentials!')

    # Log out of account
    def logout( self ):
        if self.loggedIn :
            self.loggedIn = False
            print('Successfully logged out!')
        else :
            print('You are not currently logged in!')
        
    # How to print objects of this class
    def __str__( self ):
        self.promptLogin()
        accountInfo = '***** Account Information *****\n'
        accountInfo += 'Account Number: ' + str( self.__accountNumber ) + '\n'
        accountInfo += 'Account Type: ' + str( self.__accountType ) + '\n'
        accountInfo += 'Balance: ' + str( self.__balance ) + '\n'
        return( accountInfo )

    # Invisible methods
    def promptLogin( self ) :
        if not self.loggedIn :
            print('Please login!')
            sys.exit(1)

