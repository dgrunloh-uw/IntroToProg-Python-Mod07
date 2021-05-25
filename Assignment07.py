# ------------------------------------------------- #
# Title: Assignment07
# Description: An example oF how Pickling adn Structured Error
#              Handling works.
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog: (Who, When, What)
# David Grunloh,05.24.2021,Created Script
# David Grunloh,05.24.2021,Built out IO Class functions
# David Grunloh,05.24.2021,Built out processing class functions
# David Grunloh,05.24.2021,Built out main class to call functions
# David Grunloh,05.25.2021,Cleaned up code for submission
# ------------------------------------------------- #

#  Import Modules
import pickle  # This imports code from another code file
import sys  # This imports the sys module

# Define Variables
strBrewData = "BrewData.dat"  # Captures the data file
lstBrew = []  # Defines the list that will be used throughout tool
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the status of an processing functions


# Processing ---------------------------------------------------------------- #
class Processor:
    """ Performs processing tasks """

    @staticmethod
    def add_data_to_list(brew_id, brew_name, brew_cost, list_of_data):
        """Adds data to the list

        :param brew_id: (int) with the id
        :param brew_name: (string) with the brew name
        :param brew_cost: (int) with the brew cost
        :param list_of_data: (list) you want filled with file data:
        :return: (list_of_data) of dictionary rows
        """
        list_of_data.clear()
        row = {"Brew ID": brew_id, "Brew Name": brew_name, "Brew Cost": brew_cost}
        list_of_data.append(row)
        return list_of_data, 'Success'

    @staticmethod
    def save_data_to_file(brew_file, list_of_data):
        """ Saves the data to dat file

        :param brew_file: (str) file to save content
        :param list_of_data: (str) list with data in it
        """
        file = open(brew_file, "ab")
        pickle.dump(list_of_data, file)
        file.close()


    @staticmethod
    def read_data_from_file(brew_file):
        """ Read data from teh file

        :param: brew_file: (str) with the file name
        """
        data2 = []
        file = open(brew_file, "rb")
        while True:
            try:
                data2.append(pickle.load(file))
            except EOFError:
                break
        file.close()
        list_of_data = data2
        return list_of_data


# IO

class IO:
    """ Perform Input and Output tasks """

    @staticmethod
    def print_current_brews(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current brews are: *******")
        for row in list_of_rows:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_brew():
        """Allows user to input a new brew

        :return: id: (int) with the id
        :return: brew_name: (string) with the brew name
        :return: brew_cost: (int) with the brew cost
        """
        print("Enter your brew cost information.  ")
        try:
            brew_id = int(input("Enter an Id: "))
        except ValueError as e:
            print("This field only accepts integers. ")
            print(e)
            input("Press enter to exit the application. ")
            sys.exit()

        brew_name = str(input("Enter a Brew Name: ")).strip()

        try:
            brew_cost = int(input("Enter a Brew Cost: "))
        except ValueError as e:
            print("This field only accepts integers. ")
            print(e)
            input("Press enter to exit the application. ")
            sys.exit()
        return brew_id, brew_name, brew_cost

# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, gather file name from user
lstBrew = Processor.read_data_from_file(strBrewData)
IO.print_current_brews(lstBrew)

# Step 2 - Add new brew to list
data = IO.input_new_brew()
Processor.add_data_to_list(brew_id=data[0], brew_name=data[1], brew_cost=data[2], list_of_data=lstBrew)

# Step 3 - Now we store the data with the pickle.dump method
Processor.save_data_to_file(brew_file=strBrewData, list_of_data=lstBrew)

# Step 4 - We pull the data from the pickle into the list and display it
lstBrew = Processor.read_data_from_file(strBrewData)
IO.print_current_brews(lstBrew)

# Pause the application
input("Press Enter to close the application. ")


