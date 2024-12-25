import pandas as pd
import os

file_path = os.path.join("Data", "HouseData.csv")
house_data = pd.read_csv(file_path)

house_data['price_per_sqft'] = house_data.apply(
    lambda row: row['price'] / row['house_size'] if pd.notnull(row['price']) and pd.notnull(row['house_size']) else None,
    axis=1
)

def categorize_price(price):
    if pd.isnull(price):
        return None
    elif price < 100000:
        return "Low"
    elif 100000 <= price <= 300000:
        return "Medium"
    else:
        return "High"

def categorize_lot_size(lot_size):
    if pd.isnull(lot_size):
        return None
    elif lot_size < 0.1:
        return "Small"
    elif 0.1 <= lot_size <= 0.5:
        return "Medium"
    else:
        return "Large"

def calculate_bed_bath_ratio(row):
    if pd.notnull(row['bed']) and pd.notnull(row['bath']) and row['bath'] != 0:
        return row['bed'] / row['bath']
    else:
        return None

house_data['price_category'] = house_data['price'].apply(categorize_price)
house_data['lot_size_category'] = house_data['acre_lot'].apply(categorize_lot_size)
house_data['bed_bath_ratio'] = house_data.apply(calculate_bed_bath_ratio, axis=1)

output_path = "HouseDataNew.csv"
house_data.to_csv(output_path, index=False)

print(f"Güncellenmiş veri '{output_path}' dosyasına kaydedildi.")