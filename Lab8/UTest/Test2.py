import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from dash import Dash, dcc, html

# 1. Load Data from a CSV File
# Replace 'your_file.csv' with the path to your CSV file.
file_path = '../Assets/your_file.csv'
data = pd.read_csv(file_path)

# Assuming the CSV file has columns 'Date', 'Sales_Amount', 'Advertising_Spend', and 'Product'.
data['Date'] = pd.to_datetime(data['Date'])

# 2. Identify Extreme Values by Column
print("Extreme Values by Column:")
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    print(f"{column} - Min: {data[column].min()}, Max: {data[column].max()}")

# 3. Preprocessing the Data
# Filtering data for the example, e.g., removing rows with null values.
data.dropna(inplace=True)

# Aggregate sales by product category for plotting purposes.
product_sales = data.groupby('Product')['Sales_Amount'].sum().sort_values()

# 4. Create Basic Visualization for a Single Variable
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Sales_Amount'], marker='o', color='skyblue')
plt.title('Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.grid()
plt.savefig("sales_amount_basic.png", format='png')
plt.show()

# 5. Multiple Sub-Charts in a Single Figure
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Multiple Data Visualizations")

# Subplot 1: Line Plot
axs[0, 0].plot(data['Date'], data['Sales_Amount'], color='blue', marker='o')
axs[0, 0].set_title("Sales Amount Over Time")
axs[0, 0].set_xlabel("Date")
axs[0, 0].set_ylabel("Sales Amount")
axs[0, 0].tick_params(axis='x', rotation=45)

# Subplot 2: Bar Plot
axs[0, 1].bar(product_sales.index, product_sales.values, color='green')
axs[0, 1].set_title("Total Sales by Product")
axs[0, 1].set_xlabel("Product")
axs[0, 1].set_ylabel("Sales Amount")
axs[0, 1].tick_params(axis='x', rotation=45)

# Subplot 3: Histogram
axs[1, 0].hist(data['Sales_Amount'], bins=20, color='purple', edgecolor='black')
axs[1, 0].set_title("Distribution of Sales Amount")
axs[1, 0].set_xlabel("Sales Amount")
axs[1, 0].set_ylabel("Frequency")

# Subplot 4: Scatter Plot with Trend Line
sns.regplot(x='Advertising_Spend', y='Sales_Amount', data=data, ax=axs[1, 1], scatter_kws={'alpha':0.6}, line_kws={"color":"red"})
axs[1, 1].set_title("Sales Amount vs. Advertising Spend")
axs[1, 1].set_xlabel("Advertising Spend")
axs[1, 1].set_ylabel("Sales Amount")

# Save the multiple subplots figure
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("multiple_data_visualizations.png", format='png')
plt.show()

# 6. Interactive HTML Visualization with Plotly
fig = px.line(data, x='Date', y='Sales_Amount', title='Sales Amount Over Time')
fig.write_html("sales_amount_interactive.html")
fig.show()

# Export as an interactive image (optional, requires Kaleido)
fig.write_image("sales_amount_interactive.png")

# 7. Building an Interactive Web App with Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Amount Over Time"),
    dcc.Graph(
        id="line-chart",
        figure=px.line(data, x='Date', y='Sales_Amount', title='Sales Amount Over Time')
    ),
    dcc.Graph(
        id="scatter-chart",
        figure=px.scatter(data, x='Advertising_Spend', y='Sales_Amount', trendline='ols', title='Sales vs. Advertising Spend')
    )
])

# Run the Dash app (for web app use; comment out if not testing the app)
# if __name__ == '__main__':
#     app.run_server(debug=True)
