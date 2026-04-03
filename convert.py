import csv
import os

input_files = [
    r"c:\Users\amolg\quantium!\data\datafile1.csv",
    r"c:\Users\amolg\quantium!\data\datafile2.csv",
    r"c:\Users\amolg\quantium!\data\datafile3.csv"
]
output_file = r"c:\Users\amolg\quantium!\data\output.csv"


with open(output_file, 'w', newline='') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(['Sales', 'Date', 'Region'])
    
    for input_file in input_files:
        with open(input_file, 'r') as f_in:
            reader = csv.reader(f_in)
            header = next(reader)
            
            # Find indices
            product_idx = header.index("product")
            price_idx = header.index("price")
            quantity_idx = header.index("quantity")
            date_idx = header.index("date")
            region_idx = header.index("region")
            
            for row in reader:
                
                if row[product_idx] == "pink morsel":
                    price_str = row[price_idx].replace('$', '')
                    price = float(price_str)
                    quantity = int(row[quantity_idx])
                    sales = price * quantity
                    
                    writer.writerow([sales, row[date_idx], row[region_idx]])

print("Files converted successfully!")
