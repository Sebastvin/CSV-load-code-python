import seaborn as sns
import pandas as pd
import os

from matplotlib import pyplot as plt

for dirname, _, filenames in os.walk('CarPrice_Assignment.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('CarPrice_Assignment.csv')

# Print all content from csv
print(df)

df_num = df.select_dtypes(include=['float64', 'int64'])
df_fewnums = df_num[['enginesize', 'horsepower', 'carheight', 'price']]

corr = df_fewnums.corr()

plt.figure(figsize=(10, 10))
sns.boxplot(x='carbody', y='price', data=df)
# sns.distplot(df_fewnums['price'], bins=64)
# sns.pairplot(df_fewnums) chart of each element

# plt.figure(figsize=(5, 4))
# sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

cat_features = [col for col in list(df.columns) if df[col].dtype == 'object']

# Show categories from CSV
print(cat_features)

# CSV information
print(df.head())

df.drop(['CarName', 'car_ID'], inplace=True, axis=1)

# Information about shape CSV in console.
print(df.shape)
print(df.info())

# Show matrix image of date.
# plt.figure(figsize=(15, 10))
# sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)
# plt.show()

# Information with symboling from CSV
data = pd.get_dummies(df, drop_first=True)
print(data.head())
