
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = pd.read_csv('/Users/adrian/Downloads/dermatology/dermatology.data')
print(data.columns)
print(data)
data.drop(0,axis=0,inplace=True)
data.drop('age',axis=1,inplace=True)
dataclean=data.replace(40, "?") 
print(dataclean)
fig, ax = plt.subplots()
positionlocationlist = []
for i in range(1,34):
       positionlocationlist.append(i*2)
vp = ax.boxplot(dataclean, positions=positionlocationlist, widths=1.5, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "white", "linewidth": 0.5},
                boxprops={"facecolor": "C0", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 3},
                capprops={"color": "C0", "linewidth": 1.5})

ax.set(xlim=(0, 70), xticks=np.arange(1, 70, 2),
       ylim=(0, 100), yticks=np.arange(1, 3))

plt.show()
"""plt.scatter(x='erythema', y='age', data=data)
plt.scatter(data['erythema'], data['age'], data['scaling'], data['definite'])
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot')

plt.show()
"""