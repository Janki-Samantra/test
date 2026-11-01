#  Taking input from the User

text = input("Enter the text\n").strip()

# Accessing the code
if text == "":
    print("Error: You did not enter anything!")
else:
     word_list = text.split()
     word_tuple = tuple(word_list)
     word_count = len(word_tuple)

# analyzing the text
char_count = len(text)

sentence_count = 0
for char in text:
     if char in ['.','!','?','|']:
          sentence_count +=1 

# fallback
if sentence_count == 0 and word_count >1:
     sentence_count = 1
# printing result
print("\n" + "="*20 + " RESULTS " + "="*20)
print("Total Word:", len(word_list))
print("Total character:", char_count)
print("Total Sentence:", sentence_count)
print("="*49 + "\n")
print("Hello world")
print("Hello world1")




