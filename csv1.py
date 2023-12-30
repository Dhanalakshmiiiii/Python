import csv
with open("file.csv")as file_obj:
  reader_obj=csv.reader(file_obj)
  for row in reader_obj:
    print(row)
