inputstring = input("Input: ")

# convert string to lower case to ignore all cases when counting for occurences (just following the sample output from the document)
inputstring = inputstring.lower()

# loop for going through all the characters in string
# using dictionary {} so the items that are inside are denoted in key:value pairs
# also does the ordering by first occurence automatically when added in the dictionary
# sample print if the character is in the frequency: {'c': 2, 'h': 1, 'a': 2, 'r': 2, 't': 1, 'e': 1}
frequency = {}
for i in inputstring:
   if i in frequency:
      frequency[i] += 1
   else:
      frequency[i] = 1
result = max(frequency, key = frequency.get)

#typical output
print ("Output: "+ result)