# _*_coding:UTF-8 _*     _

# prompt = "\nTell me somethings , and i will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
#
# while message != 'quit':
#     message = input(prompt)# -*- coding:UTF-8 -*-
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me somethings , and i will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#
#     if message == "quit":
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n（Enter 'quit' when you are finished.）"
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("I would like  to go to "+ city.title() +"!")

# 在循环中使用continue,返回循环开头，并根据测试条件决定是否继续执行循环
# current_number = 0
# while current_number < 10:
#     current_number +=1
#     if current_number %2 == 0:
#         continue
#     print(current_number)


# 练习题
# prompt = "Please enter the ingredient :"
# while True:
#     i = input(prompt)
#     if i != 'quit':
#         print("We would add "+ prompt.title() +" for you !")
#     else:
#         break


# prompt = "Please enter you age:"
# while True:
#     age = int(input(prompt))
#     if age < 3:
#         print("Free")
#     elif 3 < age < 12:
#         print("$10")
#     else:
#         print("$15")

# 列表间移动元素 pop & remove
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed:")
# for confirmed_users in confirmed_users:
#     print(confirmed_users.title())

# 删除包含特定值的所有列表元素 remove
# pets = ['dog','cat','cat','rabbit','cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove("cat")
# print(pets)


# responses = {}
#
# while True:
#     name = input("\nWhat is your name ?")
#     response = input("which mountain would you like to climb someday ?")
#
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         break
#
# print("\n--- Poll Results ---")
# for name,response in responses.items():
#     print(name + " would like to climb " + response + ".")

# sandwich_orders = ['a','b','c','d','e']
# finished_sandwiches = []
#
# for i in range(len(sandwich_orders)):
#
#     pop_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(pop_sandwich)
# print(finished_sandwiches)



## -----------------------  函数 -------------------------------

# def greet_user():
#     print("Hello world !")
#
# greet_user()

# 向函数传递参数
# 函数中定义的变量称为形参， 函数调用中的变量称为实参
# def greet_user(username):
#     print("Hello, " + username.title() + "!")
#
# greet_user('jenkins')

# def favorite_book(title):
#     print("one of my favorite books is " + title + " !")
#
# favorite_book("tomcat")

# 位置实参 (动物类型和名字)
# def describe_pet(animal_type, pet_name):
#     print("\nI have a " +  animal_type + ".")
#     print("My " + animal_type + "s name is " + pet_name.title() + "")
#
# describe_pet("hamster","harry")
# describe_pet(animal_type='hamster',pet_name='harry')

# 默认值
# def describe_pet(pet_name, animal_type="dog"):
#     print("\nI have a " +  animal_type + ".")
#     print("My " + animal_type + "s name is " + pet_name.title() + "")
#
# describe_pet(pet_name='willie')

#返回简单值
# def get_formatted_name(first_name,last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
#
# print(musician)

# 让实参变成可选的
# def get_formatted_name(first_name, middle_name, last_name):
#     full_name = first_name +  ' ' + middle_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

