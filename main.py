#program to count number of vowels in a String

string = input();
vowels = ['a','i','u','e','o']
vowels_in_string = []

string_chairs = list(string)
for char in string_chars:
  for vowel in vowels:
    if char == vowel:
      vowels_in_string.append(vowel)
      print(','.join(vowels_in_string))