import json

#5 Read the JSON file created in #4. Using Python code modify the JSON file to include your superhuman name and your actual name.
# Open the JSON file
with open(r"C:/Users/laoat/Documents/Projects_to_Github/OverTheWire-CTF/Web Server Technologies/lab3.json", "r") as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)

# Print the dictionary
print(data)

# Access individual values
print(data["Batman"])
print(data["WonderWoman"])
print(data["Superman"])

# Modify the dictionary to add myself
data["Cybernomics"] = "Ereek"

print(data)
print(data["Cybernomics"])