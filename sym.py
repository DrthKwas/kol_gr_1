#!/usr/bin/python

import random
import time

class Simulator:
    def __init__(self):
        self.angle = 0
        
    def run(self):
        while True:
            self.angle = self.angle + self.stder()
            self.correction = self.corect()
            self.printData()
            
            time.sleep(1)
            
    def corect(self):
        return 0.66 * self.angle 
        
    def printData(self):
        print("\nAngle: " + str(self.angle))
        print("Correction: " + str(self.correction))
        
    def stder(self):
        return random.gauss(-1,1)
        
sim = Simulator()
sim.run()
