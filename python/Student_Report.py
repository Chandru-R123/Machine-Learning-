import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('students.csv')

df['Completion_Status'] = df['Completion_Status'].fillna("No")

counts = df['Completion_Status'].value_counts()
print("Completion Count:\n", counts)
counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Course Completion Status")
plt.ylabel("")
plt.show()
