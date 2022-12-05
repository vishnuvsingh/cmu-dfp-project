import tkinter as tk
from tkinter import ttk
import pandas as pd
import webbrowser
from functools import partial
from tkHyperlinkManager import HyperlinkManager
import re
from tkinter.ttk import Scale

def clear():
    for T in elements:
        T.destroy()
    elements.clear()

def apply():
    clear()
    filtered_type = clicked.get()
    search_text = search_box.get().strip().lower()
    max_num =s1.get()
    
    filtered_df = df
    filtered_df = filtered_df[filtered_df['price1']<=max_num]
    if filtered_type == 'All Types' and search_text == '':
        print_df(filtered_df)
        return
    if filtered_type != 'All Types':
        filtered_df = filtered_df[filtered_df['bed'] == filtered_type]
    if search_text != '':
        filtered_df = filtered_df[
            (filtered_df['address'].str.lower().str.contains(search_text)) |
            (filtered_df['price'].str.lower().str.contains(search_text)) |
            (filtered_df['bed'].str.lower().str.contains(search_text)) |
            (filtered_df['baths'].str.lower().str.contains(search_text)) |
            (filtered_df['policy'].str.lower().str.contains(search_text))|
            (filtered_df['distance'].str.lower().str.contains(search_text))|
            (filtered_df['drivingtime'].str.lower().str.contains(search_text))
            # (search_text in filtered_df['Date'].str.lower()) |
            # (search_text in filtered_df['Experience Required'].str.lower())
            ]
    
    print_df(filtered_df)


def print_df(data):
    headers = ['House address', 'Link', 'Picture', 'Price', 'Bed Numbers', 'Bath Number', 'sqFt','Other Policy','distance to CMU Campus','driving time to CMU Campus']
    df_rows = data.to_numpy().tolist()
    count_label = tk.Label(scrollable_frame,
                           text='Showing ' + str(len(df_rows)) + ' of ' + str(total_entries) + ' House Listings')
    count_label.pack(anchor='w')
    elements.append(count_label)
    count = 1
    for row in df_rows:
        text = tk.Text(scrollable_frame, wrap=tk.WORD, width=200, height=25, font=('Times New Roman', 14))
        hyperlink = HyperlinkManager(text)
        text.insert(tk.INSERT, "House " + str(count) + "\n\n")
        idx = 0
        for item in row[1:]:
            if not isinstance(item, float):
                item=str(item)
                if idx == 1 or idx ==2:
                    text.insert(tk.INSERT, headers[idx] + ':\n')
                    text.insert(tk.INSERT, item, hyperlink.add(partial(webbrowser.open, item)))
                else:
                    text.insert(tk.INSERT, headers[idx] + ':\n' + item)
                text.insert(tk.INSERT, '\n\n')
            idx += 1
        text.pack()
        elements.append(text)
        count += 1


def run_shadyside():
    housing('shadyside')


def run_squirrel_south():
    housing('south_squirrel')


def run_squirrel_north():
    housing('north_squirrel')


def run_oakland():
    housing('oakland')


def housing(csv_name):
    root = tk.Tk()
    root.geometry("1500x1500")
    global df
    df = pd.read_csv('data/House/' + csv_name+'_final_housing.csv')
    global total_entries
    total_entries = df.shape[0]
    container = ttk.Frame(root)
    canvas = tk.Canvas(container)
    scrollbar_y = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    global scrollable_frame
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_y.set)
    
    type_set = list(set(df['bed']))
    type_set = [item for item in type_set if isinstance(item, str)]
    type_set.insert(0, 'All Types')
    global clicked
    clicked = tk.StringVar()
    clicked.set("All Types")
    tk.Label(scrollable_frame, text='Filters\n', font=("Arial Bold", 30)).pack(anchor='w')
    tk.Label(scrollable_frame, text='Bed Number Filter').pack(anchor='w')
    tk.OptionMenu(scrollable_frame, clicked, *type_set).pack(anchor='w')
    # tk.Button(scrollable_frame, text="Apply Type Filter", command=filter_type).pack(anchor='w')
    tk.Label(scrollable_frame, text='Search Filter').pack(anchor='w')
    global search_box
    search_box = tk.Entry(scrollable_frame)
    search_box.pack(anchor='w')
    pat = '[0-9],?[0-9]*'
    list_price = []
    for i in range(len(df)):
        out = re.findall(pat,df['price'][i])
        try:
            float_price = float(out[0].replace(',',''))
        except:
            float_price= 0
        list_price.append(float_price)
    df['price1'] = list_price
    tk.Label(scrollable_frame, text='Select the max price').pack(anchor='w')
    global s1
    s1 = tk.Scale(scrollable_frame, from_=min(df['price1']), to_=max(df['price1']), length=400,orient='horizontal')
    s1.pack(anchor='w')
    # tk.Button(scrollable_frame, text="Search", command=search).pack(anchor='w')
    tk.Button(scrollable_frame, text="Apply Filters", command=apply).pack(anchor='w')
    tk.Label(scrollable_frame, text='\nHouse Listings\n', font=("Arial Bold", 30)).pack(anchor='w')
    max_num =s1.get()
    
    
    global elements
    elements = []
    print_df(df)
    
    container.pack(fill='both', expand=1)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_y.pack(side="right", fill="y")
    
    root.mainloop()
