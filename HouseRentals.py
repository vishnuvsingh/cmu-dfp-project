from tkinter import *
from tkinter import ttk
import pandas as pd
import housing_ui


def run():
    root = Tk()
    root.geometry("1500x1500")
    container = ttk.Frame(root)
    canvas = Canvas(container)
    scrollbar_y = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_y.set)

    lb1 = Label(scrollable_frame, text="\nHousing Rentals Menu\n", font=("Helvetica", 32))
    lb1.pack(anchor='nw')

    lb2 = Text(scrollable_frame,font=("Helvetica", 12), height = 7, width = 130)
    str1 = "\nHey Tartans, here is a brief summary of the neighbourhoods closest to the campus and preffered by most " \
           "students.\n We have listed down some esential features to choose a neighbourhood based on your preference. " \
           "\n Click on any of these neighbourhoods to view the details of rentals available\n"
    lb2.insert(END, str1)
    lb2.pack(anchor='nw')

    ratings = pd.read_csv('data/House/ratings.csv')

    text = Label(scrollable_frame, text="ShadySide")
    text.pack(anchor='nw')
    click_btn1 = PhotoImage(file='images/Shadyside.png', master=scrollable_frame)
    button1 = Button(scrollable_frame, image=click_btn1, borderwidth=0, command=housing_ui.run_shadyside)
    button1.pack(anchor='nw')

    lb3 = Text(scrollable_frame, font=("Helvetica", 12), height=7, width=130)
    str2 = "Shadyside Neighbourhood Rating - \n\n" \
           + str(ratings.columns[1]) + " - " + str(ratings.iloc[0, 1]) + "\n" \
           + str(ratings.columns[2]) + " - " + str(ratings.iloc[0, 2]) + "\n" \
           + str(ratings.columns[3]) + " - " + str(ratings.iloc[0, 3]) + "\n"
    lb3.insert(END, str2)
    lb3.pack(anchor='nw')

    text = Label(scrollable_frame, text="Squirrel Hill North")
    text.pack(anchor='nw')
    click_btn2 = PhotoImage(file='images/SQN.png', master=scrollable_frame)
    button2 = Button(scrollable_frame, image=click_btn2, borderwidth=0, command=housing_ui.run_squirrel_north)
    button2.pack(anchor='nw')

    lb3 = Text(scrollable_frame, font=("Helvetica", 12), height=7, width=130)
    str2 = "Squirrel Hill North Neighbourhood Rating - \n\n" \
           + str(ratings.columns[1]) + " - " + str(ratings.iloc[2, 1]) + "\n" \
           + str(ratings.columns[2]) + " - " + str(ratings.iloc[2, 2]) + "\n" \
           + str(ratings.columns[3]) + " - " + str(ratings.iloc[2, 3]) + "\n"
    lb3.insert(END, str2)
    lb3.pack(anchor='nw')

    text = Label(scrollable_frame, text="Squirrel Hill South")
    text.pack(anchor='nw')
    click_btn3 = PhotoImage(file='images/SQS.png', master=scrollable_frame)
    button3 = Button(scrollable_frame, image=click_btn3, borderwidth=0, command=housing_ui.run_squirrel_south)
    button3.pack(anchor='nw')

    lb3 = Text(scrollable_frame, font=("Helvetica", 12), height=7, width=130)
    str2 = "Squirrel Hill South Neighbourhood Rating - \n\n" \
           + str(ratings.columns[1]) + " - " + str(ratings.iloc[1, 1]) + "\n" \
           + str(ratings.columns[2]) + " - " + str(ratings.iloc[1, 2]) + "\n" \
           + str(ratings.columns[3]) + " - " + str(ratings.iloc[1, 3]) + "\n"
    lb3.insert(END, str2)
    lb3.pack(anchor='nw')

    text = Label(scrollable_frame, text="Oakland")
    text.pack(anchor='nw')
    click_btn4 = PhotoImage(file='images/Oakland.png', master=scrollable_frame)
    button4 = Button(scrollable_frame, image=click_btn4, borderwidth=0, command=housing_ui.run_oakland)
    button4.pack(anchor='nw')

    lb3 = Text(scrollable_frame, font=("Helvetica", 12), height=7, width=130)
    str2 = "Oakland Neighbourhood Rating - \n\n" \
           + str(ratings.columns[1]) + " - " + str(ratings.iloc[3, 1]) + "\n" \
           + str(ratings.columns[2]) + " - " + str(ratings.iloc[3, 2]) + "\n" \
           + str(ratings.columns[3]) + " - " + str(ratings.iloc[3, 3]) + "\n"
    lb3.insert(END, str2)
    lb3.pack(anchor='nw')

    container.pack(fill='both', expand=1)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_y.pack(side="right", fill="y")

    root.title('Hello Python')
    root.mainloop()
