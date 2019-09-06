#!/usr/bin/python

import tkinter
from tkinter import ttk

index = 0 
class Main(tkinter.Frame):
    index = 0
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    
    def init_main(self):
        toolbar = tkinter.Frame(bg='#d7d8a0', bd=3)
        toolbar.pack( side = tkinter.TOP, fill=tkinter.X)


        #Network_view Button
        self.add_img = tkinter.PhotoImage(file='Network-icon.gif')
        btn_Network_View= tkinter.Button(toolbar, text='Network View',command = self.Network_view , bg='#d7d8a0', bd=0,
        compound=tkinter.TOP, image=self.add_img )
        btn_Network_View.pack(side = tkinter.LEFT)

        #Statistics
        self.add_img2 = tkinter.PhotoImage(file='statistics.gif')
        btn_Statistics = tkinter.Button(toolbar,text='Statistics', command=self.Statistics, bg='#d7d8a0',
         bd=0, compound=tkinter.TOP ,  image=self.add_img2)
        btn_Statistics.place( x=160, y=0)

        #Network_Clients
        self.add_img3 = tkinter.PhotoImage(file='Clients.gif')
        btn_Clients = tkinter.Button(toolbar,text='Network Clients',bg='#d7d8a0', bd=0,
        compound=tkinter.TOP ,  image=self.add_img3)
        btn_Clients.place(x=320, y=0)
        
        #Toggle On/Off
        
        self.add_img4 = tkinter.PhotoImage(file='Off.gif')
        btn_Toggle = tkinter.Button(toolbar, bg='#d7d8a0', bd=0,
        compound=tkinter.TOP, text='Off', image = self.add_img4  )
        btn_Toggle.bind('<Button-1>', lambda event: Toggle(self))
        btn_Toggle.place(x=575, y=25)

        #Help button
        self.add_img5 = tkinter.PhotoImage(file = 'Help.gif')
        btn_Help = tkinter.Button(toolbar,bg='#d7d8a0', bd=0, compound = tkinter.TOP,
         text = 'Help', image = self.add_img5)  
        btn_Help.place(x=480, y=0 )

        #function of toggle button                   
        def Toggle(self):
        
         global index 
        
         if  index == 0 :
            self.add_img4.config(file = 'On.gif') 
            btn_Toggle.config(text='On') 
            
         else:
            self.add_img4.config(file = 'Off.gif') 
            btn_Toggle.config(text='Off')
            

         index = not index
    
    
    #function of Statistics
    def Statistics(self):
        #Clear window func
        for widget in self.winfo_children():
            widget.destroy()
        #Data Table builder
        self.tree =ttk.Treeview(self, columns=('SOURCE_IP', 'SOURCE_MAC','DES_IP','DES_MAC','PROTOCOL','TIME'),
         height=15, show='headings')

        self.tree.column('SOURCE_IP', width=110, anchor=tkinter.CENTER)
        self.tree.column('SOURCE_MAC', width=110, anchor=tkinter.CENTER)
        self.tree.column('DES_IP', width=110, anchor=tkinter.CENTER)
        self.tree.column('DES_MAC', width=110, anchor=tkinter.CENTER)
        self.tree.column('PROTOCOL', width=110, anchor=tkinter.CENTER)
        self.tree.column('TIME', width=110, anchor=tkinter.CENTER)
        #Name of the columns
        self.tree.heading('SOURCE_IP', text='SOURCE IP')
        self.tree.heading('SOURCE_MAC', text='SOURCE MAC')
        self.tree.heading('DES_IP', text='DES IP')
        self.tree.heading('DES_MAC', text='DES MAC')
        self.tree.heading('PROTOCOL', text='PROTOCOL')
        self.tree.heading('TIME', text='TIME')
        
        #Data entry to the columns
        #You can assign variable of data structure to 'values' and this will work too
        self.tree.insert('','end', values=("10.100.102.1","00:A0:C9:14:C8:29","192.168.0.6",
        "00:1B:44:11:3A:B7","TCP","00:15"))   
        self.tree.insert('','end', values=("192.168.0.6","00:1B:44:11:3A:B7","10.100.102.1",
        "00:A0:C9:14:C8:29","UDP","00:17"))   
        
        self.tree.pack()
 
    def Network_view(self):
        #Clear window func
        for widget in self.winfo_children():
            widget.destroy()
        
       

    
 #this class is for second pop-up dialog window, if we need to add Error msg or smth   
class Child(tkinter.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Error")
        self.geometry('400x220+400+300')
        self.resizable(False, False) 
        
        self.grab_set()
        self.focus_set() 


if __name__ == "__main__":
    root=tkinter.Tk()
    app = Main(root)
    app.pack()
    root.title("Network Analyser")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
