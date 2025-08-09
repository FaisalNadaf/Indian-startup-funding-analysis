# Indian-startup-Funding-Analysis

This project analyzes a startup funding dataset to uncover insights about funding trends, top sectors, leading cities, popular startups, and key investors. It also visualizes the results using Matplotlib and Seaborn.

## 📂 Dataset

The script expects a CSV file named `startup_funding.csv` located at:

```
/content/startup_funding.csv
```

### Example Columns:

* `Date dd/mm/yyyy`
* `Startup Name`
* `City Location`
* `Industry Vertical`
* `Investment Type`
* `Amount in USD`
* `Investors Name`

## ⚙️ Features

* **Data Cleaning:**

  * Standardizes date formats.
  * Removes null values for essential fields.
  * Cleans and formats text columns.
  * Corrects typos in column names.
  * Converts funding amounts to numeric format.

* **Analysis Performed:**

  * Funding trend over time (monthly).
  * Top 5 sectors by startup count.
  * Top 5 cities by startup count.
  * Top 5 startups by count.
  * Top 10 startups by total funding.
  * Top 10 investors by investment count.
  * Investment type distribution.

* **Visualizations:**

  * Line plot of monthly funding trends.
  * Bar plots for top sectors and top investors.

## 📊 Example Outputs

* **Funding Trend Over Time** (Monthly Line Chart)
* **Top Sectors** (Bar Chart)
* **Top Investors** (Bar Chart)

## 🛠️ Requirements

Install the dependencies with:

```bash
pip install pandas matplotlib seaborn
```

## ▶️ How to Run

1. Place your `startup_funding.csv` file in `/content/` (or update the script path).
2. Run the script:

   ```bash
   python main.py
   ```
3. View printed summaries in the console and charts in separate windows.



Do you want me to also **add usage examples with sample charts** into the README so it looks more like a professional GitHub project? That would make it more appealing.
