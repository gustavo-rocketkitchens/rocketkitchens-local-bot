import os

import csv

# Initialize an empty dictionary
my_dict = {}
src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"
filename = 'File (5).csv'

filepath = os.path.join(src_path, filename)
print(filepath)
import pandas as pd

# Read the CSV file using pandas, specifying that the first line should be skipped
df = pd.read_csv(filepath, header=0)

# Convert the dataframe to a dictionary
my_dict = df.to_dict()

# Print the dictionary to verify that it has been created correctly
# print(my_dict)


# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(my_dict)

# Print the DataFrame to verify that it has been created correctly
# print(df.plot())
# import seaborn as sns
#
# sns.lineplot(data=df)
import matplotlib.pyplot as plt

# Create a line plot of the data
df.plot()

# Show the plot
plt.show()

# import pandas_profiling
#
# profile = pandas_profiling.ProfileReport(df)
# profile.to_html()
# Open the CSV file and use the csv.reader function to read it
# with open(filepath, 'r') as f:
#     reader = csv.reader(f)
#
#     # Iterate through the rows of the file
#     for row in reader:
#         # Save the first cell as the key and the rest of the cells as the values in a list
#         key = row[0]
#         values = row[1:]
#         my_dict[key] = values

# Print the dictionary to verify that it has been created correctly
print(my_dict)
