
class Person(object):
    population=0
    # Person constructor
    def __init__(self, firstName, lastName, dateOfBirth, gender):
        self.firstname = firstName
        self.lastname = lastName
        self.dob = dateOfBirth
        self.gender = gender
        Person.population += 1

    # Getters
    def __getDateOfBirth( self ):
        return self.dob
        pass
    

    def __getGender( self ):
        return self.gender
        pass
    

    def __getpop(  ):
        return Person.population
        pass
    
    

