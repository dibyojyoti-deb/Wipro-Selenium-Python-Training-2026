import pandas as pd
import matplotlib.pyplot as plt
import logging

# 1. Logging Setup (Txt file)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[logging.FileHandler("pandas_output_log.txt", mode='w'), logging.StreamHandler()]
)
logger = logging.getLogger()

# 2. Create Source
data = {"Product": ["A", "B", "C"], "Quantity": [10, 5, 8], "Price": [50, 100, 75]}
pd.DataFrame(data).to_excel('pandas_source.xlsx', sheet_name='2025', index=False)
logger.info("Source file 'pandas_source.xlsx' created.")

# 3. Process
df = pd.read_excel('pandas_source.xlsx', sheet_name='2025')
df['Total'] = df['Quantity'] * df['Price']
df.to_excel('pandas_summary.xlsx', index=False)
logger.info(f"DataFrame Processed:\n{df.to_string()}")

# 4. Save PNG Chart
plt.figure(figsize=(6, 4))
plt.bar(df['Product'], df['Total'], color='skyblue')
plt.title('Pandas Chart')
plt.savefig('pandas_chart_image.png')
plt.close()
logger.info("Saved log to pandas_output_log.txt and chart to pandas_chart_image.png")