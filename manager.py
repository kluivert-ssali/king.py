from tkinter import *

def populate_list():
    print("Populate")

def add_item():
    print("Add")

def remove_item():
    print("Remove")

def update_item():
    print("Update")

def clear_text():
    print("Clear")

#create awindow object
app = Tk()

#part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

#retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer Name', font=('bold', 14))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

#price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)
# parts list (list box)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(rows=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#create scrollbar
Scrollbar = Scrollbar(app)
Scrollbar.grid(row=3, column=3)
#set the scrollbar to listbox
#parts_list.config(yscrollcomand=Scrollbar.set)
#Scrollbar.config(command=parts_list.yview)

#Buttons
add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
add_btn.grid(row=2, column=3)


app.title('kingslayer')
app.geometry('700x350')

# populate data
populate_list()

# start program
app.mainloop()
