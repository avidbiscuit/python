from re import X


def greet_user():
  x =  input("Please enter your name: ")
  if x.isnumeric() == True:
    print("Numbers are not accepted. Please retry")
    x = ""
    greet_user()
  return x
