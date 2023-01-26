from plibrary.wsgi import *
import csv
from libraryapp.models import Book

with open('books3.csv', newline='') as file:
    raw_data = csv.reader(file)
    table=list(raw_data)


    for i in range(len(table)):
        b = Book(
            call_number = table[i][0],
            author = table[i][1],
            title = table[i][2],
            year = table[i][3],
            publisher = table[i][4],
            isbn = table[i][5],
            inventory = table[i][6],
            available= table[i][6],
            language = table[i][7],
            notes = table[i][8],
            )
        b.save()
