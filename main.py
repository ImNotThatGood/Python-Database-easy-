import os
from termcolor import colored

global authed

# database class to manage all database related info
class database:
    # used to setup variables with self to be used in the class
    def __init__(self):

        # student accounts
        self.personel = {
                'students': [['James', 'Male', 3.2], ['Vanessa', 'Female', 4.0], ['John', 'Male', 2.3]],                    # student's name, gender, and gpa
                'teachers': [['Siznack', 'Female', 'siznack@example.com'], ['Ramirez', 'Male', 'ramirez@example.com']]      # teacger's name, gender, and email
            }

        self.accounts = {
                'students': [['jack', 'jackAndTheBeanStalk', False, False], ['Roland', 'iKeepRollin', False, False]],                                             # student's user, pass, edit student info, edit teacher info
                'teachers': [['pints', 'iloveu', True, False]],                                                                       # teacher's user, pass, edit student info, edit teacher info
                'admin': [['admin', 'password', True, True]]                                                                              # admin's user, pass, edit student info, edit teacher info
            }

class listInfo:
    def __init__(self):
        self.db = database()
        self.personel = self.db.personel
        self.accounts = self.db.accounts

    def listStudentMales(self):
        for i in self.students:
            if 'Male' in i:
                print(i)

    def listStudentFemales(self):
        for i in self.students:
            if 'Female' in i:
                print(i)

class authenticate:
    def __init__(self):
        self.db = database()
        self.personel = self.db.personel
        self.accounts = self.db.accounts

    def auth_user_login(self, user, password, keys):
        for i in range(len(keys)):  # for loop with number of keys (3)
            for j in self.accounts[keys[i]]: # for loop. j variable is set to the values of the dictionary
                if user in j and password in j: # if username and password in j
                    return True
        return False

def main():
    # variables
    db = database() # initialize database
    lists = listInfo() # initialize listInfo
    auth = authenticate() # initialize authenticate
    personel = db.personel
    accounts = db.accounts#                                                 0           1           2
    keys = [key for key in accounts] # return all the keys in accounts (['students', 'teachers', 'admin'])
    authed = False

    while not authed:
        user = input("Enter your username: ")
        password = input("Enter your password: ")
        authed = auth.auth_user_login(user, password, keys)
        if not authed:
            print(colored("Incorrect username or password.", "red"))



if __name__ == '__main__':
    main()

'''
db = database()  # initialize the database class
db.add_personel('mathew', 'oof', False, False)  # add a student account
print(db.students)  # print all the student accounts in the students list
db.remove_personel(False, False, 2)  # removes a student account that was just created
print(db.students) # print all the student accounts in the students list

Bool Values:
    False and False == Students
    True and False == Teachers
    False and True == Supervisors
    True and True == Admins

What to do:
    Login and Student Sign Up (1/2)
    Display category information (i.e. student -> first name, last name, age, grade, gpa ... teachers -> first name, last name, grade they teach, email, phone number ... supervisor -> first name, last name, email, phone number ... admin -> first name, last name)
    Options to add, remove, or update account info or additional details depending on account permissions
    Authority Check to add, remove, or update account info or additional details
    Log out option
    clear screen for every update or input
    exception handling 
    Possibly change the list to dictionary

What to do advanced:
    Save, load, and update accounts and information in another file
    use sql to create a database
    encrypt/encode account information inside database (sql or file) to not make it plain text
        maybe add salt?
    run script when connecting from ssh with putty so thats the only thing they access (maybe)
'''
