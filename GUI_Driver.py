import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Filter_Design as f
#all the buttons are working for the first tab
#time to add frames in the phasor tab
class GUI_Driver:
    def __init__(self, master,iconPath):
       
        self.root = master
        root.geometry("816x500")
        root.title("Filter Designer")
        root.resizable(False,False)
        root.iconbitmap(iconPath)
        #creating the tab bar for the different frames in the gui
        tab_bar = ttk.Notebook(root)
        tab_bar.grid(row=0, column=0, sticky='nsew')
        tab1_frame = tk.Frame(tab_bar)
        tab2_frame = tk.Frame(tab_bar)
        tab_bar.add(tab1_frame,text="Filters")
        tab_bar.add(tab2_frame,text='Phasors')
        
        #Create the top frames in tab1
        self.frame1 = tk.LabelFrame(tab1_frame,text = "Chebyshev", width=200, 
                                    height=100, bg='white')
        self.frame2 = tk.LabelFrame(tab1_frame, text = "Bessel", width=200, 
                                    height=100, bg='white')
        self.frame3 = tk.LabelFrame(tab1_frame, text = "Buttersworth", width=200, 
                                    height=100, bg='white')

        # Create the bottom frame in tab1
        self.bottom_frame1 = tk.Frame(tab1_frame, width=600, height=400, bg='white')

        # Arrange the frames using the grid geometry manager
        self.frame1.grid(row=1, column=0)
        self.frame2.grid(row=1, column=1)
        self.frame3.grid(row=1, column=2)
        self.bottom_frame1.grid(row=2, column=0, columnspan=3)

        #frame 1 in tab1
        self.entry_1 = tk.Entry(self.frame1, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")
        self.entry_2 = tk.Entry(self.frame1, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")
        self.entry_3 = tk.Entry(self.frame1, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")
        self.entry_4 = tk.Entry(self.frame1, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")

        label_1 = tk.Label(self.frame1,text = "Ripple:",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")
        label_2 = tk.Label(self.frame1, text = "Order:", bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")
        label_3 = tk.Label(self.frame1, text = "C:",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")
        label_4 = tk.Label(self.frame1, text = "Cutoff Freq:",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")

        unitLabel_1 = tk.Label(self.frame1,text = "dB",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")
        unitLabel_2 = tk.Label(self.frame1, text = "F",
                                    bg = "white",fg = "black",font=("Arial", 9), 
                                    justify="center",padx=5, pady=5, borderwidth=2,
                                    relief="groove")
        unitLabel_3 = tk.Label(self.frame1, text = "Hz",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")

        self.button_1 = tk.Button(self.frame1, text="calculate LPF", 
                                        bg="blue", fg="white", font=("Arial", 9), 
                                        padx=5, pady=5, borderwidth=2, 
                                        relief="groove",command = self.button1_clicked)
        self.button_2 = tk.Button(self.frame1,text = "calculate HPF", 
                                        bg="red", fg="white", font=("Arial", 9), 
                                        padx=5, pady=5, borderwidth=2, 
                                        relief="groove",command = self.button2_clicked)

        #frame 2 in tab1
        self.entry_5 = tk.Entry(self.frame2, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")
        self.entry_6 = tk.Entry(self.frame2, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")
        self.entry_7 = tk.Entry(self.frame2, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")

        label_5 = tk.Label(self.frame2, text = "Order:", bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")
        label_6 = tk.Label(self.frame2, text = "C:",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")
        label_7 = tk.Label(self.frame2, text = "Cutoff Freq:",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")

        unitLabel_4 = tk.Label(self.frame2, text = "F",
                                    bg = "white",fg = "black",font=("Arial", 9), 
                                    justify="center",padx=5, pady=5, borderwidth=2,
                                    relief="groove")
        unitLabel_5 = tk.Label(self.frame2, text = "Hz",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")

        button_3 = tk.Button(self.frame2, text="calculate LPF", 
                                        bg="blue", fg="white", font=("Arial", 9), 
                                        padx=5, pady=5, borderwidth=2, 
                                        relief="groove",command = self.button3_clicked)
        button_4 = tk.Button(self.frame2,text = "calculate HPF", 
                                        bg="red", fg="white", font=("Arial", 9), 
                                        padx=5, pady=5, borderwidth=2, 
                                        relief="groove",command = self.button4_clicked)

        #frame 3 in tab1
        self.entry_8 = tk.Entry(self.frame3, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")
        self.entry_9 = tk.Entry(self.frame3, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")
        self.entry_10 = tk.Entry(self.frame3, bg="white", fg="black", 
                                    font=("Arial", 9), justify="center", 
                                    borderwidth=2, relief="groove", 
                                    insertwidth=2, insertbackground="black")

        label_8 = tk.Label(self.frame3, text = "Order:", bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")
        label_9 = tk.Label(self.frame3, text = "C:",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")
        label_l0 = tk.Label(self.frame3, text = "Cutoff Freq:",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")

        unitLabel_6 = tk.Label(self.frame3, text = "F",
                                    bg = "white",fg = "black",font=("Arial", 9), 
                                    justify="center",padx=5, pady=5, borderwidth=2,
                                    relief="groove")
        unitLabel_7 = tk.Label(self.frame3, text = "Hz",bg = "white",
                                    fg = "black",font=("Arial", 9), justify="center", 
                                    padx=5, pady=5, borderwidth=2,relief="groove")

        button_5 = tk.Button(self.frame3, text="calculate LPF", 
                                        bg="blue", fg="white", font=("Arial", 9), 
                                        padx=5, pady=5, borderwidth=2, 
                                        relief="groove",command = self.button5_clicked)
        button_6 = tk.Button(self.frame3,text = "calculate HPF", 
                                        bg="red", fg="white", font=("Arial", 9), 
                                        padx=5, pady=5, borderwidth=2, 
                                        relief="groove",command = self.button6_clicked)

        #putting the widgets in frame1
        self.entry_1.grid(row = 0,column = 1)
        self.entry_2.grid(row = 1,column = 1)
        self.entry_3.grid(row = 2, column = 1)
        self.entry_4.grid(row = 3, column = 1)

        label_1.grid(row = 0, column = 0)
        label_2.grid(row = 1, column = 0)
        label_3.grid(row = 2, column = 0)
        label_4.grid(row = 3, column = 0)

        unitLabel_1.grid(row = 0, column = 2)
        unitLabel_2.grid(row = 2, column = 2)
        unitLabel_3.grid(row = 3, column = 2)

        self.button_1.grid(row = 4, column = 0)
        self.button_2.grid(row = 4, column = 1)

        #putting widgets into frame 2
        self.entry_5.grid(row = 0,column = 1)
        self.entry_6.grid(row = 1, column = 1)
        self.entry_7.grid(row = 2, column = 1)

        label_5.grid(row = 0, column = 0)
        label_6.grid(row = 1, column = 0)
        label_7.grid(row = 2, column = 0)

        unitLabel_4.grid(row = 1, column = 2)
        unitLabel_5.grid(row = 2, column = 2)

        button_3.grid(row = 4, column = 0)
        button_4.grid(row = 4, column = 1)

        #putting widgets into frame 3
        self.entry_8.grid(row = 0,column = 1)
        self.entry_9.grid(row = 1,column = 1)
        self.entry_10.grid(row = 2, column = 1)
   
        label_8.grid(row = 0, column = 0)
        label_9.grid(row = 1, column = 0)
        label_l0.grid(row = 2, column = 0)
        
        unitLabel_6.grid(row = 0, column = 2)
        unitLabel_7.grid(row = 2, column = 2)
        
        button_5.grid(row = 4, column = 0)
        button_6.grid(row = 4, column = 1)

        #putting widgets in the bottom frame
        self.textBox = tk.Text(self.bottom_frame1, wrap='word')
        self.textBox.grid(row=0,column=0,columnspan=3)
        scrollbar = tk.Scrollbar(self.bottom_frame1, command = self.textBox.yview)
        scrollbar.grid(row=0, column=3, rowspan=3)
        # configure the Text widget to use the scrollbar
        self.textBox.configure(yscrollcommand=scrollbar.set)

    def order_Check(self,order):
        '''Checks for the correct order value inputs.

           If the order is incorrect an error message 

           pop up is generated. 
        ''' 
        if order.isdigit():
            order = int(order)
            if not (order >= 2 and order <= 10):
                error_message = f"""Invalid order: {order}. Orders range 
                from 2 - 10"""
                messagebox.showerror("Error", error_message )
    
    def ripple_Check(self,ripple,string):
        '''Checks for the correct ripple value inputs.

           If the ripple is incorrect an error message 

           pop up is generated. 
        ''' 
        if not(ripple == ".1" or ripple == "1"):
            error_message = f"""Invalid ripple: {ripple}. {string} ripple values 
            are .1dB or 1dB"""
            messagebox.showerror("Error", error_message )
   
    def button1_clicked(self):
        self.textBox.delete("1.0",tk.END) #clears the input window 
        ripple = self.entry_1.get()
        order = self.entry_2.get()
        cap =   self.entry_3.get()
        f_c =   self.entry_4.get()
        self.ripple_Check(ripple,"Chebyshev")
        self.order_Check(order)
        
        if ripple == '.1' and order == '2':
            obj = f.Chebyshev(.1,2)
            out = obj.krc2_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '3':
            obj = f.Chebyshev(.1,3)
            out = obj.krc3_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '4':
            obj = f.Chebyshev(.1,4)
            out = obj.krc4_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '5':
            obj = f.Chebyshev(.1,5)
            out = obj.krc5_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '6':
            obj = f.Chebyshev(.1,6)
            out = obj.krc6_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '7':
            obj = f.Chebyshev(.1,7)
            out = obj.krc7_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '8':
            obj = f.Chebyshev(.1,8)
            out = obj.krc8_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '9':
            obj = f.Chebyshev(.1,9)
            out = obj.krc9_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '10':
            obj = f.Chebyshev(.1,10)
            out = obj.krc10_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")

        #Ripple = 1 starts here
        if ripple == '1' and order == '2':
            obj = f.Chebyshev(.1,2)
            out = obj.krc2_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '3':
            obj = f.Chebyshev(.1,3)
            out = obj.krc3_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '4':
            obj = f.Chebyshev(.1,4)
            out = obj.krc4_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '5':
            obj = f.Chebyshev(.1,5)
            out = obj.krc5_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '6':
            obj = f.Chebyshev(.1,6)
            out = obj.krc6_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '7':
            obj = f.Chebyshev(.1,7)
            out = obj.krc7_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '8':
            obj = f.Chebyshev(.1,8)
            out = obj.krc8_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '9':
            obj = f.Chebyshev(.1,9)
            out = obj.krc9_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '10':
            obj = f.Chebyshev(.1,10)
            out = obj.krc10_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
    
    def button2_clicked(self):
        self.textBox.delete("1.0",tk.END) #clears the input window 
        ripple = self.entry_1.get()
        order = self.entry_2.get()
        cap =   self.entry_3.get()
        f_c =   self.entry_4.get()
        self.ripple_Check(ripple,"Chebyshev")
        self.order_Check(order)
        
        if ripple == '.1' and order == '2':
            obj = f.Chebyshev(.1,2)
            out = obj.krc2_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '3':
            obj = f.Chebyshev(.1,3)
            out = obj.krc3_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '4':
            obj = f.Chebyshev(.1,4)
            out = obj.krc4_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '5':
            obj = f.Chebyshev(.1,5)
            out = obj.krc5_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '6':
            obj = f.Chebyshev(.1,6)
            out = obj.krc6_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '7':
            obj = f.Chebyshev(.1,7)
            out = obj.krc7_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '8':
            obj = f.Chebyshev(.1,8)
            out = obj.krc8_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '9':
            obj = f.Chebyshev(.1,9)
            out = obj.krc9_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '.1' and order == '10':
            obj = f.Chebyshev(.1,10)
            out = obj.krc10_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")

        #Ripple = 1 starts here
        if ripple == '1' and order == '2':
            obj = f.Chebyshev(.1,2)
            out = obj.krc2_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '3':
            obj = f.Chebyshev(.1,3)
            out = obj.krc3_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '4':
            obj = f.Chebyshev(.1,4)
            out = obj.krc4_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '5':
            obj = f.Chebyshev(.1,5)
            out = obj.krc5_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '6':
            obj = f.Chebyshev(.1,6)
            out = obj.krc6_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '7':
            obj = f.Chebyshev(.1,7)
            out = obj.krc7_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '8':
            obj = f.Chebyshev(.1,8)
            out = obj.krc8_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '9':
            obj = f.Chebyshev(.1,9)
            out = obj.krc9_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if ripple == '1' and order == '10':
            obj = f.Chebyshev(.1,10)
            out = obj.krc10_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")

    def button3_clicked(self):
        self.textBox.delete("1.0",tk.END) #clears the input window 
        order = self.entry_5.get()
        cap =   self.entry_6.get()
        f_c =   self.entry_7.get()
        self.order_Check(order)
        
        if  order == '2':
            obj = f.Bessel(2)
            out = obj.krc2_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '3':
            obj = f.Bessel(3)
            out = obj.krc3_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '4':
            obj = f.Bessel(4)
            out = obj.krc4_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '5':
            obj = f.Bessel(5)
            out = obj.krc5_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '6':
            obj = f.Bessel(6)
            out = obj.krc6_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '7':
            obj = f.Bessel(7)
            out = obj.krc7_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '8':
            obj = f.Bessel(8)
            out = obj.krc8_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '9':
            obj = f.Bessel(9)
            out = obj.krc9_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '10':
            obj = f.Bessel(10)
            out = obj.krc10_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
    def button4_clicked(self):
        self.textBox.delete("1.0",tk.END) #clears the input window 
        order = self.entry_5.get()
        cap =   self.entry_6.get()
        f_c =   self.entry_7.get()
        self.order_Check(order)
        
        if  order == '2':
            obj = f.Bessel(2)
            out = obj.krc2_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '3':
            obj = f.Bessel(3)
            out = obj.krc3_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '4':
            obj = f.Bessel(4)
            out = obj.krc4_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '5':
            obj = f.Bessel(5)
            out = obj.krc5_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '6':
            obj = f.Bessel(6)
            out = obj.krc6_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '7':
            obj = f.Bessel(7)
            out = obj.krc7_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '8':
            obj = f.Bessel(8)
            out = obj.krc8_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '9':
            obj = f.Bessel(9)
            out = obj.krc9_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '10':
            obj = f.Bessel(10)
            out = obj.krc10_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")

    def button5_clicked(self):
        self.textBox.delete("1.0",tk.END) #clears the input window 
        order = self.entry_8.get()
        cap =   self.entry_9.get()
        f_c =   self.entry_10.get()
        self.order_Check(order)
        
        if  order == '2':
            obj = f.Buttersworth(2)
            out = obj.krc2_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '3':
            obj = f.Buttersworth(3)
            out = obj.krc3_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '4':
            obj = f.Buttersworth(4)
            out = obj.krc4_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '5':
            obj = f.Buttersworth(5)
            out = obj.krc5_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '6':
            obj = f.Buttersworth(6)
            out = obj.krc6_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '7':
            obj = f.Buttersworth(7)
            out = obj.krc7_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '8':
            obj = f.Buttersworth(8)
            out = obj.krc8_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '9':
            obj = f.Buttersworth(9)
            out = obj.krc9_LPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '10':
            obj = f.Buttersworth(10)
            out = obj.krc10_LPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
  
    def button6_clicked(self):
        self.textBox.delete("1.0",tk.END) #clears the input window 
        order = self.entry_8.get()
        cap =   self.entry_9.get()
        f_c =   self.entry_10.get()
        self.order_Check(order)
        
        if  order == '2':
            obj = f.Buttersworth(2)
            out = obj.krc2_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '3':
            obj = f.Buttersworth(3)
            out = obj.krc3_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '4':
            obj = f.Buttersworth(4)
            out = obj.krc4_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '5':
            obj = f.Buttersworth(5)
            out = obj.krc5_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if  order == '6':
            obj = f.Buttersworth(6)
            out = obj.krc6_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '7':
            obj = f.Buttersworth(7)
            out = obj.krc7_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '8':
            obj = f.Buttersworth(8)
            out = obj.krc8_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '9':
            obj = f.Buttersworth(9)
            out = obj.krc9_HPF(f_c,cap)
            for s in out[0]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
            for s in out[1]:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")
        
        if order == '10':
            obj = f.Buttersworth(10)
            out = obj.krc10_HPF(f_c,cap)
            for s in out:
                self.textBox.insert(tk.END,s)
                self.textBox.insert(tk.END,"\n")

if __name__ == "__main__":
    root = tk.Tk()
    iconPath = r"C:\Users\Owner\Desktop\EE436\Filter_Designer\my_icon.ico"
    my_gui = GUI_Driver(root,iconPath)
    root.mainloop()
