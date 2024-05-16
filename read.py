Instructions: Do not use functions just basic code that prints to the screen.

1.	Push your assignment file with the name firstname_lastname_5.py to your GitHub repository and add the link of your repository to your submission. – 10 marks
2.	Fill the code out in this MS Word document and upload the file with the name firstname_lastname.docx – 10 marks

3.	Given the below variable (50 marks – 5 marks each)

str = "The quick brown fox jumps over the lazy dog"
a. Print the string to the page
_____your code here________
print(str)
b. Print the length of the string to the page
_____your code here________
print(len(str))
c. Print the string in all uppercase letters
____your code here_________
print(str.upper())
d. Print the string in all lowercase letters
____your code here________
print(str.lower())
e. Print the string in the title case
____Your code here
print(str.title())
f. Print the string in reverse
____your code here_______
print(str[::-1])
g. Print the string in reverse title case
____your code here_______
print(str.title()[::-1])
h. Count the number of times the letter “a” appears in the string
___your code here______
print(str.count("a"))
i. Count the number of times the word “the” appears in the string
____your code here_______
print(str.count("the"))
j. Replace the word “the” with the word “a”
____Your code here______
print(str.replace("the", "a"))



4.	 count the frequency of each letter in the string and save the results in a dictionary (15 marks)
____your code here______
str = "The quick brown fox jumps over the lazy dog"
letter_freq = {}

for letter in str:
    if letter not in letter_freq:
        letter_freq[letter] = 1
    else:
        letter_freq[letter] += 1

print(letter_freq)



5.	Given the below lists; (15 marks)
people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]
      Interpolate the three lists into a string that reads:
      Jane the Female is 23 years old.
      John the Male is 34 years old.
      Jack the Male is 16 years old.
      Janet the Female is 28 years old.

people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for i in range(len(people)):
    print(f"{people[i]}, the {sex[i]}, is {age[i]} years old.")



