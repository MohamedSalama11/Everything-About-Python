# python is a dynamically typed language ( data can change during run time ).
# Mutable => Means That You Can Change It Just Like Lists.
# Immutable => Means That You Can't Change It Just Like Strings.
# [] => Square Brackets.
# () => Parentheses, Prackets.
# {} => Curly Braces, Curly Prackets.
# variable just refering to the location of the data in the computer memory.
# expression is part of a code that produces a value.
# statement is an entire line of code that performs some sort of action.
# Python is a grabage collection language uses the mark and sweep alghroithm in deleteing obejcts in the memory.
# ==   => checks for the equality in value.
# is   => checks for the equality in value and type.


# """
# This is
# not multipile line
# comment
# """   # This Is Not Comment It's A String


### How to see the bytecode before it converted to 0,1
# source_code = """
# def greet(name):
#     print(f"Hello {name}")
# greet("Mohamed")
# """

# compiled_code = compile(source_code, filename="code.txt", mode="exec")

# import dis
# dis.dis(compiled_code)


# name = input("What's Your Name: ")  # inpute function always produces a string
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
# help("keywords")  # Reserved Words


### Augmented Assignment Operartor ###
# value = 10
# value *= 10
# print(value)


### Opeartor Precedence ###  (الاولوية للعمليات الحسابية)
# 1- ()
# 2- **
# 3- * /
# 4- + -

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

# print("""Hello
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
# print(name)
# print(name[0:3])
# print(name[0:len(name)])
# name[0:1] = "a" # Strings In Python Are immutabile (You Can't Change The Strings)

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
# age = 2023 - birthday
# print("Your Age Is : %.2f" % (age))

# name = ["Mohamed", "Salama", "Ali"]
# name = ", ".join(name)
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


### Email Exercise ###
# username = input("Waht's Is Your Username? ").capitalize().strip()
# email = input("Waht's Is Your Email? ").strip()

# user_only = email[:email.index("@")]
# domain_only = email[email.index("@") + 1:]

# print(f"Hello {username} Your Email Is {email}")
# print(f"Your Username Is {user_only} \nYour Domain Is {domain_only}")


################ Lists ################
# [1] List items are enclosed in square brackets
# [2] List are ordered, use index to access item
# [3] List are Mutable => can be added, deleted, edited
# [4] List items is not unique
# [5] List can have different data types

# names = ["Mohamed", "Ahmed", "Abeer"]
# names.append("Rahma")
# names.extend("manar")
# new = names.extend(["Hager", "Nada", "Nour"])
# print(names)
# print(new)

# nums = [2, 1, 4, 7, 6, -6]
# nums.sort()
# nums.sort(reverse=False)
# nums.sort(reverse=True)
# print(nums)


# usernames = ["Mohamed", "Ahmed", "Manar", "Rahma"]
# usernames[0] = "Ahmed"
# print(usernames)
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


### Unpacking Lists ###
# one, two, three, four, five, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(one)
# print(two)
# print(three)
# print(four)
# print(five)
# print(*other)

# a, b, c, _ = [1, 2, 3, 4]
# print(a)
# print(b)
# print(c)
# print(_)

# my_list = ["Mohamed", "Ali", "Youssef"]
# print(*my_list)

## Lists Comprehensions ##
# It's a unique way in python for creating lists without looping or using append method
# Syntax   => [param for param in iterable]

# Old Way
# my_list = []
# for char in "Mohamed":
#     my_list.append(char)
# print(my_list)

# New Way
# my_list = [char for char in "Mohamed"]
# print(my_list)

# my_list2 = [num for num in range(1,101)]
# print(my_list2)

# my_list3 = [number ** 2 for number in range(1,100)]
# print(my_list3)
# printing only the even numbers from my_list3
# my_list4 = [num ** 2 for num in range(1,100) if num % 2 == 0]
# print(my_list4)

### Exercise => Find Duplicates in the list
# my_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# duplicates = list(set([x for x in my_list if my_list.count(x) > 1]))
# print(duplicates)


################ Tuples ################
# [1] Tuple items are enclosed in parentheses
# [2] You can remove the parentheses if you want
# [3] Tuple are ordered, to use index to access item
# [4] Tuples Are Immutables => Means That You Can not Add Or Remove Any Element In The Tuple
# [5] Tuples items is not unique
# [6] Tuple can have different data types
# [7] Operators used in strings and lists avaliavble in tuples

# Tuples Syntax
# names = ("Mohamed", "Ahmed", "Manar")
# names2 = "Mohamed", "Manar", "Abeer", 1
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

# a,b,c,_,d = (1,2,3,4,5)
# print(a)
# print(b)
# print(c)
# print(d)

# a = ("A", "B", "C", "D", "E", "F")
# x, y, z, *others = a

# print(x)
# print(y)
# print(z)
# print(*others)


################ SETS ################
# [1] Set items are enclosed in curly braces
# [2] Set items are not ordered and not indexed
# [3] Set indexing and slicing can not be done
# [4] Set has only Immutable data types (Numbers, Strings, Tuples) List and dict are not
# [5] Set items is unique

# names = {"Mohamed", "Manar", "Donia"}
# names.clear()
# print(names)
# names2 = {"Reem", "Mona"}
# print(names.union(names2))
# print(names | names2)
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


# Set Comprehension ( Same as list comprehension )
# my_set = {letter for letter in "Mohamed"}
# print(my_set)

# my_set2 = {num for num in range(1,10) if num % 2 == 0}
# print(my_set2)


############### Dictionarys ###############
# [1] Dict items are enclosed in curly braces
# [2] Dict items contains key : value
# [3] Dict key need to be Immutable => (Number, string, tuple), List not allowed
# [4] Dict value can have any data types
# [5] Dict key need to be unique
# [6] Dict is not ordered, you can access the value by it's key

# my_dict = {
#     "name": "Mohamed",
#     "age": 22,
#     "country": "Egypt",
# }
# my_dict["Gender"] = "Male"
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict["name"])

# fromkeys Method
# my_keys = "name",
# my_values = "Mohamed"

# my_dict = dict.fromkeys(my_keys, my_values)
# print(my_dict)  # Dictionary

# user_info2 = dict(name="Mohamed", age=33, country="Egypt")
# print(user_info2)


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
# print(user_info["name"])
# print(user_info.keys())
# print(user_info.values())
# print(user_info.items())


# Dictionary Comprehension
# simple_dict = {
#     "a": 1,
#     "b": 2
# }

# my_dict2 = {k:v**2 for k,v in simple_dict.items() if v % 2 == 0} # standard_way
# print(my_dict2)

# my_dict = {(key, value**2) for key,value in simple_dict.items()} # my_way => will return a dictionary contain two tuples {("a", 1), ("b", 4)}
# print(my_dict)

# my_dictionary = {num:num*2 for num in [1,2,3] if num % 2 == 0}
# print(my_dictionary)


################ Control Flow ################
### boolean Values (False) ###
# print(bool())
# print(bool(0))
# print(bool(""))
# print(bool(''))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(False))
# print(bool(None))


# name = input("What's Your Name:- ").strip().capitalize()
# country = input(f"What's Your Country {name}: ").strip().capitalize()
# student = input(
#     f"Hello {name}, Are You A Student? : (Y, N) ").strip().capitalize()
# course_name = "Python"
# course_price = 100

# if country == "Egypt" or country == "Russia":
#     if student == "Y":
#         print(
#             f"Hello {name} Because You Are A Student And From {country}\nThe Course Will Be Free For You, Enjoy :) ")
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
# age = int(input("what's your age:- ").strip())

# condition = "movie is suitable for you" if age >= movie_rate else "movie is \"not\" suitable for you, you still a baby hahhahahahahahahha, go and do your homoworks :)"
# print(condition)

# print("movie is suitable for you" if age >= movie_rate else "movie is \"not\" suitable for you, you still a baby hahhahahahahahahha, go and do your homoworks :)")


# age = int(input("Type Your Age: ").strip())
# unit = input(
#     "Choose The Unit : Months (M) Weeks (W) Days (D): ").strip().lower()

# months = age * 12
# weeks = months * 4
# days = age * 365

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


### Membership Practice ###
# List Contains Admins
# admins = ["Ahmed", "Osama", "Sameh", "Manal", "Mohamed"]

# # Login
# name = input("Please Type Your Name: ").strip().capitalize()

# # Check If The Name In Admins
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
### While Loop ###

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
#     print(f"Wrong Password, {'Last' if tries == 0 else tries} Chance Left")
#     password = input("Type The Password: ")
#     if tries == 0:
#         print("You Used All The Tries")
#         break
# else:
#     print("Correct Password")


################ For Loop ################
# numbers = [1, 2, 3, 4, 5, 6]

# for num in numbers:
#     # print(f"Number Is : {num}")
#     if num % 2 == 0:
#         print(f"{num} Is Even.")
#     else:
#         print(f"{num} Is Odd.")


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
#     print(f"My Progress In {skill} Language Is:- {mySkills[skill]}")


# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]
# skills = ["HTML", "CSS", "JS"]

# for name in peoples:
#     print(f"My Name Is {name} And My Skills Are")
#     for skill in skills:
#         print(f"{skill}")


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
#     print(f"Hello {name} Your Skills Are: ")
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
#     if number == 13:
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
#     counter += num
# print(counter)


# Range Exercises
# for _ in range(1):
#     print(list(range(10)))

# for _ in range(0, 10, 2):
#     print(list(range(0, 10)))

# To loop over numbers in the opposite direction
# for num in range(10, -1, -1):
#     print(num)


# Enumerate Exercises
# for index, letter in enumerate("Mohamed Salama"):
#     # print(str(index).zfill(2), letter)
#     print(index, letter)

# for index, num in enumerate(range(101)):
#     print(index, num)
#     # if num == 50:
#     #     print(f"The Index Of 50 Is : {index}")
#     #     break


################ Functions ################
# [1] A function is a reusable block of code can do a task
# [2] A function run when you call it
# [3] A function accept elements to deal with called [ Parameters ]
# [4] A function can do the task without returning data
# [5] A function can return data after job is finished
# [6] A function create to prevent DRY ( Don't Repeat Yourself )
# [7] A function accept elements when you call it called Arguments
# [8] There's a built-in functions and user defined functions
# [9] A function is for all team and all apps

# def => For Define

# def hello_world():
#     return "Hello World!"


# print(hello_world())


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


### Lambda Function ( Anonymous Function ) ###
# [1] It has no name.
# [2] You can call it inline without defineing it.
# [3] You can use it to return data from another function.
# [4] Lambda used for simple functions and Def handle the large tasks.
# [5] Lambda is one single expression not block of code.
# [6] Lambda type is function.

# def say_hello(name, age): return f"Hello {name} Your Age Is {age}"


# def hello(name, age): return f"Hello {name} Your Age Is {age}." // Formatter Does Not Support Lambda Fucntions


# print(say_hello("Osama", "36"))
# print(hello("Mohamed", "22"))

## Exersice on labmda function
# Square Each Item In A List
# my_list = [5,4,3]
# new_list = map(lambda num: num ** 2, my_list)
# print(list(new_list))

# Sort Depending on the second element of the tuple
# a = [(0,2), (4,3), (9,9), (10,-1)]
# a.sort(key=lambda x: x[1])
# print(a)


# Recursion Function
# def duplicates(word):
#     if len(word) == 1:
#         return word
#     if word[0] == word[1]:
#         return duplicates(word[1:])
#     return word[0] + duplicates(word[1:])


# print(duplicates("WWWoooorrrllllllddddd"))


# Function Check If The Number Even Or Odd (Clean Code)
# def is_even(num):
#     return num % 2 == 0

# print(is_even(12))


# Args & Kwargs
# Rule (Params, *args, default parameters, **kwargs)

# Function Add All The Numbers
# def add(*nums, **kwargs):
#     total = 0
#     for value in kwargs.values():
#         total += value
#     return sum(nums) + total


# print(add(1, 2, 3, 4, 5, num1=5, num2=10))


# Return The Highest Even Number
# def highest_even_num(li):
#     evens = []
#     for num in li:
#         if num % 2 == 0:
#             evens.append(num)
#     print(max(evens)) 

# highest_even_num([1,2,3,4,10,12,24])


### DocStrings ###
# def sum(num1, num2):
#     '''
#     This Fucntion Returns The Sum Of Two Integers :) (Info By Mohamed Salama)
#     '''
#     return num1 + num2


# print(sum(1, 2))
# help(sum)
# print(sum.__doc__)


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


################ in && not in Operator #################
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
# Note :- Always Use The Absoulte Path ( Recommended )
# Note :- After Ending Playing With The File It's Recommended To Close The File
## PATHS ##
# 1- Absolute path => Begin From The Root To The Target File
# 2- Relative path => Related With The Current Position Of The File

## Files Modes ##
# "a" Append  => Open File For Appending Values, Create File If Not Exists
# "r" Read    => [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   => Open File For Writing, Create File If Not Exists
# "x" Create  => Create File, Give Error If File Exists

# Creating Files
# try:
#     new = open("D:\Programming\Python\Python Projects\File Created By Python2.txt", "x")
# except FileExistsError as error:
#     print("File Exists Already, Create File With New Name Plaese")
#     raise error

# import os
# Printing The Current Working Directory
# print(os.getcwd())

# Printing The Absoulte Path Of The Current Working File
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
# my_file.truncate(1)

# Printing The Current Position Of The Cursor   (Note:- new line => 2 Characters)
# print(my_file.tell())

# Read From Specified Position
# my_file = open("D:\Programming\Python\Python Projects\mohamed.txt", "r")
# my_file.seek(11)
# print(my_file.read())

# Remove Specific File
# import os
# try:
#     os.remove(r"D:\Programming\Python\Python Projects\nada.txt")
# except FileNotFoundError as error:
#     print("No Such File In The Directory")
#     # raise(error)

# Handling Erros In I/O File
# try:
#     with open("klfds.txt", mode="r") as new_file:
#         text = new_file.read()
#         print(text)
# except FileNotFoundError as error:
#     print("File Not Found Error, BY ME :)")
#     raise error


##################### Built In Functions #####################
# 1- all() # Retrun True If All Elements Is True Otherwise Return False
# my_list = [1, 2, 3, "Mohamed", True, ""]
# print(all(my_list))
# if all(my_list):
#     print(my_list)
# else:
#     print("There's At Least One Element False")

# 2- any() # Retrun True If There's At Least One Element Is True Otherwise Return False
# my_list = [False, [], 1]
# print(any(my_list))
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

# 6- sum(iterable, start)  => Sum all the elements in the iterable object and retrun the result
# my_list = [1, 10, 20, 70]
# print(sum(my_list))
# print(sum(my_list, 20))

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
# print("Mohamed"  "Salama")
# print("Mohamed", "Salama")
# print("Mohamed", "Salama", sep="@")

# end="" => By Default Starts A New Line (\n)
# print("First Line")
# print("Seocnd Line", end=" ")
# print("Thrid Line")

# 10- abs()
# print(abs(100))
# print(abs(-100))

# 11- pow(base, exponent, modulus)
# print(pow(2, 4))
# print(2 ** 4)
# print(pow(2, 4, 1))

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

# 14- slice(start, stop, step)  => Start Is Optinal , Stop Must Write
# my_list = ["A", "B", "C", "D", "E", "F"]
# print(my_list[slice(4)])
# print(my_list[slice(1, 4)])

# 15- enumerate(iterable, start=0)
# name = enumerate("Mohamed")

# for index, letter in name:
#     print(index, letter)

# print("#" * 50)

# my_skills = enumerate(["HTML", "CSS", "JS"], 3)
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
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Fucntion Can Be Pre-Defined Function Or Lambda Function

# Use Map With Predefined Function
# def format_text(text):
#     return f"- {text.strip().capitalize()} -"


# my_texts = ["Mohamed", "OSAma", "DoNIa"]

# for name in map(format_text, my_texts):
#     print(name)

# print("#" * 50)

# Use Map With Lambda Function
# my_texts = ["Mohamed", "Osama", "DONIa"]
# for name in map(lambda name: f"- {name.strip().capitalize()} -", my_texts):
#     print(name)


# Exercise 1
# def check_number(num):
#     if num > 10:
#         return num
#     else:
#         return "Less Than Or Equal 10"

# my_numbers = [1, 19, 10, 20, 100 , 5]

# for number in map(check_number, my_numbers):
#     print(number)


# Exercise 2
# def multiply_by2(item):
#     return item * 2

# my_list = [1,2,3]

# print(list(map(multiply_by2, my_list)))
# print(my_list)


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

# Exercise
# def check_odd(num):
#     return num % 2 != 0

# my_list = [1,2,3]

# print(list(filter(check_odd, my_list)))

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
# print(sum(numbers))

# 21- zip()  => it is zip all the iterables objects you give to it
# my_list = [1,2,3,4]
# your_list = [10, 20, 30]
# print(list(zip(my_list, your_list)))


## Loop On Many Iterators With zip() ##
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length Of Lowest Object

# list1 = [1, 2, 3, 4, 5]
# list2 = ["A", "B", "C"]  # Control The Zip Object ( The Lowest One )
# tuple1 = ("Man", "Woman", "Girl", "Boy")
# dict1 = {
#     "Name": "Mohamed",
#     "age": 22,
#     "Country": "Egypt"
# }

# for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
#     print("List 1 Item =>", item1)
#     print("List 2 Item =>", item2)
#     print("Tuple 1 Item =>", item3)
#     print("Dict 1 key =>", item4, "Value =>", dict1[item4])


# ultimatel_list = zip(list1, list2)
# print(ultimatel_list)
# for item in ultimatel_list:
#     print(item)


################################ Modules ################################
# [1] Use Camel_Case for naming your modules
# [2] Module Is A File Contain A Set Of Functions
# [3] You Can Import Module In Your App To Help You
# [4] You Can Import Multiple Modules
# [5] You Can Create Your Own Modules
# [6] Modules Can Save Your Time
# [7] Everytime you create a module and run it the interpreter will create __pycache__ file
# Note:- in programming if you have this sentence "process finished with exit code 0" this means there's no errors if it's 1 this means there's an error 

# import random
# print(random)
# help(random)


# import sys
# print(sys.argv)
# print(sys.path)
# sys.path.append(r"path")   => to add a new path to the paths of the system


# Printing Random Float Number Between 0 and 1
# import random
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
# # print(sys.path)
# # print(dir(mohamedmodule))

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
# d2["b"] = 2
# d2["a"] = 1

# print(d == d2)


# Array Package
# from array import array
# list = array("i", [1, 2, 3, 4, 5, int("5")])
# print(list[1])


# Install Extrenal Packages
# [1] Package Is A Set Of Modules
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager ( PIP )
# [4] PIP Install The Package And It's Dependencies
# [5] Moduls List "https://docs.python.org/3/py-modindex.html"
# [6] Packages And Modules Direcotry "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/estable/refrence/pip_install/"
# [8] PIP => Python Index Package

# Useful Commands For External Packages
# pip --version = pip -V                     => To Display The Version Of The pip Package
# pip install --user pacakge_name --upgrade  => To Upgrade The Version Of A Package  (pip install package_name --upgrade)
# pip install pyfiglet=1.3.5                 => To Install A Package With A Specified Version
# pip install --user pacakge_name            => To Install External Package
# pip install package_name==version          => To Install External Package With A Specified Version
# pip list                                   => To List All The Packages In The Computer
# pip uninstall package_name                 => To Uninstall A Package

# import termcolor , pyfiglet

# print(dir(pyfiglet))
# print(pyfiglet.figlet_format("Abo Salama"))

# print(dir(termcolor))
# help(termcolor)
# print(termcolor.colored(pyfiglet.figlet_format("Mohamed Salama"), "red"))
# print(termcolor.colored(pyfiglet.figlet_format("Abo Salama"), "yellow"))
# print(termcolor.colored("Mohamed", "green"))

# import pyjokes
# joke = pyjokes.get_joke('en', 'neutral')
# print(joke)


# print(__name__)  # Print __main__ If It's The Main File Where Modules Imported
# if __name__ == "__main__":  # We Use This Condition To Make Sure That We Run A Module If This Is The Main File, Or The File Being Run
#     print("Hello From The Main File")


################## Date And Time ###################
# import datetime
# print(dir(datetime))
# print(dir(datetime.datetime()))

# Printing The Current Date And Time
# print(datetime.datetime.now())

# Print The Current Year, Month, Day, Second, Minute
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)

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
# print(datetime.datetime(2000, 8, 7, 10, 45, 55))

# birthday = datetime.datetime(2000, 8, 7)
# dateNow = datetime.datetime.now()
# print(f"My Brithday Is {birthday} And Date Now Is {dateNow}, So I Lived For {(dateNow - birthday).days}")


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


##################### Generators #####################
# 1- Generator is a function with "yield" keyword instead of "return"
# 2- It supports iteration and retrun generator itearator by calling "yield"
# 3- Generator functions can have one or more "yield"
# 4- By using next() it resume from where it called "yield" not from begining (Feature)
# 5- When it's called, it's not start automatically, it will give you the control
# 6- Generators can pause and resume functions


# def my_generator():
#     yield "Salama"
#     yield 2
#     yield 3
#     yield 4
#     print("Mohamed")
#     yield 5

# my_generator()
# print(my_generator())
# print(type(my_generator))


# my_gen = my_generator()

# print(next(my_gen))
# print("Hello")
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

# for number in my_gen:
#     print(number)


# Another Example
# def my_generator(num):
#     for i in range(num):
#         yield i


# my_gen = my_generator(10)
# print(next(my_gen))
# print(next(my_gen))
# next(my_gen)
# print(next(my_gen))


######################### Decorators #########################
# 1- Sometimes called Meta Programming
# 2- Everything in python is object even functions
# 3- Decorator take a function and add some functionality and return it
# 4- Decorator wrap other function and enhance their behaviour
# 5- Decorator is higher order function (function accept function as parameter)
# 6- You Can Add More Than One Decorator To The Same Function


# def my_decorator(func):  # Decorator
#     def nested_func():  # Any Name It's Just For Decoration
#         print("Before")  # Message From Decorator
#         func()  # Execute Function
#         print("After")  # Message From Decorator
#     return nested_func  # Return All Data


# @my_decorator
# def say_hello():
#     print("Hello From Say Hello Function")


# say_hello()


# My Example
# def my_decorator(any_func):
#     def nested_func():
#         print("Before")
#         any_func("Mohamed")
#         print("After")
#     return nested_func


# @my_decorator
# def say_hello(name):
#     print(f"Hello {name}")


# say_hello()

# after_decoration = my_decorator(say_hello)
# after_decoration()

# Another Example
# def my_dec(func):
#     def nested_func(*numbers):
#         for number in numbers:
#             if number < 0:
#                 print("Beware One Of The Numbers Is Less Than Zero")
#         func(*numbers)
#     return nested_func


# @my_dec
# def calculate(num1, num2, num3):
#     print(num1 + num2 + num3)


# calculate(-1, 2, 3)


# Speed Test
# from time import time


# def speed_test(func):
#     def wrapper():
#         start = time()
#         func()
#         end = time()
#         print(f"Function Running Time Is {end - start}")
#     return wrapper


# @speed_test
# def test():
#     for number in range(1, 2000):
#         print(number)


# test()


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


# func("Mohamed")
# print(func.__doc__)
# help(func)


##################### Installing And Use Pylint For Better Code #####################
# """This Is My Function"""


# def say_hello(name):
#     '''Fuction For Saying Hello To The User'''
#     msg = "Hello"
#     return f"{msg} {name}"


# say_hello("Ahmed")


############# Manipulating Images With Pillow ###############
# from PIL import Image

# # Open The Image
# my_img = Image.open(r"D:\Mohamed Salama\backgrounds for desktop\1.jpg")
# # Display The Image
# # my_img.show()
# # My Cropped Image
# # (Left, Upper, Right, Lower)
# my_box = (300, 300, 800, 800)
# my_new_image = my_img.crop(my_box)
# # Show The New Image
# my_new_image.show()

# # Black And White Image
# img_converted = my_img.convert("L")
# img_converted.show()


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


################################################### OOP ( Object Oriented Programming ) ###################################################
# Notes:-
# Objects In Python Divides Into Two Parts 1-Scaler => Can't Be Subdivided 2-Non-scaler => can be subdivided  => يعني متقدرش تشتق منها objects
# 1- Python Supports OOP
# 2- OOP Is A Paradigm Or Coding Style
# 3- Paradigm => Means structuring program so the methods ( functions ) and attributes ( data ) are bundled into objects
# 4- Methods => Act as function that use the information of the object
# 5- Python is Multi-Paradigm programming language ( Procedural, OOP, Functional ) Programming
# 6- Procedural Programming => Structure of the app like Recipe, sets of steps to make the task ( Means The Way of Structurning Our Code Like The Code We Write )
# 7- Functional Programming => Built on the concept of Mathematical Functions
# 8- We Use PascalCase ( UpperCamelCase ) For Creating Classes
# 9- Instanciate from a class => Means create an object from a class
# 10- Class is the blueprint or constructor of the object
# 11- When creating object python look for the built in __init__ method
# 12- __init__ method called every time you create an object from class
# 13- __init__ method is initialize the data for the object
# 14- Any method with two underscore in the start and the end called Dunder or Magic method
# 15- Self refer to the current instance ( object ) created from the class ( blueprint, constructor ) and must be first parameter
# 16- Self parameter can be named anything
# 17- In python you don't need to call new() keyword to create object
# 18- Instance Attributes Defined Inside The Constructor
# Instance Methods:-
# -- Take Self Parameter Which Point To Instance Created From Class
# -- Can have more than one parameter like any function
# -- Can freely access attributes and methods on the same object
# -- Can access the class itself
# 19- Class Attributes Defined Outside The Constructor ( __init__ )
# 20- Class methods makred with @classmethod Decorator to flag it as class method
# 21- Class methods take cls parameter not self to point to the class not the instance
# 22- Static methods takes no parameters
# 23- Static methods makred with @staticmethod Decorator to flag it as static method
# 24- Static methods It's Bound To The Class Not Instance
# 25- Static methods Used when doing something doesn't have access to object or class but related to class
# 26- Everything in python is an object
# 27- self.__class__ To Show You Which Class The Instance Belongs To
# 28- __str__ Gives a human-readable output of the object
# 29- __len__ Rturns the length of the container and it's called when we use the built-in len() function of the object
# 30- To override a method in the parent class you need to write it with the same name in the child class
# 31- mro() or method resoultion order => To Show You The Order Of The Classes In Your Object
# 32- When Function does not have return it returns None
# 33- child class = sub class = derived class

#### Encapsulation ####
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes (Derived Classes => Inheritance From The Base Class)
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------


# Class Syntax
# class NameOfTheClass:
#     Constructor => Do Instantiation [ create instance from a class ]
#     Each Instance is a separate object
#     def __init__(self, other_parameters):
#         body of the function


# class MemberList:
#     def __init__(self):
#         print("A New Member Has Been Added.")


# member_one = MemberList()
# member_two = MemberList()

# print(member_one)
# print(dir(MemberList))  # To Print The Attributes And The Methods Of The Class
# print(member_one.__class__)  # To See Which Class The Object Belongs To


# class Member:
#     # Creating Class Attributes
#     not_allowed_names = ["Hell", "Shit", "Baloot"]
#     users_num = 0

#     # Creating Class Method
#     @classmethod
#     def show_users_count(cls):
#         print(f"We Have {cls.users_num} Users In Our System")

#     # Creating Static Method
#     @staticmethod
#     def say_hello():
#         print("Hello From Static Method")

#     def __init__(self, fName, mName, lName, gender):
#         # Creating Instance Attributes
#         self.firstname = fName
#         self.middlename = mName
#         self.lastname = lName
#         self.gender = gender

#         Member.users_num += 1

#     # Creating Instance Methods
#     def full_name(self):
#         if self.firstname in Member.not_allowed_names:
#             raise ValueError("Not Allowed Name.")
#         else:
#             return f"{self.firstname} {self.middlename} {self.lastname}"

#     def name_with_title(self):
#         if self.gender == "Male":
#             return f"Hello Mr {self.firstname}"
#         else:
#             return f"Hello Miss {self.firstname}"

#     def get_all_info(self):
#         return f"{self.name_with_title()}, Your Full Name Is {self.full_name()}, And Your Gender Is {self.gender}."

#     def delete_user(self):
#         Member.users_num -= 1
#         return f"User {self.full_name()} Has Been Deleted."


# print(Member.users_num)

# member_one = Member("Mohamed", "Ali", "Youssef", "Male")
# member_two = Member("Salama", "Ahmed", "Ebrahim", "Male")
# member_three = Member("Donia", "Ahmed", "Ebrahim", "Female")

# print(Member.users_num)

# print(member_one.delete_user())

# print(Member.users_num)

# # Printing The Content Of The Instance (Attributes, Methods)
# print(dir(member_one))
# print(dir(Member))  # Printing The Content Of The Class (Attributes & Methods)

# To Call The Instance Attributes
# print(member_one.firstname, member_one.middlename, member_one.lastname)
# print(member_two.firstname, member_two.middlename, member_two.lastname)

# To Call The Instance Methods
# print(member_one.full_name())
# print(Member.full_name(member_one))  # What Happens Behind The Scenes
# print(member_one.name_with_title())
# print(member_three.name_with_title())
# print(member_one.get_all_info())

# To Call Class Attributes
# print(Member.users_num)

# To Call Class Methods
# Member.show_users_count()

# To Call Static Method
# Member.say_hello()


### Dunder Or Magic Methods ###
# class Skill:
#     def __init__(self):
#         self.skills = ["Html", "Css", "Js", "Python"]

#     def __str__(self):
#         return f'This Is My Skills => {self.skills}'

#     def __len__(self):
#         return len(self.skills)


# profile = Skill()
# print(profile)


# print(len(profile))

# print(profile.skills)
# profile.skills.append("PHP")
# profile.skills.append("Mysql")

# print(len(profile))


# Means Creating An Instance From The Class Str
# my_string = "Mohamed"

# print(type(my_string))
# print(my_string.__class__)
# print(dir(str))

# print(my_string.upper())
# print(str.upper(my_string))  # What Happens Behind The Scene


###### Inheritance ######
# class Food:  # Base Class
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} Is Created From The Base Class")

#     def eat(self):
#         print("Eat Method From Base Class")


# class Apple(Food):  # Derived Class
#     def __init__(self, name, price, amount):
#         # Food.__init__(self, name, price) # Created Instance From Base Class
#         super().__init__(name, price)  # Do Not Need To Put Self
#         self.amount = amount
#         print(
#             f"{self.name} Is Created From Derived Class And The Price Is {self.price} And Amount Is {self.amount}")

#     def get_from_tree(self):
#         print("Get From Tree From Derived Class")


# food_one = Food("Pizza", 30)
# food_two = Apple("Pizza", 150, 3)
# food_two.eat()
# food_two.get_from_tree()

# Check If The Object Is An Instance From The Class => isinstance(subclass, class)
# print(isinstance(food_two, Food))
# Any Functionality In Python Comes From The Main Class Of Python Which Is object ( Everything in python is object )
# print(isinstance(food_two, object))


#### Multiple Inheritance ####
# class Base:
#     print("Base")


# class DerivedOne(Base):
#     print("Derived One")


# class DerivedTwo(DerivedOne):
#     print("Derived Two")


# object1 = DerivedTwo()
# print(DerivedTwo.mro())


# class BaseOne:
#     def __init__(self):
#         print("Message From Base One")

#     def func_one(self):
#         print("One")


# class BaseTwo:
#     def __init__(self):
#         print("Message From Base Two")

#     def func_two(self):
#         print("Two")


# class Derived(BaseOne, BaseTwo):
#     pass


# object1 = Derived()
# print(Derived.mro())

# print(object1.func_one)
# print(object1.func_two)

# object1.func_one()
# object1.func_two()


##### Polymorphism ( Many Forms ) ##### 
# class A:
#     def do_something(self):
#         print("From Class A")
#         raise NotImplementedError("Derived Class Must Implement This Method")


# class B(A):
#     pass


# class C(A):
#     pass


# my_object = B()
# my_object.do_something()


##### Encapsulation #####
# class Member:
#     def __init__(self, name):
#         self.name = name  # Public


# one = Member("Mohamed")
# print(one.name)
# one.name = "Osama"
# print(one.name)

# class Member:
#     def __init__(self, name):
#         self._name = name  # Protected


# one = Member("Mohamed")
# print(one._name)
# one._name = "Osama"
# print(one._name)


# class Member:
#     def __init__(self, name):
#         self.__name = name  # Private

#     def say_hello(self):
#         return f"Hello {self.__name}"


# one = Member("Mohamed")
# print(one.__name)
# print(one.say_hello())
# print(one._Member__name) # Will Print The Name For Sorry Even If It Is A Private Attribute Because It's Like A Name Convention Between The Developers Not Built In Python

# Getters And Setters
# class Member:
#     def __init__(self, name):
#         self.__name = name # Private Property

#     def say_hello(self):
#         return f"Hello {self.__name}"

#     def get_name(self):  # Getter
#         return self.__name

#     def set_name(self, new_name):  # Setter
#         self.__name = new_name


# one = Member("Mona")

# print(one.get_name())

# one.set_name("Ebrahim")
# print(one.get_name())


# @property Decorator  => It Is Useful To Use The Method As A Property => بستخدم الديكوريتور ده لما احتاج احول اي ميسود فى الكلاس لخاصية بشرط ان الميسود متكونش بتعمل اي حاجة غير انها بترجع قية
# class Member:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         return f"Hello {self.name}"

#     @property
#     def age_in_days(self):
#         return self.age * 365


# one = Member("Mohamed", 22)
# print(one.name)
# print(one.age)
# print(one.say_hello())
# print(one.age_in_days)
# print(one.age_in_days())


##### ABC => Abstract Base Class ( مجرد يعني مبيعملش حاجة وفي نفس الوقت رئيسي) #####
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class

# from abc import ABCMeta, abstractmethod


# class Programming(metaclass=ABCMeta):
#     @abstractmethod
#     def has_oop(self):
#         pass

#     def has_name(self):
#         pass


# class Python(Programming):
#     def has_oop(self):
#         return "Yes"


# class Pascal(Programming):
#     def has_oop(self):
#         return "No"


# one = Python()
# two = Pascal()

# print(two.has_oop())


################ Exercises ( OOP ) #################
# class PlayerCharacter:
#     membership = True

#     def __init__(self, name, age):
#         if age >= 18:
#             self.name = name
#             self.age = age

#     def run(self):
#         print("Run")

#     @classmethod
#     def adding_things(cls, num1, num2):
#         return num1 + num2

#     @staticmethod
#     def adding_things2(num1, num2):
#         return num1 + num2


# player1 = PlayerCharacter("Mohamed", 22)
# player2 = PlayerCharacter("Cindy", 32)
# player1.attack = True

# print(player1.name)
# print(player2.name)
# print(player1.attack)
# print(player1.adding_things(2,4))
# print(PlayerCharacter.adding_things(2,4))
# print(player1.adding_things2(3,4))


# Exercise Extending List
# class SuperList(list):
#     def __len__(self):
#         return 1000


# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(5)
# super_list1.append(6)
# print(super_list1[0])
# print(super_list1[1])
# print(issubclass(SuperList, list))
# print(issubclass(list, object))


################################## SQLite Database ##################################
# Notes
# 1- cursor => all operations in SQL done by cursor not the connection itself
# 2- commit => save all changes
# 3- fetchone => returns a single record or None if no more rows are available, returns the data from one row and if there's no more rows it returns None
# 4- fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# 5- fetchmany(size) =>

# # Import SQLite Module
# import sqlite3

# # Create database and connect
# database = sqlite3.connect("app.db")

# # Setting up the cursor
# cr = database.cursor()

# # Create the tables and fields
# # database.execute("CREATE TABLE if not exists skills (name TEXT, progress INTEGER, user_id INTEGER)")
# cr.execute("CREATE TABLE users (user_id INTEGER, name TEXT)")

# # # Inserting data
# # cr.execute("INSERT INTO users(user_id, name) VALUES(1, 'Mohamed')")
# # cr.execute("INSERT INTO users(user_id, name) VALUES(2, 'Hoda')")
# # cr.execute("INSERT INTO users(user_id, name) VALUES(3, 'Mona')")

# users = ["Mohamed", "Ahmed", "Mona", "Abrar"]
# for id, user in enumerate(users):
#     cr.execute(f"INSERT INTO users(user_id, name) VALUES({id + 1}, '{user}')")

# # Save changes
# database.commit()

# # Close database
# # database.close()

# ## Retrieve Data From Database ##
# cr.execute("SELECT user_id, name FROM users")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())


# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------
# import sqlite3

# def get_all_data():
#     try:
#         # Connect To Database
#         db = sqlite3.connect("app.db")

#         # Print Success Message
#         print("Connected To Database Successfully")

#         # Setting Up The Cursor
#         cr = db.cursor()

#         # Fetch Data From Database
#         cr.execute("select * from users")

#         # Assign Data To Variable
#         results = cr.fetchall()

#         # Print Number Of Rows
#         print(f"Database Has {len(results)} Rows.")

#         # Printing Message
#         print("Showing Data:")

#         # Loop On Results
#         for row in results:
#             print(f"UserID => {row[0]},", end=" ")
#             print(f"Username => {row[1]}")

#     except sqlite3.Error as er:
#         print(f"Error Reading Data {er}")

#     finally:
#         if (db):
#             # Close Database Connection
#             db.close()
#             print("Connection To Database Is Closed")

# get_all_data()


#################################################### API ( Application Programming Interfaces ) ####################################################
# API :- is a set of commands, functions, protocols, and objects that programmers can use to create software or interact with an external system.
#        simply the API is an interface between your program and external program

# API Endpoint:- is simply a URL of the location of the data you want, and example of this is if you want to get some coin data you should use the URL (api.coinbase.com) to get the data.

# Some API requires parameters to work.

# Different responses or status code
# 1- 1XX :- means hold on something happening this not final.
# 2- 2XX :- means here you go everything was successful you should get the data you wanted.
# 3- 3XX :- means go away you don't have permission to the data you trying to get,
# 4- 4XX :- means you screwed up and the data you looking for doesn't even exist.
# 5- 5XX :- means the server you are looking at is down or maybe there's some other issue.

###### get the API of the ISS ( International Space Station ) ######
# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")   # this method help you to get the data you want from the endpoint
# print(response)

# print(response.status_code) # to print only the status code ( 200 means everything was successful )

# response.raise_for_status()  # there's alot of http status code so this method help us to show the user the actual problem

# data = response.json() # to get the actual data of this API
# data = response.json()["iss_position"] # to get a specific data of the json data, we get the data the as we get it in the dictionary
# print(data)

## to get the data in a tuple ##
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)

# print(iss_position)


##### generate quotes program #####
# from tkinter import *
# import requests

# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     qoute = data["quote"]
#     canvas.itemconfig(quote_text, text=qoute)

# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="./kanye-quotes/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="./kanye-quotes/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)

# window.mainloop()


####### sunrise-sunset API #######
# import requests

# my_lat = 26.820553
# my_lng = 30.802498

# parameters = {
#     "lat" : my_lat,
#     "lng" : my_lng,
#     "formatted": 0,
# }

# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()

# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# print(sunrise)
# print(sunset)


#### API Authentication ####
# when a big company has an api you must pay fot it they provide you with an API key to prevent people from abusing their service and limit their access to their API service
# and it's almost like your personal account number and password
# with this way they can track how much you're using their API and to authorize your access and deny your access once you gone over the limit.

# api_key = "d6741bc1dc48b39fdbf09ab4af79af21"   => the API key from openweathermap.org site

# apllist.fun  => is a website of fun APIs list to training on


#### HTTP requests ####
# 1- GET     => to ask the external program (request) to give us some piece of data (response)
# 2- POST    => give the external program the data and wait for response of ok
# 3- PUT     => to update the data in the external program
# 4- DELETE  => to delete the data in the external program


#### habit tracker project ####
# import requests
# from datetime import datetime

# username = "mohamedsalama"
# token = "jklf3fd34fhg34hg6"
# graph_id = "graph2"

# pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# # response = requests.post(url=pixela_endpoint, json=user_params)
# # print(response.text) # to see if the post request done right or not

# graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

# graph_config = {
#     "id": graph_id,
#     "name": "Cycling graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }

# headers = {
#     "X-USER-TOKEN": token
# }

# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)

# pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

# today = datetime(year=2023, month=10, day=11)

# pixel_data = {
#     "date": today.strftime(r"%Y%m%d"),
#     "quantity": "15",
# }

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# ## update request ##

# update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime(r'%Y%m%d')}"

# new_pixel_data = {
#     "quantity": "4.5"
# }

# requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)


# ## Delete Request ##
# delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime(r'%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

#################################################################### Exercises ####################################################################
# Practical Email Slice Exercise
# name = input("What's Your Name: \n").strip().capitalize()
# email = input("What's Your Email: \n").strip()
# username = email[:email.index("@")]
# domain = email[email.index("@") + 1:]

# print(f"Hello {name} Your Email Is {email}")
# print(f"Your Username Is {username} And Your Domain Is {domain}")


## Age Details Exercise ##
# age = int(input("What's Your Age: "))
# death = int(input("Your Full Age: "))
# life = death - age
# months = life * 12
# weeks = months * 4
# days = life * 365

# print("You will Live For: ")
# print(f"{months:,d} Months")
# print(f"{weeks:,d} Weekss")
# print(f"{days:,d} Days")


## Band Name Generator ##
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

# Solution 1
# a, b = b, a

# print(a)
# print(b)

# Solution 2
# c = a
# a = b
# b = c

# print(a)
# print(b)


# Calculate How Many months weeks days left in our lifes until 90 years
# age = 90 - int(input("Type Your Age Here: ").strip())

# months = age * 12
# weeks = months * 4
# days = age * 365

# print(f"You Have {days} Days, {weeks} Weeks, {months} Months Left.")


# Tip Calaculator
# bill = float(input("What was the total bill? $:- "))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? :- "))
# people = int(input("How many people to split the bill?:- "))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# # final_amount = round(bill_per_person, 2)
# final_result = "{:.2f}".format(bill_per_person)

# print(f"Each person should pay: ${final_result}")


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
#     "You're At A Cross Road. Where Do You Want To Go? Type \"left\" or \"right\":- ").strip().lower()
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

# # Hard Level
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

# Area Painting Calculation
# import math
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# def paint_calc(height, width, cover):
#     number_of_cans = (height * width) / cover
#     print(f"You Will Need {math.ceil(number_of_cans)} Of Paint For This Partical Area")
# paint_calc(height=test_h, width=test_w, cover=coverage)


# Primer Number Checker
# n = int(input("Check this number: "))


# def prime_checker(number):
#     if number % 2 == 0:
#         print("This Is Prime Number")
#     else:
#         print("This Is Not Prime Number")


# prime_checker(number=n)


########## Calculator App ##########
# logo = """
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
# |_____________________|
# """


# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }


# def calculator():
#     print(logo)
#     num1 = float(input("What's the first number?: "))
#     for symbol in operations:
#         print(symbol)
#     should_continue = True

#     while should_continue:
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What's the next number?: "))
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()


# calculator()


####### Caesar Cipher #######
# logo = """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
#             88             88
#            ""             88
#                           88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP""""""" 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
#               88
#               88
# """

# print(logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# while True:
#     direction = input(
#         "Type 'encode' to encrypt, type 'decode' to decrypt:\n".lower())
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     shift = shift % 26

#     def encrypt(plain_text, shift_amount):
#         cipher_text = ""
#         for letter in plain_text:
#             if letter in alphabet:
#                 position = alphabet.index(letter)
#                 new_position = position + shift_amount
#                 new_letter = alphabet[new_position]
#                 cipher_text += new_letter
#             else:
#                 cipher_text += letter
#         print(f"The Encoded Text Is {cipher_text}.")

#     def decrypt(plain_text, shift_amount):
#         decrypt_text = ""
#         for letter in plain_text:
#             if letter in alphabet:
#                 position = alphabet.index(letter)
#                 new_position = position - shift_amount
#                 new_letter = alphabet[new_position]
#                 decrypt_text += new_letter
#             else:
#                 decrypt_text += letter
#         print(f"The Decoded Text Is {decrypt_text}.")

#     if direction == "encode":
#         encrypt(plain_text=text, shift_amount=shift)
#     elif direction == "decode":
#         decrypt(plain_text=text, shift_amount=shift)
#     check = input(
#         "Type 'Yes' If You Want To Go Again. Otherwise Type 'No'. \n").capitalize()
#     if check == "Yes":
#         continue
#     else:
#         print("See You Next Time :)")
#         break


####### Grading Program ########
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Failed"

# print(student_grades)


####### Dictionary In A List ########
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]

# # print(travel_log[0]["country"])


# def add_new_country(country, times, cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = times
#     new_country["cities"] = cities
#     travel_log.append(new_country)


# add_new_country(country="Russia", times=2, cities=[
#                 "Moscow", "Saint Petersburg"])
# print(travel_log)


##### Bisection Search Alghorithm #####
# print("Please Think Of A Number Between 0 and 100:- ")
# low = 0
# high = 100
# medium = (low + high) // 2
# state = True
# while state:
#     print(f"Is Your Secret Number {medium}")
#     guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low, Enter 'c' to indicate the guess is correct:- ")
#     if guess == 'c':
#         print(f"Game Over, Your Guess {medium} Is Correct.")
#         state = False
#     elif guess == 'h':
#         high = medium
#         medium = (high + low) // 2
#     elif guess == 'l':
#         low = medium
#         medium = (high + low) // 2
#     else:
#         print("You need to enter a number")


########### Heart Shape ############
# from turtle import *
# color("red")
# begin_fill()
# pensize(10)
# left(50)
# forward(133)
# circle(50, 200)
# right(140)
# circle(50, 200)
# forward(133)
# end_fill()


########## Circle Shape ########
# import turtle
# import colorsys
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("red")
# t.speed(0)
# n = 36
# h = 0
# for i in range(460):
#     c = colorsys.hsv_to_rgb(h, 1, 0.9)
#     h += 1/n
#     t.color(c)
#     t.left(145)
#     for j in range(5):
#         t.forward(300)
#         t.left(150)


######### Flower #########
# import turtle

# turtle.penup()
# turtle.left(90)
# turtle.fd(200)
# turtle.pendown()
# turtle.right(90)
# turtle.fillcolor("red")
# turtle.begin_fill()
# turtle.circle(10, 180)
# turtle.circle(25, 110)
# turtle.left(50)
# turtle.circle(60, 45)
# turtle.circle(20, 170)
# turtle.right(24)
# turtle.fd(30)
# turtle.left(10)
# turtle.circle(30, 110)
# turtle.fd(20)
# turtle.left(40)
# turtle.circle(90, 70)
# turtle.circle(30, 150)
# turtle.right(30)
# turtle.fd(15)
# turtle.circle(80, 90)
# turtle.left(15)
# turtle.fd(45)
# turtle.right(165)
# turtle.fd(20)
# turtle.left(155)
# turtle.circle(150, 80)
# turtle.left(50)
# turtle.circle(150, 90)
# turtle.end_fill()

# turtle.left(150)
# turtle.circle(-90, 70)
# turtle.left(20)
# turtle.circle(75, 105)
# turtle.setheading(60)
# turtle.circle(80, 98)
# turtle.circle(-90, 40)

# turtle.left(180)
# turtle.circle(90, 40)
# turtle.circle(-80, 98)
# turtle.setheading(-83)

# turtle.fd(30)
# turtle.left(90)
# turtle.fd(25)
# turtle.left(45)
# turtle.fillcolor("green")
# turtle.begin_fill()
# turtle.circle(-80, 90)
# turtle.right(90)
# turtle.circle(-80, 90)
# turtle.end_fill()
# turtle.right(135)
# turtle.fd(60)
# turtle.left(180)
# turtle.fd(85)
# turtle.left(90)
# turtle.fd(80)

# turtle.right(90)
# turtle.right(45)
# turtle.fillcolor("green")
# turtle.begin_fill()
# turtle.circle(80, 90)
# turtle.left(90)
# turtle.circle(80, 90)
# turtle.end_fill()
# turtle.left(135)
# turtle.fd(60)
# turtle.left(180)
# turtle.fd(60)
# turtle.right(90)
# turtle.circle(200, 60)
# turtle.done()


###################### Messi ######################
# from sketchpy import canvas
# Turtle = canvas.sketch(x_offset=290, y_offset=320)


# Turtle.draw_fn("face_out", co=(233, 183, 151), mode=0)
# Turtle.draw_fn("beard_out", co=(30, 25, 31), mode=0)

# Turtle.draw_fn("chin1", co=(204, 139, 124), mode=0)
# Turtle.draw_fn("chin2", co=(204, 139, 124), mode=0)

# Turtle.draw_fn("lip_lower", co=(214, 125, 100), mode=0)
# Turtle.draw_fn("lip_upper", co=(186, 30, 21), mode=0)

# Turtle.draw_fn("nostril", co=(8, 15, 29), mode=0)
# Turtle.draw_fn("nose_curve", co=(128, 69, 56), mode=0)
# Turtle.draw_fn("right_eyebrow", co=(12, 16, 22), mode=0)
# Turtle.draw_fn("left_eyebrow", co=(12, 16, 22), mode=0)

# Turtle.draw_fn("noseline", co=(12, 16, 22), mode=0)

# Turtle.draw_fn("eyelid", co=(13, 15, 23), mode=0)
# Turtle.draw_fn("eye", co=(17, 12, 20), mode=0)
# Turtle.draw_fn("sclera", co=(230, 231, 229), mode=0)
# Turtle.draw_fn("eyeball", co=(15, 25, 15), mode=0)
# Turtle.draw_fn("eyeball_centre", co=(230, 231, 229), mode=0)

# Turtle.draw_fn("hair_outline", co=(12, 16, 25), mode=0)
# Turtle.draw_fn("hair_shade1", co=(12, 16, 25), mode=0)
# Turtle.draw_fn("hair_shade2", co=(61, 44, 52), mode=0)
# Turtle.draw_fn("hair_shade3", co=(119, 64, 75), mode=0)
# Turtle.draw_fn("hair_shade4", co=(119, 64, 75), mode=0)
# Turtle.draw_fn("hair_shade5", co=(61, 44, 52), mode=0)
# Turtle.draw_fn("hair_shade6", co=(119, 64, 75), mode=0)
# Turtle.draw_fn("hair_shade7", co=(61, 44, 52), mode=0)
# Turtle.draw_fn("hair_shade8", co=(61, 44, 52), mode=0)

# Turtle.draw_fn("throat", co=(245, 207, 171), mode=0)
# Turtle.draw_fn("throat_shade1", co=(236, 180, 153), mode=0)
# Turtle.draw_fn("throat_shade2", co=(236, 180, 153), mode=0)

# Turtle.draw_fn("ear_line1", co=(16, 10, 8), mode=0)
# Turtle.draw_fn("ear_line2", co=(16, 10, 8), mode=0)
# Turtle.draw_fn("ear_line3", co=(16, 10, 8), mode=0)
# Turtle.draw_fn("ear_shade1", co=(212, 138, 124), mode=0)
# Turtle.draw_fn("ear_shade2", co=(212, 138, 124), mode=0)
# Turtle.draw_fn("ear_shade3", co=(212, 134, 122), mode=0)

# Turtle.draw_fn("beard_shade1", co=(124, 77, 75), mode=0)
# Turtle.draw_fn("beard_shade2", co=(127, 76, 76), mode=0)

# Turtle.draw_fn("face_shade1", co=(209, 137, 122), mode=0)
# Turtle.draw_fn("face_shade2", co=(208, 138, 119), mode=0)

# Turtle.draw_fn("eye_shade1", co=(209, 143, 126), mode=0)
# Turtle.draw_fn("eye_shade2", co=(209, 143, 126), mode=0)

# Turtle.draw_fn("face_shade3", co=(245, 207, 171), mode=0)
# Turtle.draw_fn("face_shade4", co=(240, 208, 169), mode=0)

# Turtle.draw_fn("forhead_shade1", co=(202, 135, 119), mode=0)

# Turtle.draw_fn("tshirt", co=(0, 30, 82), mode=0)
# Turtle.draw_fn("tshirt_color1", co=(193, 36, 57), mode=0)
# Turtle.draw_fn("tshirt_color2", co=(4, 31, 138), mode=0)
# Turtle.draw_fn("tshirt_color3", co=(3, 35, 180), mode=0)

# Turtle.draw_fn("end", retain=True, co=(230, 239, 234), mode=0)


############### Annoying My Friend ##############
# import random
# import pyautogui as pg
# import time
# # my_list = ("I Hacked Your Friend Computer :)")
# time.sleep(8)
# for i in range(100):
#     # a = random.choice(animal)
#     pg.write("stop this all of you")
#     pg.press("enter")


# Drawing Bill Gates
# from sklearn.preprocessing import scale
# pic = canvas.sketch_from_svg(
#     r"D:\Programming\Python\Python Projects\7-removebg-preview.svg")
# pic.draw()


#### Drawing Elzero ####
# from sketchpy import canvas
# pic = canvas.sketch_from_svg(
#     r"D:\Programming\Python\Python Projects\manar.svg")
# pic.draw()


# ########### Convert The Image Into Sketch ##########
# import cv2
# image = cv2.imread(
#     "cristi.jpg")
# grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# invert = cv2.bitwise_not(grey_img)
# blur = cv2.GaussianBlur(invert, (21, 21), 0)
# invertedblur = cv2.bitwise_not(blur)
# sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
# cv2.imwrite("test2.png", sketch)


########### Car Game ############
# from ursina import *
# import random

# app = Ursina()
# camera.orthographic = True

# camera.fov = 10

# car = Entity(model='quad', texture='car',
#              collider='box', scale=(2, 1), rotation_z=-90, y=-3)

# road1 = Entity(model='quad', texture='road', scale=15, z=1)
# road2 = duplicate(road1, y=15)
# pair = [road1, road2]

# enemies = []


# def newEnemy():
#     val = random.uniform(-2, 2)
#     new = duplicate(car, texture='enemy', x=2*val, y=25, color=color.random_color(),
#                     rotation_z=90 if val < 0 else -90)
#     enemies.append(new)
#     invoke(newEnemy, delay=0.5)


# newEnemy()

# def update():
#     car.x -= held_keys['a']*5*time.dt
#     car.x += held_keys['d']*5*time.dt
#     for road in pair:
#         road.y -= 6*time.dt
#         if road.y < -15:
#             road.y += 30
#     for enemy in enemies:
#         if enemy.x < 0:
#             enemy.y -= 10 * time.dt
#         else:
#             enemy.y -= 5 * time.dt
#         if enemy.y < -10:
#             enemies.remove(enemy)
#             destroy(enemy)
#     if car.intersects().hit:
#         car.shake()


# app.run()

####### Tkinter Youtube Downloader #######
# from tkinter import *
# import tkinter.messagebox
# import pytube


# def download():
#     try:
#         link = entry.get()
#         yt = pytube.YouTube(link)
#         videos = yt.streams.all()
#         s = 1
#         for v in videos:
#             tkinter.messagebox.showinfo("Video Info", str(s)+" "+str(v))
#             s += 1
#         n = int(input("Enter the number of the video: "))
#         vid = videos[n-1]

#         vid.download(r"C:\Users\Moham\Downloads")
#         tkinter.messagebox.showinfo(
#             "Download Completed", "Downloaded Successfully")
#     except Exception as e:
#         tkinter.messagebox.showinfo("Error Occured", e)


# root = Tk()
# root.title("Youtube Downloader")
# root.geometry("500x600")

# # file = PhotoImage(file="youtube.png")
# # headingIcon = Label(root, image=file)
# # headingIcon.pack(side=TOP)

# label = Label(root, text="Youtube Downloader", font="Verdana 15 bold")
# label.pack(side=TOP)

# entry = Entry(root, width=50, borderwidth=5)
# entry.pack(side=TOP)

# button = Button(root, text="Download", command=download)
# button.pack(side=TOP)

# root.mainloop()


################ remove image Background ################
# from rembg import remove
# from PIL import Image
# input_path = "Mohamed.jpg"
# output_path = "Mohamed"
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)


############## Code_Wars ##############
## Lario And Muigi Pipe Problem ##
# def pipe_fix(numbers):
#     return list(range(min(numbers), max(numbers) + 1))

# print(pipe_fix([-1,3,5]))


## Digit*Digit ##
## My_Solution ##
# def square_digits(num):
#     for n in str(num):
#         print(int(n) ** 2, end="")


# square_digits(123)

# Another_Solution
# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)

# print(square_digits(123))
