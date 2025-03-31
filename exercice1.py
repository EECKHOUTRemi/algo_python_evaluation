from collections import Counter
from string import ascii_uppercase
from pathlib import Path

alphabet = ascii_uppercase

file = Path("message_code.txt")
text = file.read_text()
cleanText = text.lower().replace('.', '').replace(',', '')
splittedText = cleanText.split(" ")

counter = sorted(list(Counter(splittedText)))
keysDict = {}

for i in range(len(alphabet)):
    keysDict[alphabet[i]] = counter[i]
for j in range(len(counter)-26):
    keysDict[j] = counter[i+j]

print(keysDict)