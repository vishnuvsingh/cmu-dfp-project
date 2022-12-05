from tkinter import *
from tkinter import ttk
import HouseRentals
import jobs_ui
import furniture_ui

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

lb1 = Label(scrollable_frame, text="\nTartans in Transit\n", font=("Helvetica", 32))
lb1.pack(anchor='nw')

lb2 = Text(scrollable_frame,font=("Helvetica", 12), height=7, width=130)
str1 = "\nHey Tartans, Welcome to Tartans in Transit, your one stop destination " \
       "to kick start your life in Pittsburgh. " \
       "We have curated the below sources of information.\n Housing: All available rentals around CMU, distance from " \
       "campus and driving time to campus etc.\n On Campus Jobs: Get " \
       "information about all on campus full time and part" \
       " time jobs.\n Furniture: The best deals on furniture which could be delivered at your door step.\n"
lb2.insert(END, str1)
lb2.pack(anchor='nw')

text = Label(scrollable_frame, text="House Rentals")
text.pack(anchor='nw')
click_btn1 = PhotoImage(file='images/house.png', master=scrollable_frame)
img_label1 = Label(image=click_btn1)
button1 = Button(scrollable_frame, image=click_btn1, borderwidth=0, command=HouseRentals.run)
button1.pack(anchor='nw')

text = Label(scrollable_frame, text="Furniture")
text.pack(anchor='nw')
click_btn2 = PhotoImage(file='images/furniture.png', master=scrollable_frame)
img_label2 = Label(image=click_btn2)
button2 = Button(scrollable_frame, image=click_btn2, borderwidth=0, command=furniture_ui.run)
button2.pack(anchor='nw')

text = Label(scrollable_frame, text="On Campus Jobs")
text.pack(anchor='nw')
click_btn3 = PhotoImage(file='images/jobs.png', master=scrollable_frame)
img_label3 = Label(image=click_btn3)
button3 = Button(scrollable_frame, image=click_btn3, borderwidth=0, command=jobs_ui.run)
button3.pack(anchor='nw')

container.pack(fill='both', expand=1)
canvas.pack(side="left", fill="both", expand=True)
scrollbar_y.pack(side="right", fill="y")

root.title('Hello Python')
root.mainloop()

