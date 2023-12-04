# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:43:27 2023

@author: USER
"""

import numpy as np
# Creating the grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Calculating mean, median, and standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_deviation = np.std(grades)

# Displaying the calculated values
print("Grades Array:", grades)
print("Mean:", mean_grade)
print("Median:", median_grade)
print("Standard Deviation:", std_deviation)

# Finding maximum and minimum grades
max_grade = np.max(grades)
min_grade = np.min(grades)

# Sorting grades in ascending order
sorted_grades = np.sort(grades)

# Finding the index of the highest grade in the array
index_highest_grade = np.argmax(grades)

# Counting the number of students who scored above 90
above_90_count = np.sum(grades > 90)

# Calculating the percentage of students who scored above 90
percentage_above_90 = np.mean(grades > 90) * 100

# Calculating the percentage of students who scored below 75
percentage_below_75 = np.mean(grades < 75) * 100

# Extracting all the grades above 90 into a new array "high_performers"
high_performers = grades[grades > 90]

# Creating a new array "passing_grades" containing grades above 75
passing_grades = grades[grades > 75]


# Display calculated values
print("Number of Students who scored above 90:", above_90_count)
print("Percentage of Students who scored above 90:", percentage_above_90, "%")
print("Percentage of Students who scored below 75:", percentage_below_75, "%")
print("Grades of High Performers:", high_performers)
print("Passing Grades above 75:", passing_grades)

# Displaying the calculated values
print("Grades Array:", grades)
print("Maximum Grade:", max_grade)
print("Minimum Grade:", min_grade)
print("Grades Sorted in Ascending Order:", sorted_grades)
print("Index of Highest Grade:", index_highest_grade)