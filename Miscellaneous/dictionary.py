import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the inventory dataset
data = {
    'Product_ID': [f'P{1000 + i}' for i in range(10)],
    'Product_Name': [
        'Laptop', 'Smartphone', 'Keyboard', 'Monitor', 'Mouse',
        'Printer', 'Headphones', 'Speakers', 'Webcam', 'Tablet'
    ],
    'Category': [
        'Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories',
        'Electronics', 'Accessories', 'Accessories', 'Accessories', 'Electronics'
    ],
    'Quantity': np.random.randint(1, 100, size=10),
    'Supplier': [
        'Supplier A', 'Supplier B', 'Supplier A', 'Supplier C', 'Supplier B',
        'Supplier A', 'Supplier D', 'Supplier C', 'Supplier D', 'Supplier B'
    ],
    'Purchase_Price': np.round(np.random.uniform(20, 500, size=10), 2),
    'Selling_Price': np.round(np.random.uniform(30, 600, size=10), 2),
    'Stock_Date': [
        (datetime.now() - timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d') for _ in range(10)
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame to verify
print(df)