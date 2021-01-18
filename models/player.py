""" This module contains the Player Class. """

class Player:
    """ Represents the player in the maze game. """
    def __init__(self):
        """ Initializes attributes. """
        self._collection = []

    @property
    def collection(self):
        """ Getter for collection attribute. """
        return self._collection

    def collect_item(self, item):
        """ Adds an item into collection. """
        self._collection.append(item)
