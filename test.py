import pandas as pd
import matplotlib.pyplot as plt

# Replace "your_data.csv" with the actual path to your CSV file
csv_file_path = "homelessness-report-september-2023.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame to verify the data has been loaded
#print(df.head())


# Replace "Total Adults" with the column name you want to plot
#column_to_plot = "Total Adults"
#columns_to_plot = ["Total Adults", "Male Adults", "Female Adults", "Adults Aged 18-24"]


# Assuming df is your DataFrame with the loaded data
df.plot(kind='bar', figsize=(12, 8))
plt.title('Population Statistics by Region')
plt.xlabel('Region')
plt.ylabel('Population')
plt.show()