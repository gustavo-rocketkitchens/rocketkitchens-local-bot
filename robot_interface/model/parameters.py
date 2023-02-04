import os

import pandas as pd


class Parameters:


    def __init__(self, filepath):
        self.filepath = filepath
        # Read the CSV file using pandas, specifying that the first line should be skipped
        self.df = pd.read_csv(self.filepath, header=0)

    def read_csv(self):
        # Convert the dataframe to a dictionary
        my_dict = self.df.to_dict()

        return my_dict

    def get_row(self, variable_name):
        # Get the row where the first column has the value "variable_name"
        row_values = self.df.loc[self.df[self.df.columns[0]] == variable_name].values

        # Assign the first cell value as the name of a variable
        variable_name = row_values[0][0]

        # Assign the rest of the cells as the values in a list
        values = row_values[0][1:]

        return variable_name, values

    def get_pass(self, variable_name):
        variable_name, values = self.get_row(variable_name)
        username = None
        password = None
        for value in values:
            if isinstance(value, str):
                username = value
                break
        if username:
            for value in values[::-1]:
                if isinstance(value, str):
                    password = value
                    break
        return username, password


if __name__ == "__main__":

    # src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens_local_bot\robot_interface\model\robot_models\output"
    # filename = 'File.csv'
    # filepath = os.path.join(src_path, filename)
    # # Create an instance of the Parameters class
    # params = Parameters(filepath)
    #
    # # Read the CSV file and create the dictionary
    # my_dict = params.read_csv()

    # DO list as dict can raise in future as deprecated
    # my_list = params.read_csv()

    # Print the dictionary to verify that it has been created correctly
    # print(my_dict)
    # print('my_list')
    # print(my_list)

    # Call the get_row function, specifying the row index
    # variable_name, values = params.get_row(1)

    # variable_name, values = params.get_row("Zoey")

    # Print the variable name and values to verify that they have been assigned correctly
    # print(f'Variable name: {variable_name}')
    # print(f'Values: {values}')
    #
    # username, password = params.get_pass("Zoey")
    #
    #
    # # Print the username and password to verify that they have been assigned correctly
    # print(f'Username: {username}')
    # print(f'Password: {password}')
    print(f'Parameters: works')