print("Hello world")

#varaiables
name = "Bruce"
last_name = "Wayne"
age = 100
isAvailable = True

print(name)
print(last_name)
print(age)
print(isAvailable)

# if statement
if age < 100:
    print("You are younger than 100 years old")
elif age ==100:
    print("You are 100 years old")    
else:
    print("You are older than 99 years old")

print("im outside")

# functions
def say_hello():
    print("Hello there!")

def say_good_bye():
    print("Goodbye!")

# call a function
say_hello()
say_good_bye()

def say_hi_to(name):
    print("message say hi to" + name)

say_hi_to("Leo Miranda")

#math
print(1 + 2)
print(8 -4)
print(20 * 5)
print(100 / 10)
print(f"5 + 2 = {5+2}")
print("5 + 2 = " + str(5+2))

# for loop
for i in range(1,5):
    print(i)

for i in range(25,29):
    print(i)

for char in "hello":
    print(char)