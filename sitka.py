import csv

filename = 'data_files/the_csv_file_format/data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index,column_header in enumerate(header_row):
        print(index,column_header)