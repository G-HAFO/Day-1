import re

data = []
sum = 0
with open("data.txt", "r") as f:
    for line in f:
        data.append(line.strip  ('\n'));

replacements = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9')]









for element in  data:
    [element := element.replace(a, b) for a, b in replacements]
    print(f"Processed line : {element}") 
    element = re.findall(r'\d+', element)
    sum += int(element[0][0]) * 10 + int(element[-1][-1])
    print(element[0][0] + element[-1][-1])

print(sum)  
print("Pigs are delicious")

