import pandas as pd

def add_features(df):
    df['TotalPrice'] = df['Sales'] * df['Quantity']
    df['OrderMonth'] = df['Order Date'].dt.to_period('M')
    return df

if __name__ == '__main__':
    df = pd.read_csv('data/cleaned_sales_data.csv', parse_dates=['Order Date'])
    df = add_features(df)
    df.to_csv('data/featured_sales_data.csv', index=False)
    print("✅ Features added and saved as 'featured_sales_data.csv'")