import os
import csv
from collections import defaultdict

script_dir = os.path.dirname(os.path.realpath(__file__))
root_folder = os.path.abspath(script_dir)
data_file = os.path.join(root_folder, "csv", "raw_data.csv")

def read_csv(): #1. Read the CSV file and store them in a list
    non_sbj_keys = ['이름', '학년', '반', '번호']
    class_dict = defaultdict(list) # creates dictionary with each value of a default data type (list in this case).
    # When you access a key that doesn't exist, it automatically creates that key and initializes it with the default value (empty list in this case).
    ## 'grouped_classes' is a dictionary where each key represents a group (like 'a', 'b', 'c') and each value is initially an empty list. 

    with open(data_file, 'r', encoding='cp949') as csvfile: #superset of euc-kr
        csv_reader = csv.DictReader(csvfile)
        
        sbj_keys = [key for key in csv_reader.fieldnames if key not in non_sbj_keys]

        for row in csv_reader:
            class_key = row['반']
            class_dict[class_key].append(row)
    
    return sbj_keys, class_dict

def get_sbj_groups(sbj_keys, class_dict):
    for class_key, classes in class_dict.items():
        print(f"Class: {class_key}")
        for entry in classes:  # working
            # Perform filtering here if needed
            # For example, filtering entries with presence-in-sbj1 == 'true'
            print(entry)
            # if entry['생활과윤리'] == 'true':
                # print(entry)


def generate_excel_files():
    sbj_keys, class_dict = read_csv()
    get_sbj_groups(sbj_keys, class_dict)

generate_excel_files()
