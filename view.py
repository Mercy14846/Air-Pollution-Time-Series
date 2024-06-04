import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("1_air_quality_data.csv")

# Descriptive statistics
desc_stats = data.describe()
print(desc_stats)

# Time series plot
plt.figure(figsize=(14, 7))
# for location in data.columns:
#     plt.plot(data.index, data[location], label=location)
plt.xlabel('elevation')
plt.ylabel('top')
plt.title('Air Quality Index Over Time')
plt.legend()
# plt.show()

# Correlation matrix
corr_matrix = data.corr(method='kendell')
print(corr_matrix)

# Heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of AQI Between Locations')
plt.show()
