import csv, json

def convertCSV(csv, ref, model):
    jsonItem = []
    print(type(csv))
    for index,row in enumerate(csv):
        fields = { ref[i][0]:ref[i][1](v) for i,v in enumerate(row)}
        fields["pk"] = index
        temp = {
            "model": str(model),
            "fields": fields
        }
        jsonItem.append(temp)
    return jsonItem

model = "libraryapp.book"
ref = {
    0:["call_number", str],
    1:["author", str],
    2:["title", str],
    3:["year", str],
    4:["publisher", str],
    5:["isbn", str],
    6:["inventory", str],
    7:["language", str],
    8:["notes", str],
}

with open('books.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    jsonItem = convertCSV(csv_reader, ref, model)

    f = open("test.json", "w")
    f.write(json.dumps(jsonItem))
    f.close()
