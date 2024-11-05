import pandas as pd

# Read the CSV files
d1 = pd.read_csv("D:\\ML projects\\Student-performance-classification\\student+performance\\Data\\student-mat.csv", sep=';')
d2 = pd.read_csv("D:\\ML projects\\Student-performance-classification\\student+performance\\Data\\student-por.csv", sep=';')

# Merge the DataFrames on the specified columns
d3 = pd.merge(d1, d2, on=["school", "sex", "age", "address", "famsize", 
                            "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", 
                            "reason", "nursery", "internet"])

# Print the number of rows in the merged DataFrame
print(len(d3))  # Should output 382 students

