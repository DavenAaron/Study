# counter 是对字典的

# import collections
# obj = collections.Counter('fdasfaswefagetwerqfa')
# print(obj)


prompt = "\nTell me somethings , and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)
    print(message)