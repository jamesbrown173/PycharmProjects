import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
csv_file_path = '/Users/jamesbrown/PycharmProjects/csv-to-pdf-test/french.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path, low_memory=False)


# Create a table plot
fig, ax = plt.subplots(figsize=(8, 6)) 
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns, cellLoc = 'center', loc='center')

# Save the plot to a PDF file
pdf_file_path = '/Users/jamesbrown/PycharmProjects/csv-to-pdf-test/french.pdf'  # Replace with your desired output PDF file path
plt.savefig(pdf_file_path, format='pdf', bbox_inches='tight')

# Display a success message
print(f'CSV file "{csv_file_path}" successfully exported to PDF: "{pdf_file_path}"')

