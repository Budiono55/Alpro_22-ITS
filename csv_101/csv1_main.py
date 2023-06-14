import csv
import os

with open('csv_101\makan.csv', mode='w') as csvfile:
    fieldnames= ['first', 'last']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"first": "makan", "last": "beans"})
    writer.writerow({"first": "asu", "last": "beans"})
    writer.writerow({"first": "baked", "last": "beans"})
    writer.writerow({"first": "baked", "last": "beans"})

    