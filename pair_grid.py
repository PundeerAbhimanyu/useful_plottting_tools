import seaborn as sns
import matplotlib.pyplot as plt

#load the data
df = sns.load_dataset('iris')

# data visualisation
sns.set(style = 'darkgrid')
g = sns.PairGrid(df ,hue = 'species', diag_sharey = False)
g.map_lower(sns.kdeplot)
g.map_upper(sns.scatterplot)
g.map_diag(sns.kdeplot )
plt.show()
