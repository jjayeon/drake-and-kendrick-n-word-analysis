import csv, json

dicts = []

with open("kendrick_songs.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        if int(row[4]) > 0:
            dicts.append({
                "title": row[0],
                "release_date": row[1],
                "album": row[2],
                "n_words": row[4],
                "lyrics": row[3],
            })

with open("kendrick_songs.js", "w") as outfile:
    json.dump(dicts, outfile, indent=4)
