import re

def filter_valid_names(filename):
    try:
        with open(filename, 'r') as file:
            names = file.readlines()
        
        valid_names = []
        pattern = r"^[a-zA-Z][a-zA-Z0-9_]*([0-9])\1+$"
        
        for name in names:
            name = name.strip()
            if re.match(pattern, name):
                valid_names.append(name)
        
        if valid_names:
            return valid_names
        else:
            return ["Tidak ada nama roh yang valid."]
    except FileNotFoundError:
        return ["File not found."]
    except Exception as e:
        return [f"An error occurred: {e}"]

filename = input().strip()

valid_names = filter_valid_names(filename)
for name in valid_names:
    print(name)
