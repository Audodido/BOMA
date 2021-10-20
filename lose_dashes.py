import csv


with open('starts.csv', 'r') as csvFile:
    # csvFile.read()
    start_points_raw = [c for c in csvFile]

    out_string = ""

    for point in start_points_raw:
        out = point.replace('-', '')
        out = out.replace('(palm)', '')
        out_string = out_string + out

    print(out_string)

with open ("no_dashes.txt", "w") as f:
    f.write(out_string)

# # print(type(out))
#     f.write(out_string)
#     print(out_string)


        
    # print(out)
