import dask.dataframe as dd

# Correct file path
file_path = r"E:\SLTC\ICE\3rd Year\6th Sem\Big data\Project\dataset.csv"

# Specify column data types
dtypes = {
    'Biodiesel': 'float64',
    'Biomass Losses and Co-products': 'float64',
    'Fuel Ethanol, Excluding Denaturant': 'float64',
    'Other Biofuels': 'float64',
    'Renewable Diesel Fuel': 'float64',
    'Solar Energy': 'float64',
    'Wind Energy': 'float64'
}

# Read the CSV file with specified dtypes
dask_df = dd.read_csv(file_path, dtype=dtypes)

# Perform operations
print(dask_df.head())
