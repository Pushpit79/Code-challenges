import string
import random
from random import randint
import re

sentence = input("Enter the string: ")
sentence = " ".join(sentence.split())
word_list = sentence.split(" ")


# Type 1 Error

def type1_error():

# Selecting random word from sentence
   word_len = randint(1,len(word_list)) - 1
   rand_word = list(word_list[word_len])

# When count of Random word is more than 1
   if len(rand_word) > 1 :

# Creating a list for randomly picking up different scenarios
      list1 = [1,2,3] 
      rand_choice = random.choice(list1)
      # print(rand_choice)

      # When test case 1  
      if rand_choice == 1:  
         char_len = randint(1, len(rand_word)) -1
#swaping of words
         rand_word[char_len],rand_word[char_len-1] = rand_word[char_len-1],rand_word[char_len]

# Final sentence
         x = "".join(rand_word) 
         word_list[word_len] = x
         y = " ".join(word_list)
         print(y)

# When test case 2 
      elif rand_choice == 2:
         char_len = randint(1, len(rand_word)) -1

         new_char = rand_word[char_len] * 2    
         rand_word[char_len]  = new_char 

# Final sentence
         x = "".join(rand_word) 
         word_list[word_len] = x
         y = " ".join(word_list)
         print(y)        
  
# When test case 3 
      elif rand_choice == 3:
         char_len = randint(1, len(rand_word)) -1
         new_char = rand_word[char_len] + random.choice(string.ascii_letters)
         rand_word[char_len]  = new_char 

        # Final sentence
         x = "".join(rand_word) 
         word_list[word_len] = x
         y = " ".join(word_list)
         print(y)

# When count of Random word is equal to 1

   elif len(rand_word) == 1 :

      z = rand_word[0] + random.choice(string.ascii_letters)
      word_list[word_len] = z
      y = " ".join(word_list)
      print(y)
   
   else:

     pass

# Type 2 Error

def type2_error():

  #  print('Type 2 called')
   chars = list(sentence)
  #  list_choice = [1,2] 
  #  rand_choice2 = random.choice(list_choice)
   
# Find list of special characters
   mylist = []
   mylist1 = []
   for pos, i in enumerate(chars):
      if i in string.punctuation:
         mylist.append(i)   
         mylist1.append(pos)

   if len(mylist1) != 0 :
      
      print("Punctuation Errors")

      list_choice = [1,2] 
      rand_choice2 = random.choice(list_choice)
     
# Find spaces in sentence
      indexlist = [i for i in range(len(sentence)) if sentence[i] == ' ']
# Pick random from lists
      special_list_random = random.choice(mylist1)
# Pick random space index
      space_list_random = random.choice(indexlist)
# Pick random special charcters
      pick_random_char = random.choice(string.punctuation)

      if rand_choice2 == 1 :
   # number swaping
         temp = chars[special_list_random]
         chars[special_list_random] = chars[space_list_random]
         chars[space_list_random] = temp

         sent_string = "".join(chars)
         print(sent_string)

      else:
  # Pick random from lists
         chars[space_list_random] = pick_random_char
         sent_string = "".join(chars)
         print(sent_string)

   else:
      print("Spelling Errors")
      type1_error()
       
# Type 3 Error

def type3_error():
 
   chars = list(sentence)

# Replacing  apostrophe 's' to simple 's' 
   if "'s" in sentence:
      print("Contraction Errors")
      print(sentence.replace("'s", 's'))

# Replacing simple 's' to apostrophe 's'
   elif "'s" not in sentence and 's' in sentence:
     print("Contraction Errors")     
     indexlist = [i for i in range(len(chars)) if chars[i] == 's']
  
     replace_apostrophe = random.choice(indexlist)
     chars[replace_apostrophe] = "'s"

     x = "".join(chars)
     print(x)

   else:
      print("Spelling Errors")
      type1_error()

# Randomly selecting Type of Error

type_list = [1,2,3]
type_list_random = random.choice(type_list)

if type_list_random == 1:
  print("Spelling Errors")
  type1_error()

elif type_list_random == 2: 
   type2_error()
   
else:
  type3_error()
