# database class to manage all database related info
class database:
        # used to setup variables with self to be used in the class
        def __init__(self):

            # student accounts
            self.students = [
                    ['anthony', 'rangers20', False, False],
                    ["stephanie", "2kool4school", False, False]
                ]

            # teacher accounts
            self.teachers = [
                    ['jack', 'JacK', True, False],
                    ['ruth', 'iloveu', True, False],
                    ['max', 'p@ssword!', True, False]
                ]

            # supervisor account
            self.supervisors = [
                    ['principle', 'megaAdmin', False, True],
                    ['vicePrince', 'iliketurtles', False, True]
                ]

            # admin accounts
            self.admin = [
                    ['admin', 'admin', True, True]
                ]

        # used to add an account with permissions (creates the account selected in it's respective category i.e. student, teacher, supervisor, and admin by using the bool values)
        def add_personel(self, user, password, auth1, auth2):
            if(auth1 or auth2):
                if(auth1 == True and auth2 == False):
                    self.teachers.append([user, password, auth1, auth2])
                elif(auth1 == False and auth2 == True):
                    self.supervisors.append([user, password, auth1, auth2])
                else:
                    self.admin.append([user, password, auth1, auth2])
            else:
                self.students.append([user, password, auth1, auth2])

        # used to remove an account
        def remove_personel(self, auth1, auth2, num):

            # tries to remove desired account (finds authority by bool values and deletes the account selected in it's respective category i.e. student, teacher, supervisor, and admin)
            try:
                if(auth1 or auth2):
                    if(auth1 == True and auth2 == False):
                        self.teachers.pop(num)
                    elif(auth1 == False and auth2 == True):
                        self.supervisors.pop(num)
                    else:
                        self.admin.pop(num)
                else:
                    self.students.pop(num)

            # if there is an IndexError, print error message
            except(IndexError):
                print("Error: Cannot remove personel because the selection is not in range or there was a misconfiguration.")

            # if there is no error, print success message
            else:
                print("Personel account removed.")


db = database()  # initialize the database class
db.add_personel('mathew', 'oof', False, False)  # add a student account
print(db.students)  # print all the student accounts in the students list
db.remove_personel(False, False, 2)  # removes a student account that was just created
print(db.students) # print all the student accounts in the students list

'''

Bool Values:
    False and False == Students
    True and False == Teachers
    False and True == Supervisors
    True and True == Admins

What to do:
    Login and Student Sign Up
    Display category information (i.e. student -> first name, last name, age, grade, gpa ... teachers -> first name, last name, grade they teach, email, phone number ... supervisor -> first name, last name, email, phone number ... admin -> first name, last name)
    Options to add, remove, or update account info or additional details depending on account permissions
    Authority Check to add, remove, or update account info or additional details
    Log out option
    clear screen for every update or input
    exception handling 

What to do advanced:
    Save, load, and update accounts and information in another file
    use sql to create a database
    encrypt/encode account information inside database (sql or file) to not make it plain text
        maybe add salt?
    run script when connecting from ssh with putty so thats the only thing they access (maybe)
'''
