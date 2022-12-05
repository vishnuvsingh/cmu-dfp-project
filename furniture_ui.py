import tkinter as tk
from tkinter import ttk
import pandas as pd
import webbrowser
from functools import partial
from tkHyperlinkManager import HyperlinkManager


def clear():
    for T in elements:
        T.destroy()
    elements.clear()

def apply():
    clear()
    filtered_type = clicked.get()
    search_text = search_box.get().strip().lower()
    if filtered_type == 'All Types' and search_text == '':
        print_df(df)
        return
    filtered_df = df
    if filtered_type != 'All Types':
        filtered_df = filtered_df[filtered_df['Category'] == filtered_type]
    if search_text != '':
        filtered_df = filtered_df[
            (filtered_df['Category'].str.lower().str.contains(search_text)) |
            (filtered_df['Title'].str.lower().str.contains(search_text)) |
            (filtered_df['Link'].str.lower().str.contains(search_text)) |
            (filtered_df['Description'].str.lower().str.contains(search_text)) |
            (filtered_df['Price'].str.lower().str.contains(search_text)) |
            (filtered_df['Delivery'].str.lower().str.contains(search_text)) |
            (filtered_df['In Stock'].str.lower().str.contains(search_text))
            # (search_text in filtered_df['Date'].str.lower()) |
            # (search_text in filtered_df['Experience Required'].str.lower())
            ]
    print_df(filtered_df)


def print_df(data):
    headers = ['Category', 'Title', 'Link', 'Description', 'Price', 'Delivery', 'In Stock']
    df_rows = data.to_numpy().tolist()
    count_label = tk.Label(scrollable_frame,
                           text='Showing ' + str(len(df_rows)) + ' of ' + str(total_entries) + ' Furniture Listings')
    count_label.pack(anchor='w')
    elements.append(count_label)
    count = 1
    for row in df_rows:
        text = tk.Text(scrollable_frame, wrap=tk.WORD, width=200, height=25, font=('Times New Roman', 14))
        hyperlink = HyperlinkManager(text)
        text.insert(tk.INSERT, "Furniture " + str(count) + "\n\n")
        idx = 0
        for item in row:
            if not isinstance(item, float):
                if idx == 2:
                    text.insert(tk.INSERT, headers[idx] + ':\n')
                    text.insert(tk.INSERT, item, hyperlink.add(partial(webbrowser.open, item)))
                else:
                    text.insert(tk.INSERT, headers[idx] + ':\n' + str(item))
                text.insert(tk.INSERT, '\n\n')
            idx += 1
        text.pack()
        elements.append(text)
        count += 1

def run():
    global elements
    global clicked
    global search_box
    global df
    global scrollable_frame
    global total_entries
    root = tk.Tk()
    root.geometry("1500x1500")
    df = pd.read_excel('data/Furniture/furniture.xlsx')
    total_entries = df.shape[0]
    container = ttk.Frame(root)
    canvas = tk.Canvas(container)
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

    type_set = list(set(df['Category']))
    type_set = [item for item in type_set if isinstance(item, str)]
    type_set.insert(0, 'All Types')
    clicked = tk.StringVar()
    clicked.set("All Types")
    tk.Label(scrollable_frame, text='Filters\n', font=("Arial Bold", 30)).pack(anchor='w')
    tk.Label(scrollable_frame, text='Furniture Type Filter').pack(anchor='w')
    tk.OptionMenu(scrollable_frame, clicked, *type_set).pack(anchor='w')
    tk.Label(scrollable_frame, text='Search Filter').pack(anchor='w')
    search_box = tk.Entry(scrollable_frame)
    search_box.pack(anchor='w')
    tk.Button(scrollable_frame, text="Apply Filters", command=apply).pack(anchor='w')
    tk.Label(scrollable_frame, text='\nFurniture Listings\n', font=("Arial Bold", 30)).pack(anchor='w')

    elements = []
    print_df(df)

    container.pack(fill='both', expand=1)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_y.pack(side="right", fill="y")

    root.mainloop()
