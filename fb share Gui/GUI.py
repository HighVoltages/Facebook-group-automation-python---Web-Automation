from tkinter import *
import tkinter as tk
import webbrowser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import clipboard

content = ["","",""]
Group_list = [""]

def website(event):
    webbrowser.open_new_tab('https://www.youtube.com/channel/UCzOAiIISvLxNVdlf2suEZFw?sub_confirmation=1&fbclid=IwAR1UfbIyBZUz8o5qHvbvB-AJcMdCerDbhK1d9h2KBD7U1oeLXsf_3VUj1Iw')

def end_site(event):
    webbrowser.open_new_tab('https://www.highvoltages.co/contact-us')

def start():
    global email, Password, content, listname, t,variable
    usr = email.get()
    pwd = Password.get()
    message = msg.get()
    group_name = variable.get()

    with open("./Group_List/"+group_name+".dat") as f:
        content = f.read()
        grouplinks = content.split(",")


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("--headless")

    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
    })

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(15)  # seconds

    # Go to facebook.com
    driver.get("http://www.facebook.com")

    # Enter user email
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    # Enter user password
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    # Login
    elem.send_keys(Keys.RETURN)

    sleep(10)

    for group in grouplinks:

        # Go to the Facebook Group
        driver.get(group)

        # Click the post box
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

        # Enter the text we want to post to Facebook
        clipboard.copy(message)


        post_box.send_keys(Keys.CONTROL, 'V')

        sleep(10)
        buttons = driver.find_elements_by_tag_name("button")
        sleep(5)
        for button in buttons:
            if button.text == "Post":
                sleep(10)
                button.click()
                sleep(10)

def saveCredentials():
    global email,Password
    file = open('credentials.dat', 'w+')
    name = email.get()
    pas = Password.get()
    file.write(name+"\n"+pas)
    file.close()


def newGroup():
    global listname,t,win
    groups = t.get("1.0",tk.END)
    n = listname.get()
    file = open("./Group_List/"+n+".dat", 'w+')
    t.delete("1.0",tk.END)
    listname.delete("0",tk.END)
    file.write(groups)
    global opt,variable,win
    Group_list = [""]
    for file in os.listdir("./Group_List"):
        if file.endswith(".dat"):
            Group_list.append(file.replace(".dat",""))
    print(Group_list)
    opt['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)

    for choice in Group_list:
        opt['menu'].add_command(label=choice, command=tk._setit(variable, choice))






def main():
    global email, Password, content, listname, t, msg,variable,win,opt
    try:
        for file in os.listdir("./Group_List"):
            if file.endswith(".dat"):
                Group_list.append(file.replace(".dat",""))
        print(Group_list)
    except:
        os.mkdir("./Group_List/")


    try:
        with open("./credentials.dat") as f:
            content = f.readlines()

    except:
        pass
    win = Tk()
    win.iconbitmap('favicon.ico')
    win.title("FB EASY GROUP SHARING")
    win.resizable(False,False)
    win.geometry('570x530')
    win.config(bg="white")
    img = PhotoImage(file="./logo.png")
    logo = Label(win,image=img,bd="0")
    logo.bind('<Button-1>', website)
    logo.pack()

    Label(win,text="Facebook Email ",fg="#54b4e7",bg="white",font=("arial",15,"bold")).place(x=40,y=180)
    Label(win,text="Password ",fg="#54b4e7",bg="white",font=("arial",15,"bold")).place(x=40,y=220)
    email = Entry(win,font=("arial",15,"bold"),borderwidth=2)
    email.place(x=220,y=180)
    email.insert(0,content[0].strip())
    Password = Entry(win, font=("arial", 15, "bold"), borderwidth=2,show="*")
    Password.place(x=220, y=220)
    Password.insert(0,content[1])
    Label(win, text="Message ", fg="#54b4e7", bg="white", font=("arial", 15, "bold")).place(x=40, y=260)
    msg = Entry(win,font=("arial",15,"bold"),borderwidth=2)
    msg.place(x=220,y=260)

    Label(win, text="Select Group ", fg="#54b4e7", bg="white", font=("arial", 15, "bold")).place(x=40, y=300)
    variable = StringVar(win)
    variable.set(Group_list[0])  # default value
    opt = OptionMenu(win,variable, *Group_list)
    opt.place(x=220,y=300)

    Label(win, text="Add New List", fg="black", bg="white", font=("arial", 15, "bold")).place(x=40, y=340)
    Label(win,text="File Name",fg="#54b4e7",bg="white",font=("arial",15,"bold")).place(x=40, y=380)

    group_links = Label(win,text="Group List",fg="#54b4e7",bg="white",font=("arial",15,"bold")).place(x=40,y=420)

    listname = Entry(win,font=("arial",15,"bold"),borderwidth=2)
    listname.place(x=220,y=380)
    t = tk.Text(win,font=("arial",10,"bold"),borderwidth=2)
    t.insert(tk.INSERT,"*put group links in comma seperated format")
    t.config(width=31, height=4)

    t.place(x=220,y=420)

    # combo = TextScrollCombo(win)
    # combo.place(x=20,y=500)
    # combo.config(width=530, height=80)
    # combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
    # combo.txt.config(borderwidth=3, relief="sunken")
    # style = ttk.Style()
    # style.theme_use('clam')

    Button(win, text="Save Credentials", fg="#fa6620", bg="white", font=("arial", 12, "bold"),command=saveCredentials).place(x=350, y=300)
    Button(win, text="Start", fg="#fa6620", bg="white", font=("arial", 12, "bold"),command=start).place(x=500, y=300)
    Button(win, text="Save", fg="#fa6620", bg="white", font=("arial", 12, "bold"),command=newGroup).place(x=500, y=450)
    end = Label(win, text="                                                    For More Contact us                                                   ", fg="white", bg="#1f2024", font=("arial", 12, "bold"))
    end.bind('<Button-1>',end_site)
    end.place(x=0, y=500)

    win.mainloop()


main()