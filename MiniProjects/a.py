# Pandas is an open source library in Python.
# It provides ready to use high-performance data structures and data analysis tools.

# A CSV (comma-separated values) file is a text file that stores data in a table structure,
# with information separated by commas and records separated by newlines.
# CSV is also a Excel file.
# we can directly drag it  into the pycharm in project.

# Pandas can be import through ->

import pandas
# To read a CSV file we write:
df = pandas.read_excel("dashboard_february_17.xlsx")
# also to run this file we have to install pip install openpyxl in IT
print(df)