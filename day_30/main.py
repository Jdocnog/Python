
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
# make_pie(4)

# try:
#     file = open("a_file.txt")
#     a_diction = {"key":"value"}
#     print(a_diction["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"Key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise Er


# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight/height**2
# print(bmi)