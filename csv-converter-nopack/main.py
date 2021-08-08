import csv

with open('bao.csv', mode='r') as csv_file_in, open('ward_converted.csv', mode='w') as csv_file_out:
    csv_reader = csv.DictReader(csv_file_in)
    # csv_reader is now a csv.DictReader() object - a OrderedDict type
    fieldnames = ["ward_id","ward_tikicode","ward_name","district_id","district_tikicode","district_name","region_id","region_tikicode","region_name"]
    csv_writer = csv.writer(csv_file_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    #csv_writer.writeheader()

    # Then using dict() to convert each row to a dictionary. This is optional.
    #for row in csv_reader:
        #print(dict(row))

    n = len(fieldnames)
    print(n)

    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            csv_writer.writerow(row)
            #next(csv_reader) : use when you want to skip to next line

        my_list = list(row.values())

        for k in range(n):
            if k == 0 or k == 3 or k == 6:
                my_list[k] = int(my_list[k])

        csv_writer.writerow(my_list)
        line_count += 1


    # https://www.programiz.com/python-programming/csv

    # https://stackoverflow.com/questions/20347766/pythonically-add-header-to-a-csv-file

    #data = (int(row[0, 3, 6]) for row in csv_reader)

    # https://towardsdatascience.com/15-things-you-should-know-about-dictionaries-in-python-44c55e75405c
    # https://stackoverflow.com/questions/31087111/typeerror-list-object-is-not-callable-in-python