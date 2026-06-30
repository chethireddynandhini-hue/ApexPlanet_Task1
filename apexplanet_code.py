import pandas as pd

# Load dataset
df = pd.read_excel(r"N:\New folder\ApexPlanet_DataAnalytics_Dataset.xlsx")

#DATA PROFILING

print("Original Shape:", df.shape)

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include="all"))

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

#DATA CLEANING 

# Remove duplicates
df = df.drop_duplicates()

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing City values with mode
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Remove extra spaces
text_cols = ["Customer_Name", "Gender", "City", "Product", "Category"]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# Standardize date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Month column
df["Order_Month"] = df["Order_Date"].dt.month_name()

# Create Year column
df["Order_Year"] = df["Order_Date"].dt.year

# Create Age Group column
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 25, 35, 50, 100],
    labels=["18-25", "26-35", "36-50", "50+"]
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nFinal Shape:", df.shape)

print("\nNew Columns Added:")
print(["Order_Month", "Order_Year", "Age_Group"])

df.to_excel("Cleaned_Sales_Dataset.xlsx", index=False)

print("\nCleaned dataset saved successfully!")