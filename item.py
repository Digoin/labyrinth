# coding=utf-8

"""parent class"""
class Item:  
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = (x, y)
