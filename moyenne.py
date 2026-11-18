def moyenne(notes):
    return round(sum(notes) / len(notes), 1)


notes = [12, 15, 9, 17]
print("Moyenne :", moyenne(notes))
