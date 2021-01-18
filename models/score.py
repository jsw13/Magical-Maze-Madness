""" This module contains the Score class. """

class Score:
    """ Represents a score in a game """

    def __init__(self, name, score):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """

        if type(name) is not str or not name:
            raise ValueError("Invalid name.")
        if type(score) is not int or score < 0:
            raise ValueError("Invalid score.")

        self._name = name
        self._score = score

    def __lt__(self, other):
        """ Returns True if score is less than other score. 
        
            Args:
                other (Score): Score instance
        """
        if type(other) is not type(self):
            raise TypeError

        return self._score < other._score

    def to_dict(self):
        """ Returns dictionary with name and score. """
        return {
            "name": self._name,
            "score": self._score
        }