#def is a keyword and is a function

def say_hi(): # everything inside colon is part of the function
    print("Hello User")
say_hi()


def say_hi():
    print("Hello User")
print("Top")
say_hi()
print("Bottom")

def say_hi(name):
    print("Hello " + name)
say_hi("Mike")
say_hi("Steve")


def say_hi(name, age):
    print("Hello " + name + " you are " + str(age))
say_hi("Mike", 23)
say_hi("Steve", 43)


def say_hi(name, age):
    print("Hello " + name + " you are " + age)
say_hi("Mike", "23")
say_hi("Steve", "43")