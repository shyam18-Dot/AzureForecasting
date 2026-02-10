import pandas as pd
import numpy as np


df = pd.read_csv(r"c:\Users\HP\Downloads\cloud_usage_26.csv")
print("=" * 50)
print("INITIAL DATA")
print("=" * 50)
print(df.head())
print(f"\nShape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}")


df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df.sort_values(by='timestamp')


invalid_timestamps = df['timestamp'].isnull().sum()
if invalid_timestamps > 0:
    print(f"\n⚠ Removing {invalid_timestamps} rows with invalid timestamps")
    df = df.dropna(subset=['timestamp'])


df['region'] = df['region'].str.strip()  
df['region'] = df['region'].str.lower().str.replace(" ", "-")
df['region'] = df['region'].replace({
    'us-east': 'US-East',
    'india-south': 'India-South'
})


initial_count = len(df)
df = df.drop_duplicates()
duplicates_removed = initial_count - len(df)
if duplicates_removed > 0:
    print(f"\n✓ Removed {duplicates_removed} duplicate rows")


df = df.dropna(how='all', subset=['usage_units', 'cost_usd'])


negative_usage = (df['usage_units'] < 0).sum()
negative_cost = (df['cost_usd'] < 0).sum()
if negative_usage > 0:
    print(f"\n⚠ Found {negative_usage} negative usage values - setting to NaN")
    df.loc[df['usage_units'] < 0, 'usage_units'] = np.nan
if negative_cost > 0:
    print(f"\n⚠ Found {negative_cost} negative cost values - setting to NaN")
    df.loc[df['cost_usd'] < 0, 'cost_usd'] = np.nan


def remove_outliers_iqr(data, column, multiplier=1.5):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    
    outliers = ((data[column] < lower_bound) | (data[column] > upper_bound))
    outlier_count = outliers.sum()
    
    if outlier_count > 0:
        print(f"\n⚠ Found {outlier_count} outliers in '{column}' (IQR method)")
        print(f"  Range: [{lower_bound:.2f}, {upper_bound:.2f}]")
       
        data.loc[data[column] < lower_bound, column] = lower_bound
        data.loc[data[column] > upper_bound, column] = upper_bound
    
    return data

if df['usage_units'].notna().sum() > 0:
    df = remove_outliers_iqr(df, 'usage_units')
if df['cost_usd'].notna().sum() > 0:
    df = remove_outliers_iqr(df, 'cost_usd')

df['usage_units'] = df['usage_units'].interpolate(method='linear')
df['cost_usd'] = df['cost_usd'].fillna(df['usage_units'] * 0.5)


if len(df) > 0:
    df['cost_per_unit'] = df['cost_usd'] / df['usage_units'].replace(0, np.nan)
    median_cost_per_unit = df['cost_per_unit'].median()
    
    
    inconsistent = ((df['cost_per_unit'] > median_cost_per_unit * 5) | 
                    (df['cost_per_unit'] < median_cost_per_unit * 0.2))
    inconsistent_count = inconsistent.sum()
    
    if inconsistent_count > 0:
        print(f"\n⚠ Found {inconsistent_count} rows with inconsistent cost/usage ratio")
      
        df.loc[inconsistent, 'cost_usd'] = df.loc[inconsistent, 'usage_units'] * median_cost_per_unit
    
   
    df = df.drop(columns=['cost_per_unit'])


df = df.dropna(subset=['timestamp', 'region', 'usage_units', 'cost_usd'])


df = df.reset_index(drop=True)

print("\n" + "=" * 50)
print("CLEANED DATA SUMMARY")
print("=" * 50)
print(f"Final shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nNumerical summary:\n{df[['usage_units', 'cost_usd']].describe()}")
print(f"\nRegion distribution:\n{df['region'].value_counts()}")
print(f"\nDate range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print("\n✓ Data cleaning complete!")
print("=" * 50)
