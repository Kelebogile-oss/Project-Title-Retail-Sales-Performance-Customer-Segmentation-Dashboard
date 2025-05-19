# kpi_analysis.py
import pandas as pd

def compute_kpis(df):
    kpis = {
        'Total Sales': df['Sales'].sum(),
        'Total Profit': df['Profit'].sum(),
        'Average Discount': df['Discount'].mean(),
        'Total Quantity Sold': df['Quantity'].sum(),
        'Profit Margin (%)': (df['Profit'].sum() / df['Sales'].sum()) * 100,
        'Top Category': df.groupby('Category')['Sales'].sum().idxmax(),
        'Top Customer': df.groupby('Customer Name')['Sales'].sum().idxmax(),
        'Most Frequent Segment': df['Segment'].mode()[0]
    }
    return kpis

if __name__ == '__main__':
    df = pd.read_csv('data/featured_sales_data.csv')
    kpi_dict = compute_kpis(df)
    for k, v in kpi_dict.items():
        print(f"{k}: {v}")