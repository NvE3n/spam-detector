import nltk
import re
import pickle

email  =  input("Enter the email here - ")
tokens = nltk.word_tokenize(email)

alpha_nums     = []
non_alpha_nums = []
spam_names     = ["make", "address","all", "3d", "our", "over", "remove", "internet", "order", "mail", "receive", "will", "people", "report", "addresses", "free", "business", "email", "you", "credit", "your", "font", "000", "money", "hp", "hpl", "george", "650", "lab", "labs", "telnet", "857", "data", "415", "85", "technology", "1999", "parts", "pm", "direct", "cs", "meeting", "original", "project", "re", "edu", "table", "conference"]      
spam_marks     = [";","(", "[", "!", "$", "#"]
model_input    = []

for x in tokens:
  alpha_nums.append(re.sub(r'\W+', '', x))
  if not x.isalnum(): 
      non_alpha_nums.append(x)

for null in alpha_nums:
    if null == '':
        alpha_nums.remove('')   
           
for spam_name in spam_names:
    count = 0
    for alpha_num in alpha_nums:
        if spam_name.upper() == alpha_num.upper() :
            count = count+1
    model_input.append(count/len(alpha_nums))
    
for spam_mark in spam_marks:
    count = 0
    for non_alpha_num in non_alpha_nums:
        if spam_name == non_alpha_num :
            count = count+1
    model_input.append(count/len(non_alpha_nums))
    
all_uppercase_words = re.findall(r"[A-Z]+", email)
total_length = 0

for all_uppercase_word in all_uppercase_words:
    total_length +=  len(all_uppercase_word)

length_average = total_length/len(all_uppercase_words)
length_longest = max(all_uppercase_words, key=len)
length_total   = total_length

model_input.append(length_average)
model_input.append(len(length_longest))
model_input.append(length_total)

filename = 'predictor.pickle'
with open(filename, 'rb') as file:
    model = pickle.load(file)
pred_value = model.predict([model_input])

if pred_value == [0.]:
    print("This email is not a spam email.")
else:
    print("This email is a spam email.")
