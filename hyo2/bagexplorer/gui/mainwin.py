import os


class Point(object):
    def x(self):
        return 0

    def y(self):
        return 0


class MainWin(object):
    """
    Main window
    """

    here = os.path.abspath(os.path.dirname(__file__))  # this overwrite where look for resources as images, icons, pdf

    def __init__(self, verbose=False, hyo_win=None):
        pass

    def show(self):
        print("show")

    def pos(self):
        return Point()

    def move(self, point):
        pass
