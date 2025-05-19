import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the featured dataset
df = pd.read_csv('data/featured_sales_data.csv', parse_dates=['Order Date'])

# Make sure the dashboard directory exists
os.makedirs('dashboard', exist_ok=True)

# Set a consistent and elegant visual style
sns.set(style="whitegrid", palette="pastel", font_scale=1.1)

def sales_by_category():
    plt.figure(figsize=(10, 6))
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=True)
    sns.barplot(x=category_sales.values, y=category_sales.index)
    plt.title('Total Sales by Category', fontsize=16)
    plt.xlabel('Sales')
    plt.ylabel('Category')
    plt.tight_layout()
    plt.savefig('dashboard/sales_by_category.png')
    plt.close()

def monthly_sales_trend():
    df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

    plt.figure(figsize=(14, 6))
    sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o', color='crimson')
    plt.xticks(rotation=45)
    plt.title('Monthly Sales Trend', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig('dashboard/monthly_sales_trend.png')
    plt.close()

def top_10_customers_by_sales():
    top_customers = df.groupby('Customer Name')['Sales'].sum().nlargest(10).sort_values()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_customers.values, y=top_customers.index, palette='muted')
    plt.title('Top 10 Customers by Sales', fontsize=16)
    plt.xlabel('Sales')
    plt.ylabel('Customer Name')
    plt.tight_layout()
    plt.savefig('dashboard/top_10_customers_by_sales.png')
    plt.close()

def profit_by_region():
    region_profit = df.groupby('Region')['Profit'].sum().reset_index()

    plt.figure(figsize=(8, 6))
    sns.barplot(data=region_profit, x='Region', y='Profit', palette='Set2')
    plt.title('Profit by Region', fontsize=16)
    plt.ylabel('Profit')
    plt.xlabel('Region')
    plt.tight_layout()
    plt.savefig('dashboard/profit_by_region.png')
    plt.close()

def main():
    print("Generating beautiful dashboard visuals in 'dashboard/' directory...")
    sales_by_category()
    monthly_sales_trend()
    top_10_customers_by_sales()
    profit_by_region()
    print("✅ All charts saved successfully!")

if __name__ == "__main__":
    main()
