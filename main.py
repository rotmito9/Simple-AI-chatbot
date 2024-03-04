import random

# Simple Chat Bot

greetings = ["Hello!", "Whats up!", "Howdy!", "Greetings!"]
goodbyes = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]
keywords = ["music", "pet", "book", "game"]
responses =  ["Music is so relaxing!", "Dogs are man's best friend!", "I know about a lot of books." , "I like to play video games."]
print(random.choice(greetings))

#welcome user
print("Welcome to Chatbot 3000!")

#Ask user for name
userName = input("What is your name? ")

print("Nice to meet you, " + userName + "!")

if userName == "Noah":
  print ("My best friend's name is Noah!")
else:
  print ("I hope you're having a great day!")

user = input ("Say something (or type bye to quit): ")
user = user.lower()

while (user != "bye"):
  keyword_found = False

  for index in range(len(keywords)):
    if(keywords[index] in user):
      print("Bot: " + responses[index])
      keyword_found = True

  if (keyword_found == False):
    new_keyword = input("I'm not sure how to respond. What keyword should I respond to? ")
    keywords.append(new_keyword)
    new_response = input("How should I respond to " + new_keyword + "? ")
    responses.append(new_response)

  user = input("Say something (or type bye to quit): ")
  user = user.lower()

print(random.choice(goodbyes))