import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[logging.FileHandler("test_log.txt", mode='a'), logging.StreamHandler()]
)
logger = logging.getLogger()

# Dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# 1. Matplotlib Line Chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1) # Side-by-side plot (1 row, 2 columns, plot 1)
plt.plot(months, sales, marker='o', color='b', linestyle='-')
plt.title('Monthly Sales (Matplotlib Line)')
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.grid(True)

# 2. Seaborn Bar Plot
plt.subplot(1, 2, 2) # Plot 2
sns.barplot(x=months, y=sales, palette='viridis', hue=months, legend=False)
plt.title('Monthly Sales (Seaborn Bar)')
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout and save
plt.tight_layout()
plt.savefig("sales_comparison.png")
logger.info("Visualizations generated and saved as 'sales_comparison.png'.")

plt.show()