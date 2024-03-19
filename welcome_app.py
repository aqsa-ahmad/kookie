import streamlit as st

def welcome_student(name):
    st.write("Welcome, {}! We're thrilled to have you as a part of our community.".format(name))

def main():
    st.title("Welcome Student!")
    student_name = st.text_input("Please enter your name:")
    if student_name:
        welcome_student(student_name)

if __name__ == "__main__":
    main()
