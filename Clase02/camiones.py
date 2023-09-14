file = '../Data/camion.csv'
fruits = []

with open(file=file, mode='rt') as file:
    headers = next(file) # Save the first line as headers
    for lote in file:
        # rest of code

print(fruits)