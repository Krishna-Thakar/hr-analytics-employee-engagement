# -*- coding: utf-8 -*-
"""
HR Analytics - Employees Engagement Analysis
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('HRDataset_v14.csv')

# Data Overview
print("Data Shape:", df.shape)
print("Data Info:")
print(df.info())
print("Missing Values:", df.isnull().sum())

# Data Cleaning
df.fillna("0", inplace=True)
df.drop_duplicates(inplace=True)

# EDA
# Top 10 highest salaries
top_10_salaries = df['Salary'].sort_values(ascending=False).head(10)
print("Top 10 Highest Salaries:\n", top_10_salaries)

# Employees needing special attention (PIP)
people_pip = df[df['PerformanceScore'] == 'PIP']
print("Employees on Performance Improvement Plan (PIP):", len(people_pip))

# Absences analysis
absences_count = df['Absences'].value_counts()
print("Absences Count:\n", absences_count)

# Recruitment sources
recruitment_sources = df['RecruitmentSource'].value_counts()
print("Recruitment Sources:\n", recruitment_sources)

# Special Projects Analysis
special_projects = df[df['SpecialProjectsCount'] != 0]
print("Employees with Special Projects:\n", special_projects)

# Visualizations
# Highest vs Lowest Salaries
plt.figure(figsize=(10, 6))
plt.bar(range(1, 11), top_10_salaries, color='g', label='Highest Salaries')
plt.bar(range(1, 11), df['Salary'].sort_values(ascending=True).head(10), color='r', label='Lowest Salaries')
plt.title('Top 10 Highest vs Lowest Salaries')
plt.xticks(range(1, 11))
plt.ylabel('Salaries')
plt.legend()
plt.show()

# Sources of Recruitment
plt.figure(figsize=(10, 6))
sns.barplot(x=recruitment_sources.index, y=recruitment_sources.values, palette='pastel')  # Changed to a valid palette
plt.title('Sources of Recruitment')
plt.xlabel('Recruitment Source')
plt.ylabel('Number of Candidates Hired')
plt.xticks(rotation=45)
plt.show()

# Performance Score Trend
performance_trend = df['PerformanceScore'].value_counts()
plt.figure(figsize=(10, 6))
sns.lineplot(data=performance_trend, marker='o', color='purple', linewidth=2)
plt.title('Performance Trend Analysis')
plt.xlabel('Performance Score')
plt.ylabel('Count')
plt.grid()
plt.show()

# Employee Satisfaction
emp_satisfaction = df['EmpSatisfaction'].value_counts()
plt.figure(figsize=(10, 6))
plt.stem(emp_satisfaction.index, emp_satisfaction)
plt.title('Employee Satisfaction Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Employees')
plt.xticks(emp_satisfaction.index)
plt.show()

# Department Salary Boxplot
plt.figure(figsize=(15, 8))
sns.boxplot(x='Department', y='Salary', data=df, palette='viridis')
plt.title("Department vs Salary")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.show()

# Marital Status by Gender
plt.figure(figsize=(10, 6))
sns.countplot(x='MaritalDesc', hue='GenderID', data=df, palette='pastel')
plt.title('Marital Status by Gender')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()

# Average Engagement Score by Department
avg_engagement = df.groupby('Department')['EngagementSurvey'].mean()
plt.figure(figsize=(10, 6))
avg_engagement.plot(kind='bar', color='skyblue')
plt.title('Average Engagement Score by Department')
plt.xlabel('Department')
plt.ylabel('Average Engagement Score')
plt.xticks(rotation=45)
plt.show()

# Termination Analysis
termination_count = df[df['Termd'] == 1].groupby('Position')['Employee_Name'].count()
print("Termination Count by Position:\n", termination_count)

# Median Salary by Gender
median_salary_gender = df.groupby('Sex')['Salary'].median()
print("Median Salary by Gender:\n", median_salary_gender)

# Save the cleaned data for future use
df.to_csv('Cleaned_HRDataset.csv', index=False)
