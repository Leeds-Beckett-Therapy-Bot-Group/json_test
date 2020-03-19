import datetime
import json
import random
import time


class test():
    def __init__(self):
        self.tracker = []

    def create_json(self):
        for i in range(1, 6):
            mood = {'index': len(self.tracker) + 1,
                    'timestamp': str(datetime.datetime.now()),
                    'happiness': random.randint(1, 10),
                    'confidence': random.randint(1, 10),
                    'activeness': random.randint(1, 10), }
            self.tracker.append(mood)

            with open('mood.json', 'a') as outfile:
                json.dump(mood, outfile, indent=4)
                outfile.write(",")

            print("object " + str(i) + " created")
            time.sleep(1)
        return mood


test().create_json()
