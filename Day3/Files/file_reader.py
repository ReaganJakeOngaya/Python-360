file_source = 'Day3/Files/pi_digits.txt'

with open(file_source) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    
with open(file_source) as file_object:
    for line in file_object:
        print(line.rstrip())
        