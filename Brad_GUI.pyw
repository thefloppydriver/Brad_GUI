import smtplib
import time
import random
import os
import threading
import queue
from tkinter import *
from PIL import Image, ImageTk
from email.message import EmailMessage
from email.mime.text import MIMEText

global Jomar
global realcarrier
global oof
global victim
global delay
global number
global stupid
global me
global mee
global makeentry
global e1
global e2
global T
global spamit
global qspamDelay
global stop_spamming
global spamitthread
global e1get
global e2get
global e3get
global executestorage
global execute
global starttt
global startttt
global starttt
global nametxt
global messagetxt
global emailtxt
global passwordtxt
global contactstxt
global notestxt

nametxt = 'Melissia'
messagetxt = 'SPAMMMM'
emailtxt = 'fearmypowergoodsir@gmail.com'
passwordtxt = 'sp4m.m3!'
contactstxt = {'jomar':2163198688,
               'jayden':8032432431,
               'kendall':8034934103,
               'ryan':9809257025,
               'gracee':8035041480,
               'rene':8036166880,
               'ada':7049890912}
notestxt = '''Kendall is on Verizon
Jomar is on T-Mobile
Jayden is on T-Mobile
Kylee is on T-Mobile
Gracee is on AT&T
Rene is on Boost Mobile
I'm on Verizon (Ryan)
Ada is on Verizon'''

e1get = queue.Queue()
e2get = queue.Queue()
e3get = queue.Queue()
e1get.put(1000000000)
e2get.put('v')
e3get.put(1)

executestorage = queue.Queue()
executestorage.put("pass")
qspamDelay = queue.Queue()
stop_spamming = queue.Queue()



stop_spamming.put(False)

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    global spamitthread
    global execute
    global starttt
    global startttt
    starttt = True
    
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    def init_window(self):
        global e1
        global e2
        global e3
        global e4
        global T
        ################################
        numberOrContact = Label(self.master, text="Number or contact:",font = ('Courier New',9))##.grid(row=0)
        victimsCarrier = Label(self.master, text="Victim's carrier:",font = ('Courier New',9))##.grid(row=1)
        spamDelay = Label(self.master, text="Message Delay (s):",font = ('Courier New',9))
        writeToFileLabel = Label(self.master, text="Write to fileMenu:",font = ('Courier New',9))
        e1 = Entry(self.master)
        e2 = Entry(self.master)
        e3 = Entry(self.master) #this is the delay MULTI-THREAD IT!!!
        e4 = Entry(self.master)
        S = Scrollbar(self)
        T = Text(self, height=4, width=47)
        # changing the title of our master widget      
        self.master.title("Brad v6.0 with Multi-Threading")

        # allowing the widget to take the full space of the root window
        self.pack(fill=X, side=BOTTOM, expand=0)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=RIGHT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        
        # creating a button instance
        spamitButton = Button(self.master, text="SPAM",command=self.update_spamit_thread)
        ##getButton = Button(self.master, text="get",command=self.show_entry_fields)
        stopSpammingButton = Button(self.master, text="sToP", command=self.stop_spamit_thread)
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Contacts", command=self.showContacts)
        #edit.add_command(label="Show Text", command=self.showText)
        edit.add_command(label="Edit message.txt", command=self.editMessage)
        edit.add_command(label="Edit name.txt", command=self.editName)
        edit.add_command(label="Show notes.txt", command=self.showNotes)
        
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)
        
        # placing the button on my window
        spamitButton.place(x=0, y=200)
        stopSpammingButton.place(x=50, y=200)
        #getButton.place(x=50, y=0)

        numberOrContact.place(x=0, y=0)
        victimsCarrier.place(x=0, y=50)
        spamDelay.place(x=0, y=100)
        writeToFileLabel.place(x=0, y=150)
        e1.place(x=130, y=0)
        e2.place(x=130, y=50)
        e3.place(x=130, y=100)
        e4.place(x=130, y=150)

        
    def showContacts(self):
        global contactstxt
        noot = Tk()
        Q = Scrollbar(noot)
        R = Text(noot, height=10, width=50)
        Q.pack(side=RIGHT, fill=Y)
        R.pack(side=LEFT, fill=Y)
        Q.config(command=R.yview)
        R.config(yscrollcommand=Q.set)
        noot.title("Contacts")
        bibby = list(map(lambda x:x,contactstxt))
        R.insert(END, "Working Contacts: "+"\n"+("\n".join(map(str, bibby))))
        mainloop()


    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def editMessage(self):
        global messagetxt
        messagetxt = e4.get()
        T.insert(END, 'Message updated successfully! \n')
        T.insert(END, 'Message: '+messagetxt+'\n')
    def editName(self):
        global nametxt
        nametxt = e4.get()
        T.insert(END, 'Name updated successfully! \n')
        T.insert(END, 'Name: '+nametxt+'\n')
    def alert_ryan(self):
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('fearmypowergoodsir@gmail.com', 'sp4m.m3!')
        s.sendmail('fearmypowergoodsir@gmail.com', '9809257025@vtext.com', 'Subject: ALERT'+str(random.randint(0, 10000))+'\n'+'To: , 9809257025@vtext.com'+'\n'+'Someone just tried to spam '+e1.get()+'.')
        s.quit()
            
    def showNotes(self):
        global notestxt
        soot = Tk()
        C = Scrollbar(soot)
        D = Text(soot, height=10, width=50)
        C.pack(side=RIGHT, fill=Y)
        D.pack(side=LEFT, fill=Y)
        C.config(command=D.yview)
        D.config(yscrollcommand=C.set)
        soot.title("Notes")
        D.insert(END, notestxt)
        mainloop()
        
    def execute():
        exec(executestorage.get())
        executestorage.put("pass")
        
    def spamit(self, e1get, e2get, e3get):
        global stop_spamming
        global nametxt
        global messagetxt
        global contactstxt
        global emailtxt
        global passwordtxt
        
        stop_spammingget = stop_spamming.get()
        stop_spamming.put(stop_spammingget)
        if stop_spammingget == True:
            stop_spamming.put(False)
            raise NameError("yeet")
        if stop_spammingget == False:
            if str(e1get).isdigit() == True:
                while True:
                    try:
                        if int(e1get) >= 10000000000 or int(e1get) <= 999999999:
                            quit()
                        if int(e1get) <= 10000000000 and int(e1get) >= 999999999:
                            break
                    except ValueError:
                        quit()
                        
                if e1get == '7049890912' or e1get == 7049890912 or e1get == '9809257025':
                    self.alert_ryan()
                    root.destroy()
                    quit() 
                    
                number=e1get
                T.insert(END, 'Target number:'+number)
                
            if str(e1get).isdigit() == False:
                if e1get.lower() == 'ada' or e1get.lower() == 'ryan':
                    self.alert_ryan()
                    T.insert(END, 'oH \n')
                    time.sleep(2)
                    T.insert(END, 'sO tHaT\'S hOw It iS NoW \n')
                    time.sleep(2)
                    root.destroy()
                    quit()

                try:
                    number = contactstxt[e1get.lower()]
                except KeyError:
                    T.insert(END, e1get.lower()+' is not in the list of contacts. (Go tell Ryan, he\'ll fix it for you :] )\n')

            if e2get.lower().startswith('v'):
                realcarrier='@vtext.com'
            elif e2get.lower().startswith('t'):
                realcarrier='@tmomail.net'
            elif e2get.lower().startswith('a'):
                realcarrier='@txt.att.net'
            elif e2get.lower().startswith('s'):
                realcarrier='@messaging.sprintpcs.com'
            elif e2get.lower().startswith('m'):
                realcarrier='@mymetropcs.com'
            elif e2get.lower().startswith('b'):
                realcarrier='@sms.myboostmobile.com'
            else:
                T.insert(END, 'THATS NOT A SUPPORTED CARRIER!!! (Go tell Ryan, he\'ll fix it for you :] )\n')
            
            msg = EmailMessage()
            msg.set_content(messagetxt)    
            thread_number = random.randint(0, 10000)
            msg['Subject'] = nametxt + str(thread_number)
            msg['From'] = emailtxt
            msg['To'] = str(number)+realcarrier
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(emailtxt, passwordtxt)
            s.sendmail(emailtxt, str(number)+realcarrier, msg.as_string())

            T.insert(END, "Spam message sent to: " + str(number)+realcarrier + '\n')
            s.quit()

        e1get2 = e1get
        e2get2 = e2get
        e3get2 = e3get
        stop_spammingget = stop_spamming.get()
        stop_spamming.put(stop_spammingget)
        if stop_spammingget == False:
            print(e3.get())
            time.sleep(int(e3get))
            root.update()
            #stop_spamming.put(False)
            self.spamit(e1get2, e2get2, e3get2)
        if stop_spammingget == True:
            T.insert(END, 'Stopped. \n')
            stop_spamming.put(False)
            
    def update_spamit_thread(self):
        global spamitthread
        spamitthread = threading.Thread(target=self.spamit, args=(e1.get(), e2.get(), e3.get()))
        spamitthread.start()
            
    def stopit(self):
        global spamitthread
        global stopspamming
        global T
        try:
            if spamitthread != None:
                stop_spamming.put(True)
                spamitthread.join()
        except NameError:
            T.insert(END, "Uhh... \n")
            root.update()
            time.sleep(2)
            T.insert(END, "...no. \n")
            root.update()
            
    def stop_spamit_thread(self):
        global stopitthread
        global spamitthread
        global T
        stopitthread = threading.Thread(target=self.stopit, args=())
        stopitthread.start()
                
    def client_exit(self):
        root.destroy()
        quit()
        
    def show_entry_fields(self):
        T.insert(END, "First Name: %s\nLast Name: %s\n" % (e1.get(), e2.get()))
        
root = Tk()
root.geometry("400x300")
app = Window(root)
execute()  
root.mainloop()


