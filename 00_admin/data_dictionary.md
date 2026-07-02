# Data Dictionary — Global Superstore Dataset

## Source
Kaggle — Global Super Store Dataset  
URL: https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset

## Dataset Overview
- Rows: 51,290
- Columns: 24
- Time Period: 2011–2014

## Column Descriptions

| Column | Type | Description |
|---|---|---|
| Row ID | Integer | Unique row identifier |
| Order ID | String | Unique order identifier (format: XX-YYYY-NNNNNN) |
| Order Date | Date | Date the order was placed |
| Ship Date | Date | Date the order was shipped |
| Ship Mode | String | Shipping method (First Class, Second Class, Standard Class, Same Day) |
| Customer ID | String | Unique customer identifier |
| Customer Name | String | Full name of the customer |
| Segment | String | Customer segment (Consumer, Corporate, Home Office) |
| City | String | City of delivery |
| State | String | State of delivery |
| Country | String | Country of delivery |
| Postal Code | String | Postal code of delivery address |
| Market | String | Market region (Africa, APAC, Canada, EMEA, EU, LATAM, US) |
| Region | String | Sub-region within market |
| Product ID | String | Unique product identifier |
| Category | String | Product category (Furniture, Office Supplies, Technology) |
| Sub-Category | String | Product sub-category (e.g. Chairs, Phones, Binders) |
| Product Name | String | Full product name |
| Sales | Float | Revenue from the order (USD) |
| Quantity | Integer | Number of units ordered |
| Discount | Float | Discount applied (0.0 to 1.0) |
| Profit | Float | Profit from the order (USD, can be negative) |
| Shipping Cost | Float | Cost of shipping (USD) |
| Order Priority | String | Priority level (Critical, High, Medium, Low) |

## Derived Columns (added during analysis)
| Column | Created In | Description |
|---|---|---|
| Profit Margin | Practical 8 | Profit divided by Sales |
| Shipping Delay | Practical 8 | Days between Order Date and Ship Date |
| Profitability | Practical 4 | "Profitable" if Profit > 0, else "Loss" |
| Target | Practical 8 | Binary label — 1 (Profitable), 0 (Loss) |
| Cluster | Practical 9 | K-Means cluster label (0–3) |
