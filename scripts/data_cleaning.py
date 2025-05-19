import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, delimiter=';', dtype=str)

    # Convert numeric columns (replace comma with dot for float conversion)
    numeric_cols = ['Sales', 'Quantity', 'Discount', 'Profit']
    for col in numeric_cols:
        df[col] = df[col].str.replace(',', '.', regex=False).astype(float)

    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%Y/%m/%d')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%Y/%m/%d')

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    return df

if __name__ == '__main__':
    df = load_and_clean_data('data/Superstore.csv')
    df.to_csv('data/cleaned_sales_data.csv', index=False)
    print("✅ Data cleaned and saved as 'cleaned_sales_data.csv'")