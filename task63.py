import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('housing.csv')

#sns.scatterplot(data=df, x='households', y='population')
#sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)
#sns.histplot(data=df, x='housing_median_age')
sns.histplot(data=df, x='median_house_value', hue='housing_median_age')

plt.show()