from models.score import Score
import json

class ScoreManager:
    """ Simple class to manage a collection of scores
    
    Attributes:
        scores (list): the list of scores managed by the instance
    """

    def __init__(self):
        """ Initializes private attributes """
        self._scores = list()

    @property
    def scores(self):
        """ Returns a list of dictionaries sorted in descending order by score """
        return [score.to_dict() for score in sorted(self._scores, reverse=True)]
         
    def add_score(self, score):
        """ Adds a score instance to the score list 
        
            Arg:
                score: Score instance

            Raises:
                TypeError: if argument is not a Score instance
        """
        if type(score) is not Score:
            raise TypeError("Invalid score.")

        self._scores.append(score)

    def remove_user_score(self, user_name):
        """ Removes all score instances in scores list that match the name
        
            Arg:
                user_name (str): name of scores to remove
        """
        revised_scores = []
        for score in self._scores:
            if score._name != user_name:
                revised_scores.append(score)
        self._scores = revised_scores

    def remove_all_scores(self):
        """ Removes all scores from the scores list """
        self._scores = []
        
    def __len__(self):
        """ Returns length of the scores list """
        return len(self._scores)

    def serialize(self):
        """ Returns list of dictionaries of score instance names and scores. """
        return self.scores

    def from_json(self, json_file):
        """ Load scores from json file into score manager 
        
            Arg:
                json_file (str): name of json file to load scores from
        """
        with open(json_file, "r") as fp:
            data = json.load(fp)
            for item in data["scores"]:
                new_score = Score(item["name"], item["score"])
                self.add_score(new_score)

    def to_json(self, json_file):
        """ Write scores from score manager into json file 
        
            Arg:
                json_file (str): name of json file to write scores to
        """
        with open(json_file, "w") as fp:
            json.dump({"scores": self.serialize()}, fp)
