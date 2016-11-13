# -*- coding: utf-8 -*-
import random
import time

from plane import Plane


class Simulator(object):
    def __init__(self):
        self.plane = Plane()
        self.correction = 0

    def run(self):
        while True:
            self.plane.angle += self.stder()
            self.correction = self.correct()
            self.plane.angle -= self.correction
            self.print_data()

            time.sleep(1)

    def correct(self):
        return 0.66 * self.plane.angle

    def print_data(self):
        print("\nAngle: " + str(self.plane.angle))
        print("Correction: " + str(self.correction))

    def stder(self):
        return random.gauss(-1, 1)
