from todo import Todo
from weather import Weather
from clearConsole import clearConsole

def routing(input):
  if input == "1":
    action = Todo()
    action.showMenu()
  if input == "2":
    action = Weather()
    action.showMenu()
  elif input == "0":
    exit()

def mainMenu():
  while(True):
    clearConsole()
    print("Office Utilities:")
    print("1. Todo List")
    print("2. Weather")
    print("0: Exit")
    routing(input(": "))

if(__name__ == "__main__"):
  mainMenu()