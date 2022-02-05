from fileio import readFile, writeFile
from clearConsole import clearConsole
from messager import Messager
from datetime import date
import asyncio

class Todo:
  def __init__(self):
    self.fileName = "todo-list.json"
    self.openMenu = True

  def __getPreviousList(self):
    self.__todoList = readFile(self.fileName)
    return self.__todoList

  def __addItem(self, item):
    self.__todoList.append({"name":item,"done" :False})
    writeFile(self.fileName,self.__todoList)

  def __removeItem(self, index):
    del self.__todoList[index-1]
    writeFile(self.fileName,self.__todoList)

  def __completeItem(self, index):
    self.__todoList[index-1]["done"] = True
    writeFile(self.fileName,self.__todoList)

  def __reportList(self):
      reportingList = "Task List ({0})\n".format(date.today().strftime("%d/%m/%Y"))
      previousList = self.__getPreviousList()
      for idx in range(len(previousList)):
        reportingList+="{2}[{0}] {1}\n".format(idx+1, previousList[idx]['name'], previousList[idx]['done']and"✓"or"☐")
      messager = Messager()
      asyncio.run(messager.sendMessage(self.__contactDictionary,reportingList))

  def __routing(self,action):
    if(action == "1"):
      newItem = input("Please input new task: ")
      self.__addItem(newItem)

    elif(action == "2"):
      targetItemIndex = input("Please input task to state as completed (number): ")
      targetItemIndex = int(targetItemIndex)
      confirm = input("Confim completing \033[1m[{0}] {1} \033[0m?(y/n) : ".format(str(targetItemIndex),self.__todoList[targetItemIndex-1]['name']))
      if(confirm == 'y'):
        self.__completeItem(targetItemIndex)
      else:
        return

    elif(action == "3"):
      targetItemIndex = input("Please input task to remove (number): ")
      targetItemIndex = int(targetItemIndex)
      confirm = input("Confim removing \033[1m[{0}] {1} \033[0m?(y/n) :  ".format(str(targetItemIndex),self.__todoList[targetItemIndex-1]['name']))
      if(confirm == 'y'):
        self.__removeItem(targetItemIndex)
      else:
        return

    elif(action == "4"):
      self.__contactDictionary = readFile("contactBook.json")["todoList"]
      contact = ''
      for idx in range(len(self.__contactDictionary )):
        contact+= "\033[1m"+ self.__contactDictionary[idx]["alias"] + " "
      confirm = input("Confim reporting to {0} \033[0m?(y/n) :  ".format(contact))
      if(confirm == 'y'):
        self.__reportList()
      else:
        return
        

    elif(action == "0"):
      self.openMenu = False

  def showMenu(self):
    while(self.openMenu):
      previousList = self.__getPreviousList()
      clearConsole()
      print("***** Todo List *****\n")
      for idx in range(len(previousList)):
        print("[{0}] {1:40} {2}\033[0m".format(idx+1, previousList[idx]['name'], previousList[idx]['done']and"\033[0;37;42mCompleted"or"\033[0;37;41mNot Completed"))
      print("\n**********************\n")

      print("1. Add Item")
      print("2. Complete Item")
      print("3. Remove Item")
      print("4: Report List")
      print("0: Back")
      self.__routing(input(": "))