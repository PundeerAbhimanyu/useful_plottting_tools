import seaborn as sns
import matplotlib.pyplot as plt

# loading data
df = sns.load_dataset("iris")

#plotting data
sns.set(style="ticks")

sns.pairplot(df, hue = 'species')
plt.show()

