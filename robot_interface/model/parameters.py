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

    def get_row(self, row_index):
        # Get the values of the specified row
        row_values = self.df.iloc[row_index].values

        # Assign the first cell value as the name of a variable
        variable_name = row_values[0]

        # Assign the rest of the cells as the values in a list
        values = row_values[1:]

        return variable_name, values


if __name__ == "__main__":
    src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"
    filename = 'File.csv'
    filepath = os.path.join(src_path, filename)
    # Create an instance of the Parameters class
    params = Parameters(filepath)

    # Read the CSV file and create the dictionary
    my_dict = params.read_csv()

    # Print the dictionary to verify that it has been created correctly
    # print(my_dict)

    # Call the get_row function, specifying the row index
    variable_name, values = params.get_row(1)

    # Print the variable name and values to verify that they have been assigned correctly
    print(f'Variable name: {variable_name}')
    print(f'Values: {values}')