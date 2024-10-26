"""
    File: street_builder.py
    Author: Aryaman Mehra
    Course: CSC-120 , Spring 2024
    Purpose: This program constructs a street layout with components 
             such as buildings, parks, and empty lots based on user
             input specifications.
"""

class Building:
    """
    Represents a building on the street. 
    This class defines methods to construct a building and retrieve
    its attributes such as width, height, and building material.
    """
    
    def __init__(self, specs):
        spec= specs.split(",")
        self._width = int(spec[0])
        self._height = int(spec[1])
        self._brick = spec[2]
        self._building1 = []
        self.build_building(self._width, self._height, self._brick)

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def get_brick(self):
        return self._brick
    
    def get_building(self):
        return self._building1
    
    def build_building(self, width, height, brick):
        """
        Constructs the building recursively.

        Parameters:
           width: Width of the building.
           height: Height of the building.
           brick: Material used in the building.

        Returns:
           Nothing
        """
        if height!= 0:
            self._building1.append(width*brick)
            self.build_building(width, height-1, brick)

    def component_at_height(self, height):
        """
        Returns the building structure at a given height.

        Parameters:
           height: Height at which the component is requested.

        Returns:
           The structure of the building at the specified height.
        """
        if height>= self._height:
            return " " * self._width
        return self._building1[height]
    
    def __str__(self):
        return "Width: " + str(self._width) + ", Height: " + str(self._height)\
        + ", Brick: " + self._brick + ", Building: " + str(self._building1)
    
class Park:
    """
    Represents a park on the street.
    This class defines methods to construct a park and 
    retrieve its attributes such as width and foliage type.
    """
    
    def __init__(self, specs):
        spec= specs.split(",")
        self._width = int(spec[0])
        self._foliage = spec[1]
        self._park1 = []
        self.build_park(self._width, self._foliage, 5)

    def get_width(self):
        return self._width
    
    def get_foliage(self):
        return self._foliage
    
    def get_park(self):
        return self._park1
    
    def build_park(self, width, foliage, height):
        """
        Constructs the park recursively.

        Parameters:
           width: Width of the park.
           foliage: Type of foliage in the park.
           height: Height of the park structure.
        Returns:
           Nothing
        """
        if height!=0:
            halfw = width // 2
            if height == 5:
                self._park1.append(halfw * " " + foliage + halfw * " ")
            elif height == 4:
                self._park1.append((halfw-1) * " " + foliage * 3 + \
                                   (halfw-1) * " ")
            elif height == 3:
                self._park1.append((halfw-2) * " " + foliage * 5 + \
                                   (halfw-2) * " ")
            else:
                self._park1.append(halfw * " " + "|" + halfw * " ")
            self.build_park(width, foliage, height-1)

    def component_at_height(self, height):
        """
        Returns the park structure at a given height.

        Parameters:
           height: Height at which the component is requested.

        Returns:
           The structure of the park at the specified height.
        """
        if height>4:
            return self._width * " "
        return self._park1[4-height]
    
    def __str__(self):
        return "Width: " + str(self._width) + ", Foliage: " \
            + self._foliage + ", Park: " + str(self._park1)
    
class Empty_Lot:
    """
    Represents an empty lot on the street.
    This class defines methods to construct an empty lot and
    retrieve its attributes such as width and trash content."""
    
    def __init__(self, specs):
        spec = specs.split(",")
        self._width = int(spec[0])
        self._trash = spec[1]
        self._lot = []
        self.build_lot(self._width, self.clean_trash(self._trash))

    def get_width(self):
        return self._width
    
    def get_trash(self):
        return self._trash
    
    def get_lot(self):
        return self._lot
    
    def build_lot(self, width, trash):
        """
        Constructs the empty lot.

        Parameters:
           width: Width of the empty lot.
           trash: Content of trash in the empty lot.

        Returns:
           Nothing
        """
        if width <= len(trash):
            self._lot += trash[:width]
        else:
            self._lot += trash
            self.build_lot(width-len(trash), trash)

    def clean_trash(self, str):
        """
        Cleans the trash content from the empty lot.

        Parameters:
           str: String representing the trash content.

        Returns:
           Cleaned trash content.
        """
        if str=="":
            return ""
        elif str[0]=="_":
            return " " + self.clean_trash(str[1:])
        else:
            return str[0]+self.clean_trash(str[1:])
        
    def component_at_height(self, height):
        """
        Returns the empty lot structure at a given height.

        Parameters:
           height: Height at which the component is requested.

        Returns:
           The structure of the empty lot at the specified height.
        """
        if height == 0:
            return "".join(self._lot)
        return self._width * " "
    
    def __str__(self):
        return "Width: " + str(self._width) + ", Trash: "+\
            self._trash + ", Empty Lot: " + str(self._lot)
    
class Street:
    """
    Represents a street layout.
    This class defines methods to construct a street layout
    by adding buildings, parks, and empty lots."""
    def __init__(self):
        self._street1 = []
        self._height = 0
        self._width = 0

    def get_street(self):
        return self._street1
    
    def get_height(self):
        return self._height
    
    def get_width(self):
        return self._width
    
    def set_height(self, height):
        if height > self._height:
            self._height = height

    def set_width(self, width):
        self._width += width

    def add_to_street(self, obj):
        """Adds a component to the street layout.

           Parameters:
           - obj: Object representing a building, park, or empty lot.
        """
        self._street1.append(obj)

    def print_street(self, height):
        """
        Prints the entire street layout.

        Parameters:
           height: Height of the street layout to print.

        Prints:
           The entire street layout.
        """
        if height == -1 :
            print ("+" + "-" * self.get_width() + "+")
        elif height == self.get_height():
            print ("+" + "-" * self.get_width() + "+")
            print ("|" + " " * self.get_width() + "|")
            self.print_street(height-1)
        else:
            print ("|" + self.street_components(self._street1, \
                                                height) + "|")
            self.print_street(height-1)

    def street_components(self, street1, height):
        """
        Returns the components at a given height of the street.

        Parameters:
           street1: List of street components.
           height: Height at which the components are requested.

        Returns:
           Components at the specified height.
        """
        if street1 == []:
            return ""
        return str(street1[0].component_at_height(height)) +\
        self.street_components(street1[1:], height)
    
    def __str__(self):
        return "Height: " + str(self._height) + ", Width: "\
              + str(self._width) + ", Street: " + str(self._street1)
    
def assign(list_streets, street):
    """
    Assigns components to the street layout.

    Parameters:
       list_streets: List of specifications for street components.
       street: Street object to which components are assigned.
    """
    if list_streets != []:

        if list_streets[0][0] == "b":
            b_obj = Building(list_streets[0][2:])
            street.add_to_street(b_obj)
            street.set_height(b_obj.get_height())
            street.set_width(b_obj.get_width())

        if list_streets[0][0] == "p":
            p_obj = Park(list_streets[0][2:])
            street.add_to_street(p_obj)
            street.set_height(5)
            street.set_width(p_obj.get_width())        

        if list_streets[0][0] == "e":
            el_obj = Empty_Lot(list_streets[0][2:])
            street.add_to_street(el_obj)
            street.set_height(1)
            street.set_width(el_obj.get_width())
        assign(list_streets[1:], street)

def main():
    """
    Main function to execute the street layout construction.
    """
    street = Street()
    input_street = input("Street: ").split()
    assign(input_street, street)
    street.print_street(street.get_height())

main()


