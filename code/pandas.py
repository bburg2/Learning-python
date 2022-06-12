dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

# pandas is a data manipulation tool, and pandas also has dataframes
# I had to install pandas using: "pip install pandas" in the terminal
import pandas as pd
brics = pd.DataFrame(dict)
print(brics)


# Set the index for brics, with "index" you can change the key
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

# you can also import csv files, I downloaded this example csv file from: https://www.w3schools.com/python/pandas/pandas_csv.asp
workout = pd.read_csv('data/data.csv')

# Print out workout
print(workout)

# Only print the Pulse column
print(workout['Pulse'])

# Print out Pulse column as Pandas DataFrame
print(workout[['Pulse']])

# Print the pulse and Duration column as a pandas dataframe
print(workout[['Pulse', 'Duration']])

# Print out first 4 observations
print(workout[0:4])

# Print out fifth and sixth observation
print(workout[4:6])

# print the second row
print(workout.iloc[2])

# Print 110 and 120
print(workout.loc[[110, 120]])
