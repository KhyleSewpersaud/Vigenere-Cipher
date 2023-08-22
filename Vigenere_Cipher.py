# Importing built-in string library to use for removing puncuation.
import string

v_table = [] 

start_ascii = 65  # Capital 'A' starts at ASCII number 65.

# Nested for loop that makes a 2d list to create the table.
for i in range(26):
   row = [] # Used to create each row.
   # Looking at the table, the first coloum going down is the alphabet. 
   # So we have to start each new row with the next letter in the alphabet.
   temp_ascii = start_ascii 
   for j in range(26):
      # If statement to ensure alphabet wraps around.
      if temp_ascii > 90:  # ASCII number 90 is capital 'Z'.
         temp_ascii = 65  # Resets the counter back to 'A'.
         row.append(temp_ascii)
         temp_ascii += 1
      else:
         row.append(temp_ascii)
         temp_ascii += 1
   v_table.append(row)  # Once row is filled up, append it to the 2D list.
   start_ascii += 1  # Next row will start at the next letter in the alphabet.

plaintext = input("Please enter plaintext: ")
key = input("Please enter key: ")

# Capitalizes, removes spaces, and removes puncutation using built-in
# Python methods. Learned them from https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
# and https://www.geeksforgeeks.org/python-ways-to-remove-numeric-digits-from-given-string/ 
clean_plaintext = (plaintext.upper().strip().replace(" ", "")
.translate(str.maketrans('', '', string.punctuation))
.translate(str.maketrans('', '', string.digits)))

clean_key = (key.upper().strip().replace(" ", "")
.translate(str.maketrans('', '', string.punctuation))
.translate(str.maketrans('', '', string.digits)))
   
updated_key = ""

# While loop to place copies of the key to line up with the plaintext.
# Goes on until the plaintext and key line up in length.
while len(updated_key) < len(clean_plaintext):
   # To prevent adding too much letters to the key, if statement is needed.
   if (len(clean_key)+len(updated_key)) > len(clean_plaintext):
      # Finds the difference between the plaintext and the key and adds that
      # many letters using string slicing.
      updated_key += clean_key[:(len(clean_plaintext)-len(updated_key))]
   else:
      # If there is enough space, add one full length key.
      updated_key += clean_key

cypher = ""

# Creates the encrypted text.
for z in range(len(clean_plaintext)):
   # Since the table is in ASCII, we must first cast into a character.
   # The first row and coloumn in the table is the alphabet in acending order.
   # Knowing the alphabet is 26 characters, we can navigate the list.
   # We find the indexes by adding the ASCII value of a character
   # to -65. So to find 'A', we add 65(ASCII value of 'A') to -65,
   # this equals 0 and to find the next letter we do the same thing.
   # This then finds the row and coloumn for the encrypted letter.  
   cypher += (chr(v_table[-65+(ord(updated_key[z]))]
   [-65+(ord(clean_plaintext[z]))]))

print("Encrypted text: " + cypher)
