# coding=utf8
import tkinter as tk					
from tkinter import ttk,messagebox
import os, sys
#ชื่อไฟล์ ฐานข้อมูล
from mongodb_quiz1 import insert_doc,find_all_people,delete_doc_by_id,replace_one
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date

plt.rcParams['font.family']='Tahoma'
plt.rcParams['font.size']=13


def graph(_data):
  
    print(_data)
    lists1 = []
    lists2 = []
    lists3 = []

    for x in _data:
        tmp = list(x.values())
        print(tmp)
        lists1.append(tmp[3])
        lists2.append(tmp[4])
        lists3.append(tmp[2])
    
    print(lists1,lists2)
    #exit()
   
    data1 = { 'Amount': lists1,
               'Price': lists2,
               'Order': lists3
         }
    df1 = pd.DataFrame(data1)

    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['Order', 'Price', 'Amount']].groupby('Amount').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Order List')
    root.mainloop()

def delete(_id):
    selected_item = _id.selection()[0]
    print(_id.item(selected_item)['values'][4])
    delete_doc_by_id(_id.item(selected_item)['values'][4])
    messagebox.showinfo("รายการสินค้าถูกลบ เรียบร้อยแล้ว")
    root.config()

def update(_id):
    selected_item = _id.selection()[0]  
    updatepage(_id.item(selected_item)['values'][0],_id.item(selected_item)['values'][1],_id.item(selected_item)['values'][2],_id.item(selected_item)['values'][3],_id.item(selected_item)['values'][4])

  
def clearToTextInput():
    tk.Entry.delete("1.0","end")

def fTabSwitched(event):
        global tabControl
        l_tabText = tabControl.tab(tabControl.select(), "text")
        if (l_tabText == 'Order List'):
            label = tk.Label(tab2, text="รายการสินค้าในสต๊อกทั้งหมด", font=("Kanit",20)).grid(row=0, columnspan=2)
            # create Treeview with 3 columns
            cols = ('รายการสินค้า','จำนวน','ราคาสินค้า','ราคารวมสินค้า')
            listBox = ttk.Treeview(tab2, columns=cols, show='headings')
            # set column headings
            for col in cols:
                listBox.heading(col, text=col)    
            listBox.grid(row=1, column=0, columnspan=2)

            tempList = find_all_people()
            for x in tempList:
                tmp = list(x.values())
                listBox.insert("", "end", values=(tmp[1],tmp[2],tmp[3],tmp[4],tmp[0]))
                  
            b2 = tk.Button(tab2, text='แก้ไขสินค้า',command=lambda: update(listBox)).grid(row=4, column=0,sticky="news", padx=5, pady=5)
            b1 = tk.Button(tab2, text='ลบสินค้า',command=lambda: delete(listBox)).grid(row=4, column=1,sticky="news", padx=5, pady=5)
            b3 = tk.Button(tab2, text="แสดงกราฟ", command=lambda: graph(tempList)).grid(row=5, columnspan=2,sticky="news", padx=5, pady=5)
            closeButton = tk.Button(tab2, text="ปิดหน้าต่าง", command=exit).grid(row=6, columnspan=2,sticky="news", padx=5, pady=5)
        
        
def find_bmi():
    orderlist = orderlist_entry.get()
    #weight = weight_entry.get()
    amount = height_entry.get()
    price =  price_entry.get()
    h = height_entry.get()
    # check height and weight filled in
    if amount and price and h:
        #amount = float(amount)
        total = round(float(price) * float(amount))
        print(f"h : {amount}\nw : {price}\nbmi : {total}\ncomputer name : {os.environ['COMPUTERNAME']}")
        if total != 0:
            #color_zone = "green"
            texts1 = "บันทึกสินค้าเข้าสต็อกเรียบร้อยแล้ว"
            texts2 = "สามารถตรวจสอบรายการได้ที่เมนู Order List"
            
        else:
            #color_zone = "yellow"
            texts1 = "บันทึกสินค้า ไม่ถูกต้อง"
            texts2 = "ทำการบันทึกข้อมูลใหม่ให้ครบทุกช่อง"

        show_data.config(text = f"\nชื่อสินค้า : {orderlist}\nจำนวนสินค้า : {amount}\nราคารวมสินค้า : {total} บาท\n\n{texts1}\n{texts2}\n")
        insert_doc(orderlist,amount,price,total)

    else:
        tk.messagebox.showwarning(title="Error", message="Weight and Height are required.")
        show_data.config(text='')
        show_desc.config(text='')

def update_order(_id):
    orderlist2 = orderlist_entry2.get()
    amount2 = height_entry2.get()
    price2 =  price_entry2.get()
    h2 = height_entry2.get()
    # check height and weight filled in
    if amount2 and price2 and h2:
        total2 = round(float(price2) * float(amount2))
        print(f"h : {amount2}\nw : {price2}\nbmi : {total2}\ncomputer name : {os.environ['COMPUTERNAME']}")
        if total2 != 0:
            #color_zone = "green"
            texts12 = "บันทึกสินค้าเข้าสต็อกเรียบร้อยแล้ว"
            texts22 = "สามารถตรวจสอบรายการได้ที่เมนู Order List"
            
        else:
            #color_zone = "yellow"
            texts12 = "บันทึกสินค้า ไม่ถูกต้อง"
            texts22 = "ทำการบันทึกข้อมูลใหม่ให้ครบทุกช่อง"

        show_data.config(text = f"\nชื่อสินค้า : {orderlist2}\nจำนวนสินค้า : {amount2}\nราคารวมสินค้า : {total2} บาท\n\n{texts12}\n{texts22}\n")
        replace_one(_id,orderlist2,amount2,price2,total2)
       
    else:
        pages.destroy
        tk.messagebox.showwarning(title="Error", message="จำนวนสินค้า จำนวน ราคา ไม่ถูกต้อง !!!")
        show_data2.config(text='')
        show_desc2.config(text='')

def updatepage(a,b,c,d,e):
    print(a,b,c,d,e)
    global pages
    global orderlist_entry2
    global height_entry2
    global price_entry2
    global show_data2
    global show_desc2
    pages = tk.Tk()
    pages.title("แก้ไขรายการสินค้าในสต๊อก:")

    info_frame = ttk.LabelFrame(pages, text="รายการสินค้า")
    info_frame.grid(row= 0, column=0, padx=35, pady=30)

    orderlist_label = ttk.Label(info_frame, text=f"ชื่อสินค้า : =>  {a} ")
    orderlist_label.grid(row=1, column=0)

    height_label = ttk.Label(info_frame, text=f"จำนวน : =>  {b} ")
    height_label.grid(row=2, column=0)

    price_label = ttk.Label(info_frame, text=f"ราคาขาย(หน่วย) : =>  {c} ")
    price_label.grid(row=3, column=0)

    orderlist_entry2 = ttk.Entry(info_frame)
    orderlist_entry2.grid(row=1, column=1)

    height_entry2 = ttk.Entry(info_frame)
    height_entry2.grid(row=2, column=1)

    price_entry2 = ttk.Entry(info_frame)
    price_entry2.grid(row=3, column=1)

    for widget in info_frame.winfo_children():
        widget.grid_configure(padx=100, pady=15)

    # Button
    button = ttk.Button(info_frame, text="บันทึกสินค้าแก้ไข", command=lambda:update_order(e))
    button.grid(row=4, column=0, sticky="news", padx=5, pady=5)

    button = ttk.Button(info_frame, text="ปิดหน้าต่าง",command=pages.destroy)
    button.grid(row=4, column=1, sticky="news", padx=5, pady=5)

    show_data2 = ttk.Label(pages, text="",background="")
    show_data2.grid(rowspan=3,columnspan=2)
    show_desc2 = ttk.Label(pages, text="")
    show_desc2.grid(rowspan=8,columnspan=2)

    pages.mainloop()


def mainpage():
    global root
    global tabControl
    global tab1
    global tab2
    global tab3
    global orderlist_entry
    global height_entry
    #global weight_entry
    global price_entry
    global show_data
    global show_desc
    root = tk.Tk()
    root.title("หจก. ขนิษฐาพาณิชย์ :")

    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    # Create an instance of ttk style
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="snow3")
    s.map("TNotebook", background= [("selected", "snow3")])

    tabControl.add(tab1, text ='Order New')
    tabControl.add(tab2, text ='Order List')
    tabControl.bind("<ButtonRelease-1>",fTabSwitched)
    tabControl.pack(expand = 1, fill ="both")

    info_frame = ttk.LabelFrame(tab1, text="รายการสินค้า")
    info_frame.grid(row= 0, column=0, padx=35, pady=30)

    orderlist_label = ttk.Label(info_frame, text="ชื่อสินค้า : ")
    orderlist_label.grid(row=1, column=0)

    # weight_label = ttk.Label(info_frame, text="ชื่อสินค้า : ")
    # weight_label.grid(row=1, column=0)

    height_label = ttk.Label(info_frame, text="จำนวน : ")
    height_label.grid(row=2, column=0)

    price_label = ttk.Label(info_frame, text="ราคาขาย(หน่วย) : ")
    price_label.grid(row=3, column=0)

    # weight_entry = ttk.Entry(info_frame)
    # weight_entry.grid(row=1, column=1)

    orderlist_entry = ttk.Entry(info_frame)
    orderlist_entry.grid(row=1, column=1)
    
    height_entry = ttk.Entry(info_frame)
    height_entry.grid(row=2, column=1)

    price_entry = ttk.Entry(info_frame)
    price_entry.grid(row=3, column=1)

    for widget in info_frame.winfo_children():
        widget.grid_configure(padx=100, pady=15)

    # Button
    button = ttk.Button(info_frame, text="บันทึกรายการสินค้าใหม่", command=find_bmi)
    button.grid(row=4, columnspan=2, sticky="news", padx=5, pady=5)

    # button = ttk.Button(info_frame, text="Clear", command=clearToTextInput)
    # button.grid(row=3, column=1, sticky="news", padx=5, pady=5)

    button = ttk.Button(info_frame, text="ปิดหน้าต่าง", command=root.destroy)
    button.grid(row=5, columnspan=2, sticky="news", padx=5, pady=5)

    show_data = ttk.Label(tab1, text="",background="")
    show_data.grid(rowspan=3,columnspan=2)
    show_desc = ttk.Label(tab1, text="")
    show_desc.grid(rowspan=8,columnspan=2)

    root.mainloop()

mainpage()