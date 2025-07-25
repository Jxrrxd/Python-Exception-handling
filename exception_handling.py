
try:
    print(x)
except:
    print("An exception has occurred")


try:
    print(z)
except NameError:
    print("Variable z is not defined")
except:
    print("An exception occurred")


try:
    print(y)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

#Part2

try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Everything went wrong")


y = -1

if y<0:
    raise Exception("Sorry, no numbers below zero")