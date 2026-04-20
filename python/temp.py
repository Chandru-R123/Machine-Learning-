import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('temp.csv')

df['Min_Temp'] = df['Min_Temp'].fillna(df['Min_Temp'].mean())
df['Max_Temp'] = df['Max_Temp'].fillna(df['Max_Temp'].mean())

df['Average_Temp'] = (df['Min_Temp'] + df['Max_Temp'])/2

highest_date = df.loc[df['Average_Temp'].idxmax(), 'Date']
print("Date with highest average temperature:",highest_date)

plt.plot(df['Date'],df['Average_Temp'], marker='x')
plt.title("Average Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Average Temperature")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()
