#This program illustrates the use of .setdefault() method in dictionaries

msg = "It's a great day today and I'm excited to be learning Python"

count = {}

for character in msg:
    count.setdefault(character, 0)
    count[character] += 1
    
print(count) 
