

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.DataFrame({
    'Name': ['Ravi','Ravi','Ravi','Ayush','Ayush','Ayush','Aman','Aman','Aman'],
    'Semester': [1,2,3,1,2,3,1,2,3],
    'Subject': ['Math','Math','Math','Math','Math','Math','Math','Math','Math'],
    'Marks': [72,68,75,90,92,94,45,50,48],
    'Attendance': [85,80,88,95,96,97,60,65,62]
})



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



trend = data.groupby(['Name', 'Semester'])['Marks'].mean().reset_index()

subject_difficulty = data.groupby('Subject')['Marks'].mean().sort_values()

consistency = data.groupby('Name')['Marks'].std().reset_index()
consistency.columns = ['Name', 'Consistency_Score']


def risk_level(mark):
    if mark < 40:
        return 'High Risk'
    elif mark < 60:
        return 'Medium Risk'
    else:
        return 'Low Risk'


data['Risk_Level'] = data['Marks'].apply(risk_level)


correlation = data['Marks'].corr(data['Attendance'])
print('Correlation between Attendance & Marks:', correlation)



for name in data['Name'].unique():
    temp = trend[trend['Name'] == name]
    plt.plot(temp['Semester'], temp['Marks'], marker='o', label=name)


plt.xlabel('Semester')
plt.ylabel('Average Marks')
plt.title('Student Performance Trends')
plt.legend()
plt.show()


subject_difficulty.plot(kind='bar', title='Subject Difficulty Index')
plt.ylabel('Average Marks')
plt.show()


plt.figure()
data.boxplot(column='Marks', by='Name')
plt.title('Performance Spread')
plt.suptitle('')
plt.show()