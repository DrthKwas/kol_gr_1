# -*- coding: utf-8 -*-
import random
import time


class Simulator(object):
    def __init__(self):
        self.angle = 0

    def run(self):
        while True:
            self.angle = self.angle + self.stder()
            self.correction = self.correct()
            self.angle -= self.correction
            self.print_data()

            time.sleep(1)

    def correct(self):
        return 0.66 * self.angle

    def print_data(self):
        print("\nAngle: " + str(self.angle))
        print("Correction: " + str(self.correction))

    def stder(self):
        return random.gauss(-1, 1)


if __name__ == "__main__":
    sim = Simulator()
    sim.run()
