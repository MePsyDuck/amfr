from tkinter import *
from tkinter import filedialog

from facial_recog.app import *


def train_button():
    for class_id in get_all_classes():
        train(class_id=class_id)
    status_text.set('Training of classifiers successful')


def add_stud_button():
    if not e1.get() or e2.get():
        status_text.set('Please enter subject ID and class ID')
    else:
        add_subject_to_class(sub_id=e1.get(), class_id=e2.get())
        status_text.set('Student added to records successfully')


def choose_image_button():
    if e2.get():
        file = filedialog.askopenfilename(initialdir="C:/",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")),
                                          title="Choose an image")
        print(file)
        label = predict(img=path_to_img(file), class_id=int(e2.get()))
        if label is not None:
            status_text.set(str(label) + ' is present in this class')
        else:
            status_text.set('The student does not belong to this class')
    else:
        status_text.set('Please enter a class ID')


root = Tk()

root.title("Attendance Monitoring")

Label(root, text="Student ID").grid(row=0)
Label(root, text="Class ID").grid(row=1)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(root, text='Detect Image', command=choose_image_button)
b2 = Button(root, text='Add Student', command=add_stud_button)
b3 = Button(root, text='Train', command=train_button)
b1.grid(row=3, column=0, sticky=W, pady=5, padx=0)
b2.grid(row=3, column=1, sticky=W, pady=5, padx=0)
b3.grid(row=4, column=0, sticky=W, pady=5, padx=0)

status_text = StringVar()

w1 = Label(root, textvariable=status_text)
w1.grid(row=5)

root.mainloop()
