# Import Steamlit so we will be able to use it's methods/functions
import streamlit as st

# Exercise 1 : Input , Output and Variables
# name = st.text_input("Enter your name")

# only prints the Hello {name} if input box is not empty
# if name:
#     st.write("Hello " + name)

st.divider()

# Challenge 1 (answer)
# name = st.text_input("Enter your name")
# gender = st.selectbox("State your gender", ["Male", "Female"])
# age = st.text_input("State your age", 18)

# if name and gender and age:
#     st.text(f"Hello {name}, you are {gender} and this year you are {age} years old")

st.divider()

# Exercise 2 : Logical Conditioning
# age = 23
# if else statement
# if age >= 18:
#     st.write("You are an adult ")
# else:
#     st.write("You are not an adult")

# Challenge 2 : Logical Conditioning
# name = st.text_input("Enter your name")
# gender = st.selectbox("State your gender", ["Male", "Female"])
# age = int(st.text_input("State your age", 18))
# photo = st.camera_input("Smile! take a picture here.")

# conditional logic to run different statements
# All inputs and photo must be provided before any condition below is true
# if age >= 18 and gender == "Male" and photo:
#     st.write("You are a male adult")
#     st.image(photo)
# elif age < 18 and gender == "Male" and photo:
#     st.write("You are a young boy")
#     st.image(photo)
# elif age >= 18 and gender == "Female" and photo:
#     st.write("You are a female adult")
#     st.image(photo)
# elif age < 18 and gender == "Female" and photo:
#     st.write("You are a young girl")
#     st.image(photo)

st.divider()

# Exercise 3 : Data and Loops (part 1)
# data list
# fruits = ["apple", "banana", "orange"]

# Dictionary
# person = {"name": "John", "age": 30, "city": "New York"}

# For loop to show list
# for fruit in fruits:
#     st.write(fruit)

# While loop
# for key, value in person.items():
#     st.write(key + ": " + str(value))

# Challenge 3 : Data and Loops
# name = st.text_input("Enter your name")
# gender = st.selectbox("State your gender", ["Male", "Female"])
# age = st.text_input("State your age", 18)

# mydict = {}
# mydict["name"] = name
# mydict["gender"] = gender
# mydict["age"] = age

# st.write(mydict)
# Alternatively, just write the name of the variable to "print" the dictionary on the webpage
# mydict

# Extra challenge:
# mylist = []
# mylist.append(mydict)


# Exercise 3 : Functions (part 2)
# def check_age_gender(age, gender):
#     if age >= 18:
#         if gender == "male":
#             st.write("You are an adult male")
#         elif gender == "female":
#             st.write("You are an adult female")
#     else:
#         if gender == "male":
#             st.write("You are a young boy")
#         elif gender == "female":
#             st.write("You are a young girl")


# def main():
#     st.title("Age and Gender Check")

#     age = st.number_input("Enter your age:")
#     gender = st.selectbox("Select your gender:", ["male", "female"])

#     check_age_gender(age, gender)


# if __name__ == "__main__":
#     main()

st.divider()

# Exercise 4 : Complete a Streamlit app with function


def my_list_func():
    name = st.text_input("Enter your name")
    gender = st.selectbox("State your gender", ["Male", "Female"])
    age = int(st.text_input("State your age", 18))

    mydict = {}
    mydict["name"] = name
    mydict["gender"] = gender
    mydict["age"] = age

    st.write(mydict)


def main():
    my_list_func()


if __name__ == "__main__":
    main()

# Exercise 5 : Elements of a chatbot
