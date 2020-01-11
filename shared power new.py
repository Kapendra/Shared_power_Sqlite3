#import Database_back
import sqlite3
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
from tkinter import Frame
import tkinter.messagebox
from tkinter import ttk
import time
import json
from datetime import date
import os
import calendar
import hashlib
from PIL import Image, ImageTk
from tkinter import Tk, filedialog



'''
            
This is Homepage screen Class which will initialize the software and redirects you to Register Page

'''
class SplashScreenFrame(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, padx=2, pady=2)



        self.button = Button(master,text="Click Here To Rent Tools", font=("bold", 10),bg= 'Blue', relief="groove", activebackground="green",command=self.command1).place(x=255, y=310)

       


        #self.label_6 = Label(master, text="Shared Power Rental Service software", width=60,font=('Helvetica', 9), cursor="hand2")
        #self.label_6.place(x=90, y=340)

        #self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        title = Label(root, text="Shared Power :Tools Rental Service", width=30, font=("bold", 22))
        title.place(x=97, y=35)

       # self.img2 = PhotoImage(file="Images\yup1.png")
        #self.lab2 = Label(master, image=self.img2)
        #self.lab2.place(x=10, y=5)

        self.img1 = PhotoImage(file="Images\Background3.png")

        self.lab1 = Label(master, image=self.img1)
        self.lab1.place(x=145, y=75)

    def open_terms(self):
        os.startfile("Terms.txt")



    def command1(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position

                root.state('withdrawn')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = RegistrationFrame(self.newWindow)
                self.newWindow.geometry('550x570+450+110')

                self.newWindow.title("Shared Power Registeration Form")

    def run(self):
        self.progress_bar.start()
        #self.progress_bar['maximum'] = 100






'''

This is LoginFrame Class which will login user into their respective UserPanels .Registered User Can enter their 
credentials inorder to start their session in our software. 

'''

class LoginFrame():
    def __init__(self, master):

        global entry_username, login_password

        self.master = master
        self.frame = tk.Frame(master)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17), relief="groove", activebackground="blue",
                                 command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_destroy = Button(master, text="X", width=2, font=("bold", 17), relief="groove", activebackground="red",
                                command=endProgram)
        self.button_destroy.place(x=515, y=3)


        self.label_username = Label(master, text="Username", width=20, font=("bold", 13))
        self.label_username.place(x=80, y=130)

        self.entry_username = Entry(master, bd=5)
        self.entry_username.place(x=240, y=130, width=180)

        self.label_password = Label(master, text="    Password", width=20, font=("bold",13))
        self.label_password.place(x=68,y=180)

        self.login_password = Entry(master, bd=5,show="*")
        self.login_password.place(x=240, y=180, width=180)

        # var2 = IntVar()
        # Checkbutton(master, text="Keep me logged in", variable=var2, font=('Times', 13,'underline'),cursor="hand1").place(x=190, y=225 , width=200)

        Button(master, text='Log In', font=("bold", 11), width=20, bg='deep sky blue', fg='white', command=self.login_info).place(
            x=215, y=280)

        #self.img2 = PhotoImage(file="Images\yup1.png")

        #self.lab2 = Label(master, image=self.img2)
        #self.lab2.place(x=20, y=23)

        self.img1 = PhotoImage(file="Images\login2.png")

        self.lab1 = Label(master, image=self.img1)
        self.lab1.place(x=180,y=30)

       # self.label_6 = Label(master, text="Shared Power Rental Service software", width=60, font=('Helvetica', 9), cursor="hand2")
       # self.label_6.place(x=88, y=320)
       # self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        master.resizable(False,False)
        master.overrideredirect(True)



    def open_terms(self):
        os.startfile("Terms.txt")

    

    '''

    This login_info method will save the login info of user and as well as this will check the 
    credentials inorder to start their user session in our software. 

    '''

    def login_info(self):

        self.passw1=self.login_password.get()
        self.Username_Login = self. entry_username.get()
        self.Password_Login = hashlib.sha1(self.login_password.get().encode()).hexdigest()

        db=sqlite3.connect("spower.db")
        c=db.cursor()
        c.execute("Select* FROM userinfo WHERE Fullname = ? and password= ? ",(self.Username_Login,self.Password_Login))
        #result=c.fetchall()
        #return result
        db.commit()
        # db.commit()
        #result

        # find=c.fetchall()
        # db.commit()
        # return


        if  self.Username_Login and self.Password_Login in c.fetchone():
            
            tm.showinfo("Login successful", "Welcome User")
            self.master.withdraw()

            #print('Button is pressed!')
            # self.RegistrationFrame.destroy()
            self.newWindow = tk.Toplevel(self.master)
            self.app = UserPanelFrame(self.newWindow)
            self.newWindow.geometry('720x720+350+15')
            self.newWindow.title("Shared Power Login Form")

        elif self.Username_Login == "Insurance!" and self.passw1 =="INS!@#":
            self.master.withdraw()
            tm.showinfo("Login successful", "Welcome to Insurance Company Profile ")
            #print('Button is pressed!')
            # self.RegistrationFrame.destroy()
            self.newWindow = tk.Toplevel(self.master)
            self.app = InsuranceCompany(self.newWindow)
            self.newWindow.geometry('550x550+450+140')
            self.newWindow.title("Insurance Company Form")

        else:
            tm.showerror("Login error", "Invalid Username Or Password")

    def minimizeProgram(self):
        #self.master.wm_state('iconic')
        self.master.withdraw()



    def _login_btn_clicked(self):


        username = self.entry_username.get()
        password = self.login_password.get()

      

        if username and password =="kapendra" :
            tm.showinfo("Login info", "Welcome User")
            self.master.withdraw()

            #print('Button is pressed!')
            # self.RegistrationFrame.destroy()
            self.newWindow = tk.Toplevel(self.master)
            self.app = UserPanelFrame(self.newWindow)
            self.newWindow.geometry('720x720+350+15')
            self.newWindow.title("Shared Power Login Form")
        else:
            tm.showerror("Login error", "Invalid Credentials")





'''

This is UserPanel Class. After getting loged in with correct credentials the user will be redirected to this 
panel.This user Panel gives the user the function like searching the tool , uploading the tool, hiring the tool
, returning the tool, and generating the invoice by clicking on respective functions.

'''


class UserPanelFrame(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)

        self.title = Label(master, text="  Current Time", font=("bold", 11))
        self.title.place(x=605, y=80)

        self.q = Canvas(master)
        self.q.place(x=600, y=97)

        self.localtime = time.asctime(time.localtime(time.time()))
        self.q.create_text(14, 28, text=self.localtime, font=('arial', 12, 'bold'))

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=661, y=2)

        self.button_destroy = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=endProgram)
        self.button_destroy.place(x=685, y=3)


        #self.label_6 = Label(master, text="Shared Power Rental Service software", width=60, font=('Helvetica', 9),cursor="hand2")
        #self.label_6.place(x=196, y=682)
        #self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)


        self.title = Label(master, text="Welcome !! ", width=30, font=("bold", 22))
        self.title.place(x=110, y=35)

        #self.tool = PhotoImage(file="Images\Tool1.png")

        #self.tool1 = Label(master, image=self.tool)
        #self.tool1.place(x=125, y=90)

        #self.tool1 = PhotoImage(file="Images\Tool1.png")

        #self.tool12 = Label(master, image=self.tool1)
        #self.tool12.place(x=520, y=90)

        #self.img2 = PhotoImage(file="Images\yup1.png")

        #self.lab2 = Label(master, image=self.img2)
        #self.lab2.place(x=10, y=5)

        #self.img3 = PhotoImage(file="Sp1234.png")

        #self.lab1 = Label(master, image=self.img3)
        #self.lab1.place(x=590, y=620)

        master.resizable(False, False)
        master.overrideredirect(True)

        #self.button_cal = Button(master, text="Calendar", font=("bold", 9), relief="groove",
         #                        activebackground="red", command=self.cal1)
        #self.button_cal.place(x=10, y=680)

        self.show_profile = Button(master, text="View Profile", font=("bold", 9), relief="groove",
                                 activebackground="Grey", command=self.profile)
        self.show_profile.place(x=564, y=180)

        self.logout = PhotoImage(file="Images\logout.png")
        self.user_logout = Button(master, image=self.logout, width=55, height=55, relief="flat",
                                   activebackground="Blue", command=self.logOut)
        self.user_logout.place(x=659, y=659)



        self.man = PhotoImage(file="Images\Man.png")

        self.manphoto = Label(master, image=self.man)
        self.manphoto.place(x=10, y=160)


        self.fetch = Label(master, text="Fetch your Desire! ", width=25, font=("bold", 16))
        self.fetch.place(x=203, y=100)
        self.s1 = PhotoImage(file="Images\s1.png")
        self.search_tools = Button(master, text="Search Tools",  width=210, height=160, image=self.s1,
                                   font=('arial', 16, "bold"),  command=self.search,
                                   activebackground="blue")
        self.search_tools.place(x=210, y=215)

        self.search1 = Label(master, text="Search Tools ", font=("arial", 16,"bold"))
        self.search1.place(x=240, y=395)


        self.upload1 = PhotoImage(file="Images\yup1.png")
        self.up = PhotoImage(file="Images\Vis3.png")
        self.up = PhotoImage(file="Images\pload1.png")
        self.upload_tools = Button(master, text="Upload Tools", width=210, height=160, image=self.up,
                                   font=('arial', 7, "bold"), cursor="hand1",command=self.upload,
                                   activebackground="green",
                                   activeforeground="red")
        self.upload_tools.place(x=438, y=215)

        self.upload1 = Label(master, text="Upload Tools ", font=("arial", 16,"bold"))
        self.upload1.place(x=475, y=395)

        self.hire = PhotoImage(file="Images\hire1.png")
        self.hire_tools = Button(master, text="Hire Tools",  width=210, height=160, image=self.hire,font=('arial', 16, "bold"), cursor="hand1",command=self.hire1,activebackground="cyan")
        self.hire_tools.place(x=210, y=445)

        self.hire13 = Label(master, text="Hire Tools ", font=("arial", 16,"bold"))
        self.hire13.place(x=257, y=623)

        self.pay = PhotoImage(file="Images\paynow1.png")
        self.pay_tools = Button(master, text="Payment & Delivery", width=210, height=160, image=self.pay,font=('arial', 16, "bold"), cursor="hand1",command=self.pay1,activebackground="brown",activeforeground="green")
        self.pay_tools.place(x=438, y=445)

        self.pay13 = Label(master, text="Payment & Delivery ", font=("arial", 16,"bold"))
        self.pay13.place(x=446, y=623)

        # self.image_tk = PhotoImage(self.select_image())
        # self.canvas.create_image(0, 0, image=self.image_tk)


    def search(self):

                self.master.withdraw()
                self.newWindow = tk.Toplevel(self.master)
                self.app = SearchTools(self.newWindow)
                self.newWindow.geometry('650x550+450+140')
                self.newWindow.title("Search Tools Form")



    # This will redirect the user to upload tools GUI where after entering some details we can upload tools.
    def upload(self):


                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = uploadTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Upload Tools Form")


    # This will redirect the user to Payment GUI where after entering some details we can generate invoice
    # after returning the tool.

    def pay1(self):

                self.master.withdraw()

                
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = payTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Payment Tools Form")


    # This will redirect the user to hire tools GUI where after entering some details we can sucessfully hire uploaded tools.

    def hire1(self):


                self.master.withdraw()

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = hireTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Hire Tools Form")


    # This will show the user to Calendar which will be easy and convenient to know current time and date.

    def cal1(self):
        pass



               
                # self.RegistrationFrame.destroy()
                # self.newWindow = tk.Toplevel(self.master)
                # self.app = CalendarShow(self.newWindow)
                # self.newWindow.title("Calendar")
                # def select_image(self):

    # This will redirect the user to search tools GUI where user can search the uploaded tools inorder to hire those tools.
    def profile(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = profile(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Search Tools Form")



    # This will preview the instance information of newly registered user
    def show_info(self):
        os.startfile("Text File Handling\ViewUserInfo.txt")



    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")

    # This logOut function will help user to logout him or her from software .
    def logOut(self):
        #print("This will logout you from user panel.")

        tm.showwarning("Confirm LogOut",
                    "Are You sure want to LogOut from Shared Power? ")

        self.master.withdraw()

        #print('Button is pressed!')
        # self.RegistrationFrame.destroy()
        self.newWindow = tk.Toplevel(self.master)
        self.app = LoginFrame(self.newWindow)
        self.newWindow.geometry('550x350+450+220')
        self.newWindow.title("Shared Power Login Form")



def onRegister():
        # json_data = open(file_directory).read()
        tkinter.messagebox.showinfo("Successful!! You are successfully registered!!")


def minimizeProgram():
    #root.wm_state('iconic')
    root.withdraw()
    #root.state("withdrawn")

def endProgram():
    # top.quit()
    tm.showinfo("Confirm Exit",
                   "Are You sure want to exit Shared Power? " )
    root.destroy()




"""THIS A user profile where user can see their own details but cant edit their or update therir details
                                                                                                            """
class profile(Frame):
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(master)



        self.label_1 = Label(master, text="Name", width=20, font=("bold", 13))
        self.label_1.place(x=68, y=130)



        self.label_2 = Label(master, text="Email", width=20, font=("bold", 13))
        self.label_2.place(x=68, y=180)





        self.label_3 = Label(master, text="Gender", width=20, font=("bold", 13))
        self.label_3.place(x=70, y=280)





        self.label_4 = Label(master, text="Country", width=20, font=("bold", 13))
        self.label_4.place(x=70, y=330)





        label_q = Label(master, text="    Phone No", width=20, font=("bold", 13))
        label_q.place(x=70, y=380)




'''

This is RegisterationFrame Class which will help the visitor user to registered into our software inorder to 
use search , hire , upload, return tools and monthly invoice generation. 
 
'''


class RegistrationFrame(Frame):

    def __init__(self, master):





        global entry_fullname, \
            entry_Email, \
            entry_password, \
            entry_phoneno, \
            country, \
            var_P, \
            var_nonP, \
            register_gender, gender_value





        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),
                                      relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_destroy = Button(master, text="X", width=2, font=("bold", 17) ,
                                     relief="groove" , activebackground="red",command=endProgram)
        self.button_destroy.place(x=515, y=3)

        self.label_1 = Label(master, text="FullName",width=20,font=("bold", 13))
        self.label_1.place(x=80,y=130)

        self.fullname=StringVar()
        self.entry_fullname = Entry(master,bd =5, textvariable=self.fullname)
        self.entry_fullname.place(x=240,y=130 ,width=180)


        self.label_2 = Label(master, text="Email",width=20,font=("bold", 13))
        self.label_2.place(x=68,y=180)

        self.entry_Email = Entry(master,bd =5)
        self.entry_Email.place(x=240,y=180,width=180)

        self.label_password = Label(master, text="    Password", width=20, font=("bold", 13))
        self.label_password.place(x=70, y=230)

        self.entry_password = Entry(master, bd=5,show="*")
        self.entry_password.place(x=240, y=230, width=180)

        self.label_3 = Label(master, text="Gender",width=20,font=("bold", 13))
        self.label_3.place(x=70,y=280)

        gender_value = StringVar()
        gender_value.set(' ')

        Radiobutton(master, text="Male", font=("bold", 10), padx=5 , variable=gender_value, value="Male",
                    command=RegistrationFrame.selected_gender).place(x=235, y=280)
        Radiobutton(master, text="Female", variable=gender_value, value="Female",
                    command=RegistrationFrame.selected_gender).place(x=290, y=280)

   

        self.label_4 = Label(master, text="Country",width=20,font=("bold", 13))
        self.label_4.place(x=70,y=330)

        list1 = ['Afghanistan','Algeria','Andorra','Angola','Antigua and Barbuda','Bangladesh', 'Thailand','Canada','India','UK','Nepal','Iceland','South Africa','Uganda','Maldives'];
        country=StringVar()

        country_droplist =OptionMenu(master,country, *list1, command=RegistrationFrame.countey_selected)
        country_droplist.config(width=20)

        country.set('Select your Country')
        country_droplist.place(x=240,y=330)

        label_q = Label(master, text="    Phone No", width=20, font=("bold", 13))
        label_q.place(x=70, y=380)

        self.entry_phoneno = Entry(master, bd=5)
        self.entry_phoneno.place(x=240, y=380, width=180)

        label_4 = Label(master, text="      Applied Account",width=20,font=("bold", 13))
        label_4.place(x=85,y=430)

        var_nonP = IntVar()
        Checkbutton(master, text="Buyer", variable=var_nonP,command=RegistrationFrame.selected_account).place(x=265,y=430)

        var_P = IntVar()
        Checkbutton(master, text="Seller", variable=var_P, command=RegistrationFrame.selected_account).place(x=375,y=430)


        self.registerButton=Button(master, text='Register',font=("bold", 11),width=20,bg='cyan2',fg='white' ,command =self.save_info).place(x=208,y=462)


        self.label_5 = Button(master, text="Already Have A Account ", width=65, font=('Times', 12,'underline'),activebackground="blue",command=self.command)
        self.label_5.place(x=0, y=500)



        #self.label_6 = Label(master, text="Shared Power Rental Service software", width=60, font=('Helvetica', 9), cursor="hand2")
        #self.label_6.place(x=80, y=542)
        #self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)


        #self.img2 = PhotoImage(file="Images\yup1.png")

        #self.lab2 = Label(master, image=self.img2)
        #self.lab2.place(x=20, y=23)

        self.img1 = PhotoImage(file="Images\Regfinal1.png")

        self.lab1 = Label(master, image=self.img1)
        self.lab1.place(x=160,y=35)

        master.resizable(False, False)
        master.overrideredirect(True)

    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")

    @staticmethod
    def selected_gender(event=None):
        global gender_selected
        gender_selected = gender_value.get()
        #print(gender_selected)

    @staticmethod
    def countey_selected(event=None):
        global country_selected, name
        country_selected = country.get()
        #print(country_selected)

    @staticmethod
    def selected_account(event=None):
        global account_selected2 , account_selected1
        account_selected1 = var_nonP.get()
        account_selected2 = var_P.get()
        account_selected1=str(account_selected1)
        account_selected2= str(account_selected2)

        #print(account_selected2)
        #print(account_selected1)


    def command(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = LoginFrame(self.newWindow)
                self.newWindow.geometry('550x350+450+220')
                self.newWindow.title("Shared Power Login Form")



            #File handling by normal text format


    def valid(self):
        self.username = self.entry_fullname.get()
        self.password = self.entry_password.get()

        if len(self.username) == 0 and len(self.password)==0:
            tm.showerror("Registration Error",
                         "Registration is unsucessful. Can be validation error or may be one or more field is empty.Please Register again with required Validation")
        else:
            print("Its ok Fine")


    def save_info(self):

       
       self.name = self.entry_fullname.get()
       self.passw = self.entry_password.get()
       self.Username = self.entry_Email.get()
       self.Password = hashlib.sha1(self.entry_password.get().encode()).hexdigest()
       self.pno = self.entry_phoneno.get()
       self.account_selected1 = var_nonP.get()
       self.account_selected2 = var_P.get()
       self.account_selected1 = str(self.account_selected1)
       self.account_selected2 = str(self.account_selected2)
       self.gender_selected = gender_value.get()
       self.country_selected = country.get()

       self.Date = date.today()




     
       
       
       if (len(self.name) == 0 and len(self.passw) == 0) and (len(self.passw) != 8):
           tm.showerror("Registration Error",
                        "Registration is unsucessful. Can be validation error or may be one or more field is empty.Please Register again with required Validation")


       else:
           self.name = self.entry_fullname.get()
           self.passw = self.entry_password.get()
           self.Username = self.entry_Email.get()
           self.Password = hashlib.sha1(self.entry_password.get().encode()).hexdigest()
           self.pno = self.entry_phoneno.get()
           self.account_selected1 = var_nonP.get()
           self.account_selected2 = var_P.get()
           self.account_selected1 = str(self.account_selected1)
           # self.account_selected2 = str(self.account_selected2)
           self.gender_selected = gender_value.get()
           self.country_selected = country.get()
           self.Date = date.today()

           db = sqlite3.connect("spower.db")
           c = db.cursor()
           c.execute("CREATE TABLE IF NOT EXISTS userinfo (Fullname TEXT UNIQUE NOT NULL,"
                     "Email TEXT,password VARCHAR(20),gender INTEGER(2),"
                     "Country TEXT,phoneno INTEGER(10),AccountType TEXT,Date DATE)")
           db.commit()
           c.execute("INSERT INTO userinfo VALUES (?,?,?,?,?,?,?,?)",( self.name, self.Username, self.Password,
                      self.gender_selected, self.country_selected, self.pno, self.account_selected1,self.Date))
           db.commit()

           tm.showinfo("Successful!!",
                       " You are successfully registered!! Now yo will be redirected to LoginPage")

           self.master.withdraw()

           self.newWindow = tk.Toplevel(self.master)
           self.app = LoginFrame(self.newWindow)
           self.newWindow.geometry('550x350+450+220')
           self.newWindow.title("Shared Power Login Form")















'''

This is Upload Image class which give the user the function of to upload the desired image of respective tools
while uploading the tools details.  

'''


class UploadImage(Frame):
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        self.master.resizable(False, False)

    def create_widgets(self):

        self.select = Button(self.master,text='Select Image', font=("arial", 13, "bold"), bg="green", fg='white',command=self.select_image)
        self.select.pack()
        self.canvas = Canvas(self.master, width= 400, height=400, bg="grey")
        self.canvas.pack()

        self.store = Button(self.master, text='Store Image', font=("arial", 13, "bold"), bg="#e37b17", fg='white',
                            command=self.store_image)
        self.store.pack()


    def select_image(self):
        global file_path

        file_path = filedialog.askopenfilename()
        des = Image.open(file_path)
        bg_image = ImageTk.PhotoImage(des)
        self.canvas.bg_image = bg_image
        self.canvas.create_image(200 , 200, image=self.canvas.bg_image)
        print(file_path)

    def store_image(self):



        #print("The selected tool image has been uploaded to our database.")

        self.store = file_path

      

        tm.showinfo("Successfully Uploaded ToolImage!", "Your selected image is uploaded in ToolImage Database. !! Keep Exploring Shared power")
        self.master.withdraw()

        # print('Button is pressed!')
        # self.RegistrationFrame.destroy()
        self.newWindow = tk.Toplevel(self.master)
        self.app = SearchTools(self.newWindow)
        self.newWindow.geometry('650x550+450+140')
        self.newWindow.title("Upload Tools Form")




'''

This is upload Tools class which enables the function of uploading Tool Details into our database which is carried out by
registered user so that the other registered user can hire the tools .

'''

class uploadTools(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=self.back)
        self.button_back.place(x=515, y=3)

        self.label_name = Label(master, text="Tool Name",width=20,font=("arial", 17))
        self.label_name.place(x=30,y=165)

        self.entry_toolname = Entry(master,bd =5,font=("arial", 13))
        self.entry_toolname.place(x=280,y=165 ,width=200, height=38)

        self.label_tooldes = Label(master, text="Description",width=20,font=("arial", 17))
        self.label_tooldes.place(x=30,y=235)

        self.entry_tooldes = Entry(master,bd =5, font=("arial", 13))
        self.entry_tooldes.place(x=280,y=235,width=200, height=38)

        self.label_toolcondition = Label(master, text="Condition", width=20, font=("arial", 17))
        self.label_toolcondition.place(x=23, y=305)

        self.entry_toolcondition = Entry(master, bd=5, font=("arial", 13))
        self.entry_toolcondition.place(x=280, y=305, width=200, height=38)

        self.label_rate = Label(master, text="Tool Rate",width=20,font=("arial", 17))
        self.label_rate.place(x=30,y=375)
        self.entry_toolrate = Entry(master, bd=5, font=("arial", 13))
        self.entry_toolrate.place(x=280, y=375, width=90, height=38)

        self.label_fullrate = Label(master, text="Full Day",width=20,font=("arial", 10))
        self.label_fullrate.place(x=243,y=418)

        self.entry_toolrate2 = Entry(master, bd=5, font=("arial", 13))
        self.entry_toolrate2.place(x=390, y=375, width=90, height=38)

        self.label_halfrate = Label(master, text="Half Day",width=20,font=("arial", 10))
        self.label_halfrate.place(x=353,y=418)

        Button(master, text='Upload Tools',font=("arial", 13,"bold"),width=15,bg='#e37b17',fg='white', command=self.upload_info).place(x=298,y=464)

        Button(master, text='Upload Image', font=("arial", 13, "bold"), bg="green", fg='white',
               command=self.upload_image1).place(x=58, y=464)

       # self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9), cursor="hand2")
        #self.label_6.place(x=80, y=512)
        #self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        #self.img2 = PhotoImage(file="Images\yup1.png")

        #self.lab2 = Label(master, image=self.img2)
        #self.lab2.place(x=20, y=23)

        self.upload12 = PhotoImage(file="Images\pload12.png")

        self.ph = Label(master, image=self.upload12)
        self.ph.place(x=160,y=35)

        master.resizable(False, False)
        master.overrideredirect(True)

    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def upload_image(self):
        print("Lets begin to upload")


    def upload_image1(self):
                tm.showwarning("Before Uploading TooolImage!",
                       "You should upload details of tool first then you need to upload Tool Image.\n If you have uploaded ToolDetails then Click OK  to continue")

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                # self.master = master

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UploadImage(self.newWindow)
                self.newWindow.title("Upload Tools Form")
                # def select_image(self):
                # file_path = filedialog.askopenfilename()
                # return Image.open(file_path)

    def back(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UserPanelFrame(self.newWindow)
                self.newWindow.geometry('720x720+350+15')
                self.newWindow.title("Shared Power Login Form")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")


    def upload_info(self):
       # global gender_selected

        #global country_selected
        #global account_selected2, account_selected1
        #global name, Username, Password,CNo

       self.nameTool = self.entry_toolname.get()

       self.ToolDescription = self.entry_tooldes.get()

       self.Toolcondition = self.entry_toolcondition.get()

       self.FullRate = self.entry_toolrate2.get()

       self.HalfRate = self.entry_toolrate.get()

       self.nameTool = self.entry_toolname.get()

       self.list1 = [self.nameTool, self.ToolDescription, self.Toolcondition, self.FullRate, self.HalfRate]
       #print(self.list1)

       self.Dict = {'Name of Tool:': self.nameTool, 'Tool Description:': self.ToolDescription, 'Tool Condition:':self.Toolcondition,'FullDayRate':self.FullRate,'HalfDayRate':self.HalfRate }

       if len(self.nameTool) == 0 and len(self.ToolDescription) == 0 and len(self.Toolcondition) == 0 :
           tm.showerror("Upload Tool Error",
                        "UploadTool is unsucessful. May be one or more field is empty.")
       else:

            self.ToolDescription = self.entry_tooldes.get()

            self.Toolcondition = self.entry_toolcondition.get()

            self.FullRate = self.entry_toolrate2.get()

            self.HalfRate = self.entry_toolrate.get()

            self.Date = date.today()

            db = sqlite3.connect("spower.db")
            c = db.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS toolsinfo(Toolname NOT NULL,"
                      "Disc TEXT,Condition TEXT,fulldayp INTEGER,"
                      "halfdayp INTEGER,date DATE)")
            db.commit()
            c.execute("INSERT INTO toolsinfo VALUES (?,?,?,?,?,?)", (self.nameTool,self.ToolDescription,self.Toolcondition, self.HalfRate, self.FullRate,
                                                                     self.Date))
            db.commit()

            tm.showinfo("Successfully Uploaded Tool!", "Now your tool can be hired other Registered User . !! Keep Exploring shared power")




'''

This is SearchTool Class which gives a function of searching  uploaded tools inorder to get directed
to HireTool GUI for hiring a specific tool.  

'''

class SearchTools(Frame):

    def __init__(self, master):

        global entry_ToolName
        global Searched_Tool

        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=591, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=self.back)
        self.button_back.place(x=615, y=3)

        self.label_ToolName = Label(master, text="Tool Name",font=("arial", 22))
        self.label_ToolName.place(x=125,y=140)

        Searched_Tool = StringVar()


        self.entry_ToolName = Entry(master,bd =5, font=("arial", 14), textvariable=Searched_Tool)
        self.entry_ToolName.place(x=296,y=140 ,width=230, height=40)
        self.searched_Tool = self.entry_ToolName.get()

        self.imgi = PhotoImage(file="Images\Vis3.png")
        self.button_vis = Button(master, image=self.imgi, font=("bold", 17),
                                     activebackground="red", command=self.search_results)
        self.button_vis.place(x=508, y=140)

        Button(master, text='Wanna Hire This Tool', font=("arial", 13, "bold"),  bg='#e37b17', fg='white', command=self.hire1).place(x=259,
                                                                                                                  y=470)


     

        #self.img2 = PhotoImage(file="Images\yup1.png")

        #self.lab2 = Label(master, image=self.img2)
        #self.lab2.place(x=20, y=10)

        self.img1 = PhotoImage(file="Images\search3.png")

        self.lab1 = Label(master, image=self.img1)
        self.lab1.place(x=200,y=5)


        master.resizable(False, False)
        master.overrideredirect(True)

    #def open_terms(self):
        #os.startfile("Terms.txt")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")

    def hire1(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                # self.master = master
                self.master.withdraw()

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = hireTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Upload Tools Form")
                # def select_image(self):
                # file_path = filedialog.askopenfilename()
                # return Image.open(file_path)

    def back(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UserPanelFrame(self.newWindow)
                self.newWindow.geometry('720x720+350+22')
                self.newWindow.title("Shared Power Login Form")

    def search_results(self):

        global Searched_Tool

      

      
        self.Searched_Tool = self.entry_ToolName.get()


    
        if self.entry_ToolName.get()=="kapendra":
        #if self.Searched_Tool and self.Searched_Tool != "            " in self.searchTool:
            
            self.newwindow = tk.Frame(self.frame,takefocus=True,bg='red',width=root.winfo_screenwidth(),height=root.winfo_screenheight()//8)
            
            lbl = Label(self.newwindow, text="Username")
            lbl1 = Label(self.newwindow, text="Password")


       #self.app = UserPanelFrame(self.newWindow)
       #self.newWindow.geometry('220x220+350+22')
       #self.newWindow.title("Shared Power Login Form")
          
        else:
            tm.showerror("Invalid ToolName", "No Such Tool Is Uploaded By Any Registered User In Our Database")


    def searchYes(self):
        self.Searched_Tool = self.entry_ToolName.get()
        return self.Searched_Tool


'''

This is HireTools Class .This will enable a function of hiring a uploaded tool . Registered user can search tool
first and can be redirected to this page too for hiring the specific tool if he doesnt know the tool name.

'''


class hireTools(SearchTools):

    def __init__(self, master):

        global entry_toolname
        # self.showyes = ok.searched_Tool
        # self.var2 = master.var2

        self.master = master
        self.frame = tk.Frame(master)

        # self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17), relief="groove",
                                      activebackground="blue", command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17), relief="groove", activebackground="red",
                                  command=self.back)
        self.button_back.place(x=515, y=3)

        self.label_toolname = Label(master, text="Tool Name", width=20, font=("arial", 17))
        self.label_toolname.place(x=30, y=165)




        # self.controller.get_page("searchTools").Searched_Tool.get()
        # label = tk.Label(self, text=VertexNumber)

        # self.searchget = self.object1.searchYes()
        self.entry_toolname = Entry(master, bd=5, font=("arial", 13))
        self.entry_toolname.place(x=280, y=165, width=200, height=38)
        #self.entry_toolname.insert(0, "Wire Cutter")
        self.entry_toolname.insert(0, self.d['Name of Tool:'])
        # self.entry_toolname.insert(0, master.searched_Tool)
        # self.entry_toolname.insert(0, "Wire Cutter")

        self.label_hireDate = Label(master, text="Hire Date", width=20, font=("arial", 17))
        self.label_hireDate.place(x=30, y=235)

        self.Date = date.today()
        self.entry_hireDate = Entry(master, bd=5, font=("arial", 13))
        self.entry_hireDate.place(x=280, y=235, width=200, height=38)
        self.entry_hireDate.insert(0, self.Date)

        self.label_hireDays = Label(master, text="Hire Days", width=20, font=("arial", 17))
        self.label_hireDays.place(x=23, y=305)

        self.entry_hireDays = Entry(master, bd=5, font=("arial", 13))
        self.entry_hireDays.place(x=280, y=305, width=200, height=38)
        self.entry_hireDays.insert(0, " Max 3 Days")

        # self.entry_hireDays.bind("<FocusIn>", hireTools.clear_hireDays)

        self.label_rate = Label(master, text="Tool Rate", width=20, font=("arial", 17))
        self.label_rate.place(x=30, y=375)
        self.tool_rate = Entry(master, bd=5, font=("arial", 13))
        self.tool_rate.place(x=280, y=375, width=90, height=38)
        self.tool_rate.insert(0, "234")

        self.label_fullrate = Label(master, text="Full Day", width=20, font=("arial", 10))
        self.label_fullrate.place(x=243, y=418)

        self.tool_rate2 = Entry(master, bd=5, font=("arial", 13))
        self.tool_rate2.place(x=390, y=375, width=90, height=38)
        self.tool_rate2.insert(0, "123")

        self.label_halfrate = Label(master, text="Half Day", width=20, font=("arial", 10))
        self.label_halfrate.place(x=353, y=418)

        Button(master, text='Hire This Tool', font=("arial", 13, "bold"), width=18, bg='#1f3a93', fg='white'
               , command=self.hired_tools).place(x=210,
                                                 y=464)

       # self.label_6 = Label(master, text="Copyright@ Developers of Shahu, 2019", width=60, font=('Helvetica', 9),
                             #cursor="hand2")
        #self.label_6.place(x=80, y=512)
        #self.label_6.bind('<Button-1>', SplashScreenFrame.open_terms)

        #self.img2 = PhotoImage(file="Images\yup1.png")

        #self.lab2 = Label(master, image=self.img2)
        #self.lab2.place(x=20, y=23)

        self.hire1 = PhotoImage(file="Images\hiretool.png")

        self.hire12 = Label(master, image=self.hire1)
        self.hire12.place(x=173, y=43)

        master.resizable(False, False)
        master.overrideredirect(True)

    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")

    def hired_tools(self):
        # global gender_selected

        # global country_selected
        # global account_selected2, account_selected1
        # global name, Username, Password,CNo

        self.nameTool = self.entry_toolname.get()

        self.HireDate = self.entry_hireDate.get()

        self.HireDays = self.entry_hireDays.get()

        self.FullRate = self.tool_rate2.get()

        self.HalfRate = self.tool_rate.get()

        if len(self.nameTool) == 0 and len(self.HireDays) == 0 :
            tm.showerror("Upload Tool Error",
                         "UploadTool is unsucessful. May be one or more field is empty.")

        else:

            self.nameTool = self.entry_toolname.get()

            self.HireDate = self.entry_hireDate.get()

            self.HireDays = self.entry_hireDays.get()

            self.FullRate = float(self.tool_rate2.get())

            self.HalfRate = float(self.tool_rate.get())

            self.InsurancePlus = self.HalfRate + 5.00

            self.InsurancePlus2 = self.FullRate + 5.00

            self.Date = date.today()

            tm.showinfo("Hired Tools Sucessful!! ",
                        "Your desired tool has been successfully added to your hired tool list. !!Keep Exploring shared power!! ")
            self.master.withdraw()

            # print('Button is pressed!')
            # self.RegistrationFrame.destroy()
            self.newWindow = tk.Toplevel(self.master)
            self.app = UserPanelFrame(self.newWindow)
            self.newWindow.geometry('720x720+350+22')
            self.newWindow.title("Shared Power Login Form")

    def back(self):
        # print(self.showyes)
        # I need make windows itself destroy after clicking on this button and make other window appear in same position
        # self.master = master
        self.master.withdraw()

        # print ('Button is pressed!')
        # self.RegistrationFrame.destroy()
        self.newWindow = tk.Toplevel(self.master)
        self.app = UserPanelFrame(self.newWindow)
        self.newWindow.geometry('720x720+350+22')
        self.newWindow.title("Shared Power Login Form")


'''

This is ReturnTool Class which enables the function of returning a hired tool which is most essential 
in printing the invoice . 

'''


class ReturnTools(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17), relief="groove",
                                      activebackground="blue", command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17), relief="groove", activebackground="red",
                                  command=self.back)
        self.button_back.place(x=515, y=3)

        self.listOfTools = Listbox(master, selectmode=EXTENDED, exportselection=0,font=("arial", 17, "bold")
                                   ,width=30, height=10,bg='#808e9b',fg='white',highlightcolor="green")
        self.listOfTools.place(x=95, y=160)

        self.data = ["scissor","laptop","washing machine","cooler"]
        #with open("Text File Handling\displayReturn.txt", "r") as f:
         #   for line in f:
          #      self.data += line.splitlines()

        # Create your listbox here.
        for i in range(len(self.data)):
            self.listOfTools.insert(i + 1, self.data[i])


        Button(master, text='Return This Tool', font=("arial", 13, "bold"), width=18, bg='#1f3a93', fg='white'
               , command=self.delete_selected_item).place(x=205, y=464)

    

        self.img2 = PhotoImage(file="Images\Returnlogo.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=10, y=31)

        self.return1 = PhotoImage(file="Images\ReturnTools.png")

        self.return12 = Label(master, image=self.return1)
        self.return12.place(x=153,y=38)

        master.resizable(False, False)
        master.overrideredirect(True)

    def delete_selected_item(self):

        tm.showwarning("Confirm ReturnTool",
                       "Are You sure want to return this tool ? If you return this tool , this tool will be deleted from "
                       "your hired tool database. ")
        self.indexes = self.listOfTools.curselection()
        for index in self.indexes:
            self.listOfTools.delete(index)



    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")
    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")




    def back(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UserPanelFrame(self.newWindow)
                self.newWindow.geometry('720x720+350+22')
                self.newWindow.title("Shared Power Login Form")



'''

This is Return Tool and Payment Class which enables the function of this GUI whhich are returning a tool
and after returning tool the user can only preview invoice and inoreder to print the iinvoice it need to be last
day of month

'''

class payTools(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)



        #self.label = Label(root, text="Registration form",width=20,fg='#1f3a93',bg = "#81cfe0 ",font=("Times", 30),borderwidth=3, relief="sunken").place(x=55,y=53)

        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=self.back)
        self.button_back.place(x=515, y=3)

        self.returnTool = PhotoImage(file="Images\Tool2.png")
        self.returnTool1 = Button(master, width=210, height=160, image=self.returnTool,
                                font=('arial', 16, "bold"), cursor="hand1",
                                activebackground="pink",
                                activeforeground="green", command=self.return1)
        self.returnTool1.place(x=45, y=168)
        self.ret13 = Label(master, text=" Return Tools ", font=("arial", 16, "bold"))
        self.ret13.place(x=77, y=358)

        #if draw.drawing == False:
            #resetall.config(state=DISABLED)
        #elif draw.drawing == True:
            #resetall.config(state=NORMAL)

        self.pay = PhotoImage(file="Images\invoice12.png")
        self.pay_tools = Button(master, text="Payment & Delivery", width=210, height=160, image=self.pay,
                                font=('arial', 16, "bold"), cursor="hand1",
                                activebackground="cyan",
                                activeforeground="green", command=self.print_invoice)
        self.pay_tools.place(x=295, y=168)



        self.pay13 = Label(master, text="  Print Invoice ", font=("arial", 16, "bold"))
        self.pay13.place(x=318, y=358)

        self.thankYou = Label(master, text="Thank You !!  ", width=30, font=("bold", 23))
        self.thankYou.place(x=20, y=438)

        

        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=20, y=21)

        self.pay1 = PhotoImage(file="Images\Cash.png")

        self.pay12 = Label(master, image=self.pay1)
        self.pay12.place(x=194,y=27)

        master.resizable(False, False)
        master.overrideredirect(True)


    def print_invoice(self):

        self.date=date.today()

        if self.date == self.date:
            tm.showwarning("Something went wrong while generating invoice","Today is not the last of month \n.You cannot print the invoice but inorder to preview invoice click OK ")

            os.startfile("Text File Handling\Invoice.txt")
            file = open("Text File Handling\Invoice.txt", "r")
            self.searchTool = file.read()
            print(self.searchTool)

        # if self.Searched_Tool== "   ":
        # tm.showerror("Invalid ToolName", "No Such Tool Is Uploaded By Any Registered User In Our Database")


        #self.show_gui = Label(self.master, text=self.searchTool, font=('courier', 12, 'bold'), bg="#0984e3")
        #self.show_gui.place(x=18, y=220)



    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def back(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                #self.master = master
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = UserPanelFrame(self.newWindow)
                self.newWindow.geometry('720x720+350+22')
                self.newWindow.title("Shared Power Login Form")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")



    def return1(self):

                # I need make windows itself destroy after clicking on this button and make other window appear in same position
                # self.master = master
                self.master.withdraw()

                #print('Button is pressed!')
                # self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = ReturnTools(self.newWindow)
                self.newWindow.geometry('550x550+450+140')
                self.newWindow.title("Upload Tools Form")



'''

This is Insurance Company Profile .Insurance Agent can login in our system by providing their valid 
credentials inorder to start their session in our software. 

'''


class InsuranceCompany(Frame):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)



        self.button_minimize = Button(master, text="_", width=1, font=("bold", 17),relief="groove",activebackground="blue",command=self.minimizeProgram)
        self.button_minimize.place(x=491, y=2)

        self.button_back = Button(master, text="X", width=2, font=("bold", 17) , relief="groove" , activebackground="red",command=self.back)
        self.button_back.place(x=515, y=3)
        self.title = Label(master, text="Welcome !! ", width=30, font=("bold", 20))
        self.title.place(x=55, y=55)

        self.logout = PhotoImage(file="Images\logout.png")
        self.user_logout = Button(master, image=self.logout, width=55, height=55, cursor="hand1", relief="flat",
                                  activebackground="red", command=self.logOut)
        self.user_logout.place(x=489, y=489)


        self.title2 = Label(master, text=" Insurance Agent Profile", width=30, font=("bold", 17))
        self.title2.place(x=91, y=125)

        self.view = PhotoImage(file="Images\Viewinfo.png")
        self.view_info = Button(master,  width=210, height=160, image=self.view,
                                font=('arial', 16, "bold"), cursor="hand1",
                                activebackground="cyan",
                                activeforeground="green", command=self.view_info1)
        self.view_info.place(x=45, y=198)

        self.view13 = Label(master, text=" View User Info ", font=("arial", 16, "bold"))
        self.view13.place(x=70, y=408)


        self.view2 = PhotoImage(file="Images\Viewtool.png")
        self.view_info1 = Button(master, width=210, height=160, image=self.view2,
                                font=('arial', 16, "bold"), cursor="hand1",
                                activebackground="cyan",
                                activeforeground="green", command=self.view_info12)
        self.view_info1.place(x=295, y=198)

        self.view132 = Label(master, text="  View All Uploaded Tool", font=("arial", 16, "bold"))
        self.view132.place(x=270, y=408)



        self.img2 = PhotoImage(file="Images\yup1.png")

        self.lab2 = Label(master, image=self.img2)
        self.lab2.place(x=5, y=21)


        master.resizable(False, False)
        master.overrideredirect(True)


    


    def logOut(self):
       

        tm.showwarning("Confirm LogOut",
                    "Are You sure want to LogOut from  shared Power? ")

        self.master.withdraw()

        
        self.newWindow = tk.Toplevel(self.master)
        self.app = LoginFrame(self.newWindow)
        self.newWindow.geometry('550x350+450+220')
        self.newWindow.title("Shared Power Login Form")



    def open_terms(self):
        os.startfile("Text File Handling\Terms.txt")

    def back(self):
                tm.showwarning("Confirm Exit",
                       "Are You sure want to exit from Shared Power? ")


        # I need make windows itself destroy after clicking on this button and make other window appear in same position
                
                self.master.withdraw()

                #print ('Button is pressed!')
                #self.RegistrationFrame.destroy()
                self.newWindow = tk.Toplevel(self.master)
                self.app = LoginFrame(self.newWindow)
                self.newWindow.geometry('550x350+450+220')
                self.newWindow.title("Shared Power Login Form")

    def minimizeProgram(self):
        # root.wm_state('iconic')
        self.master.withdraw()
        # root.state("withdrawn")





root = Tk()
root.geometry('600x370+340+190')
root.title("Registration Form")
rf = SplashScreenFrame(root)         #in this i need to change and try to implement all the frames in one coding
root.resizable(False, False)
root.overrideredirect(False)
#root.wm_iconbitmap('Icon1.ico')



root.mainloop()
