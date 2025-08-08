# Visualization For Performance Across Asset Classes

## Dataset
- File: `data.csv`
- Key Columns:
  - "#"
  - "Company"
  - "Symbol"
  - "Weight"
  - "Price"
  - "Chg"
  - "% Chg"

## Required Visualizations

1. **Grouped Bar Chart**
   - **Purpose**: Compare the combined market weight grouping the companies in batches of 10.
   - **Batches**
     - Batch 1 - 1-10
     - Batch 2 - 11-20
     - Batch 3 - 21-30
     - Batch 4 - 31-40
     - Batch 5 - 41-50
     - Batch 6 - 51-60
     - Batch 7 - 61-70
     - Batch 8 - 71-80
     - Batch 9 - 81-90
     - Batch 10 - 91-100
     - Batch 11 - 101-110
     - Batch 12 - 111-120
     - Batch 13 - 121-130
     - Batch 14 - 131-140
     - Batch 15 - 141-150
     - Batch 16 - 151-160
     - Batch 17 - 161-170
     - Batch 18 - 171-180
     - Batch 19 - 181-190
     - Batch 20 - 191-200
     - Batch 21 - 200-500
   - **X-axis**: Batch
   - **Y-axis**: Weight
   - **Bar Layout**: 
     - Display a bar for each batch of 10 companies.
   - **Color**: Assign a distinct color to each batch class.
   - **Formatting**: 
    - The Y-axis values should be percentages rounded to the nearest whole number.
    - The X-axis lables should include the range of comapanies in the batch.
   - **Output**: Save the output as a image file to the current working directory. Do not show as standard output.

2. **Table View**
  - **Purpose**: Show a table summarizing the combined market weight.
     - **Batches**
     - Batch 1 - 1-10
     - Batch 2 - 1-25
     - Batch 3 - 1-50
     - Batch 4 - 1-75
     - Batch 5 - 1-100
     - Batch 6 - 1-125
     - Batch 7 - 1-150
  - **Sorting**: Year
  - **Formatting**:
    - Show the year as a 4 digit integer.
    - Show values as percentages with no decimal places.
    - Lable each Batch with both the Batch Number and the range of companies in the batch.
  - **Output**: Save the output as a text file to the current working directory. Do not show as standard output.

3. **Table View**
  - **Purpose**: List the top 25 companies.
  - **Sorting**: '#'
  - **Columns**:
    - '#' as Rank
    - Company Name
    - Symbol
    - Weight
    - Price
  - **Output**: Save the output as a text file to the current working directory. Do not show as standard output.