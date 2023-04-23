import csv

# Open the input file
with open('toClean2020.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header row
    
    # Create a dictionary to hold the parameters grouped by ID
    parameters_by_id = {}
    
    # Iterate over the rows in the input file
    for row in reader:
        # Parse the ID and parameter values from the row
        id_values = []
        param_values = []
        for i in range(0, 12, 2):
            if row[i] != '':
                id_values.append(int(row[i]))
                param_values.append(row[i+1])
        
        # Group the parameters by ID
        for id_value, param_value in zip(id_values, param_values):
            if id_value not in parameters_by_id:
                parameters_by_id[id_value] = [param_value]
            else:
                parameters_by_id[id_value].append(param_value)
                
    # Open the output file
    with open('clean2020.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write the header row
        writer.writerow(['ID'] + ['P{}'.format(i) for i in range(1, 7)])
        
        # Iterate over the IDs in ascending order
        for id_value in sorted(parameters_by_id.keys()):
            # Check if all six parameters are present for this ID
            if len(parameters_by_id[id_value]) == 6:
                # Write the ID and parameter values to a new row
                writer.writerow([id_value] + parameters_by_id[id_value])
