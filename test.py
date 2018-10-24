# make a student dictionary
# allow students to add values themselves
# allow students to change or remove values

#dictionary where student info will be stored
student = {"first-name" : "","last-name" : "", "age" : "",}

firstname = input("Please enter your first name: ")
student["first-name"] = firstname
lastname= input("Please enter your last name: ")
student["last-name"] = lastname
ent_age = input("please enter your age: ")
student["age"] = ent_age

#Opens welcome message.txt and puts it into W_contents variable
with open('Welcome message.txt', 'r') as W:
	W_contents = W.read()

#variable needs to be defined before being used in a loop	
answez = ""

# will print the info entered earlier and ask for confirmation
print("So your name is " + student["first-name"].capitalize() + " and your last name \
is " + student["last-name"].capitalize() + " and you are " + student["age"] + " years old?")
while answez == "":
    answer = input("Is your information correct? (please answer 'yes' or 'no'): ").lower()
    #yes will break loop
    if answer == "yes":
    	#prints welcome message.txt and break loop
	    print(W_contents)
	    break
    #if answered no it will break loop
    elif answer == "no":
	    print("Please re-enter your information.")
	    break
	#will continue loop and ask again    
    else:
	    print("Your input was not understood")
#print(firstname)

class Employee:
	def __init__(self, fname, lname, Tworked):
		self.fname = fname
		self.lname = lname
		self.Tworked = Tworked
		self.email = fname + '.' + lname + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

#emp1 = Employee('Abdirashiid', 'Jama', 4)

#print(emp1.fullname())
#print(emp1.email)
#print(emp1.Tworked)

print("Please tell us if some referred you, and if they did what their name is")

response = ''

while response != 'no':

    response = input("Did someone refer you? please enter yes or no: ").lower()
	firstname = input("Please enter their first name: ")
	lastname = input("Please enter their last name: ")