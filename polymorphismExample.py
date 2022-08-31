print("This is a single person called by various name by different people.") 
class School():
    def my_name(self):
        print("Everybody calls me Anuj in school.")
class Gym():
    def my_name(self):
        print("Everybody calls me monster in gym.")
class Friends():
    def my_name(self):
        print("My friends call me Idiot.")
class Parents():
    def my_name(self):
        print("My parents call me Chintu at home.")

def call(name):
    name.my_name()

brah = Gym()
mates = School()
bois = Friends()
guardians = Parents()

for x in (brah, mates, bois, guardians):   #I used for loop to print every line in short code. Here 'call' function is not used.
    x.my_name()
print("\n")

#but to print a individual line, 'call' function will be used ->
call(bois) 
