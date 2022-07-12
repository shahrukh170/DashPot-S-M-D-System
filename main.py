#!/usr/bin/python3
# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
#http://python-control.sourceforge.net/manual/creation.html
#https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.signal.StateSpace.html
#sys: Lti (StateSpace, or TransferFunction)
#https://stackoverflow.com/questions/16114971/scipy-step-response-plot-seems-to-break-for-some-values
from numpy import min
from scipy import linspace
from scipy.linalg import solve
from matplotlib import pyplot as p
from scipy.signal import lti, step2,step
from scipy import signal
from scipy.signal.ltisys import TransferFunction as ss2tf

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.pyplot as plt2
import matplotlib.pyplot
matplotlib.use("TkAgg")
from matplotlib import style
style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plot
from scipy.integrate import odeint
import math
import itertools
import sys
import matplotlib.pylab as pylab
from pylab import cos, pi, arange, sqrt, pi, array

try:
   from tkinter import *
   import tkinter as tk
   import tkinter as ttk
except ImportError:
    import Tkinter as ttk
    
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
    
import tkinter as tk
from tkinter import ttk

import matplotlib as mpl 
  
LARGE_FONT= ("Verdana", 12)
f = Figure(figsize=(3,2.1), dpi=100)
FigSubPlot = f.add_subplot(111)
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Sea of BTC client")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        self.logo = tk.Label(self, text="Logo", background="orange")
        self.buttons = []
        self.buttonsX = []
        self.var = DoubleVar()
        self.msg = StringVar()

        #start time = initial Time  =iTime
        #end time = final Time  =Time
        self.iTime = 0.0 
        self.Time = 10.0
        
        self.SingleBump = 0
        self.Velocity=5.0
        
        self.Mass1 = 400.0
        self.Stiffness1 = 20000.0
        self.Damper1 = 2000.0
        
        self.Mass2 = 30.0
        self.Stiffness2 = 80000.0
        self.Damper2 = 1.0
      
        
        self.BumpHeight = 0.01 #ft
        self.BumpFrequency=1.0  #hertz 
        self.BumpPitch=1 #ft
        self.BumpTimePeriod = 0.1 #secs

        self.Cc1 = 0.0
        self.Cc2 = 0.0
       
        self.Zeta1=0.0
        self.wn1=0.0
        self.f1=0.0
        self.r1=0.0

        self.Zeta2=0.0
        self.wn2=0.0
        self.f2=0.0
        self.r2=0.0


        #Initial Conditions  
        #self.i0=np.empty(4)
        self.i0 = [0.0, 1.2,0.0,1.2]  #initial conditions [x01 , v01 ,x02 ,v02]   [m, m/sec]
        
        self.iTime = 0.0  # initial time
        self.Time = 10.0  # final time
        step = 0.001  # step
        self.t = arange(self.iTime,self.Time, step)

        #time points
        self.t=np.linspace(self.iTime,self.Time)
                
        fields = ('1/4 Mass Of Car', 'Mass Wheel', 'Stiffness K1', 'Tyre Stiffness K2', 'Damping C1', 'Tyre Damping C2')
         
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        #ents = self.makeform( fields)
        #self.bind('<Return>', (lambda event, e=ents: fetch(e)))
        row = Frame(self)

        lab = Label(row, width=22, text="1/4 Mass Of Car:[Kgm]", anchor='w')
        ent = Tk.Scale(row, from_=50.0, to=1000.0,showvalue=True,resolution=1,sliderlength=12, orient='horizontal',command=self.MyPlot)
        row.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row, width=22, text="Damping ,C1:[N-Sec/m]", anchor='w')
        ent = Tk.Scale(row, from_=1000.0, to=10000.0,showvalue=True,resolution=10,sliderlength=12, orient='horizontal',command=self.MyPlotX2)
        row.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row, width=22, text="Stiffness Sping ,K1:[N/m] ", anchor='w')
        ent = Tk.Scale(row, from_=10000, to=200000,showvalue=True,resolution=1000,sliderlength=12, orient='horizontal',command=self.MyPlotX3)
        row.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)
        
        lab = Label(row, width=22, text="Time:[Secs] ", anchor='w')
        ent = Tk.Scale(row, from_=5.5, to=10.0,showvalue=True ,resolution=0.05,sliderlength=12 ,orient='horizontal',command=self.MyPlotX4)
        row.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, fill=Y)
        
        row2 = Frame(self)

        lab = Label(row2, width=22, text="Mass Of Tyre:[Kgm] ", anchor='w')
        ent = Tk.Scale(row2, from_=5.0, to=100.0,showvalue=True ,resolution=5,sliderlength=12, orient='horizontal',command=self.MyPlotX5)
        row2.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row2, width=22, text="Damping C2,[N-sec/m]: ", anchor='w')
        ent = Tk.Scale(row2, from_=0, to=10000,showvalue=True ,resolution=10,sliderlength=12, orient='horizontal',command=self.MyPlotX6)
        row2.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row2, width=22, text="Tyre Stiffness:[N/m] ", anchor='w')
        ent = Tk.Scale(row2, from_=10000, to=150000,showvalue=True,resolution=1000,sliderlength=12, orient='horizontal',command=self.MyPlotX7)
        row2.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)
        
        lab = Label(row2, width=22, text="Bump Time Period [secs]", anchor='w')
        ent = Tk.Scale(row2, orient='horizontal', from_=1, 
                  to=0.1, showvalue=True, resolution=0.25,  sliderlength=12,command=self.MyPlotX8)
        row2.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, fill=Y)

        row3 = Frame(self)

        lab = Label(row3, width=22, text="Car Velocity:[Miles/Hr] ", anchor='w')
        ent = Tk.Scale(row3, from_=1.0, to=100.0,showvalue=True,resolution=10,sliderlength=12, orient='horizontal',command=self.MyPlotX9)
        row3.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row3, width=22, text="Bump Pitch :[ft] ", anchor='w')
        ent = Tk.Scale(row3, from_=1.0, to=30.0,showvalue=True,tickinterval=0.1 ,resolution=0.5,sliderlength=12, orient='horizontal',command=self.MyPlotX10)
        row3.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row3, width=22, text=" Height:[ft] ", anchor='w')
        ent = Tk.Scale(row3,orient='horizontal', tickinterval=0.01, from_=0.01, 
                  to=2.0, showvalue=True, resolution=0.01,  sliderlength=12,command=self.MyPlotX11)
        row3.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)
        
        lab = Label(row3, width=22, text="Frequency:[Hz]", anchor='w')
        ent = Tk.Scale(row3, from_=0.05, to=3,showvalue=True,tickinterval=1 ,resolution=0.5,sliderlength=12, orient='horizontal',command=self.MyPlotX12)
        row3.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, fill=Y)
        
        #scale = Tk.Scale(self, from_=0, to=100, orient='horizontal',command=lambda x:self.MyPlot(scale.get()))
        #scale.pack(side=Tk.TOP)
        #scale = Tk.Scale(self, from_=0, to=100, orient='horizontal',command=lambda x:self.MyPlot(scale.get()))
        #scale.pack(side=Tk.RIGHT)
        
        #f = Figure(figsize=(5,5), dpi=100)
        #self.FigSubPlot = f.add_subplot(111)
        FigSubPlot.clear()
                
        #state = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        #q=self.euler(self.AnalyseRidePerfromance,self.i0,self.t,10)
        #print(state[:],[0]) 
        #x = np.array(self.t)
        y= []
        z = []
        #y=state[:][0][0]
        #z=np.asarray(state[:,2])
        #self.refreshFigure(t,x)
    
        #z = z.append(q[:][1])
        #self.FigSubPlot.scatter(x,y,color='red')
        #self.line1 = self.FigSubPlot.plot(x,y,'r-',linewidth=3)
        #self.line2 = self.FigSubPlot.plot(x,z,'b-',linewidth=3)
        
        #a.invert_yaxis()

        FigSubPlot.set_title ("Estimation Grid", fontsize=16)
        FigSubPlot.set_ylabel("Y", fontsize=14)
        FigSubPlot.set_xlabel("X", fontsize=14)

       
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.update_idletasks()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
 
        return

    def euler(self,f,x0,tx,h):
        t,y = 0,0
        while t <= range(0,10,1):
           print( "%6.3f %6.3f" % (t,y))
           t += h
           y += h * f(x0[t],tx[t])
        return [t,y] 
		
    def refreshFigure(self,t3,y3,t4,y4,t,u):
        FigSubPlot.clear()

        FigSubPlot.legend(['y1'],loc='best')
        FigSubPlot.legend(['y2'],loc='best')
        #p.subplot(4,1,3)
        self.line1=FigSubPlot.plot(t3,y3,'k-',linewidth=2)
        self.line2=FigSubPlot.plot(t4,y4,'b-',linewidth=2)
        FigSubPlot.plot(t,u,'r-')
        #self.FigSubPlot.ylabel('Problem 3')
        FigSubPlot.legend(['y1-Sprung Mass','y2-UnSprung Mass','u-Input'],loc='best')
        #self.FigSubPlot.xlabel('Time')
        #self.line1.set_xdata(t)
        #self.line1.set_ydata(y3)
        self.canvas.draw()
        self.toolbar.update()
        print("Zeta1:",self.Zeta1)
        print("wn1:",self.wn1)
        print("f1:",self.f1)
        print("r1:",self.r1)

        print("Zeta2:",self.Zeta2)
        print("wn2:",self.wn2)
        print("f2:",self.f2)
        print("r2:",self.r2)
        
    
    def MyPlot(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Mass1 = self.var.get()
        print(self.Mass1)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return
      
    def MyPlotX2(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Damper1 = self.var.get()
        print(self.Damper1)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return
      
    def MyPlotX3(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Stiffness1 = self.var.get()
        print(self.Stiffness1)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return

    def MyPlotX4(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Time = self.var.get()
        print(self.Time)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return

    def MyPlotX5(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Mass2 = self.var.get()
        print(self.Mass2)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return

    def MyPlotX6(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Damper2 = self.var.get()
        print(self.Damper2)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return

    def MyPlotX7(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Stiffness2 = self.var.get()
        print(self.Stiffness2)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return

    def MyPlotX8(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.BumpTimePeriod = self.var.get()
        print(self.BumpTimePeriod)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return
      
    def MyPlotX9(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Velocity= self.var.get()
        print(self.Velocity)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return
      
    def MyPlotX10(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.BumpPitch= self.var.get()
        print(self.BumpPitch)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return

    def MyPlotX11(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.BumpHeight= self.var.get()
        print(self.BumpHeight)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = self.AnalyseRidePerfromance(self.i0,t)
        t3=np.array(q[0])
        y3=np.array(q[1])
        
        t4=np.array(q[2])
        y4=np.array(q[3])

        t=np.array(q[4])
        u=np.array(q[5])

        
        self.refreshFigure(t3,y3,t4,y4,t,u)
        return

    def MyPlotX12(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.BumpFrequency= self.var.get()
        print(self.BumpFrequency)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        step=0.05
        t =array(arange(self.iTime,self.Time,step))
        q = self.AnalyseRidePerfromance(self.i0,t)
        x=t
        y=np.array(q[1])
        z=np.array(q[2])
        self.refreshFigure(x,y,z)
        return

    def ConvertDegrees(self,Angle):
        #180 Degrees = Pi Radians
        return ((180/np.pi)*Angle)

    def  AnalyseRidePerfromance(self,x,tx):
        m1 = self.Mass1      #Kgm -Sprung Mass
        m2 = self.Mass2      #Kgm - UnSprung Mass   
        b1 = self.Damper1    #N-sec/m - shock Damper
        b2 = self.Damper2    #N-sec/m  - tyre Damper 
        k1 = self.Stiffness1 #N/m   - Spring Damper   
        k2 = self.Stiffness2 #N/m   - Tyre Stiffness

        a1 = 1.0
        a2 = ((m1*(b1+b2))+(b1*m2))/(m1*m2)
        a3 = ((m1*(k1+k2)) - ( b1 ** 2 ) + (b1*(b1+b2)) + (k1*m2))/(m1*m2)
        a4= ((b1*(k1+k2)) - (2*k1*b1) + (k1*(b1+b2)))/(m1*m2)
        a5= ((k1*(k1+k2))-(k1 ** 2))/(m1*m2)

        u=k1/(m1*m2)

        #Road Surface Period[Length or pitch Of Bump] = P = 15m
        P=self.BumpPitch #20.20     #ft or 15 m
        #print("Road Surface Period",P,"ft (15 m)")

        #REQUIRED :
        #		Steady State motion Amplitude X(t) = ?
        #		Force Transmitted To The Chasis  F(t) = ?
        #SOLUTION :
        #w = 50 [ mi / hr ] x [ 5280 ft / 1 mile ] x [ 1 cycle / 20 ft ] x [2 .Pi rad / 1 cycle ]  x [ 1hr /3600 ]
        w=self.Velocity*5280*(1/P)*(2*math.pi)*(1/3600)
        #print("Forced Vibration Frequency",w,"rad/sec")


        #Critical Damping Co efficient
        #Critical Damping Co efficient
        self.Cc1 = 0.0
        self.Cc2 = 0.0
        self.Cc1 = (2.0 * ( ( self.Stiffness1/self.Mass1)**0.5 ) * self.Mass1)
        self.Cc2 = (2.0 * ( math.sqrt( self.Stiffness2/self.Mass2) ) * self.Mass2)

        self.Zeta1=self.Damper1/self.Cc1  
        #print("Zeta1 : ",self.Zeta1)
       
        #wn = Natural Frequency Of System = sqrt( k / m ) = sqrt( 2.9 x 10 E4 /362.5) = 8.94 rad/sec
        self.wn1= math.sqrt(self.Stiffness1/self.Mass1)
        #print("Wn1" , self.wn1)

        #Frequency f1
        self.f1 = (self.wn1/(2*math.pi))    #Herta [bump frequency ]
        #print("Frequency ,f1:",self.f1)
       
        #Frequency Ratio ,r = w /wn = 23.04 / 8.94 = 2.58
        self.r1= w/self.wn1
        #print("Frequency Ratio ,r1 :  ", self.r1)

        if(self.Damper2 <= 1 ):
           self.Zeta2 = 0.0
        else:
          
           self.Zeta2= float(self.Damper2)/self.Cc2
          
        #print("Zeta2 : ",self.Zeta2)

        #wn = Natural Frequency Of System = sqrt( k / m ) = sqrt( 2.9 x 10 E4 /362.5) = 8.94 rad/sec
        self.wn2= math.sqrt(self.Stiffness2/self.Mass2)
        #print("Wn1" , self.wn2)

        #Frequency f1
        self.f2 = (self.wn2/(2*math.pi))    #Herta [bump frequency ]
        #print("Frequency ,f2:",self.f2)
       
        #Frequency Ratio ,r = w /wn = 23.04 / 8.94 = 2.58
        self.r2= w/self.wn2
        #print("Frequency Ratio ,r2 :  ", self.r2)

       
       
        #Road Profile 1st[5 cm jump ]
        z0=self.BumpHeight #5.0/100
       
        #Road Profile = U(t) = 0.03 ft . ( 1 / 3.28 ft) = 0.0009 m
        Utx=z0 * ( 1 / 3.28 )
        omega = self.ConvertDegrees(w)
        #Bump Time Period = T = 2 x Pi / w
        #if(self.BumpTimePeriod == 0):
        #   self.BumpTimePeriod = ((2*math.pi)/w)    #sec [bump time ]
      
        #print(Utx)
        if(omega > 90):
            omega = np.abs(1 - (omega/360))*360
            if(omega > 90):
                omega =omega - 90
        #print(omega)
        r=z0*np.sin(omega * self.BumpTimePeriod)
        #Road Profile 2ndt
        #r=0.80
       
        # problem 3
        A = [[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0],[-a5,-a4,-a3,-a2]]
        print(np.linalg.eig(A)[0])
        B = [[0.0],[0.0],[0.0],[1.0]]
        C = [k1,b1,0.0,0.0]
        D = [0.0]
        print(D)
        sys3 = signal.StateSpace(A,B,C,D)
        step=0.001
        t = np.arange(self.iTime,self.Time,step)
        u = np.zeros(len(t))
        u[5:50] = 1.0 # first step input
        u[50:] = 2.0  # second step input
        t3,y3,x3 = signal.lsim(sys3,u,t)

         
        # problem 3
        A = [[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0],[-a5,-a4,-a3,-a2]]
        print(np.linalg.eig(A)[0])
        B = [[0.0],[0.0],[0.0],[1.0]]
        C = [k1,b1,m1,0.0]
        D = [0.0]
        print(D)
        sys3 = signal.StateSpace(A,B,C,D)
        step=0.001
        t = np.arange(0.0,10.0,step)
        u = np.zeros(len(t))
        u[5:50] = 1.0 # first step input
        u[50:] = 2.0  # second step input
        t4,y4,x4 = signal.lsim(sys3,u,t)

        return [t3,y3,t4,y4,t,u]
        

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.logo = tk.Label(self, text="Logo", background="orange")
        self.buttons = []
        self.buttonsX = []
        self.var = DoubleVar()
        self.msg = StringVar()

        #start time = initial Time  =iTime
        #end time = final Time  =Time
        self.iTime = 0.0 
        self.Time = 10.0
        
        self.SingleBump = 0
        self.Velocity=5.0
        
        self.Mass1 = 400.0
        self.Stiffness1 = 20000.0
        self.Damper1 = 2000.0
        
        self.Mass2 = 30.0
        self.Stiffness2 = 80000.0
        self.Damper2 = 1.0
      
        
        self.BumpHeight = 0.01 #ft
        self.BumpFrequency=1.0  #hertz 
        self.BumpPitch=1 #ft
        self.BumpTimePeriod = 0.1 #secs

        self.Cc1 = 0.0
        self.Cc2 = 0.0
       
        self.Zeta1=0.0
        self.wn1=0.0
        self.f1=0.0
        self.r1=0.0

        self.Zeta2=0.0
        self.wn2=0.0
        self.f2=0.0
        self.r2=0.0


        #Initial Conditions  
        #self.i0=np.empty(4)
        self.i0 = [0.0, 1.2,0.0,1.2]  #initial conditions [x01 , v01 ,x02 ,v02]   [m, m/sec]
        
        self.iTime = 0.0  # initial time
        self.Time = 10.0  # final time
        step = 0.001  # step
        self.t = arange(self.iTime,self.Time, step)

        #time points
        self.t=np.linspace(self.iTime,self.Time)
                
        fields = ('1/4 Mass Of Car', 'Mass Wheel', 'Stiffness K1', 'Tyre Stiffness K2', 'Damping C1', 'Tyre Damping C2')
         
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        #ents = self.makeform( fields)
        #self.bind('<Return>', (lambda event, e=ents: fetch(e)))
        row = Frame(self)

        lab = Label(row, width=22, text="1/4 Mass Of Car:[Kgm]", anchor='w')
        ent = Tk.Scale(row, from_=50.0, to=1000.0,showvalue=True,resolution=1,sliderlength=12, orient='horizontal',command=self.MyPlot)
        row.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row, width=22, text="Damping ,C1:[N-Sec/m]", anchor='w')
        ent = Tk.Scale(row, from_=1000.0, to=10000.0,showvalue=True,resolution=10,sliderlength=12, orient='horizontal',command=self.MyPlotX2)
        row.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row, width=22, text="Stiffness Sping ,K1:[N/m] ", anchor='w')
        ent = Tk.Scale(row, from_=10000, to=200000,showvalue=True,resolution=1000,sliderlength=12, orient='horizontal',command=self.MyPlotX3)
        row.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)
        
        lab = Label(row, width=22, text="Time:[Secs] ", anchor='w')
        ent = Tk.Scale(row, from_=5.5, to=10.0,showvalue=True ,resolution=0.05,sliderlength=12 ,orient='horizontal',command=self.MyPlotX4)
        row.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, fill=Y)
        
        row2 = Frame(self)

        lab = Label(row2, width=22, text="Mass Of Tyre:[Kgm] ", anchor='w')
        ent = Tk.Scale(row2, from_=5.0, to=100.0,showvalue=True ,resolution=5,sliderlength=12, orient='horizontal',command=self.MyPlotX5)
        row2.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row2, width=22, text="Damping C2,[N-sec/m]: ", anchor='w')
        ent = Tk.Scale(row2, from_=0, to=10000,showvalue=True ,resolution=10,sliderlength=12, orient='horizontal',command=self.MyPlotX6)
        row2.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row2, width=22, text="Tyre Stiffness:[N/m] ", anchor='w')
        ent = Tk.Scale(row2, from_=10000, to=150000,showvalue=True,resolution=1000,sliderlength=12, orient='horizontal',command=self.MyPlotX7)
        row2.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)
        
        lab = Label(row2, width=22, text="Bump Time Period [secs]", anchor='w')
        ent = Tk.Scale(row2, orient='horizontal', from_=1, 
                  to=0.1, showvalue=True, resolution=0.25,  sliderlength=12,command=self.MyPlotX8)
        row2.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, fill=Y)

        row3 = Frame(self)

        lab = Label(row3, width=22, text="Car Velocity:[Miles/Hr] ", anchor='w')
        ent = Tk.Scale(row3, from_=1.0, to=100.0,showvalue=True,resolution=10,sliderlength=12, orient='horizontal',command=self.MyPlotX9)
        row3.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row3, width=22, text="Bump Pitch :[ft] ", anchor='w')
        ent = Tk.Scale(row3, from_=1.0, to=30.0,showvalue=True,tickinterval=0.1 ,resolution=0.5,sliderlength=12, orient='horizontal',command=self.MyPlotX10)
        row3.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)

        lab = Label(row3, width=22, text=" Height:[ft] ", anchor='w')
        ent = Tk.Scale(row3,orient='horizontal', tickinterval=0.01, from_=0.01, 
                  to=2.0, showvalue=True, resolution=0.01,  sliderlength=12,command=self.MyPlotX11)
        row3.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=Y)
        
        lab = Label(row3, width=22, text="Frequency:[Hz]", anchor='w')
        ent = Tk.Scale(row3, from_=0.05, to=3,showvalue=True,tickinterval=1 ,resolution=0.5,sliderlength=12, orient='horizontal',command=self.MyPlotX12)
        row3.pack(side=TOP, fill=Y, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, fill=Y)
        
        #scale = Tk.Scale(self, from_=0, to=100, orient='horizontal',command=lambda x:self.MyPlot(scale.get()))
        #scale.pack(side=Tk.TOP)
        #scale = Tk.Scale(self, from_=0, to=100, orient='horizontal',command=lambda x:self.MyPlot(scale.get()))
        #scale.pack(side=Tk.RIGHT)
        
        #f = Figure(figsize=(5,5), dpi=100)
        #FigSubPlot = f.add_subplot(111)
        FigSubPlot.clear()
                
        #state = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        #q=self.euler(self.AnalyseRidePerfromance,self.i0,self.t,10)
        #print(state[:],[0]) 
        #x = np.array(self.t)
        y= []
        z = []
        #y=state[:][0][0]
        #z=np.asarray(state[:,2])
        #self.refreshFigure(t,x)
    
        #z = z.append(q[:][1])
        #self.FigSubPlot.scatter(x,y,color='red')
        #self.line1 = self.FigSubPlot.plot(x,y,'r-',linewidth=3)
        #self.line2 = self.FigSubPlot.plot(x,z,'b-',linewidth=3)
        
        #a.invert_yaxis()

        FigSubPlot.set_title ("Estimation Grid", fontsize=16)
        FigSubPlot.set_ylabel("Y", fontsize=14)
        FigSubPlot.set_xlabel("X", fontsize=14)

       
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.update_idletasks()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
 
        return

    def euler(self,f,x0,tx,h):
        t,y = 0,0
        while t <= range(0,10,1):
           print( "%6.3f %6.3f" % (t,y))
           t += h
           y += h * f(x0[t],tx[t])
        return [t,y] 
		
    def refreshFigure(self,t,x,y):
        FigSubPlot.clear()
        #self.line1 = self.FigSubPlot.plot(x,y,'r-',linewidth=3)
        #self.line1=self.FigSubPlot.plot(x,y,'r-',linewidth=3)[0]
        self.line1=FigSubPlot.plot(t,x,'b--',linewidth=2,label='sprung M Travel')[0]
        self.line2=FigSubPlot.plot(t,y,'r-',linewidth=2,label='Unsprung M Travel')[0]
        #self.FigSubPlot.xlabel('time')
        #self.FigSubPlot.ylabel('travel')
        FigSubPlot.legend()
        #self.FigSubPlot.show()
        self.line1.set_xdata(t)
        #self.line1.set_xdata(x)
        self.line1.set_ydata(x)
        self.canvas.draw()
        self.toolbar.update()
        print("Zeta1:",self.Zeta1)
        print("wn1:",self.wn1)
        print("f1:",self.f1)
        print("r1:",self.r1)

        print("Zeta2:",self.Zeta2)
        print("wn2:",self.wn2)
        print("f2:",self.f2)
        print("r2:",self.r2)
        
    
    def MyPlot(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Mass1 = self.var.get()
        print(self.Mass1)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
               
        self.refreshFigure(x,y,z)
        return
      
    def MyPlotX2(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Damper1 = self.var.get()
        print(self.Damper1)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return
      
    def MyPlotX3(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Stiffness1 = self.var.get()
        print(self.Stiffness1)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return

    def MyPlotX4(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Time = self.var.get()
        print(self.Time)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return

    def MyPlotX5(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Mass2 = self.var.get()
        print(self.Mass2)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return

    def MyPlotX6(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Damper2 = self.var.get()
        print(self.Damper2)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return

    def MyPlotX7(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Stiffness2 = self.var.get()
        print(self.Stiffness2)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return

    def MyPlotX8(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.BumpTimePeriod = self.var.get()
        print(self.BumpTimePeriod)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
                   
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return
      
    def MyPlotX9(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.Velocity= self.var.get()
        print(self.Velocity)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return
      
    def MyPlotX10(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.BumpPitch= self.var.get()
        print(self.BumpPitch)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return

    def MyPlotX11(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.BumpHeight= self.var.get()
        print(self.BumpHeight)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        t=np.linspace(0.0,self.Time)
        q = odeint(self.AnalyseRidePerfromance,self.i0,self.t,full_output=0)
        x=self.t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return

    def MyPlotX12(self,X):
        x =[]
        y = []
        self.var.set(X)
        self.BumpFrequency= self.var.get()
        print(self.BumpFrequency)
        FigSubPlot.clear()
        # file is opened here and some data is taken
        # I've just set some arrays here so it will compile alone
        #initial Conditions
        

        #time points
        step=0.05
        t =array(arange(self.iTime,self.Time,step))
        q = odeint(self.AnalyseRidePerfromance_X2,self.i0,t,full_output=0)
        x=t
        y=np.array(q[:,0])
        z=np.array(q[:,2])
        self.refreshFigure(x,y,z)
        return
      
    def ConvertDegrees(self,Angle):
        #180 Degrees = Pi Radians
        return ((180/np.pi)*Angle)

    def AnalyseRidePerfromance(self,x,t):

       #Road Surface Period[Length or pitch Of Bump] = P = 15m
       P=self.BumpPitch #20.20     #ft or 15 m
       #print("Road Surface Period",P,"ft (15 m)")

       #REQUIRED :
       #		Steady State motion Amplitude X(t) = ?
       #		Force Transmitted To The Chasis  F(t) = ?
       #SOLUTION :
       #w = 50 [ mi / hr ] x [ 5280 ft / 1 mile ] x [ 1 cycle / 20 ft ] x [2 .Pi rad / 1 cycle ]  x [ 1hr /3600 ]
       w=self.Velocity*5280*(1/P)*(2*math.pi)*(1/3600)
       #print("Forced Vibration Frequency",w,"rad/sec")


       #Critical Damping Co efficient
       #Critical Damping Co efficient
       self.Cc1 = 0.0
       self.Cc2 = 0.0
       self.Cc1 = (2.0 * ( ( self.Stiffness1/self.Mass1)**0.5 ) * self.Mass1)
       self.Cc2 = (2.0 * ( math.sqrt( self.Stiffness2/self.Mass2) ) * self.Mass2)

       self.Zeta1=self.Damper1/self.Cc1  
       #print("Zeta1 : ",self.Zeta1)
       
       #wn = Natural Frequency Of System = sqrt( k / m ) = sqrt( 2.9 x 10 E4 /362.5) = 8.94 rad/sec
       self.wn1= math.sqrt(self.Stiffness1/self.Mass1)
       #print("Wn1" , self.wn1)

       #Frequency f1
       self.f1 = (self.wn1/(2*math.pi))    #Herta [bump frequency ]
       #print("Frequency ,f1:",self.f1)
       
       #Frequency Ratio ,r = w /wn = 23.04 / 8.94 = 2.58
       self.r1= w/self.wn1
       #print("Frequency Ratio ,r1 :  ", self.r1)

       if(self.Damper2 <= 1 ):
          self.Zeta2 = 0.0
       else:
          
          self.Zeta2= float(self.Damper2)/self.Cc2
          
       #print("Zeta2 : ",self.Zeta2)

       #wn = Natural Frequency Of System = sqrt( k / m ) = sqrt( 2.9 x 10 E4 /362.5) = 8.94 rad/sec
       self.wn2= math.sqrt(self.Stiffness2/self.Mass2)
       #print("Wn1" , self.wn2)

       #Frequency f1
       self.f2 = (self.wn2/(2*math.pi))    #Herta [bump frequency ]
       #print("Frequency ,f2:",self.f2)
       
       #Frequency Ratio ,r = w /wn = 23.04 / 8.94 = 2.58
       self.r2= w/self.wn2
       #print("Frequency Ratio ,r2 :  ", self.r2)

       
       
       #Road Profile 1st[5 cm jump ]
       z0=self.BumpHeight #5.0/100
       
       #Road Profile = U(t) = 0.03 ft . ( 1 / 3.28 ft) = 0.0009 m
       Utx=z0 * ( 1 / 3.28 )
       omega = self.ConvertDegrees(w)
       #Bump Time Period = T = 2 x Pi / w
       #if(self.BumpTimePeriod == 0):
       #   self.BumpTimePeriod = ((2*math.pi)/w)    #sec [bump time ]
      
       #print(Utx)
       if(omega > 90):
           omega = np.abs(1 - (omega/360))*360
           if(omega > 90):
               omega =omega - 90
       #print(omega)
       r=z0*np.sin(omega * self.BumpTimePeriod)
       #Road Profile 2ndt
       #r=0.80

       #state variables defined as
       q1,q2,q3,q4=x
       

       #q1 is my sprung mass body travel
       #q2 is my sprung mass body velocity
       #q2dot is my sprung mass body acceleration

       #q3 is my unsprung mass body travel
       #q4 is my unsprung mass body velocity
       #q4dot is my unsprung mass body acceleration


       #state variables defined as
       q1,q2,q3,q4=x
    

       #q1 is my sprung mass body travel
       #q2 is my sprung mass body velocity
       #q2dot is my sprung mass body acceleration

       #q3 is my unsprung mass body travel
       #q4 is my unsprung mass body velocity
       #q4dot is my unsprung mass body acceleration


       #4 first order differential equations for the system
       q1dot = q2
       q2dot= -((self.Stiffness1/self.Mass1)*(q1-q3))- (( self.Damper1 /self.Mass1)* (q2-q4))
    
       q3dot = q4
       q4dot= ((self.Stiffness1/self.Mass2)*(q1-q3)) + (( self.Damper1 /self.Mass2)* (q2-q4)) - ((self.Stiffness2/self.Mass2)*(q3-r))- ((self.Damper2/self.Mass2)*(q3-r))
       #-((Tyre_Damping/UnSprungMass)*(q3-r))
   
    
       #write the above equations in matrix form
       states=[q1dot,q2dot,q3dot,q4dot]
       return states

    def AnalyseRidePerfromance_X2(self,x,t):
   
        #Critical Damping Co efficient
        Cc1 = (2.0 * ( ( self.Stiffness1/self.Mass1)**0.5 ) * self.Mass1)
        Cc2 = (2.0 * ( ( self.Stiffness2/self.Mass2)**0.5 ) * self.Mass2)
        
        #print(Cc)
    
        #Critical Damping Co efficient
        #Cc = (2 * Zeta * ( ( Spring_Stiffness/SprungMass)**0.5 ) * SprungMass)
        #print(Cc)
       
        #Road Surface Period[Length or pitch Of Bump] = P = 15m
        P=self.BumpPitch #20.20     #ft or 15 m
        #print("Road Surface Period",P,"ft (15 m)")

        #REQUIRED :
        #		Steady State motion Amplitude X(t) = ?
        #		Force Transmitted To The Chasis  F(t) = ?
        #SOLUTION :
        #w = 50 [ mi / hr ] x [ 5280 ft / 1 mile ] x [ 1 cycle / 20 ft ] x [2 .Pi rad / 1 cycle ]  x [ 1hr /3600 ]
        w=self.Velocity*5280*(1/P)*(2*math.pi)*(1/3600)
        #print("Forced Vibration Frequency",w,"rad/sec")

        #Road Profile 1st[5 cm jump ]
        z0=self.BumpHeight #5.0/100
       
        #Road Profile = U(t) = 0.03 ft . ( 1 / 3.28 ft) = 0.0009 m
        Utx=z0 * ( 1 / 3.28 )
        omega = self.ConvertDegrees(w)
        #Bump Time Period = T = 2 x Pi / w
        if(self.BumpTimePeriod == 0):
           self.BumpTimePeriod = (1/self.BumpFrequency)    #[secs ]
      
        #print(Utx)
        if(omega > 90):
            omega = np.abs(1 - (omega/360))*360
            if(omega > 90):
                omega =omega - 90
        #print(omega)
        r=z0*np.sin(omega * np.array(t))
        #Road Profile 2ndt
        #r=0.80

        #state variables defined as
        q1,q2,q3,q4=x
    

        #q1 is my sprung mass body travel
        #q2 is my sprung mass body velocity
        #q2dot is my sprung mass body acceleration

        #q3 is my unsprung mass body travel
        #q4 is my unsprung mass body velocity
        #q4dot is my unsprung mass body acceleration


        #4 first order differential equations for the system
        q1dot = q2
        q2dot= -((self.Stiffness1/self.Mass1)*(q1-q3))- (( self.Damper1 /self.Mass1)* (q2-q4))
    
        q3dot = q4
        q4dot= ((self.Stiffness1/self.Mass2)*(q1-q3)) + (( self.Damper1 /self.Mass2)* (q2-q4)) - ((self.Stiffness2/self.Mass2)*(q3-r))- ((self.Damper2/self.Mass2)*(q3-r))
        #-((Tyre_Damping/UnSprungMass)*(q3-r))
   
    
        #write the above equations in matrix form
        states=[q1dot,q2dot,q3dot,q4dot]
        return states
     
      

    
    def makeform(self,fields):
        entries = {}
        for field in fields:
           row = Frame(self)
           lab = Label(row, width=22, text=field+": ", anchor='w')
           ent = Entry(row)
           ent.insert(0,"0")
           row.pack(side=TOP, fill=X, padx=5, pady=5)
           lab.pack(side=LEFT)
           ent.pack(side=RIGHT, expand=YES, fill=X)
           entries[field] = ent
           
                 
        return entries

      

app = SeaofBTCapp()
app.mainloop()
def onclick():
   pass

def onload():
   pass
   
def destroy(e):
    sys.exit()
      
