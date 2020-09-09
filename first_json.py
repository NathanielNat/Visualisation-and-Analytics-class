import json

# Explore the structure of the data. 
basepath = 'data_files/'
filename =  basepath +'mapping_global_data_sets/data/eq_data_1_day_m1.json' 
with open(filename) as f:
    all_eq_data = json.load(f)
readable_file = basepath +'mapping_global_data_sets/data/readable_eq_data.json' 
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)