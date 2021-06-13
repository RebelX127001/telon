"""
!/usr/bin/env python3
__AUTHOR = "JIMOH IDRIS OLANSHILE"
__DATE = "DEC 2019 - till date."
__TECHNOLOGIES = "PY+adb+Batch+Programming+PIL+Tkinter"
"""
import os as gd, subprocess as sp, time
from tkinter import messagebox as mb
from tkinter import*
import indiv, js
from PIL import ImageTk
def mainActivity():
        def connActivity():
            def telonActivity():
                def userComm():
                    uTime = t.get()
                    uTime = uTime.lower()
                    uTime = uTime.rpartition ("=")#Extra feature for geeks
                    if uTime [0] == "s":
                        tt = int (uTime [2])
                        print (tt, "seconds")
                    elif len (uTime[2]) > 0 and uTime [0] == "" and uTime [0] == "": #if the spinbox was used
                        mb.showinfo ("Got here")
                        tt = int (uTime [2]) * 60
                    elif uTime [0] == "m" and len (uTime[2]) == 1:
                        tt = int (uTime [2]) * 60
                        print (tt, "seconds.")
                    elif uTime [0] == "h":
                        tt = int (uTime [2]) * 60 * 60
                        print (tt, "seconds")
                    else:
                        mb.showerror ("Error", "Invalid input.")
                    userI = fdBck.get()
                    userInput = userI.lower() #convert userinput to lower case for easier iteration
                    if userInput == "":mb.showerror("Error", "Field can't be empty.")
                    elif userInput.count (indiv.comm["h"]) > 0:time.sleep(tt),howtF()
                    elif userInput.count (indiv.comm["ab"]) > 0:time.sleep(tt),abtF()
                    elif userInput.count (indiv.comm["dn"]) > 0:time.sleep(tt),dontF()
                    elif userInput.count (indiv.comm["dc"]) > 0:time.sleep(tt),discF()
                    elif userInput.count (indiv.comm["lc"]) > 0:time.sleep(tt),indiv.lnchA()
                    elif userInput.count (indiv.comm["ud"]) > 0:time.sleep(tt),indiv.instAppUp()
                    elif userInput.count (indiv.comm["is"]) > 0:time.sleep(tt),indiv.instApp()
                    elif userInput.count (indiv.comm["un"]) > 0:time.sleep(tt),indiv.unInst()
                    elif userInput.count (indiv.comm["mu"]) > 0:time.sleep(tt),indiv.instApp()
                    elif userInput.count (indiv.comm["sc"]) > 0:time.sleep(tt),indiv.sCap()
                    elif userInput.count (indiv.comm["sr"]) > 0:time.sleep(tt),indiv.sRec()                                                                                                                    
                    elif userInput.count (indiv.comm["sd"]) > 0:time.sleep(tt),indiv.shutDwn()
                    elif userInput.count (indiv.comm["lk"]) > 0:time.sleep(tt),indiv.lck()
                    elif userInput.count (indiv.comm["ulk"]) > 0:time.sleep(tt),indiv.lck()
                    elif userInput.count (indiv.comm["rb"]) > 0:time.sleep(tt),indiv.reb()
                    elif userInput.count (indiv.comm["bu"]) > 0:time.sleep(tt),indiv.bkUp()
                    elif userInput.count (indiv.comm["sh"]) > 0:time.sleep(tt),indiv.devWin()
                    elif userInput.count (indiv.comm["dev"]) > 0:time.sleep(tt),indiv.devWin()
                    elif userInput.count (indiv.comm["gn"]) > 0:time.sleep(tt),indiv.passGen()
                    elif userInput.count (indiv.comm["sC"]) > 0:time.sleep(tt),indiv.passGen()
                    elif userInput.count (indiv.comm["pw"]) > 0:time.sleep(tt),indiv.passGen()
                    elif userInput.count (indiv.comm["lk"]) > 0:time.sleep(tt),indiv.opnL()
                    elif userInput.count (indiv.comm["ng"]) > 0:time.sleep(tt),indiv.opnL()
                    elif userInput.count (indiv.comm["cl"]) > 0:time.sleep(tt),indiv.killWin()
                    elif userInput.count (indiv.comm["kl"]) > 0:time.sleep(tt),indiv.killWin()
                    else:
                        mb.showerror("Error", "Command not understood.")
                        """print (userInput)
                        print (time)"""

                def abtF ():
                    abtP = Tk()
                    abtP.title("TeLon@About-Us")
                    abtP.geometry("610x350+385+200")
                    titLab = Label (abtP, text = "About Us", font = ("times new roman", 15, "bold")).place (x=0,y=15,relwidth=1)
                    aboutUs = """Alright, so I like to call TeLon (then JayHack) an Automation Software but it can also go beyond that to demonstrate the power of programming. This project was written and is still managed by Jimoh Idris Olanshile, a computer programmer and a security & privacy advocate. I started the project in my 4th year in college back in 2019 with just 3 features. (0) To Screenshot my phone's screen and display the image on my PC's screen. (1) To get the APK file of an installed App. (2) To force-close currently opened window.\nAt the time, it only had a Command Line Interface given that I was using it for myself and could care less about a UI. At the end of my 4th year, the features had already grown to 12 and I was really happy with myself.
    However, as i kept using the program and kept showing it people I realized it wasnt user friendly, and thats how my next quest began; To create the GUI version called TeLon before my convocation day. \nPS: the name TeLon was coined from the names of two of the greatest minds to ever walk the earth; "Nikola Tesla" and "Elon Musk"."""
                    txt = Text(abtP, width = 70, height = 17, wrap = WORD)
                    txt.insert(INSERT, aboutUs)
                    txt.place(x=22, y=60)
                    abtP.mainloop()
                    
                def howtF ():
                    howtP = Tk()
                    howtP.title("TeLon@How-To")
                    howtP.geometry("610x350+385+200")
                    titLab = Label (howtP, text = "How to TeLon", font = ("times new roman", 15, "bold")).place (x=0,y=15,relwidth=1)
                    howText = """Hey, I heard you needed my help. This how-to should be simple and straightforward.\n\n1. Find Developer's Options on the device and Enable USB debugging.\nPS: If you can't find Developer's Options simply go to "About Phone" and Tap the text "Build Number" 3 times to enable it.\n\n2. Connect the PC to your phone's Hotspot or just make sure they're both on the same network.\n\n3. Visit www.TeLon.com/Download to register and download TeLon.\n\n4. Fire up and Login with your credentials.\n\n5. Attach your device with a USB cord and detach it once you've connected with your IP Address."""
                    txt = Text(howtP, width = 70, height = 15, wrap = WORD)
                    txt.insert(INSERT, howText)
                    txt.place(x=25, y=60)
                    howtP.mainloop()

                def discF ():
                    #Alrigth so whats happening here is a simple trick. In order to disconnected I'm creating a string variable that holds the predicted outcome of a disconnected device
                    #the string is then compared with the output of the command that disconnects the device from TeLon.
                    ipAd = ip.get()
                    predOut = "b'disconnected " + ipAd + ":" + port + "\\r\\n'"
                    try:
                        serialNo = ipAd + ":" + port
                        outP = sp.check_output("zaglarh disconnect " + serialNo)
                        if str(outP) == predOut:mb.showinfo("Success", "Disconnected " + serialNo)
                    except sp.CalledProcessError:
                        mb.showerror("Error", "No device connected to TeLon")
                        indiv.clr()

                def dontF ():
                    dontP = Tk()
                    dontP.title("TeLon@Assist-us")
                    dontP.geometry("610x350+385+200")
                    titLdon = Label (dontP, text = "Assist The Programmer", font = ("times new roman", 15, "bold")).place (x=0,y=25,relwidth=1)
                    donText = "I truly appreciate your interest to make a donation as your donation will go a long way in the developnment and the continual improvement of TeLon no matter how little it may be, Thank you in advance.\n\n\n" + line + "\nBank Name: GtBank\nAccount Name: Jimoh Idris Olansile\nAccount Number: 0202884092\nPhone Number: +2348159344489"
                    txt = Text(dontP, width = 70, height = 10, wrap = WORD)
                    txt.insert(INSERT, donText)
                    txt.place(x=25, y=80)
                    dontP.mainloop()

                def run():
                    if rOption.get() == 1:telonP.destroy(), indiv.opnL()
                    elif rOption.get() == 2:indiv.bulkee()
                    elif rOption.get() == 3:print (rOption.get())
                    elif rOption.get() == 4:telonP.destroy(), js.js_MainActivity()
                    elif rOption.get() == 5:indiv.devWin()
                    elif rOption.get() == 6:print (rOption.get())
                    elif rOption.get() == 7:telonP.destroy(), indiv.passGen()
                    elif rOption.get() == 8:print (rOption.get())
                    elif rOption.get() == 9:indiv.shutDwn()
                    elif rOption.get() == 10:telonP.destroy(), indiv.unLck()
                    elif rOption.get() == 11:indiv.reb()
                    elif rOption.get() == 12:indiv.lck()
                    elif rOption.get() == 13:indiv.killWin()
                    elif rOption.get() == 14:indiv.sCap()
                    elif rOption.get() == 15:telonP.destroy(), indiv.imgCap()
                    elif rOption.get() == 16:telonP.destroy(), indiv.vidCap()
                    elif rOption.get() == 17:telonP.destroy(), indiv.sRec()
                    elif rOption.get() == 18:indiv.devMirror()
                    elif rOption.get() == 19:telonP.destroy(), indiv.puApp()
                    elif rOption.get() == 20:indiv.instAppUp()
                    elif rOption.get() == 21:indiv.instApp()
                    elif rOption.get() == 22:telonP.destroy(), indiv.unInst()
                    elif rOption.get() == 23:indiv.lnchA()
                    elif rOption.get() == 24:print (rOption.get())
                    elif rOption.get() == 25:indiv.bkUp()
                    else:mb.showerror("Error", "Select an option!!!")
                        
                telonP = Tk()
                telonP.title("TeLon@Main-Page")
                telonP.geometry("800x540+290+90")
                Bg = ImageTk.PhotoImage(file = "C:/virtualenvironment/TeLon/include/images/back.png")
                telonBg = Label (telonP, image = Bg)
                telonBg.place(x = 0, y = 0, relwidth = 1, relheight = 1)
                title = Label(telonP, text = "TELON", font = ("times new roman", 30, "bold"), bg = "#2896e0", fg = "WHITE", bd = 10, relief = FLAT)
                title.place (x=0,y=0,relwidth=1)
                scrFrame = Frame (telonP, bg = "WHITE")
                scrFrame.place (x=380, y=110)
                genFrame = Frame (telonP, bg = "WHITE")
                genFrame.place (x = 100, y = 110)
                sysFrame = Frame (telonP, bg = "WHITE")
                sysFrame.place (x = 100, y = 300)
                appFrame = Frame (telonP, bg = "WHITE")
                appFrame.place (x = 380, y = 300)
                simpFrame = Frame (telonP, bg = "WHITE")
                simpFrame.place (x = 600, y = 230)
                rOption = IntVar()
                r1 = Radiobutton(scrFrame, command = "", text = "Screenshot the Device", value = 14, variable = rOption, bg = "WHITE").grid(row = 2, column = 1)
                r2 = Radiobutton(scrFrame, text = "Record the Screen", value = 17, variable = rOption, bg = "WHITE").grid(row = 5, column = 1)
                r3 = Radiobutton(scrFrame, text = "Mirror the Device", value = 18, variable = rOption, bg = "WHITE").grid(row = 6, column = 1)
                r4 = Radiobutton(scrFrame, text = "Record with (Back-Camera)", value = 16, variable = rOption, bg = "WHITE").grid(row = 4, column = 1)
                r5 = Radiobutton(scrFrame, text = "Take a Picture (Back-Camera)", value = 15, variable = rOption, bg = "WHITE").grid(row = 3, column = 1)
                r6 = Radiobutton(scrFrame, text = "Close Opened Window ", value = 13, variable = rOption, bg = "WHITE").grid(row = 1, column = 1)
                r7 = Radiobutton(genFrame, text = "Navigate to a link (Default Browser)", value = 1, variable = rOption, bg = "WHITE").grid(row = 1, column = 1)
                r8 = Radiobutton(genFrame, text = "Send or Receive Files", value = 4, variable = rOption, bg = "WHITE").grid(row = 4, column = 1)
                r9 = Radiobutton(genFrame, text = "WhatsApp Bulkee", value = 2, variable = rOption, bg = "WHITE").grid(row = 2, column = 1)
                rA = Radiobutton(genFrame, text = "Developer's Shell", value = 5, variable = rOption, bg = "WHITE").grid(row = 5, column = 1)
                rB = Radiobutton(genFrame, text = "Play Files Anonymously", value = 3, variable = rOption, bg = "WHITE").grid(row = 3, column = 1)
                rC = Radiobutton(genFrame, text = "Scare Text", value = 6, variable = rOption, bg = "WHITE").grid(row = 6, column = 1)
                rD = Radiobutton(appFrame, text = "Launch an App", value = 23, variable = rOption, bg = "WHITE").grid(row = 5, column = 1)
                #rE = Radiobutton(appFrame, text = "Install an App", value = 24, variable = rOption, bg = "WHITE").grid(row = 6, column = 1)
                rF = Radiobutton(appFrame, text = "Install an App update", value = 20, variable = rOption, bg = "WHITE").grid(row = 2, column = 1)
                rG = Radiobutton(appFrame, text = "Uninstall an App", value = 22, variable = rOption, bg = "WHITE").grid(row = 4, column = 1)
                rH = Radiobutton(appFrame, text = "Pull APK file of an App", value = 19, variable = rOption, bg = "WHITE").grid(row = 1, column = 1)
                rI = Radiobutton(appFrame, text = "Install App(s)", value = 21, variable = rOption, bg = "WHITE").grid(row = 3, column = 1)
                #rJ = Radiobutton(sysFrame, text = "Display a Phone Contact", value = 8, variable = rOption, bg = "WHITE").grid(row = 2, column = 1)
                rK = Radiobutton(sysFrame, text = "Generate Secure Password", value = 7, variable = rOption, bg = "WHITE").grid(row = 1, column = 1)
                rL = Radiobutton(sysFrame, text = "Reboot the Device", value = 11, variable = rOption, bg = "WHITE").grid(row = 5, column = 1)
                rM = Radiobutton(sysFrame, text = "Shutdown the Device", value = 9, variable = rOption, bg = "WHITE").grid(row = 3, column = 1)
                rN = Radiobutton(sysFrame, text = "Lock the Device", value = 12, variable = rOption, bg = "WHITE").grid(row = 6, column = 1)
                rO = Radiobutton(sysFrame, text = "Unlock the Device", value = 10, variable = rOption, bg = "WHITE").grid(row = 4, column = 1)
                rP = Radiobutton(sysFrame, text = "Android BackUp / Restore", value = 25, variable = rOption, bg = "WHITE").grid(row = 7, column = 1)
                rQ = Radiobutton(simpFrame, command = abtF, text = "About", value = 100, variable = rOption, bg = "WHITE").grid(row = 1, column = 1)
                rR = Radiobutton(simpFrame, command = howtF, text = "How To", value = 101, variable = rOption, bg = "WHITE").grid(row = 2, column = 1)
                rS = Radiobutton(simpFrame, command = discF, text = "Disconnect", value = 102, variable = rOption, bg = "WHITE").grid(row = 3, column = 1)
                rT = Radiobutton(simpFrame, command = dontF, text = "Donate", value = 103, variable = rOption, bg = "WHITE").grid(row = 4, column = 1)
                fdBck = StringVar()
                ftEntry = Entry (telonP, bd = 5, width = 45, textvariable = fdBck)
                ftEntry.place(x = 100, y = 500)
                t = StringVar()
                timeS = Spinbox (telonP, width = 5, wrap = True, from_ = 1, to = 60, textvariable = t)
                timeS.grid (padx = 400, pady = 505)
                sndBtn = Button (telonP, command = userComm, text = "Schedule", bg = "Red", fg = "WHITE")
                sndBtn.place(x = 465, y = 500)
                runBtn = Button (telonP, command = run, text = "Run", bg = "Red", fg = "White")
                runBtn.place(x=735, y=270)
                telonP.mainloop()
            def connIP():
                ipa = ip.get() #get ip address from entry widget
                por = sp.check_output("zaglarh tcpip " + port)
                output = sp.check_output("zaglarh connect " + ipa + ":" + port)
                confOutput = "b'connected to " + str(ipa) + ":" + port + "\\r\\n'"
                if confOutput == str(output):
                    time.sleep(5)
                    indiv.clr()
                    res = mb.askokcancel ("Device Connected", "You can pull it out now (^~^)\n Press OK to continue.")
                    if res == True:conn.destroy(), telonActivity()
                else:mb.showerror("Not Connected", "Try again!!!\n\nPS: Check that the IP ADDRESS is correct.\nAnd also that you're on the same network")

            def skipConn():
                conn.destroy()
                telonActivity()

            login.destroy()
            conn = Tk()
            conn.title("TeLon@Connection Page")
            conn.geometry("800x540+290+90")
            bgPic=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/back.png")
            connLogo=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/cn.png")
            connBackground = Label(conn, image=bgPic)
            connBackground.place(x=0, y=0, relwidth=1, relheight=1)
            #++++++++++++++++++Set Display Name#++++++++++++++++++
            title = Label(conn, text = "CONNECT", font = ("times new roman", 30, "bold"), bg = "#2896e0", fg = "WHITE", bd = 10, relief = FLAT)
            title.place (x=0,y=0,relwidth=1)
            #++++++++++++++++++Create Connection Frame#++++++++++++++++++
            connFrame = Frame (conn, bg="WHITE")
            connFrame.place(x=245, y=260)
            logoL = Label(connFrame, image = connLogo, bg = "white", bd = 0).grid(row = 0, columnspan = 2, padx = 100, pady = 20)
            try:
                byteIP = sp.check_output("zaglarh shell ip route")
                stringIP = str(byteIP).rpartition("src")
                rIP = stringIP[2]
                rrIP = rIP.rpartition("\\r\\n")
                ipAdd = rrIP[0]
                devName = sp.check_output("zaglarh shell getprop transsion.device.name")
                text = Text(conn, width = 70, height = 10, wrap = WORD)
                text1 = sp.check_output("zaglarh devices")
                text2 = "PS: If you device isnt connected, kindly get your IP Address below and place it in the to box connect. Or skip if your device is present.\n\n" + line
                text3 = byteIP
                text.insert(INSERT, text1)
                text.insert(INSERT, text2)
                text.insert(INSERT, text3)
                text.place(x=115, y=100)
                ip = StringVar()
                pType = StringVar()
                ipEntry = Entry (connFrame, bg = "WHITE", width = 30, textvariable = ip).grid (rows = 2, columnspan = 2, pady = 20)
                spPhone = Spinbox (connFrame, state = "readonly", textvariable = pType, bg = "WHITE", wrap = True, width = 30, values = (devName, "HUAWEI Y7 Prime 2019", "Infinix Note 5 Stylus", "Samsung Galaxy S7 Edge", "Samsung Galaxy S8 Edge", "Nokia ")).grid(row = 3, columnspan = 2, padx = 10, pady = 1)
                btn = Button(connFrame, relief = GROOVE, command = connIP, text = "Connect", bg = "#2896e0", width = 6, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 4, column = 0, pady = 10)           
                btn2 = Button(connFrame, relief = GROOVE, text = "Skip", command = skipConn, bg = "RED", width = 6, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 4, column = 1)
                conn.mainloop()
            except sp.CalledProcessError:
                indiv.clr()
                mb.showerror("Device Not Attached", "Hey, put it inside me (^~^)")

        def loginP():
            username = userN.get()
            password = passW.get()
            if username == "" or password == "":connActivity(), #mb.showerror("Error", "All fields are required!!!")
            elif username == "Admin" and password == "admin":connActivity()
            else:mb.showwarning("Wrong Info", "Incorrect password or username.")

        login = Tk()
        login.title("TeLon@Login Page")
        global line
        line = "-" * 70
        global abspath 
        abspath = gd.path.join ("C://", "virtualenvironment", "TeLon")
        gd.system("cd " + abspath)
        #disC = sp.check_output("zaglarh disconnect")
        indiv.clr()
        login.geometry("800x540+290+90")
        bgPict=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/back.png")
        logoIcon=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/L.png")
        userIcon=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/u.png")
        passIcon=PhotoImage(file="C:/Virtualenvironment/TeLon/Include/images/p.png")
        userN = StringVar()
        passW = StringVar()
        global port
        port = "4204"
        background = Label(login, image=bgPict)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        title = Label(login, text = "LOGIN", font = ("times new roman", 30, "bold"), bg = "#2896e0", fg = "WHITE", bd = 10, relief = FLAT)
        title.place (x=0,y=0,relwidth=1)
        Login_Frame = Frame (login, bg="white")
        Login_Frame.place(x=165, y=95)
        logoLbl = Label(Login_Frame, image = logoIcon, bg = "white", bd = 0).grid(row = 0, columnspan = 2, padx = 100, pady = 20)
        userLbl = Label(Login_Frame, text = "Username", image=userIcon, compound = LEFT, font=("times new roman", 20, "bold"), bg = "white").grid(rows=1, column=0, padx=20, pady=0)
        userTxt = Entry(Login_Frame, width = 13, bd =5, relief=GROOVE, textvariable = userN, font = ("", 15)).grid(row = 1, column = 1, padx = 20, pady = 0 )
        passLbl = Label(Login_Frame, text = "Password", image=passIcon, compound = LEFT, font=("times new roman", 20, "bold"), bg = "white").grid(rows=1, column=0, padx=20, pady=0)
        passTxt = Entry(Login_Frame, width = 13, bd =5, relief=GROOVE, textvariable = passW, font = ("", 15)).grid(row = 2, column = 1, padx = 20, pady = 0)
        loginButton = Button(Login_Frame, relief = GROOVE, command = loginP, text = "Login", bg = "#2896e0", width = 10, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 3, column = 1, pady = 10)
        login.mainloop()

mainActivity()
