import pandas as pd
import numpy as np

# Generate a sample dataset
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Sales_Amount': np.random.randint(200, 500, 10),
    'Advertising_Spend': np.random.randint(100, 300, 10),
    'Product': np.random.choice(['Product A', 'Product B', 'Product C'], 10)
})

# Save as CSV
data.to_csv('your_file.csv', index=False)
print("Sample dataset saved as your_file.csv")

