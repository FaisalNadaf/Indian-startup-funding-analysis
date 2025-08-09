import pandas as pd
df=pd.read_csv('/content/startup_funding.csv')
display(df.head())
display(df.info())


--------------------------------------------------------------------------------------------------


# Drop the 'Remarks' column if it exists
if 'Remarks' in df.columns:
    df = df.drop('Remarks', axis=1)

# Fill missing values in specified columns with 'Unknown'
for col in ['Industry Vertical', 'SubVertical', 'City  Location', 'Investors Name', 'InvestmentnType']:
    df[col].fillna('Unknown', inplace=True)

# Clean 'Amount in USD': remove commas and plus signs, convert to numeric, fill missing with 0
df['Amount in USD'] = df['Amount in USD'].astype(str).str.replace(',', '', regex=False).str.replace('+', '', regex=False)
df['Amount in USD'] = pd.to_numeric(df['Amount in USD'], errors='coerce')
df['Amount in USD'].fillna(0, inplace=True)

# Clean 'Date dd/mm/yyyy': convert to datetime objects, handle potential errors
df['Date dd/mm/yyyy'] = pd.to_datetime(df['Date dd/mm/yyyy'], format='%d/%m/%Y', errors='coerce')

# Handle inconsistent formats in specified columns
for col in ['Startup Name', 'Industry Vertical', 'SubVertical', 'City  Location', 'Investors Name', 'InvestmentnType']:
    df[col] = df[col].astype(str).str.strip().str.replace(r'[^\x00-\x7F]+', '', regex=True) # Remove non-ASCII characters and trim
    df[col] = df[col].str.replace(r'\s+', ' ', regex=True) # Handle multiple spaces
    df[col] = df[col].str.lower() # Convert to lowercase for consistency

display(df.info())
display(df.head())


--------------------------------------------------------------------------------------------------

df['FundingYear'] = df['Date dd/mm/yyyy'].dt.year
df['FundingMonth'] = df['Date dd/mm/yyyy'].dt.month
yearly_funding_trends = df.groupby('FundingYear').agg(
    total_funding_usd=('Amount in USD', 'sum'),
    number_of_deals=('Sr No', 'count')
).reset_index()
display(yearly_funding_trends)

--------------------------------------------------------------------------------------------------

monthly_funding_trends = df.groupby('FundingMonth').agg(
    total_funding_usd=('Amount in USD', 'sum'),
    number_of_deals=('Sr No', 'count')
).reset_index()
display(monthly_funding_trends)

--------------------------------------------------------------------------------------------------

# Group by Industry Vertical and sum the funding amount
sector_funding = df.groupby('Industry Vertical')['Amount in USD'].sum().reset_index()
sector_funding = sector_funding.sort_values(by='Amount in USD', ascending=False)
print("Top 10 Sectors by Funding:")
display(sector_funding.head(10))

# Group by City Location and sum the funding amount
city_funding = df.groupby('City  Location')['Amount in USD'].sum().reset_index()
city_funding = city_funding.sort_values(by='Amount in USD', ascending=False)
print("\nTop 10 Cities by Funding:")
display(city_funding.head(10))

# Group by Startup Name and sum the funding amount
startup_funding = df.groupby('Startup Name')['Amount in USD'].sum().reset_index()
startup_funding = startup_funding.sort_values(by='Amount in USD', ascending=False)
print("\nTop 10 Startups by Funding:")
display(startup_funding.head(10))

--------------------------------------------------------------------------------------------------

investor_activity = df.groupby('Investors Name').agg(
    total_funding_usd=('Amount in USD', 'sum'),
    number_of_deals=('Sr No', 'count')
).reset_index()


--------------------------------------------------------------------------------------------------

top_investors_by_funding = investor_activity.sort_values(by='total_funding_usd', ascending=False)
print("Top 10 Investors by Total Funding:")
display(top_investors_by_funding.head(10))
top_investors_by_deals = investor_activity.sort_values(by='number_of_deals', ascending=False)
print("Top 10 Investors by Number of Deals:")
display(top_investors_by_deals.head(10))

--------------------------------------------------------------------------------------------------

investment_type_summary = df.groupby('InvestmentnType').agg(
    total_funding_usd=('Amount in USD', 'sum'),
    number_of_deals=('Sr No', 'count')
).reset_index()
investment_type_summary_by_funding = investment_type_summary.sort_values(by='total_funding_usd', ascending=False)
print("Investment Types by Total Funding:")
display(investment_type_summary_by_funding)
investment_type_summary_by_deals = investment_type_summary.sort_values(by='number_of_deals', ascending=False)
print("\nInvestment Types by Number of Deals:")
display(investment_type_summary_by_deals)

--------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# 1: Yearly Funding Trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_funding_trends, x='FundingYear', y='total_funding_usd',
             marker='o', label='Total Funding (USD)')
sns.lineplot(data=yearly_funding_trends, x='FundingYear', y='number_of_deals', marker='o', label='Number of Deals')
plt.title('Yearly Funding Trends')
plt.xlabel('Year')
plt.ylabel('Amount / Count')
plt.xticks(yearly_funding_trends['FundingYear'])
plt.grid(True)
plt.legend()
plt.show()

--------------------------------------------------------------------------------------------------


import seaborn as sns
import matplotlib.pyplot as plt

# 1: Yearly Funding Trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_funding_trends, x='FundingYear', y='total_funding_usd',
             marker='o', label='Total Funding (USD)')
sns.lineplot(data=yearly_funding_trends, x='FundingYear', y='number_of_deals', marker='o', label='Number of Deals')
plt.title('Yearly Funding Trends')
plt.xlabel('Year')
plt.ylabel('Amount / Count')
plt.xticks(yearly_funding_trends['FundingYear'])
plt.grid(True)
plt.legend()
plt.show()

# 2. Top 10 Sectors by Funding
plt.figure(figsize=(14, 7))
sns.barplot(data=sector_funding.head(10), x='Industry Vertical', y='Amount in USD', palette='viridis')
plt.title('Top 10 Sectors by Total Funding')
plt.xlabel('Industry Vertical')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 3. Top 10 Cities by Funding
plt.figure(figsize=(14, 7))
sns.barplot(data=city_funding.head(10), x='City  Location', y='Amount in USD', palette='viridis')
plt.title('Top 10 Cities by Total Funding')
plt.xlabel('City Location')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 4. Top 10 Startups by Funding
plt.figure(figsize=(14, 7))
sns.barplot(data=startup_funding.head(10), x='Startup Name', y='Amount in USD', palette='viridis')
plt.title('Top 10 Startups by Total Funding')
plt.xlabel('Startup Name')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 5. Top 10 Investors by Funding
plt.figure(figsize=(14, 7))
sns.barplot(data=top_investors_by_funding.head(10), x='Investors Name', y='total_funding_usd', palette='viridis')
plt.title('Top 10 Investors by Total Funding')
plt.xlabel('Investors Name')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 6. Top 10 Investors by Deals
plt.figure(figsize=(14, 7))
sns.barplot(data=top_investors_by_deals.head(10), x='Investors Name', y='number_of_deals', palette='viridis')
plt.title('Top 10 Investors by Number of Deals')
plt.xlabel('Investors Name')
plt.ylabel('Number of Deals')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 7. Top 10 Investment Types by Funding
plt.figure(figsize=(14, 7))
sns.barplot(data=investment_type_summary_by_funding.head(10), x='InvestmentnType', y='total_funding_usd', palette='viridis')
plt.title('Top 10 Investment Types by Total Funding')
plt.xlabel('Investment Type')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 8. Top 10 Investment Types by Deals
plt.figure(figsize=(14, 7))
sns.barplot(data=investment_type_summary_by_deals.head(10), x='InvestmentnType',
y='number_of_deals', palette='viridis')
plt.title('Top 10 Investment Types by Number of Deals')
plt.xlabel('Investment Type')
plt.ylabel('Number Of Deals')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



--------------------------------------------------------------------------------------------------
