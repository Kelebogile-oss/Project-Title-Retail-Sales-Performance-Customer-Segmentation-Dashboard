# rfm_segmentation.py
import pandas as pd
from datetime import datetime

def calculate_rfm(df):
    current_date = datetime(2015, 1, 1)
    rfm = df.groupby('Customer ID').agg({
        'Order Date': lambda x: (current_date - x.max()).days,
        'Order ID': 'nunique',
        'Sales': 'sum'
    })
    rfm.columns = ['Recency', 'Frequency', 'Monetary']

    # Segment customers
    rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1]).astype(int)
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4]).astype(int)
    rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4]).astype(int)
    rfm['RFM_Score'] = rfm[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)

    return rfm

if __name__ == '__main__':
    df = pd.read_csv('data/featured_sales_data.csv', parse_dates=['Order Date'])
    rfm_df = calculate_rfm(df)
    rfm_df.to_csv('data/rfm_segmented.csv')
    print("✅ RFM segmentation complete and saved as 'rfm_segmented.csv'")