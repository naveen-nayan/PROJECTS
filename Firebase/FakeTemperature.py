#!/usr/bin/python3

__author__ = 'naveen'

import os
import datetime
import time
import random
from firebase import firebase as fb

class FAKETEMP:

    '''constructor definition'''
    def __init__(self):
        self.__temperatue_log = os.path.expanduser("~") + "/PROJECTS/Firebase/temperature.log"
        self.__dbURL = "https://faketemperature.firebaseio.com/"
        self.__ESP_MAC = "5C:CF:7F:AC:DA:CA"
        self.__CYCLE_RATE = 5
        self.__Time_format = "%Y-%m-%d_%H:%M:%S"

    '''This function eill generate fake temperature at every 5 second'''
    def FakeTemp(self):
        fh = open(self.__temperatue_log, "a+")
        current_time = datetime.datetime.today().strftime(self.__Time_format)
        fake_temp = round(random.uniform(28.0, 30.0), 2)
        data = str(current_time) + ' [-] "PUT /data/Temperature/?mac=' + str(self.__ESP_MAC) + '&CYCLE_RATE='  + str(self.__CYCLE_RATE)  + "&temperature="  + str(fake_temp) + '"\n'
        print(data)
        fh.writelines(data)
        time.sleep(self.__CYCLE_RATE)
        fh.close()
        return current_time , fake_temp

    def pushTemperature(self, time, temp):
        firebase = fb.FirebaseApplication(self.__dbURL, authentication=None)
        node = "/Device/RPi-1/ESP_" + str(self.__ESP_MAC) + '/'
        result = firebase.patch(node, {time: temp})

def main():
    obj = FAKETEMP()
    while True:
        time, temp = obj.FakeTemp()
        obj.pushTemperature(time, temp)

if __name__ == "__main__":
    main()