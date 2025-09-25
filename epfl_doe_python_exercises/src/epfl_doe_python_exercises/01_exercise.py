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

# Add axis 1
ax = plt.subplot(2, 1, 1)
ax.plot([2000 + i for i in range(18)], [df.loc['AFG', 2000 + i] for i in range(18)], 'bo', markersize=5, alpha=0.5)
ax.set_xticks([2000 + i for i in range(18)])
ax.set_xlabel('Year')
ax.set_ylabel('')
ax.grid(True, alpha=0.3)

# Reset index before continuing
df.reset_index(inplace=True)

# Aggregate data
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
aggregated = df.groupby('Region')[numeric_cols].agg(['mean', 'sum', 'std', 'min', 'max', 'count'])
ax = plt.subplot(2, 1, 2)
print(aggregated)
for indx in aggregated.index:
    ax.bar(indx, aggregated[2000]['mean'][indx])

plt.tight_layout()
plt.show()