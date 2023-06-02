import csv

# open the input CSV file
with open(r"C:\Users\KIIT\Downloads\merged_data - Sheet1.csv", 'r') as infile:
    reader = csv.reader(infile)
    # skip the header row
    next(reader)
    # open a new CSV file to write the output
    with open('merged_data.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        # write the header row for the output file
        writer.writerow(['Latitude', 'Longitude', 'Direction', 'Vehicle ID', 'Wrong Side'])
        # loop over the rows in the input file
        for row in reader:
            # get the direction from the row
            direction = float(row[2])
            # check if the direction is within the range of wrong side driving
            if (direction > 60 and direction < 120) or (direction > 240 and direction < 300):
                # add a new column with the value 'True'
                row.append('True')
            else:
                # add a new column with the value 'False'
                row.append('False')
            # write the row to the output file
            writer.writerow(row)

