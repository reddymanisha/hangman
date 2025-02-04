# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "You are____________"
 # human ="Beautiful"  # some string variable

# a few ways to do this
# print("You are " + human)
# print("You are {}".format(human))
# print(f"You are {human}")


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib =f"computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"


print(madlib)