


import os
import json
from firebase import firebase as fb


class DATABASE:

    '''constructor definition'''
    def __init__(self):
        self.__projectURL = "https://faketemperature.firebaseio.com/"
        self.__temperatue_log = os.path.expanduser("~") + "/PROJECTS/Firebase/temperature.log"

    firebase = fb.FirebaseApplication("https://faketemperature.firebaseio.com/", authentication=None)
    result =  firebase.patch("/Device/RPi-1/ESP/MAC_5C:CF:7F:AC:DA:CB", {"time2": "14"})