import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PRINTS VERSION OF NUMPY
# print(np.__version__)

# Creates a 1 dimensional array of numbers from 0-9
# array = np.arange(10)
# print(array)

# Creates a 3x3 array of all True's
# boolArray = np.full((3, 3), True, bool)
# print(boolArray)

# Outputs odd numbers of an array
# arr = np.arange(10)
# print(arr[arr % 2 == 1])

# Changes odd values into -1
# arr = np.arange(10)
# arr[arr % 2 == 1] = -1
# print(arr)

# Makes an array that copies one array then
# replaces odds with -1
# arr = np.arange(10)
# out = np.where((arr % 2 == 1), -1, arr)

# reshape can adjust dimensions of array
# arr = np.arange(10)
# print(arr.reshape(2, -1))

# Testing random seed function, seed determines what random number is based on
np.random.seed(0)
# Array with 5 entries
v = np.random.randint(10, size=5)
# Array with 3 arrays, each with 3 entries
v1 = np.random.randint(10, size=(3, 3))

# Large array, holding 3 arrays, each of those arrays holds 3 arrays with
# 3 entries
v2 = np.random.randint(10, size=(3, 3, 3))

# Printing spliced versions of your array using :
indexArray = np.random.randint(10, size=(5, 5))
# print(indexArray)
# print(indexArray[0, 2:])

# Code does good job of telling you why you can't combine hstack/vstack
# You can use splicing to combine arrays with different dimensions
# To use vstack, first dimension need equal magnitudes
# To use hstack, first dimension need equal magnitudes, EXAMPLES
# print(np.hstack([indexArray[:3], v1]))
# print(np.vstack([indexArray[:, :3], v1]))

# Just testing the broadcasting things
broadcast1 = np.ones((3, 3)) + np.arange(3)
broadcast2 = np.arange(3).reshape(3, 1) + np.arange(3)

# Solving equations with it
coef = np.array([[2, 6], [5, 3]])
depvars = np.array([6, -9])
solution = np.linalg.solve(coef, depvars)

# pandas to create dictionaries and tables
age = np.array([20, 20, 24, 25])
name = np.array(['Jonathan', 'Daniela', 'Bryan', 'Adolfo'])
weight = np.array([165, 120, 180, 120])
people_dict = {"Age": pd.Series(age, index=name), "Weight": pd.Series(
    weight, index=name)}
people = pd.DataFrame(people_dict)
print(people[people["Weight"] < 150])

# Plotting with matplotlib
x = np.array([10, 11, 12, 11, 15, 17, 18, 19])
numBins = 5
plt.hist(x, numBins, color='red')
plt.show()
