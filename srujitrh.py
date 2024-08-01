import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



titanic = pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\repo\\tested.csv")

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Age', data=titanic)
plt.title('Boxplot of Age by Pclass')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
titanic['Survived'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'], labels=['Died', 'Survived'])
plt.title('Pie Chart of Survival')
plt.ylabel('')
plt.show()

# Bar plot
plt.figure(figsize=(10, 6))
sns.countplot(x='Pclass', hue='Survived', data=titanic, palette='viridis')
plt.title('Bar Plot of Survival by Pclass')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=titanic, palette='coolwarm')
plt.title('Scatter Plot of Age vs Fare')
plt.show()