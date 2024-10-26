"""
    File: dates.py
    Author: Aryaman Mehra
    Course: CSC 120, Spring 2024
    Purpose: This program manages a calendar, allowing users to add events to 
             specific dates and retrieve events for a given date.
"""

class Date:
    def __init__(self, date, event):
        """
        Class representing a date with associated events.

        Arguments:
            date (str): The date of the event.
            event (str): The event associated with the date.
        """
        self._date=date
        self._event=[event]

    def get_date(self):
        """
        Get the date of the event.
        
        Returns:
            str: The date of the event.
        """
        return self._date
    
    def get_event(self):
        """
        Get the events associated with the date.

        Returns:
            list: A list of events associated with the date.
        """
        return self._event
    
    def add_event(self, event):
        """
        Add an event to the date.

        Arguments:
            event (str): The event to be added.
        """
        self._event.append(event)

    def __str__(self):
        """
        String representation of the Date object.

        Returns:
            str: A formatted string representing the Date object.
        """
        return f"{self._date}: {', '.join(self._event)}"
    
class DateSet:
    def __init__(self):
        """
        Class representing a set of dates with associated events.
        """
        self._date_dict={}

    def add_date(self, date, event):
        """
        Add a date and its associated event to the set.

        Arguments:
            date (str): The date to be added.
            event (str): The event associated with the date.
        """
        if date not in self._date_dict:
            obj=Date(date,event)
            self._date_dict[date]= obj
        else:
            self._date_dict[date].add_event(event)
            
        
    def get_dict(self):
        """
        Get the dictionary containing date-event pairs.

        Returns:
            dict: A dictionary containing date-event pairs.
        """
        return self._date_dict

    def get_events(self, date):
        """
        Get the events associated with a specific date.

        Arguments:
            date (str): The date for which events are to be retrieved.

        Returns:
            list: A list of events associated with the specified date.
        """
        return self._date_dict[date]
    
    def print_dict(self,temp_date):
        """
        Print events associated with a specific date.

        Arguments:
            temp_date (str): The date for which events are to be printed.
        """
        if temp_date in self._date_dict:
            events_list=self._date_dict[temp_date].get_event() 
            for event in sorted(events_list):
                print("{}: {}".format(temp_date, event))
             
    def __str__(self):
        """
        String representation of the DateSet object.

        Returns:
            str: A formatted string representing the DateSet object.
        """
        str_data_dict="{"
        c=1
        for dates in self._date_dict:
            if len(self._date_dict)==c:
                str_data_dict+= "'"+dates+"': '"+str(self._date_dict[dates])\
                                +"'}"
            else:
                str_data_dict += "'"+dates+"': '"+str(self._date_dict[dates])\
                                +"',"
                c+=1
        return str_data_dict
    
def canonicalize_date(date_str):
    """
    Canonicalize the date format.

    Arguments:
        date_str (str): The input date string.

    Returns:
        str: The canonicalized date string.
    """
    seperated = date_str.split()
    if '-' in date_str:
        yyyy, mm, dd = date_str.split('-')
    elif '/' in date_str:
        mm, dd, yyyy = date_str.split('/')
    else:
        month_dict = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
        }
        mm = month_dict[seperated[0]]
        dd = seperated[1]
        yyyy = seperated[2]

    return "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))

def add_event(dict_dates,line):
    """
    Add an event to the DateSet.

    Arguments:
        dict_dates(DateSet:The DateSet object to which the event will be added.
        line (list): A list containing date and event information.
    """
    temp_date=canonicalize_date(line[0].strip())
    temp_event=": ".join(line[1:]).strip(":").strip()
    dict_dates.add_date(temp_date,temp_event)

def print_event(dict_dates,line):
    """
    Print events associated with a specific date.

    Arguments:
        dict_dates(DateSet): The DateSet object from which events will be 
                             printed.
        line (list): A list containing date information.
    """
    temp_date=canonicalize_date(line[0].strip())
    dict_dates.print_dict(temp_date)

def main():
    """
    Main function to run the calendar program.
    """
    file_name=input()
    file= open(file_name,'r')
    dict_dates=DateSet()
    for lines in file:
        line=lines.strip()
        if line[0]=='I':
            add_event(dict_dates, line[1:].split(": "))
        elif line[0]=='R':
            print_event(dict_dates,line[1:].split(": "))
        else:
            print("Error - Illegal operation.")    
    file.close()  

main()
