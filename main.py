import os
import csv

script_dir = os.path.dirname(os.path.realpath(__file__))
# root_folder = os.path.abspath(os.path.join(script_dir, "..", "..")) # when script is in another subfolder
root_folder = os.path.abspath(script_dir)
data_file = os.path.join(root_folder, "csv", "raw_data.csv")


def read_csv(): #1. Read the CSV file and store them in a list
    entries_list = []

    with open(data_file, 'r', encoding='cp949') as csvfile: #superset of euc-kr
        reader = csv.DictReader(csvfile)
        # header = next(reader)
        for row in reader:
            entry = row
            entries_list.append(entry)
    
    # return header, entries_list
    return entries_list

result = read_csv()
print(result)

# # Print the first entry
# print(result[0])

# # Access specific values by header name
# print(result[0]['header1'])