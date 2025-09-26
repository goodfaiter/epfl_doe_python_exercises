import numpy as np
import matplotlib.pyplot as plt
from scipy import io
import pandas as pd

# Load Data
file_path = '/workspace/data/Series_DOE_1_data_scientifc_publication.xlsx'
df = pd.read_excel(file_path)

# Display basic information about the data
print("Data shape:", df.shape)
print("Column names:", df.columns.tolist())
print("First 5 rows:")
print(df.head())

# Make the main plot object
plot = plt.figure(figsize=(15, 10))

# Set code as the main index
df.set_index('Code', inplace=True, drop=True)

# Add axis 1 looking for abberations
ax = plt.subplot(2, 2, 1)
colors = plt.cm.Paired(np.linspace(0, 1, len(df.index)))
for i, code in enumerate(df.index):
    ax.plot([2000 + i for i in range(18)], [df.loc[code, 2000 + i] for i in range(18)], color=colors[i], markersize=2, alpha=0.1)
ax.set_xticks([2000 + i for i in range(18)])
ax.set_xlabel('Year')
ax.set_ylabel('')
ax.grid(True, alpha=0.3)

# Add axis 2 looking for abberations
df.sort_values(by='pop2000', ascending=False, inplace=True)
ax = plt.subplot(2, 2, 2)
ax.semilogy([i for i in range(len(df.index))], [df.loc[code, 'pop2000'] for code in df.index], 'b-')
ax.semilogy([i for i in range(len(df.index))], [df.loc[code, 'pop2018'] for code in df.index], 'r-')

# Add axis 3 with relative change
df.loc[:, 'pop_diff'] = (df.loc[:, 'pop2018'] - df.loc[:, 'pop2000']) / df.loc[:, 'pop2000']
ax = plt.subplot(2, 2, 3)
ax.plot([i for i in range(len(df.index))], [df.loc[code, 'pop_diff'] for code in df.index], 'b-')

# Reset index before continuing
df.reset_index(inplace=True)

# Aggregate data by Region
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
aggregated = df.groupby('Region')[numeric_cols].agg(['mean', 'sum', 'std', 'min', 'max', 'count'])
ax = plt.subplot(2, 2, 4)
print(aggregated)
for indx in aggregated.index:
    ax.bar(indx, aggregated[2000]['mean'][indx])

# Save plots
plt.tight_layout()
plt.savefig('/workspace/data/01_exercise_01.png', dpi=300)

# Bubble plots
ax = plt.subplot(2, 2, 1)
ax.clear()
ax.scatter(aggregated['pop2000']['sum'].values, aggregated[2000]['sum'].values)
# Here we can add labeling code

ax = plt.subplot(2, 2, 2)
ax.clear()
df.sort_values(by=(2000), ascending=False, inplace=True)
cumsum = np.cumsum(df[2000].values)
ax.bar(range(len(df.index)), df[2000].values)
ax2 = ax.twinx()
ax2.plot(cumsum / cumsum[-1], 'r-')


plt.tight_layout()
plt.savefig('/workspace/data/01_exercise_02.png', dpi=300)
plt.show()