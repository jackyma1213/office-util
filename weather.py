import requests
import asyncio
from fileio import readFile
from messager import Messager
from datetime import datetime, date
from clearConsole import clearConsole

try:
  to_unicode = unicode
except NameError:
  to_unicode = str

class Weather:

  def __init__(self):
    self.__openMenu = True

  def __getWeatherForecast(self):
    generalForecast = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc').json()
    currentWeather =  requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc').json()
    report = "日期： {0}\n".format(date.today().strftime("%d/%m/%Y"))
    report += "天氣狀況： {0}\n".format(generalForecast['generalSituation'])
    report += "{0}： {1}{2}\n".format(generalForecast['forecastPeriod'],generalForecast['forecastDesc'],generalForecast['outlook'])
    report += "最後更新： {0}\n".format(datetime.fromisoformat(generalForecast['updateTime']).strftime('%H:%M'))
    report += "氣溫： {0}° ，記錄時間： {1}".format(currentWeather["temperature"]["data"][1]["value"], datetime.fromisoformat(currentWeather["temperature"]["recordTime"]).strftime('%H:%M'))
    return report

  def __sendWeather(self):
    foreCastReport = self.__getWeatherForecast()
    messager = Messager()
    asyncio.run(messager.sendMessage(self.__contactDictionary,foreCastReport))

  def __routing(self, action):
    if(action == "1"):
      self.__contactDictionary = readFile("contactBook.json")["weather"]
      contact = ''
      for idx in range(len(self.__contactDictionary )):
        contact+= "\033[1m"+ self.__contactDictionary[idx]["alias"] + " "
      confirm = input("Confim message to {0} \033[0m?(y/n) :  ".format(contact))
      if(confirm == 'y'):
        self.__sendWeather()
      else:
        return

    elif(action == "0"):
      self.__openMenu = False

  def showMenu(self):
    report = self.__getWeatherForecast()
    while(self.__openMenu):
      clearConsole()
      print("***** Weather *****\n")
      print(report)
      print("\n*****************\n")
      print("1. Message Weather Forecast")
      print("0: Back")
      self.__routing(input(": "))


