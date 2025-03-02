## 1. WAP to detect double space in string
text ="  Programming  is fun and  Python  is awesome."
## 1. using For loop
space_Count=0
for i  in range (len(text)-1):
    if text[i] ==" "and text[i+1]==" ":
        space_Count+=1
print("The occurrence of double space is:", space_Count)  # Output: 4

## 2. using count() method
text ="  Programming  is fun and  Python  is awesome."
space_Count=text.count("  ")
print("The occurrence of double space is:", space_Count)  # Output: 4

## 2. Count the number of characters
text ="Programming is fun and Python is awesome."
letter_Count={}
for char  in text:
    if char.isalpha():
        char =char.lower()
        if char in  letter_Count:
            letter_Count[char]+=1
        else:
            letter_Count[char]=1
for char ,count in letter_Count.items():
    print(char,count)
              
## 3. Find longest word in a list.
words_list=["PHP", "Exercises", "Backend", "Apple","Programming"]
longest_word=""
length=0
for word in words_list:
    if len(word)> len(longest_word):
        longest_word= word
        length=len(longest_word)

print("The longest word is: ",longest_word, "with length of: ", length)


## 4.  Print area (rectangle) and volume (cylinder).
# Area of the rectangle
l = 5.1
h = 6.6
area = l * h
decimals = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))

# Volume of the cylinder
r = 5.1  
h = 6.6
volume_Cy = 3.14 * r**2 * h  # Correct formula for cylinder volume
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume_Cy, decimals))


## 5. Count and display the vowels of a given text
text ="Programming is fun and Python is awesome."
vowels_count=0
vowels = "aeiou"
for char in text:
    if char.isalpha() or char.isspace():
        char= char.lower()
        if char in vowels:
            vowels_count+=1

print("The number of vowels is:", vowels_count)


## 6. Remove spaces from a given string
word = "Pr o gr a  mm i ng"
new_word = ""
for char in word:
    if char != " ":
        new_word += char

print(new_word)