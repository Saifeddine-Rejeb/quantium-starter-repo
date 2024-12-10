import csv
import os

DATA = './data'
OUTPUT = './formatted_data.csv'

with open(OUTPUT, 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    header = ['Sales', 'Date', 'Region']
    writer.writerow(header) 

    for file in os.listdir(DATA):
        with open(os.path.join(DATA, file), 'r') as in_file:
            reader = csv.DictReader(in_file)
            
            for row in reader:
                if row['product'] == "pink morsel":
                    price = float(row['price'][1:])
                    sale = price * int(row['quantity'])
                    output_row = [sale, row['date'], row['region']]
                    writer.writerow(output_row)
