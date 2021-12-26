#modules for GUI
from tkinter import *
from tkinter import ttk
from tkinter import font
#modules for AES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
#modules for RSA
from getLargePrimes import generateLargePrime
from messagePreprocess import preprocess
from expMode import exp_mode
import time
from gcd import ext_gcd
import os

class Application(Frame):
    def __init__(self,master=None) -> None:
        Frame.__init__(self, master)
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Times New Roman', 22))
        self.style.configure('TButton', font=('Times New Roman', 18))
        self.style.configure('custom.TButton', font=('Times New Roman', 15))
        self.window_init()
        self.createWidgets()
        self.pack()
    
    def window_init(self):
        self.master.title('Welcome to Encryption Machine!')
        
        self.master.geometry("1300x750")

    def createWidgets(self):
        #frame 1 --title
        self.fm1 = Frame(self)
        self.titleLabel = ttk.Label(self.fm1, text="Encryption Machine",style='TLabel')
        
        self.titleLabel.pack(anchor='center')
        self.fm1.grid(row=0, column=0)

        #frame 2 -- primes display
        self.create_frame2()
        self.create_frame3()
        self.create_frame456()
        self.create_frame7()


    def create_frame2(self):
        prime_row = 6
        #frame 2 -- primes display
        self.fm2 = Frame(self)
        #title label for prime 1
        self.primeLabel1_desc = ttk.Label(self.fm2, text="p :  ", width=15,anchor='w',style='TLabel')
        self.primeLabel1_desc.grid(row=1, column=0, sticky='w')
        #value label
        self.prime1 = IntVar()        
        self.primeLabel1_val = Label(self.fm2, textvariable=self.prime1, width=100,height=7,wraplength=600)        
        self.primeLabel1_val.grid(row=1, column=1, sticky='w')

        #title label for prime 2
        self.primeLabel2_desc = ttk.Label(self.fm2, text="q :  ", width=15,anchor='w',style='TLabel')
        self.primeLabel2_desc.grid(row=prime_row, column=0, sticky='w')
        #value label
        self.prime2 = IntVar()
        self.primeLabel2_val = Label(self.fm2, textvariable=self.prime2, width=100,height=7,wraplength=600)
        self.primeLabel2_val.grid(row=prime_row, column=1, sticky='w')

        #choose two primes' length--- 512 and 1024
        prime_var = IntVar()
        primeChoice_col = 3
        self.label512 = ttk.Radiobutton(self.fm2, text="512 bits", variable=prime_var, value = 1,command=self.prime512,style='TButton')
        self.label1024 = ttk.Radiobutton(self.fm2, text="1024 bits", variable=prime_var, value = 2,command=self.prime1024,style='TButton')        
        self.label512.grid(row=1, column=primeChoice_col, sticky='w')
        self.label1024.grid(row=6, column=primeChoice_col, sticky='w')        
        self.fm2.grid(row=1,  sticky='w')    
        
    def create_frame3(self):
        prime_row = 6

        #frame 3 -- fi N shown
        self.fm3 = Frame(self)
        #title label
        self.nLabel_desc = ttk.Label(self.fm3, text="N (p * q) : ", width=15,anchor='w',style='TLabel')        
        self.nLabel_desc.grid(row= 2*prime_row+1, column=0, sticky='w')
        #value label        
        self.fiN = IntVar()
        #只需要展示n, fin就只是计算而已
        self.n = IntVar()       
        self.nLabel_val = Label(self.fm3, textvariable=self.n, width=100,height=7,wraplength=600)        
        self.nLabel_val.grid(row= 2*prime_row+1, column=1, sticky='e')       
        self.fm3.grid(row= 2*prime_row+1,  sticky='w')
    
    def create_frame456(self):
        prime_row = 6

        #frame 4 -- e shown/ Let e be a set prime 65537
        self.fm4 = Frame(self)
        #title label
        self.eLabel_desc = ttk.Label(self.fm4, text="Private Key e : ", width=15,anchor='w',style='TLabel')        
        self.eLabel_desc.grid(row= 3*prime_row+1, column=0, sticky='w')
        
        #value label                
        self.eLabel_val = Label(self.fm4, text="65537", width=100,height=3)       
        self.eLabel_val.grid(row= 3*prime_row+1, column=1, sticky='e')       
        self.fm4.grid(row=3*prime_row+1,  sticky='w')

        #frame 5 -- d shown
        self.fm5 = Frame(self)
        #title label
        self.dLabel_desc = ttk.Label(self.fm5, text="Public Key d : ", width=15,anchor='w',style='TLabel')        
        self.dLabel_desc.grid(row= 4*prime_row+1, column=0, sticky='w')
        
        #value label
        self.d = IntVar()        
        self.dLabel_val = Label(self.fm5, textvariable=self.d, width=100,height=7,wraplength=600)       
        self.dLabel_val.grid(row= 4*prime_row+1, column=1, sticky='e')       
        self.fm5.grid(row=4*prime_row+1,  sticky='w')

        #frame 6 -- RSA and AES buttons
        self.fm6 = Frame(self)
        self.AESLabel = ttk.Button(self.fm6, text="AES", command=self.run_AES, width=50,style='custom.TButton')
        self.RSALabel = ttk.Button(self.fm6, text="RSA", command=self.runRSA, width=50,style='custom.TButton')
        self.AESLabel.grid(row=5*prime_row+1, column=1, sticky='w',columnspan=3)
        self.RSALabel.grid(row=5*prime_row+1, column=4, sticky='w', columnspan=3)    
        self.fm6.grid(row=5*prime_row+1,  sticky='w')

    def create_frame7(self):
        prime_row = 6

        #frame 7 -- display a table
        self.fm7 = Frame(self)

        #variables to store processing time        
        self.R1,self.R2,self.R3 = IntVar(), IntVar(), IntVar()
        self.R4,self.R5,self.R6 = IntVar(), IntVar(), IntVar()
        self.A1,self.A2,self.A3 = IntVar(), IntVar(), IntVar()
        
        variableList = [self.R1,self.R2,self.R3,self.R4,self.R5,self.R6,self.A1,self.A2,self.A3]
        for k in range(len(variableList)):
            variableList[k].set(0)

        #form a table
        data = [("Length/thousand char","300","2100","6300"),("RSA-512/μs",self.R1.get(),self.R2.get(),self.R3.get()), 
        ("RSA-1024/μs",self.R4.get(),self.R5.get(),self.R6.get()),("AES/μs",self.A1.get(),self.A2.get(),self.A3.get())]
        area=("","Text1","Text2","Text3")
        ac=('all','m','c','e')
        self.tv=ttk.Treeview(self.fm7,columns=ac,show='headings',
                height=4)

        self.style.configure("Treeview.Heading", font=('Calibri', 22,'bold'))
        self.style.configure('Treeview',rowheight=35,font=('Arial',22))
        for i in range(4):
            self.tv.column(ac[i],width=290,anchor='center')
            self.tv.heading(ac[i],text=area[i])
        self.tv.grid(row=6*prime_row+3, column=0 ,sticky='w')

        for i in range(4):
            self.tv.insert('','end',values=data[i])
            
        self.fm7.grid(row=10*prime_row+2, column=0 ,sticky='w')


    def set_prime(self,length):
        self.prime1.set(generateLargePrime(length)) 
        self.prime2.set(generateLargePrime(length)) 

    def prime512(self):
        self.set_prime(256)
        self.n.set(self.prime1.get() * self.prime2.get())
        self.fiN.set((self.prime1.get() - 1) * (self.prime2.get() - 1))
        r,x,y = ext_gcd(65537,self.fiN.get())
        self.d.set(x)
        
    
    def prime1024(self):
        self.set_prime(512)
        self.n.set(self.prime1.get() * self.prime2.get())
        self.fiN.set((self.prime1.get() - 1) * (self.prime2.get() - 1))
        r,x,y = ext_gcd(65537,self.fiN.get())
        self.d.set(x)
        
    
    # def get_n(self, length):
    #     self.n.set(self.prime1.get() * self.prime2.get())
    #     self.fiN.set((self.prime1.get() - 1) * (self.prime2.get() - 1))
    #     r,x,y = ext_gcd(65537,self.fiN.get())
    #     while x <= 0:
    #         self.set_prime(length)
    #         r,x,y = ext_gcd(65537,self.fiN.get())
    #     self.d.set(x)


    def run_AES(self):
        
        '''
        AES的ECB模式加密方法
        :param key: 密钥
        :param data:被加密字符串（明文）
        :return:密文
        '''
        BLOCK_SIZE = 16  # Bytes
        
        key = "iEpSxImA0vpMUAab"
        key = key.encode('utf8')
        messages = self.read_files()
        times = [self.A1,self.A2,self.A3]
        
        #iterate three text files
        for i in range(3):
            #each message as a list in the outer list
            m = messages[i].encode('utf8') #get byte string
            
            #time record starts
            startTime = time.time()
            print(startTime)
            #preprocess the message by padding
            data = pad(m,BLOCK_SIZE)
            cipher = AES.new(key, AES.MODE_ECB)
            result = cipher.encrypt(data)
            
            #time record ends
            endTime = time.time()
            print(endTime)
            interval = float(endTime - startTime) * 1000000            
            times[i].set(interval)
            
        
        #update the time value
        self.tv.item('I004',values=('AES/μs',self.A1.get(),self.A2.get(),self.A3.get()))

    def runRSA(self):
        #identify digits of keys first and then decide which function to call
        #digits generated are not stable as 155
        if len(str(self.d.get())) < 200:
            self.rsaAlgo512()
        else:
            self.rsaAlgo1024()

        print(len(str(self.d.get())))

    def rsaAlgo512(self):
        times = [self.R1,self.R2,self.R3]
        location = 'I002'
        title = '512'
        self.rsaAlgo(times,location,title)

    def rsaAlgo1024(self):
        times = [self.R4,self.R5,self.R6]
        location = 'I003'
        title = '1024'
        self.rsaAlgo(times,location,title)

    def rsaAlgo(self,times,location,title):
        #only do encryption here
        messages = self.read_files()
                
        #iterate three text files
        for i in range(3):
            #each message as a list in the outer list
            m = messages[i]
            print(len(m))
            #processed is a list of truncated messages converted into numbers
            nLength = len(str(self.n.get()))
            processed = preprocess(m, nLength)
            
            #iterate all messages
            startTime = time.time()
            
            for j in range(len(processed)):
                connectedStr = "".join(processed[j])            
                exp_mode(int(connectedStr), 63357, self.n.get())
                
            endTime = time.time()
            
            interval = float(endTime - startTime) * 1000000
            #print("------")
            #print(interval)            
            times[i].set(interval)
            # print(times[i].get())

        # for i in times:
        #     print(i.get())

        #update the time value
        rowTitle = 'RSA-' + title +'/μs'
        self.tv.item(location,values=(rowTitle,times[0].get(),times[1].get(),times[2].get()))
            

    def read_files(self):
        #read text file
        messages = []
        for i in range(1,4):
            #find the absolute path for current directory
            #text files are in the same
            path = [os.path.dirname(os.path.realpath(__file__)),'\\','text',str(i),'.txt']
            
            filename = ''.join(path)
            with open(filename, errors='ignore') as f:
                #readlines provide list
                messages.append("".join(f.readlines()))

        
        return messages



if __name__=='__main__':
    app = Application()
    app.mainloop()
