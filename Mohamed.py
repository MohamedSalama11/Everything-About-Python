# Mutable => Means That You Can Change It Just Like Lists
# Immutable => Meanst That You Cannot Change It Just Like Strings
# [] => Square Brackets
# () => Parentheses
# {} => Curly Braces

# name = input("What's Your Name: ")
# print("Hello " + name)
# print(type(name))  # Always String
# a = 20 / 5
# print(a)
# print(4 // 4)
# print(26 // 4)
# print(16 // 5)
# print(abs(-9.3))
# print(bin(150))
# print(int("0b10010110", 2))
# help("keywords")


# name = "Mohamed"
# age = 20
# fullInfo = "Hello My Name Is " + name + " And My Age Is " + str(age)
# print(fullInfo)

# Augmented Assignment Operartor
# value = 10
# value *= 10
# print(value)

# first_name = "Mohamed"
# second_name = "Salama"

# full_name = first_name + " " + second_name
# print(full_name)

# type conversion
# a = str(100)
# b = int(a)
# c = type(b)

# print(c)


###### escape sequneces ######
# ----------------------------
# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
# ----------------------------

# Back Space
# print("Hello\bWorld")  # Will Remove o

# Escape New Line + Back Slash
# print("Hello \
# I Love \
# Python")

# print(""" Hello
# I Love
# Python
# """)

# Escape Back Slash
# print("I Love Back Slash \\")

# Escape Single Quote
# print('I Love Single Quote \'Test\' ')

# Escape Double Quotes
# print("I Love Double Quotes \"Test\" ")

# Line Feed
# print("Hello World\nSecond Line")

# Carriage Return
# print("123456\rAbcde")

# Horizontal Tab
# print("Hello\tPython")

# Character Hex Value
# print("\x4F\x73")
# weather = "\tIt's sunny \"today\"\n\tHope you have a beautiful \"day\""
# print(weather)


##################### string Format #####################
# name = "Mohamed"
# age = 22
# print("Hello " + name + " You Are " + str(age) + " Years Old.")
# print(f"Hello {name} You Are {age} Years Old.")
# print("Hello {} You Are {} Years Old".format(name, age))
# print("Hello %s You are %.2f Years Old." % (name, age))


##################### Indexing In Python #####################
# Slicing: [start:End:Step]  => Not Including The End
# name = "Mohamed"
# name[0:1] = "a"
# print(name[0:3])
# print(name[0:len(name)])

# name[0:1] = "a" Strings In Python Are immutabile (You Can't Change The Strings)

# name = "Mohamed Salama"
# name2 = name.replace("Mohamed", "Gehad")
# print(name)
# print(name2)

# name = "Mohamed"
# age = 22
# relationship_Status = "It's Complicated"
# relationship_Status = "Single"
# print(relationship_Status)

# birthday = int(input("What Year Were You Born? "))
# age = 2022 - birthday
# print("Your Age Is : %.2f" % (age))

# name = ["Mohamed", "Salama", "Ali"]
# name = " ".join(name)
# print(name)
### Hidden Password Challenge ###
# username = input("What's Is Your Name: ")
# password = input("Type Your Password Here: ")
# password_length = len(password)
# hidden_password = password_length * "*"
# print(f"Hello {username} Your Password Is {hidden_password} And It's {password_length} letters long")

# name = "mohamed salama"
# print(name.capitalize())

# Complex Numbers
# complex_number = 1 + 2j
# print(type(complex_number))
# print(complex_number.real)
# print(complex_number.imag)
# print(
#     f"Real Part In {complex_number} Is {complex_number.real} And Imaginary Part Is {complex_number.imag}")


# username = input("Waht's Is Your Username? ").capitalize()
# email = input("Waht's Is Your Email? ")

# username = username.strip()
# email = email.strip()

# user_only = email[:email.index("@")]
# domain_only = email[email.index("@") + 1:]

# print(f"Hello {username} Your Email Is {email}")
# print(f"Your Username Is {user_only} \nYour Domain Is {domain_only}")


################ Lists ################
# names = ["Mohamed", "Ahmed", "Abeer"]
# names.append("Rahma")
# names.extend("Reham")
# new = names.extend(["Hager", "Nada", "Nour"])
# print(names)
# print(new)

# nums = [2, 1, 4, 7, 6, -6]
# nums.sort(reverse=False)
# nums.sort(reverse=True)
# print(nums)


# usernames = ["Mohamed", "Ahmed", "Manar", "Rahma"]
# usernames[0] = "Ahmed"
# new_users = usernames[:]
# new = "Mohmed" in usernames
# new = usernames.reverse()
# print(new)
# print(new_users)

# alphabet = ["a", "b", "c", "z", "d"]
# alphabet.sort()
# alphabet.reverse()
# print(alphabet[::-1])
# print(alphabet)

# two_diminsional_list = [[1, "One"], [2], [3], 4]
# print(two_diminsional_list[0][1])


# print(list(range(101)))
# sentence = " "
# my_name = sentence.join(["Mohamed", "Ali", "Salama"])
# print(my_name)


# Unpacking Lists
# one, two, three, four, five, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(one)
# print(two)
# print(three)
# print(four)
# print(five)
# print(*other)

# my_list = [1, 2, 3, 4, 5, 6]
# print(*my_list)

################ Tuples ################
# Tuples Are Immutables => Means That You Cannot Add Or Remove Any Element In The Tuple
# Tuples Syntax
# names = ("Mohamed", "Ahmed", "Manar")
# names2 = "Mohamed", "Manar", "Abeer"
# print(names)
# print(type(names2))

# Tuples With One Element
# my_tuple = ("Mohamed",)
# name = "Mohamed",

# print(type(my_tuple))
# print(type(name))

# Tuple Destruct
# a = ("A", "B", 2, "C")
# x, y, _, z = a

# print(x)
# print(y)
# print(z)

# a = ("A", "B", "C", "D", "E")
# x, y, z, *others = a

# print(x)
# print(y)
# print(z)
# print(*others)


################ SETS ################
# names = {"Mohamed", "Manar", "Donia"}
# names.clear()
# print(names)
# names2 = {"Reem", "Mona"}
# print(names.union(names2))
# print(names)
# names.add('Heba')
# print(names)
# new = names.copy()
# print(names)
# print(new)
# names.add("Reem")
# print(names)
# print(new)
# names.remove("Mohamed")
# print(names)
# names.discard("Abeer")
# print(names)
# print(names.pop())
# print(names)
# names.update(names2)
# print(names)

# my_set = {"Mohamed", 1, 2, 4, 3}
# my_set.add(6)
# new_set = my_set.copy()

# print(my_set)
# print(new_set)

# my_list = [1, 2, 3, 4, 5, 5]
# print(set(my_list))


############### Dictionarys ###############
# my_dict = {
#     "name": "Mohamed",
#     "age": 22,
#     "country": "Egypt",
# }
# my_dict["sex"] = "Male"
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict["name"])

# fromkeys Method
# my_keys = "name",
# my_values = "Mohamed"

# my_dict = dict.fromkeys(my_keys, my_values)
# print(my_dict)  # Dictionary


# dictionary = {
#     "One": ["Mohamed", "Hager", [
#         "Man", "Girl"]],
#     "Two": 2,
#     "Three": 3,
#     "Four": 4,
#     True: "true",
#     123: "One",
#     "Mohamed": "Mohamed",
#     "Mohamed": "Mona"
# }
# print(dictionary)


# user_info = {
#     "name": "Mohamed"
# }
# print(user_info.get("name"))
# print(user_info.values())
# print(user_info.items())

# user_info2 = dict(name="Mohamed", age=33)
# print(user_info2)


# my_dict = {
#     (1, 2): ["one", "two"],
#     "age": 22
# }
# print(my_dict[(1, 2)])


################ If Statements ################
# name = "Mohamed"
# country = input(f"What's Your Country {name}: ").strip().capitalize()
# student = input(
#     f"Hello {name}, Are You A Student? : (Y, N) ").strip().capitalize()
# course_name = "Python"
# course_price = 100

# if country == "Egypt" or country == "Russia":
#     if student == "Y":
#         print(
#             f"Hello {name} Because You Are A Student And From {country} The Course Will Be Free For You, Enjoy :) ")
#     else:
#         print(
#             f"Hello {name} Because You Are From {country}\nThe Course Price Will Be {course_price - 90}")
# else:
#     print(
#         f"Hello {name} Because You Are From {country}\n The Course Price Will Be {course_price}")


# is_old = False
# is_licenced = False

# if is_old:
#     print("You Are Able To Drive The Car.")
# elif is_licenced:
#     print("You Are Able To Drive.")
# else:
#     print("Sorry You Can Not Drive The Car.")
# is_magician = True
# is_expert = True

# if is_magician and is_expert:
#     print("You Are A Master Magician")
# elif is_magician and not is_expert:
#     print("At Least You're Getting There")
# elif not is_magician:
#     print("You Need Some Magic Powers")

# username = input("Waht's Is Your Name? ").strip()
# country = input("What's Is Your Country? ").strip().capitalize()
# user_age = int(input("What's Is Your Age? "))
# course_price = 100

# if country == "Egypt" and user_age == 18:
#     print(
#         f"Hello {username} Because You Are From {country} And Your Age Is {user_age} The Course Price Is $0")
# else:
#     print(
#         f"Hello {username} Because You Are From {country} The Course Price Is ${course_price}")

# Ternary Condition
# movie_rate = 18
# age = 18

# condition = "Enjoy The Movie" if age >= movie_rate else "The Movie Is Not Good For You."
# print(condition)

# age = int(input("Type Your Age: ").strip())
# unit = input(
#     "Choose The Unit : Months (M) Weeks (W) Days (D): ").strip().lower()

# months = int(age) * 12
# weeks = months * 4
# days = int(age) * 365

# if unit == "months" or unit == "m":
#     print(f"Your Age In Months Is: {months} Months.")
# elif unit == "weeks" or unit == "w":
#     print(f"Your Age In Weeks Is : {weeks} Weeks.")
# elif unit == "days" or unit == "d":
#     print(f"Your Age In Days Is : {days} Days.")
# else:
#     print("Please Fill The Age Input.")

# country = input("What's Your Country? ").strip().capitalize()

# countries_one = ["Egypt", "Bahrain", "Syria", "Libya"]
# countries_one_dis = 80

# countries_two = ["USA", "Italy", "Spain"]
# countries_two_dis = 10

# if country in countries_one:
#     print(f"Because You Are Arabian You Have ${countries_one_dis} Discount.")
# else:
#     print(f"Because You Are Foreign You Have ${countries_two_dis} Discount.")


# Membership Practice
# List Contains Admins
# admins = ["Ahmed", "Osama", "Sameh", "Manal", "Mohamed"]

# # Login
# name = input("Please Type Your Name: ").strip().capitalize()

# Check If The Name In Admins
# if name in admins:
#     print(f"Welcome Back {name}.")

#     option = input("Delete (D) Or Update (U) Your Name? ").strip().capitalize()
#     # Check If Option Is Updated
#     if option == "Update" or option == "U":
#         new_name = input("Type Your New Name? ")
#         admins[admins.index(name)] = new_name
#         print("Your Name Updated")
#         print(admins)
#     # Check If Option Is Deleted
#     elif option == "Delete" or option == "D":
#         admins.remove(name)
#         print("You Delete Your Name")
#         print(admins)
#     else:
#         print("Choose An Option First Please")

# # Check If The Name Is Not In Admins
# else:
#     status = input(
#         "Sorry, You Are Not An Admin, Do You Want To Be An Admin? (Y, N)").strip().capitalize()
#     if status == "Yes" or status == "Y":
#         print("You Are Admin Now.")
#         admins.append(name)
#         print(admins)
#     else:
#         print("You Are Not Added.")


################ Loop ################
# While Loop

# a = 0
# while a < 10:
#     print(a)
#     a += 1
# else:
#     print("Loop Is Done.")

# friends = ["Mohamed", "Ahmed", "Donia", "Abeer", "Mona", "Reem", "Abrar"]

# index = 0

# while index < len(friends):
#     print(f"#{str(index + 1).zfill(2)} {friends[index]}")
#     index += 1


# Bookmark Manager Exercise
# my_favourite_webs = []
# maximum_webs = 5

# while maximum_webs > 0:
#     website = input("Enter The Website URL Without https://").strip().lower()
#     if "." not in website:
#         print("Sorry You Need To Enter A Valid Website.")
#     else:
#         my_favourite_webs.append(website)
#         maximum_webs -= 1
#         print(f"Website Added, {maximum_webs} Left")
#         print(my_favourite_webs)
# else:
#     print("Bookmark Is Full.")


# Password Checker Exercise
# tries = 4
# correct_password = "Mohamed@123"
# password = input("Type The Password: ")

# while password != correct_password:
#     tries -= 1
#     print(f"Wrong Password, {'Last' if tries == 0 else tries} left")
#     password = input("Type The Password: ")
#     if tries == 0:
#         print("You Used All The Tries")
#         break
# else:
#     print("Correct Password")


################ For Loop ################

# numbers = [1, 2, 3, 4, 5, 6]

# for number in numbers:
#     # print(f"Number Is : {number}")
#     if number % 2 == 0:
#         print(f"{number} Is Even.")
#     else:
#         print(f"{number} Is Odd.")


# name = "Mohamed"
# for letter in name:
#     print(f"The Letter Is: {letter.upper()}")


# myRange = range(1, 10)
# for number in myRange:
#     print(number)


# mySkills = {
#     "HTML": "20%",
#     "CSS": "30%",
#     "Js": "40%",
#     "Python": "50%"
# }

# for skill in mySkills:
#     # print(mySkills[skill])
#     print(f"My Progress In Language {skill} Is: \n{mySkills[skill]}")


# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]
# skills = ["HTML", "CSS", "JS"]

# for name in peoples:
#     print(f"My Name Is {name} And My Skills Is")
#     for skill in skills:
#         print(f"\t     {skill}")


# peoples = {
#     "Osama": {
#         "HTML": "90%",
#         "CSS": "80%",
#         "JS": "70%",
#     },
#     "Ahmed": {
#         "HTML": "60%",
#         "CSS": "50%",
#         "JS": "40%",
#     },
#     "Sayed": {
#         "HTML": "30%",
#         "CSS": "20%",
#         "JS": "10%",
#     }
# }

# for name in peoples:
#     print(f"Hello {name} Your Skills Is: ")
#     for skill in peoples[name]:
#         print(f"\t{skill} => {peoples[name][skill]}")


##### Continue, Break, Pass #####
# Continue
# numbers = [1, 2, 3, 4, 5, 6, 13, 15, 16, 17, 18, 20]
# for number in numbers:
#     if number == 5:
#         continue
#     print(number)

# Break
# for number in numbers:
#     if number == 15:
#         break
#     print(number)

# Pass
# for number in numbers:
#     if number == 100:
#         pass
#     print(number)


# Advanced Loop In Dictionary
# skills = {
#     "HTML": "90%",
#     "CSS": "80%",
#     "JS": "60%"
# }

# for skill_key, skill_value in skills.items():
#     print(f"{skill_key} => {skill_value}")

# my_ultimate_skills = {
#     "HTML": {
#         "Main": "90%",
#         "PugJs": "80%"
#     },
#     "CSS": {
#         "Main": "70%",
#         "SASS": "60%"
#     }
# }

# for skill_key, skill_value in my_ultimate_skills.items():
#     print(f"{skill_key} Progress Is")
#     for inner_key, inner_value in skill_value.items():
#         print(f"- {inner_key} => {inner_value}")


# personal_info = {
#     "name": "Mohamed",
#     "age": 22,
#     "can_swim": False
# }

# for item in personal_info:
#     print(item)  # Will Print The Keys

# for item in personal_info.items():
#     print(item)  # Will Print The Whole Dictionary Keys And Values Each One In A Tuple

# for item in personal_info.keys():
#     print(item)  # Will Print The Keys

# for item in personal_info.values():
#     print(item)  # Will Print The Values

# Loop Exercise
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# counter = 0
# for num in my_list:
#     # print(num)
#     # counter = counter + num
#     counter += num
# print(counter)

# Range Exercises
# for _ in range(1):
#     print(list(range(10)))

# for _ in range(0, 10, 2):
#     print(list(range(0, 10)))

# Enumerate Exercises
# for index, letter in enumerate("Mohamed Salama"):
#     print(str(index).zfill(2), letter)

# for index, num in enumerate(range(101)):
#     print(index, num)
#     if num == 50:
#         print(f"The Index Of 50 Is : {index}")
#         break


################ Functions ################
# def => For Define

# def hello_world():
#     return "Hello World!"


# hello_world()

# name = input("Type Your Name: ").strip().capitalize()


# def say_hello(name):
#     print(f"Hello {name}")


# say_hello(name)


# def addition(a, b):
#     if type(a) != int or type(b) != int:
#         print("Sorry You Enter An Invalid Data")
#     else:
#         print(a + b)


# addition(5, 5)


# def full_name(fName, mName, lName):
#     print(
#         f"Hello {fName.capitalize().strip()} {mName.capitalize():.1s} {lName.strip().capitalize()}")


# full_name("Mohamed", "Ali", "Salama")

# def say_hello(*names):
#     for name in names:
#         print(f"Hello {name}")


# say_hello("Osama", "Elzero", "Sayed", "Mona")


# def show_details(name, *skills):
#     print(f"Hello {name} Your Skills Is : ")
#     for skill in skills:
#         print(f"{skill}")


# show_details("Mohamed", "Swimming", "Fighting", "Coding", "Touch Typing")

# def info(name, age, country="Egy"):
#     print(f"Hello {name} Your Age Is {age}, And Your Country Is {country}")


# info("Mohamed", "22")

# my_skills = {
#     "HTML": "50%",
#     "CSS": "80%"
# }


# def info(**skills):
#     for key, value in skills.items():
#         print(f"{key} => {value}")


# info(html="50%", css="80%")
# info(**my_skills)

# my_tuple = ("Reading", "Fighting", "Killing", "Touch Typing")
# my_skills = {
#     "HTML": "10%",
#     "CSS": "20%",
# }


# def skills(name, *skills_without_progress, **skill_with_progress):
#     print(f"Hello {name} \nYour Skills Without Progress Is")
#     for skill in skills_without_progress:
#         print(f"- {skill}.")
#     print(f"Your Skills With Progress Is:")
#     for key, value in skill_with_progress.items():
#         print(f"- {key} => {value}")


# skills("Mohamed", *my_tuple, **my_skills)

### Nested Functions ###
# def sum(num1, num2):
#     def sum2(n1, n2):
#         return n1 + n2
#     return num1 + num2


# print(sum(1, 2))


##### Scope In Python #####
# x = 2  # Global Scobe


# def num():
#     global x
#     x = 10
#     print(x)


# def num2():
#     x = 6
#     print(x)


# print(x)
# num()
# num2()


# Lambda Function
# Anonymous Function

# def say_hello(name, age): return f"Hello {name} Your Age Is {age}"


# def hello(name, age): return f"Hello {name} Your Age Is {age}." // Formatter Does Not Support Lambda Fucntions


# print(say_hello("Osama", "36"))
# print(hello("Mohamed", "22"))

# Recursion Function
# def duplicates(word):
#     if len(word) == 1:
#         return word
#     if word[0] == word[1]:
#         return duplicates(word[1:])
#     return word[0] + duplicates(word[1:])


# print(duplicates("WWWoooorrrllllllddddd"))


# DocStrings
# def sum(num1, num2):
#     '''
#     This Fucntion Returns The Sum Of Two Integers :) (Info By Mohamed Salama)
#     '''
#     return num1 + num2


# print(sum(1, 2))
# help(sum)
# print(sum.__doc__)


# Function Check If The Number Even Or Odd (Clean Code)
# def even_odd(num):
#     if num % 2 == 0:
#         return f"{num} Is Even."
#     return f"{num} Is Odd"


# print(even_odd(13))


# Args & Kwargs
# Rule (Params, *args, default parameters, **kwargs)

# Function Add All The Numbers
# def add(*nums, **kwargs):
#     total = 0
#     for value in kwargs.values():
#         total += value
#     return sum(nums) + total


# print(add(1, 2, 3, 4, 5, num1=5, num2=10))


################ Walrus Operator (:=) ################
# name = "Mohamed"
# if (n := len(name)) > 5:
#     print(f"The String Is Too Long: {n} Elements.")

# while (n := len(name)) > 1:
#     print(n)
#     name = name[:-1]
# print(name)

# name = "mohamed"
# while (length := len(name)) > 0:
#     print(length)
#     name = name[:-1]
################ in not in Operator #################
# print(" " in "Mohamed")


# arabic_countries = ["Egypt", "Libya", "Syria", "Lebanon", "Bahryin", "Qatar"]
# main_price = 100
# arabic_discount = 90
# foreign_countries = ["USA", "Italy", "Germany", "China", "France", "Russia"]
# foreign_discount = 60

# country = input("What's Your Country: ").strip().capitalize()

# if country in arabic_countries:
#     print(
#         f"Hello Because You Are An Arabian You Will Have A Discount Of {main_price - arabic_discount}")
# else:
#     print(
#         f"Hello Because You Are A Foreign You Will Have A Discount Of {main_price - foreign_discount}")


#################### Files Handling ####################
# Note :- Use The Absoulte Path (Recommended)
# Note := After Ending With Playing With The File It's Recommended To Close The File
# PATHS
# 1- absolute path => Begin From The Root To The Target File
# 2- relative path => Related With The Current Position Of The File

## Files Modes ##
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists


# Creating Files
# try:
#     new = open("D:\Programming\Python\Python Projects\File Created By Python.txt", "x")
# except FileExistsError:
#     print("File Exists Already, Create File With New Name Plaese")

# import os
# Printing The Current Working Directory
# D:\Programming\Python\Python Projects     (Current Working Directory)
# print(os.getcwd())

# Printing The Absoulte Path Of The Current Working File
# d:\Programming\Python\Python Projects\Mohamed.py
# print(os.path.abspath(__file__))

# Standard Way Of File I/O
# with open("sad.txt", mode="a") as new_file:
#     text = new_file.write("This Is The New Text\n" * 10)
#     print(new_file.encoding)
#     print(new_file.name)
#     print(new_file.mode)


### Reading The File ###
# x = open("D:\Programming\Python\Python Projects\Test.txt", "r")
# print(x)  # File Data Object
# print(x.name)  # File Name
# print(x.mode)  # File Mode
# print(x.encoding)  # File Encoding

# print(x.read())  # Reading The Whole File
# print(x.read(7))  # Reading The Specified Bytes

# print(x.readline())  # Read The Whole Line
# print(x.readline(10))  # Read The Specified Bytes Of The Line

# print(x.readlines())
# for line in x:
#     print(line)
#     if line.startswith("S"):
#         break

# Closing The File (Recommended)
# x.close()


# Write To The File
# my_file = open("D:\Programming\Python\Python Projects\Test2.txt", "w")
# my_file.write("Hello From Source Code.\n")
# my_file.write("Hello From Source Code 1000 Time :) \n" * 10)

# my_list = ["Line1\n", "Line2\n", "Line3\n"]
# my_file.writelines(my_list)

# # Append To The File
# file = open("D:\Programming\Python\Python Projects\Test2.txt", "a")
# file.write("\nWrite Without Deleting")

# Slice A Piece Of Text In The File
# my_file = open("D:\Programming\Python\Python Projects\Test2.txt", "a")
# my_file.truncate(3)

# # Printing The Current Position Of The Cursor   (Note:- new line => 2 Characters)
# print(my_file.tell())

# Read From Specified Position
# my_file = open("D:\Programming\Python\Python Projects\mohamed.txt", "r")
# my_file.seek(6)
# print(my_file.read())

# Remove Specific File
# import os
# os.remove(r"D:\Programming\Python\Python Projects\nada.txt")

# Handling Erros In I/O File
# try:
#     with open("klfds.txt", mode="r") as new_file:
#         text = new_file.read()
#         print(text)
# except FileNotFoundError as error:
#     print("File Not Found Error, BY ME :)")
#     raise error


##################### Built In Functions #####################
# 1- all() # All Elements Is True
# my_list = [1, 2, 3, "Mohamed", True, 0]
# if all(my_list):
#     print(my_list)
# else:
#     print("There's At Least One Element False")

# 2- any() # At Least One Element Is True
# my_list = [False, [], 0]
# if any(my_list):
#     print(my_list)
# else:
#     print("There's No True Elements")

# 3- bin()
# print(bin(100))

# 4- int()
# print(int("0b1100100", 2))

# 5- id()  Print The Id Of Any Object In The Memory
# first_name = "Mohamed"
# second_name = "Salama"
# print(id(first_name))
# print(id(second_name))

# 6- sum(iterable, start)
# my_list = [1, 10, 20, 70]
# print(sum(my_list))
# print(sum(my_list, 10))

# 7- round(number, NumOfDigits)
# print(round(100.65567))
# print(round(100.6567, 2))

# 8- range(start, end, step)
# print(list(range(1)))
# print(list(range(1, 10)))
# print(list(range(1, 10, 2)))

# 9- print()
# Default Separator Between Words Is Space
# print("Mohamed Salama")
# print("Mohamed" "Salama")
# print("Mohamed", "Salama")
# print("Mohamed", "Salama", sep="@")

# end="" => By Default Start A New Line (\n)
# print("First Line")
# print("Seocnd Line", end=" ")
# print("Thrid Line")

# 10- abs()
# print(abs(100))
# print(abs(-100))

# 11- pow(base, exponent, modulus)
# print(pow(2, 4))
# print(pow(2, 4, 2))

# 12- min(item, item, item or iterator)
# print(min(1, 2, 3, 4, 5))
# print(min("A", "B", "C", "D"))
# my_list = [1, 2, 3, -10]
# print(min(my_list))

# 13- max(item, item, item or iterator)
# print(max(1, 2, 3, 4, 5))
# print(max("A", "B", "C", "D"))
# my_list = [1, 2, 3, -10]
# print(max(my_list))

# 14- slice(start, stop, step)  => Start Is Optinal , End Must Write
# my_list = ["A", "B", "C", "D", "E", "F"]
# print(my_list[slice(4)])
# print(my_list[slice(1, 4)])

# 15- enumerate(iterable, start=0)
# name = enumerate("Mohamed")

# for index, letter in name:
#     print(index, letter)

# print("#" * 50)

# my_skills = enumerate(["HTML", "CSS", "JS"])
# for index, skill in my_skills:
#     print(index, skill)

# 16- help()
# print(help(abs))

# 17- reversed(iterable)
# text = "Mohamed Salama"
# for letter in reversed(text):
#     print(letter)

# my_list = [1, 2, 3, 4, 5, 6]
# for num in reversed(my_list):
#     print(num)


# 18- map(function, iterator)
# [1] Map Take A Function + Iteratro
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Fucntion Can Be Pre-Defined Function Or Lambda Function

# Use Map With Predefined Function

# def format_text(text):
#     return f"- {text.strip().capitalize()} -"


# my_texts = ["Mohamed", "OSAma", "DoNIa"]

# for name in map(format_text, my_texts):
#     print(name)

# print("#" * 50)

# def check_number(num):
#     if num > 10:
#         return num
#     else:
#         return "Less Than Or Equal 10"

# my_numbers = [1, 19, 10, 20, 100 , 5]

# for number in map(check_number, my_numbers):
#     print(number)

# Use Map With Lambda Function
# my_texts = ["Mohamed", "Osama", "DONIa"]
# for name in map(lambda name: f"- {name.strip().capitalize()} -", my_texts):
#     print(name)

# 19- filter()
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True (Important)
# [5] The Function Need To Return Boolean Value

# def checkNumber(num):
#     return num > 10   # Treat Like A Condition


# myNumbers = [1, 19, 10, 20, 100, 5]

# myResult = filter(checkNumber, myNumbers)
# for number in myResult:
#     print(number)

# print("#" * 40)

# With Lambda Function
# names = ["Mohamed", "Donia", "Manar", "Heba"]
# for person in filter(lambda name: name.startswith("M"), names):
#     print(person)

# With Pre-Defined Function
# def check_names(name):
#     return name.startswith("M")
# names = ["Mohamed", "Donia", "Manar", "Heba"]
# for person in filter(check_names, names):
#     print(person)


# 20- reduce()  => Higher Order Function
# [1] Reduce Take Function + Iterator
# [2] The Function Can Be Pre-Defined Function Or Lambda Function
# [3] Reduce Run A Function On First And Second Element And Give Result
# [4] Then Run Function On Result And Third Element
# [5] Then Run Function On Result And Fourth Element And So On
# [6] Till One Element Is Left And This Is The Result Of The Reduce Function


# from functools import reduce


# def sum_numbers(num1, num2):
#     return num1 + num2


# numbers = [1, 8, 2, 9, 100, 1, 8, 2, 9, 100]
# result = reduce(sum_numbers, numbers)

# print(result)

################################ Modules ################################
# [1] Module Is A File Contain A Set Of Functions
# [2] You Can Import Module In Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Can Save Your Time

# import random
# print(random)
# help(random)


# import sys
# print(sys.argv)


# print(__name__)  # Print Main If It's The Main File Where Models Imported
# if __name__ == "__main__":
#     print("Hello From The Main File")

# Printing Random Float Number Between 0 and 1
# print(f"Random Float Number {round(random.random(), 2)}")

# Choose Random Element
# print(random.choice([1,2,3]))

# Shuffle Elements
# my_list = [1, 2, 3, 4, 5, 6]
# random.shuffle(my_list)
# print(my_list)

# Show All Function Inside Module
# print(dir(random))

# Import One Or Two Functions From The Module
# from random import randint, random
# print(f"Print Random Float {random()}")
# print(f"Print Random Integer {randint(1, 10)}")

# Create My Own Module
# import sys
# import mohamedmodule as my_module
# print(sys.path)
# print(dir(mohamedmodule))

# my_module.name("Mohamed")

# Useful Modules
# from collections import Counter, defaultdict, OrderedDict

# Counter Usage
# my_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 8]
# print(Counter(my_list))

# sentence = "Hello Mohamed Salama Python Course"
# print(Counter(sentence))


# deafultdict Usage
# my_dict = defaultdict(lambda: "Does Not Exist", {"a": 1, "b": 2})
# print(my_dict["c"])

# OrderedDict Usage
# d = OrderedDict()
# d["a"] = 1
# d["b"] = 2

# d2 = OrderedDict()
# d2["a"] = 1
# d2["b"] = 2


# Array Package
# from array import array
# list = array("i", [1, 2, 3, 4, 5, int("5")])
# print(list[1])

# print(d == d2)
# Install Extrenal Packages
# [1] Package Is A Set Of Modules
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager ( PIP )
# [4] PIP Install The Package And Its Dependencies
# [5] Moduls List "https://docs.python.org/3/py-modindex.html"
# [6] Packages And Modules Direcotry "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/estable/refrence/pip_install/"
# [8] PIP => Python Index Package

# Useful Commands For External Packages
# pip --version  = pip -V                    => To Display The Version Of The pip Package
# pip install --user pacakge name --upgrade  => To Upgrade The Version Of A Package
# pip install --user pacakge name            => To Install External Package
# pip install package name==version          => To Install External Package With A Specified Version
# pip list                                   => To List All The Packages In The Computer
# pip uninstall package name                 => To Uninstall A Package

# import termcolor
# import pyfiglet

# print(dir(pyfiglet))
# print(pyfiglet.figlet_format("Mohamed Salama"))

# print(dir(termcolor))
# print(termcolor.colored(pyfiglet.figlet_format("Mohamed Salama"), "red"))


# import pyjokes
# joke = pyjokes.get_joke('en', 'neutral')
# print(joke)


######## Itreable Vs iterator ########
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)

# Iterator
# [1] Object Used To Iterate Over Iteralbe Using next() Method Retrun 1 Element At Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method On The Iteralbe Behind The Scene
# [4] Gives "StopIteration" If There's No Next Element

# name = "Mohamed"

# for letter in iter(name):
#     print(letter, end=" ")
# my_iterator = iter(name)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))


################## Date And Time ###################
# import datetime
# print(dir(datetime))
# print(dir(datetime.datetime))

# Printing The Current Date And Time
# print(datetime.datetime.now())

# Print The Current Year
# print(datetime.datetime.now().year)

# Print Start And End Of Date
# print(datetime.datetime.min)
# print(datetime.datetime.max)

# Print The Current Time
# print(datetime.datetime.now().time())

# Print The Current Time Hour
# print(datetime.datetime.now().time().hour)

# Print Start And End Of Time
# print(datetime.time.min)
# print(datetime.time.max)

# Print Specific Date
# print(datetime.datetime(2000, 8, 7, 10, 45, 55, 54544354))

# birthday = datetime.datetime(2000, 8, 7)
# dateNow = datetime.datetime.now()
# print(f"My Brithday Is {birthday} And Date Now Is {dateNow}, So I Lived For {(dateNow - birthday).days}")


###################### Errors Handling ######################
# [1] Exceptions Is A runtime Error Reporting Mechanism
# [2] Exceptions Gives You The Message To Understand the Problem
# [3] Traceback Gives You The Line To Look For The Code In This Line
# [4] Excpetions Have Types (SyntaxError, IndexError, KeyError, ValueError, TypeError, NameError, ZeroDivisionError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions

# number = "Mohamed"

# if type(number) != int:
#     raise Exception("Sorry You Need To Enter A Number")
#     raise TypeError("Only Numbers Allowed")
#     raise ValueError("Only Numbers Allowed")
# else:
#     print("You Entered The Correct Number")


# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors  # EOF => Means End Of File
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code

# while True:
#     try:
#         age = int(input("What's Your Age:-").strip())
#         10 / age
#     except ZeroDivisionError:
#         print("Your Age Can't Be Zero, Type Your Age Please")
#     except:
#         print("Enter A Number PLease")
#     else:
#         print(f"Your Age Is {age}")
#         print("Thank You!")
#         break


# try:  # Try The Code And Test Errors
#     number = int(input("Type Your Number Please:- "))
#     print("This Is Integer, From try")
# except:  # Handle The Error If Exist
#     print("This Is Not Integer")
# else:  # If There's No Errors
#     print("This Is Integer, From else")
# finally:  # Run Whatever Happened
#     print("Print From Finally Whatever Happened")

# try:
#     # print(100 / 0)
#     # print(name)
#     int(input("Type Your Number:- ").strip())
# except ZeroDivisionError:
#     print("Zero Division Error Happened")
# except NameError:
#     print("Name Error Happened")
# except ValueError:
#     print("Value Error")
# except:
#     print("Error Happened Try Again :)")


# Advanced Error Handling Example
# the_file = None
# the_tries = 5

# while the_tries > 0:
#     try:  # Try To Open The File
#         print("Enter The File Name With Absolute Path To Open")
#         print(f"You Have {the_tries} Tries Left")
#         print("Example: D:\Python\Files\yourfile.extension")

#         file_name_and_path = input("File Name => : ").strip()
#         the_file = open(file_name_and_path, 'r')

#         print(the_file.read())
#         break

#     except FileNotFoundError:
#         print("File Not Found Please Be Sure The Name is Valid")

#         the_tries -= 1
#     except:
#         print("Error Happened")
#     finally:
#         if the_file is not None:
#             the_file.close()

#             print("File Closed.")
# else:
#     print("All Tries Is Done")


#################### Debugging Code ####################
# my_list = [1, 2, 3, 4, 5, 6]
# my_dict = {
#     "Name": "Mohamed",
#     "Age": 22,
#     "Country": "Egypt"
# }

# for num in my_list:
#     print(num)

# for key, value in my_dict.items():
#     print(f"{key} => {value}")


# def function_one():
#     print("Hello From Function One")


# function_one()

## Debugging With pdb Module ##
# import pdb

# def add(num1, num2):
#     pdb.set_trace()
#     return num1 + num2


# print(add(1, 2))

########## Type Hinting ##########
# def say_hello(name) -> str:
#     print(f"hello {name}")


# say_hello("Mohamed")


# def add(n1, n2) -> int:
#     print(n1 + n2)


# add(1, 2)


##################### Docstrings And Commenting VS Documenting #####################

# def func(name):
#     # Single Line DocString
#     # '''This Function Only Say Hello'''

#     # Multiple Line DocString
#     '''
#     This Function Only Say:
#         Hello For The Name Argument
#     '''
#     print(f"Hello {name}")


# # func("Mohamed")
# # print(func.__doc__)
# help("keywords")


##################### Installing And Use Pylint For Better Code #####################
# """This Is My Function"""


# def say_hello(name):
#     '''Fuction For Saying Hello To The User'''
#     msg = "Hello"
#     return f"{msg} {name}"


# say_hello("Ahmed")


##################### Regular Expressions #####################
# search() => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches And Empty List If No Match
# split(pattern, string, maxsplit) => Return A List Of Elements Splitted On Each Match
# sub(pattern, Replace, string, replaceCount) => Replace Matches With What You Want
# Email Pattern => [A-z0-9\n]+@[A-z0-9]+\.(com|net|org|info)
# Regular Expression Return None If There's Match

# import re
# my_string = "This Is My String"
# regualr = re.search("My", my_string)
# print(regualr.start())
# print(regualr.end())

# my_search = re.search(r"[A-Z]{2}", "MMohamedSSalama")
# print(my_search)
# print(my_search.span())
# print(my_search.string)
# print(my_search.group())


# is_email = re.search(
#     r"[A-z0-9\n]+@[A-z0-9]+\.(com|net|org|info)", "os@osama.com")
# if is_email:
#     print("Valid Email")
# else:
#     print("Not Valid Email")

# email_input = input("Write Your Email Here Please: ").strip()
# search = re.findall(r"[A-z0-9\n]+@[A-z0-9]+\.com|net|org|info", email_input)
# my_list = []
# if search != []:
#     my_list.append(search)
#     print("Email Added")
# else:
#     print("Not Valid Email")

# for email in my_list:
#     print(email)


# string_one = "I Love Python Programming Language"
# search_one = re.split(r"\s", string_one, 2)
# print(search_one)


# string_two = "How-To_Write_A_Very-Good-Article"
# search_two = re.split(r"-|_", string_two)
# print(search_two)


# Get Words From URL
# for index, word in enumerate(search_two, 1):
#     if len(word) == 1:
#         continue
#     print(f"Word Number: {index} => {word.lower()}")

# my_string = "I Love Python Programming Language"
# print(re.sub(r"\s", "-", my_string, 2))

# website = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"
# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", website)
# print(dir(search))
# print(search.group(1))
# print(search.groups())

# for item in search.groups():
#     print(item)

# print(f"Protocol: {search.group(1)}")
# print(f"Sub Domain: {search.group(2)}")
# print(f"Domain Name: {search.group(3)}")
# print(f"Top Level Domain: {search.group(4)}")
# print(f"Port: {search.group(5)}")
# print(f"Query String: {search.group(6)}")
#################################################################### Exercises ####################################################################

# Practical Email Slice Exercise
# name = input("What's Your Name: \n").strip().capitalize()
# email = input("What's Your Email: \n").strip()
# username = email[:email.index("@")]
# domain = email[email.index("@") + 1:]

# print(f"Hello {name} Your Email Is {email}")
# print(f"Your Username Is {username} And Your Domain Is {domain}")


# # Age Details Exercise
# age = int(input("What's Your Age: "))

# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# print("You Lived For: ")
# print(f"{months:,d} Months")
# print(f"{weeks:,d} Weekss")
# print(f"{days:,d} Days")
# print(f"{hours:,d} Hours")
# print(f"{minutes:,d} Minutes")
# print(f"{seconds:,d} Seconds")


# Band Name Generator
# print("#" * 100)
# print(" Welcome To The Band Name Generator. ".center(60, "#"))
# print("#" * 100)F


# country = input("What's Name Of The City You Grow Up In? \n").capitalize()
# pet = input("What's Your Pet's Name? \n").capitalize()

# print(f"Your Band Name Could Be {country} {pet}.")

# name = input("What's Your Name? ").strip().capitalize()

# print("Your Name Length Is " + str(len(name)) + " .")


# Replace Variable Value With Another Variable Value
# a = input("a : ")
# b = input("b : ")

# c = a
# a = b
# b = c

# print(a)
# print(b)


# Two Digit Numbers Add
# num = input("Type Your Number Here: ")

# first_num = int(num[0])
# second_num = int(num[1])
# add = first_num + second_num

# print(add)


# BMI Exercise

# height = float(input("Enter Your Height In Meters: "))
# weight = int(input("Enter Your Weight In Kilograms: "))

# BMI = round(weight / (height * height))

# if BMI < 18.5:
#     print(f"Your BMI Is {BMI}, And You Are Underweight.")
# elif BMI < 25:
#     print(f"Your BMI Is {BMI}, And You Have Normal Weight.")
# elif BMI < 30:
#     print(f"Your BMI Is {BMI}, And Are OverWeight.")
# elif BMI < 35:
#     print(f"Your BMI Is {BMI}, And Are Obese.")
# else:
#     print(f"Your BMI Is {BMI}, You Are Clinically obese.")

# print(int(BMI))

# Calculate How Many months weeks days left in our lifes until 90 years

# age = 90 - int(input("Type Your Age Here: ").strip())

# months = age * 12
# weeks = months * 4
# days = age * 365

# print(f"You Have {days} Days, {weeks} Weeks, {months} Months Left.")

# Tip Calaculator

# Print The Welcoming Message Of The Program
# print("Welcome To The Tip Calculator.")

# # Asking For The Bill
# bill = float(input("What Was The Total Bill? $"))

# # Asking For The Tip Percentage
# tip = int(input(
#     "What Percentage Tip Would You Like To Give To The Waiter? (10, 12 Or 15) "))
# # Asking For Number Of People
# people_num = int(input("How Many People To Split The Bill? "))

# # Calulating The Percentage Tip
# percentage = (tip / 100) * bill

# Tip Caluculator Again
# Asking For The Bill Amount
# bill = int(input("Enter The Bill Amount: "))

# # Calculate The Percentage Tip
# tip = (20 / 100) * bill

# # Printing The Output As Float
# print(f"The Tip Is {tip}")


# # Calculating What Every Person Should Pay
# pay_for_person = (bill + percentage) / people_num
# # final_result = round(pay_for_person, 2)
# final_result = "{:.2f}".format(pay_for_person)
# print(f"Each One Should Pay ${final_result}")


# Odd Or Even?
# print("This Is Odd Even Checker.")
# # Asking For The Number
# number = int(input("Which Number Do You Want To Check? "))

# # Check If The Number Odd Or Even
# module = number % 2
# if module == 0:
#     print(f"{number} Is Even Number")
# else:
#     print(f"{number} Is Odd Number")


# Check If The Year Is Leap Year (366) Or Normal Year (365)
# year = int(input("Which Year Do You Want To Check? "))
# if year % 4 == 0:
#     if year % 100:
#         if year % 400:
#             print("Leap Year.")
#         else:
#             print("Not Leap Year.")
#     else:
#         print("Leap Year.")
# else:
#     print("Not Leap Year.")


# Pizza Order Program
# Small Pizza Price: $15
# Medium Pizza Price: $20
# Large Pizza Price: $25
# pepperoni for small pizza: +$2
# pepperoni for medium or large pizza: +$3
# extra cheese for any pizza size: +$1

# print("Welcome To Python Pizza Deliveries!")
# size = input("What Size Pizza Do You Want? S, M, Or L :").strip().capitalize()
# add_pepperoni = input("Do You Want Pepperoni? Y Or N :").strip().capitalize()
# extra_cheese = input("Do You Want Extra Cheese? Y Or N :").strip().capitalize()

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your Final Bill Is ${bill}.")


# Love Calculator Exercise
# print("Welcome To Love Calculator Program!")
# name1 = input("What is your name? \n")
# name2 = input("What's their names? \n")

# combined_name = name1 + name2
# lower = combined_name.lower()

# t = lower.count("t")
# r = lower.count("r")
# u = lower.count("u")
# e = lower.count("e")

# true = t + r + u + e  # int

# l = lower.count("l")
# o = lower.count("o")
# v = lower.count("v")
# e = lower.count("e")

# love = l + o + v + e  # int

# love_score = int(str(true) + str(love))

# if (love_score < 10) or (love_score > 90):

#     print(
#         f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")


# Treasure Island
# print("Welcome To The Treasure Island \nYour Mission Is To Find The Treasure.")
# choice1 = input(
#     "You're At A Cross Road. Where Do You Want To Go? Type \"left\" or \"right\" ").strip().lower()
# if choice1 == "left":
#     choice2 = input(
#         "You Came To Lake, There Is An Island there is an island in the center of the lake, Type \"wait\" for a boat, Type swim to \"swim\" to the island ").strip().lower()
#     if choice2 == "wait":
#         choice3 = input(
#             "You Arrive Unharmed At The Island, There Is A House With Three Doors , One Is Red, One Yellow, And One Blue, Which Color Do You Choose? ").strip().lower()
#         if choice3 == "red":
#             print("It's Is A Room Fill Of Fire, Game Over:)")
#         elif choice3 == "yellow":
#             print("You Found The Treasure, You Win.")
#         elif choice3 == "blue":
#             print("You Entered A Room Of Beasts, Game Over:)")
#         else:
#             print("You Choose A Door That Doesnt't Exist, Game Over:)")
#     else:
#         print("You Got Attacked!, Game Over :)")
# else:
#     print("You Choose Wrong, Game Over.:)")


# Random Module
# import random
# int_num = random.randint(1, 10)
# print(int_num)

# decimal_num = random.random()
# print(round(decimal_num, 2))


# Head Or Tail Exercise
# import random
# num = random.randint(0, 1)
# if num == 1:
#     print("Heads")
# else:
#     print("Tails")


# Who Will Pay The Bill Program
# Solution One
# import random

# names_string = input("Give Me Everybody's Names, Separated By A Comma. ")
# names = names_string.split(", ")

# print(random.choice(names))

# Soultion 2
# import random
# names_string = input("Give Me Everybody's Names, Separated By A Comma. ")

# names = names_string.split(", ")
# rand_int = random.randint(0, len(names) - 1)
# the_name = names[rand_int]

# print(f"The Person Who Should Pay The Bill Is {the_name} :)")


# Treasure Map Exercise
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")

# # Asking Where Do You Want To Put The Treasure
# position = input("Where do you want to put the treasure? ")
# # Getting The Position Of The Two Digits Inputs
# horizonal = int(position[0])
# vertical = int(position[1])
# # Replace The Two Digits Into The List
# map[vertical - 1][horizonal - 1] = "X"

# # Printing The Map With The Place Of The Treasure
# print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Sessior Exercise
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]

# user_choice = int(
#     input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# else:
#     print(game_images[user_choice])

#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])

#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw")

# GUI Exercise
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]

# empty = " "
# star = "*"
# for each_list in picture:
#     for bin in each_list:
#         if bin == 1:
#             print(star, end="")
#         else:
#             print(empty, end="")
#     print()  # print("") == print("", end="\n")

# Find Duplicates In A List
# some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# duplicates = []
# for letter in some_list:
#     if some_list.count(letter) > 1:
#         duplicates.append(letter)
# print(list(set(duplicates)))


# Average Height Exercise
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# summing = 0
# for num in student_heights:
#     summing = summing + num
# # print(summing)


# count = 0
# for counting in student_heights:
#     count += 1
# # print(count)


# average_height = round(summing / count)
# print(average_height)


# High Score Exercise
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# for num in student_scores:
#     student_scores.sort()
# print(f"The Highest Score In The Class Is {student_scores[-1]}")

# Adding All The Numbers From 1 To 100
# sum = 0
# for num in range(1, 101):
#     sum += num
# print(sum)

# Adding All The Even Numbers From 1 To 100
# even_sum = 0
# for num in range(1, 101):
#     if num % 2 == 0:
#         even_sum += num
# print(even_sum)

# Another Solution
# even_sum = 0
# for num in range(2, 101, 2):
#     even_sum += num
# print(even_sum)


# Fizz Buzz Game
# for num in range(1, 101):
#     # print(num)
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz ")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# Password Generator Project
# Easy Level
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))

# # Printing The Random Letter
# for letter in letters:
#     random_letters = random.choices(letters, k=nr_letters)
# final_letters = "".join(random_letters)

# # Printing The Random Number
# for num in numbers:
#     random_numbers = random.choices(numbers, k=nr_numbers)
# final_numbers = "".join(random_numbers)

# # Printing The Random Symbol
# for symbol in symbols:
#     random_symbols = random.choices(symbols, k=nr_symbols)
# final_symbols = "".join(random_symbols)

# # Printing The Final Password
# final_password = final_letters + final_numbers + final_symbols

# print(f"Your Password Could Be {final_password}")

# Hard Level
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))

# password = []
# for letter in range(0, nr_letters):
#     password += random.choice(letters)

# for num in range(0, nr_numbers):
#     password += random.choice(numbers)

# for symbol in range(0, nr_symbols):
#     password += random.choice(symbols)

# random.shuffle(password)
# final_password = "".join(password)
# print(f"Your Password Could Be {final_password}")

# Finding The Highest Even Number In A List
# def highest_even_num(my_list):
#     # Creating List That Contains The Even Numbers
#     evens = []
#     # Looping The Items In The List
#     for num in my_list:
#         # Check if the number is even
#         if num % 2 == 0:
#             evens.append(num)
#     # Return the hightest even number
#     return f"The Highest Even Number In The List Is {max(evens)}."


# # Play the function
# print(highest_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 100]))


##### Guessing Number Game #####
# import random
# answer = random.randint(1, 10)

# while True:
#     print(answer)
#     try:
#         user_guess = int(input("Guess A Number From 1 To 10:- ").strip())
#         if 0 < user_guess < 11:
#             if user_guess == answer:
#                 print("Correct Number :)")
#                 break
#     except ValueError:
#         print("You Need To Type A Number Not A String")
#     except:
#         print("Error Happened")


# Building A Translator
# from translate import Translator
# translator = Translator(to_lang="ja")

# try:
#     with open("Translate.txt", mode="r") as my_file:
#         text = my_file.read()
#         translation = translator.translate(text)
#         print(translation)
# except FileNotFoundError as error:
#     print("Check Your File Path.")
# except UnicodeEncodeError:
#     print("Encode Error")


################################ Hangman Game ##################################
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
guess = input("Guess A Letter: ").strip().lower()


for _ in range(len(chosen_word)):
    display += "_"
    # display.append("_")
print(display)

for letter in chosen_word:
    if letter == guess:
        print("right")


#################################################### Git Commands ####################################################
# git clone                                             => To Clone (Copy) The Project From Remote Repo (GitHub) To Local Repo (PC)
# git status                                            => Show You What Happens In Your Working Directory
# git add                                               => To Add The Files From Working Directory To The Staging Area
# git add *                                             => To Add All The Files From Working Directory To The Staging Area
# git add *.extension                                   => To Add All The Files With The Same Extension
# git restore --staged filename filename...             => To Restore The Files From The Staging Area To The Working Directory
# git commit -m "Here The Message You Want To Write"    => To Add The Files From Staging Area To The Local Repo
# git branch                                            => Show You All The Branches In The Local Repo
# git remote -v                                         => Show You The Remote Repo
# git push origin main                                  => To Push The Changes From Local Repo To The Remote Repo
# git pull origin                                       => To Pull The Changes From The Remote Repo To The Local Repo
# git config -l                                         => To List All The Configuration Of Git
# git help config                                       => To Open The Configuration Manual
# git config --global user.email "The Github Email"     => To Show The Terminal My Email
# git config --global user.name "Github Name"           => To Show The Terminal My Name
# git config --global user.email                        => To Print The Email Name In The Config
# git config --global user.name                         => To Print The Email Of The User In The Config Settings
# git config -l --show-origin                           => To Show You Where The Configuration Comes From
# git config --global --unset Config Name               => To Delete A Specified Configuration
# git config --global --edit                            => To Change The Configuration With The Editor (VS)
# ssh-keygen -t rsa -b 4090 -C "Here Your Gmail"        => To Create SSH Key
# ssh -T git@github.com                                 => To Test The SSH Key
# git init                                              => To Create Repositery From Existing Project
# git push -u origin master                             => To Push The Changes From The Local Repo To The Remote Repo
# git config --global alias.st status                   => To Create An Alias To The git status Command
# git config --global alias.st                          => To Show You The Command Alias
# git branch Branch Name                                => To Create New Branch
# git checkout Branch Name                              => To Go To The Branch You Want
# git branch -d Branch Name                             => To Delete Specified Branch
# git branch -D Branch Name                             => To Force Delete The Branch Even If There's Changes In The Branch
# git checkout -b Branch Name                           => To Create A New Branch And Go To It
# git branch -m New Branch Name                         => To Rename An Existing Branch
# git merge Branch Name                                 => To Merge The Branch With The Main Branch
#
#
#
#
#
#
#
#
