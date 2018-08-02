from tkinter import *

def insert_box():
    root = Tk()
    root.title("Email Validator")
    T = Text(root, height=5, width=35)
    T.pack()
    email = T.insert(END, "Please enter your\nemail address here: \n")
    mainloop()
    return email

def insert():
    email = input("please enter your email address here:")
    return email

def separator(email):
    if "@" in email:
        part1, part2 = email.split("@")
    else:
        return False, email
    return True, (part1, part2)

def validate1(part1):
    if len(part1.split(" ")) > 1:
        return False, part1
    else:
        name = part1
        return True, name

def validate2(part2):
    if len(part2.split(" ")) > 1:
        return False, part2
    else:
        extensions = part2.split(".")
        return True, extensions

def validate_ext(ext):
    if len(ext) > 4:
        return False, None, None
    host = ext[0]
    extension = ext[1:]
    return True, host, extension


def main():
    email = insert()
    bool, object = separator(email)
    if bool:
        bool2, object2 = validate1(object[0])
        if bool2:
            bool3, ext = validate2(object[1])
            if bool3:
                bool4, host, extension = validate_ext(ext)
            else:
                bool3 = False
        else:
            bool2 = False

    else:
        bool2 = False
    if bool2 and bool3 and bool4:
        print("your email is correct: " + str(email))
    else:
        print("your email is incorrect")

if __name__ == "__main__":
    main()
