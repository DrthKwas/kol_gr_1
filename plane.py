class Plane(object):
    def __init__(self):
        self.angle = 0

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
