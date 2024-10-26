"""
File: bball.py
Author: [Your Name]
Course: CSc 120, Basketball Data Analysis
Purpose: This program analyzes historical win-loss data for Division I NCAA 
         women’s basketball teams, computes the win ratio for each team, and
         identifies the conference(s) with the highest average win ratio.
"""

class Team:
    """
    Represents information about a basketball team.
    """
    
    def __init__(self, line):
        """
        Initializes a Team object using information extracted from input line.
        Assigns values to attributes.

        Parameters:
        line (str): Input line containing team information.

        Returns: Nothing
        """
        first_para=line.find("(")
        last_para=line.rfind("(")
        if first_para != last_para:
            name_end=last_para-1
        else:
            name_end=line.find("(")-1
        self._name=line[:name_end]
        
        end_conf_name=line.rfind(")")
        self._conference=line[last_para+1:end_conf_name]

        win_and_loss=line[end_conf_name+1:].split()
        win=int(win_and_loss[0])
        loss=int(win_and_loss[1])
        win_ratio= win/(win+loss)
        self._win_ratio=win_ratio
              

    def name(self):
        """
        Returns the name of the team.
        """
        return self._name
    
    def conf(self):
        """
        Returns the conference of the team.
        """
        return self._conference
    
    def win_ratio(self):
        """
        Returns the win ratio for the team.
        """
        return self._win_ratio
    
    def __str__(self):
        """
        Returns a string with information about the team.
        """
        name=self._name
        win_ratio_str=str(self._win_ratio)
        return "{} : {}".format(name, win_ratio_str)

class Conference:
    """
    Represents information about a collection of basketball teams.
    """
    
    def __init__(self, conf):
        """
        Initializes a Conference object with the name of the conference.
        
        Parameters:
        conf (str): Name of the conference.

        Returns: Nothing
        """
        self._conf_name=conf
        self._teams=[]

    def __contains__(self, team):
        """Checks if a team is in the conference."""
        return team in self._teams
    
    def name(self):
        """Returns the name of the conference object."""
        return self._conf_name
    
    def add(self, team):
        """
        Adds a team to the list of teams associated with the conference.
        """
        if team not in self._teams:
            self._teams.append(team)

    def win_ratio_avg(self):
        """
        Returns the average win ratio for the conference.
        """
        sum_win_ratio=0
        total_win_ratios=len(self._teams)
        for object in self._teams:
            sum_win_ratio+=object._win_ratio
        avg_win_ratio=sum_win_ratio/total_win_ratios
        return avg_win_ratio
    
    def __str__(self):
        """
        Returns a string with information about the conference.
        """
        name= self._conf_name
        win_ratio_str=str(self.win_ratio_avg())
        return "{} : {}".format(name, win_ratio_str)
    
class ConferenceSet:
    """
    Represents a collection of basketball conferences.
    """

    def __init__(self):
        """
        Initializes the collection of conferences to be empty.

        Parameters: None

        Returns: Nothing
        """
        self._conf_collection=[]

    def add(self, team):
        """
        Adds a team to the appropriate conference in the collection.

        Parameters:
            team: Team object
        
        Returns: Nothing
        """
        conf_name=team.conf()
        condition=True
        for obj in self._conf_collection:
            if obj.name()==conf_name:
                obj.add(team)
                condition=False
                break
        
        if condition:
            new_obj=Conference(conf_name)
            new_obj.add(team)
            self._conf_collection.append(new_obj)

    def best(self):
        """
        Returns a list of conferences with the highest average win ratio.

        Parameters: None

        Returns: 
            sorted_conferences: list of conferences with the highest 
                                average win ratio
        """
        
        if len(self._conf_collection)==0:
            return []
        
        highest_avg_wr=0
        # to find the highest average win ratio
        for obj in self._conf_collection:
            if obj.win_ratio_avg()>highest_avg_wr:
                highest_avg_wr=obj.win_ratio_avg()
        
        required_conf=[]
        # to find the conferences with highest average
        for obj2 in self._conf_collection:
            if obj2.win_ratio_avg()==highest_avg_wr:
                required_conf.append(obj2)

        sorted_conferences = []
        # to sort the final conferences
        while required_conf:
            min_conf = required_conf[0]
            for conf in required_conf:
                if conf.name() < min_conf.name():
                    min_conf = conf
            sorted_conferences.append(min_conf)
            required_conf.remove(min_conf)

        return sorted_conferences
    
    def __repr__(self):
        return repr(self._conferences)

def main():
    """
    Reads input, processes data, and prints results of the analysis.
    """
    conf_set = ConferenceSet()
    file_name = input()
    file = open(file_name, 'r')
    for lines in file:
        if lines[0] != "#":
            if lines[0].isdigit():
                lines=lines[1:]
            team = Team(lines)
            conf_set.add(team)
    file.close()
    best_conf=conf_set.best()
    for conf in best_conf:
        print("{} : {}".format(conf.name(), conf.win_ratio_avg()))
        
main()




