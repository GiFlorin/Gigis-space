import json
import os

books_proprierties = {
    'title': str(), 
    'author': str(), 
    'cover-url': str(), 
    'publication-year': int(), 
    'pages': int(), 
    'type': str(), 
    "series" :{
        'name': str(), 
        'number': int(), 
        'total': int()
    }, 
    'genres': ['Fiction'], 
    'read-in': "2023-08-19", 
    'rating': "★★★★★", 
    'synopsis': str(),
    'review': str()
    }

movie_proprierties = {
    
}

# asks the user what file to change
file_choice = input("Choose a file to load data into: \n[1] books.json \n[2] movies-series.json \n--> ")
if file_choice == "1":
    file_name = 'books.json'
    new_data = books_proprierties
else:
    file_name = 'movies-series.json'
    new_data = movie_proprierties

# opens the selected file
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_name)

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
else:
    print("File doesn't exist")

# creates a new dict depending on the file
if file_choice == '1' or '2':
    for key, value in books_proprierties.items():
        # if the value is a dict
        if type(value) is dict:
            for key2, vv in value.items():
                res = input(f"\nEnter {key} -> {key2}, must be {type(vv)}: ")
                new_data[key][key2] = res

        # if the value is a list
        elif type(value) is list:
            res = []
            i = 0
            while True:
                x = input(f"\nAdd value({i}) to {key}, must be {type(value)}, to stop enter 0: ")
                i += 1
                if x == '0':
                    break
                else: 
                    res.append(x)
            new_data[key] = res

        # if the value is a string
        elif type(value) is str or int or float:
            res = input(f"\nEnter {key}, must be {type(value)}: ")
            new_data[key] = res

print('-*'*30)
print("New data:")
for key, value in new_data.items():
    print(f"{key}: {value}")
print('-*'*30)

confirmation = input("\nAre you sure you want to add this data? (y/n): ")
if confirmation in 'yY':
    print("Data added")
    data.append(new_data)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
else:
    print("Data not added")
