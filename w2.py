def cal_cone(a,b):
       global wlabel
       myButton23['state'] = DISABLED
       t3=(1/3)*pi*a*a*b       
       if t1>0 and t2 >0:
                wlabel.config(text=t3)
                wlabel.place(x=305, y=211)
       else:
               wlabel = Label(win, text="Please input with right minimum number")
               wlabel.place(x=255, y=211)


def cal_cube():
       global wlabel
       t1=int(a.get())
       myButton23['state'] = DISABLED
       t3=t1**3
       
       
       if t1>0 :
                
                wlabel.config(text=t3)
                wlabel.place(x=305, y=211)
       else:
               wlabel = Label(win, text="Please input with right minimum number")
               wlabel.place(x=255, y=211)
               
def cal_ball():
       global wlabel
       t1=int(a.get())
       myButton23['state'] = DISABLED
       t3=(4/3)*pi*t1**3
       
       
       if t1>0 :
                
                wlabel.config(text=t3)
                wlabel.place(x=305, y=211)
       else:
               wlabel = Label(win, text="Please input with right minimum number")
               wlabel.place(x=255, y=211)

def cal_beam():
       global wlabel
       t1=int(a.get())
       t2=int(b.get())
       t4=int(c.get())
       myButton23['state'] = DISABLED
       t3=t1*t2*t4
       
       
       if t1>0 and t2 >0:
                wlabel.config(text=t3)
                wlabel.place(x=305, y=211)
       else:
               wlabel = Label(win, text="Please input with right minimum number")
               wlabel.place(x=255, y=211)
    
               
       
def myDel(): 
    wlabel.place_forget()
    myButton23['state'] = NORMAL      
