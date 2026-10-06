# strings_formating

# name = "sahil"
# phone =" 1234567890"
# college ="muffakhamja college"
# greating =f'''hello{name},

# your phone number is {phone}. 

# thanks for joining {college}'''
# print(greating)

# sting_indexing.

# name = "sahil"
# print(name[0])  # Output: s
# print(name[1])  # Output: a
# print(name[-2])  # Output: h
# print(name[3])  # Output: i
# print(name[4])  # Output: l

# sting_slicing.

# str = "sahil"
# print(str[0:3])  # Output: sah
# print(str[1:4])  # Output: ahi
# print(str[:3])   # Output: sah
# print(str[2:])   # Output: hil
# print(str[0:3:2])  # Output: sh

# sen = "monday is a hectic day"
# print(sen[15:19])
# print(len(sen))
# print(sen[15])
# print(sen[2:9:3])
# print(sen.count)

# acc = "1212 5152 3636"
# a=(acc[9:])
# print(f"**** **** {a}")


# string_problems 
#  1.
# name = "sahil"
# amount = "50000"
# due_days = "10"
# # template = f'''
#         hi {name},
#         how are you?
#         you have rs.{amount} pending 
#         kindly clear dues before {due_days}
#         thanks '''
# print(template)

#   2.prob
     
# template = '''
#                hi ,name
#                how are you?
#                you have rs.xxxx pending 
#                kindly clear dues before x days
#                thank'''
# new= template.replace("name", name).replace("xxxx", '7000').replace("x", '7')
# print(new)

#   3. prob

# sen="i like roses, but i use guns"
# a=sen.count("a")
# b=sen.count("e")
# c=sen.count("i")
# d=sen.count("o")
# e=sen.count("u")
# print(a+b+c+d+e)        

# GRADE CALCULATOR
# m=int(input("marks in maths: "))
# s=int(input("marks in science: "))
# e=int(input("marks in english: "))
# total_marks =m+s+e
# average= total_marks/3
# percentage=average 
# grade=""
# if percentage>=90:
#     grade="A"
# elif percentage>=80 and percentage<90:
#     grade="B"
# elif percentage>=70 and percentage<80:
#     grade="C"
# else:
#     grade="p"
# print(f"total marks: {total_marks} \naverage: {average} \ngrade: {grade}")

# CHECK PALINDROME 
# n=input("enter a string: ")
# s=(n[::-1])
# if n==s:
#     print("palindrome")
# else:
#     print("not palindrome")

# GREATEST OF THREE NUMBERS
# n1=int(input("give"))
# n2=int(input("give"))
# n3=int(input("give"))
# great="0"
# if n1>n2:
#     if n1>n3:
#         great=n1
#     else:
#         great=n3
# elif n2>n1:
#     if n2>n3:
#         great=n2
#     else:
#         great=n3
# elif n3>n1:
#     if n3>n2:
#         great=n3
#     else:
#         great=n2
# print(great)

# LEAP YEAR CHECKER

# year =int (input())
# leap=False
# if year%100==0 and year%400 !=0:
#     leap=False
# elif year%4==0:
#     leap=True
# else:
#     leap=False
# print(leap)

# temperature conversion

temperature = float(input("Enter temperature: "))
unit = input("Enter Units (K or F or C): ").upper()

if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273
    print(f"Temperature in Fahrenheit: {fahrenheit:.1f}F")
    print(f"Temperature in Kelvin: {kelvin:.0f}K")

elif unit == "F":
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273
    print(f"Temperature in Celsius: {celsius:.1f}C")
    print(f"Temperature in Kelvin: {kelvin:.0f}K")

elif unit == "K":
    celsius = temperature - 273
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Celsius: {celsius:.1f}C")
    print(f"Temperature in Fahrenheit: {fahrenheit:.1f}F")

else:
    print("Invalid Unit! Please enter K, F, or C.")


    
