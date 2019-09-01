from tkinter import *

fle=open('./4041 colors.txt','a')
fle.close()

def makefile(name,cnt):
    file0=open(name,'w')
    file0.write(cnt)
    file0.close()
    
def makestr(lst):
    st=','.join(lst)
    return st

def readfile(name):
    file0=open(name,'r')
    return file0.read()

def makelist(str0):
    li=str0.split(',')
    return li

def pri_lis(root,lst):
    for i in range(len(lst)):
        root4=Canvas(root,bg='#ffffff')
        root4.place(width=270,height=28,x=734,y=22+i*48)
        root4.create_rectangle(2,2,25,25,fill='#'+lst[i][1]+lst[i][2]+'0000')
        root4.create_text(39,14,text='+')
        root4.create_rectangle(52,2,75,25,fill='#00'+lst[i][3]+lst[i][4]+'00')
        root4.create_text(89,14,text='+')
        root4.create_rectangle(102,2,125,25,fill='#0000'+lst[i][5]+lst[i][6])
        root4.create_text(149,14,text='=')
        root4.create_rectangle(172,2,195,25,fill=lst[i])
        root4.create_text(230,14,text=lst[i])
    if len(lst)==0:
        root7=Canvas(root,bg='#ffffff')
        root7.place(width=270,height=28,x=734,y=22)
        str1=makestr(lst)
        makefile('./4041 colors.txt',str1)
    elif len(lst)<13 :
        root7=Canvas(root,bg='#ffffff')
        root7.place(width=270,height=28,x=734,y=22+(i+1)*48)
        str1=makestr(lst)
        makefile('./4041 colors.txt',str1)

def af():
    root8=Canvas(root,bg='#ffffff')
    root8.place(width=270,height=28,x=734,y=22+(len(lst))*48)
    
def putmesag(color):
    if len(lst)<13:
        print(len(lst))
        root8=Canvas(root,bg='#ffffff')
        root8.place(width=270,height=28,x=734,y=22+(len(lst))*48)
        root8.create_text(100,14,text='you have this colour already')
        root8.after(2000,af)
        
def add(root, color):
    global lst
    if color in lst:
        putmesag(color)
    elif len(lst)<13:
        lst.append(color)
        pri_lis(root,lst)
    return color

def dele(root,lst,num):
    del lst[num]
    pri_lis(root,lst)
    return lst

def create_frame(root, color, i, j, k, p):
    xx=24*i+216*k+26
    yy=24*j+216*p+26
    root3=Frame(root)
    root3.configure(bg=color)
    root3.place(width=20,height=20,x=xx,y=yy)
    root3.bind('<Button-1>', lambda e: print(add(root,color)))
    
def remove(m):
    bb0=Button(root)
    bb0.place(width=60,height=20,x=1005,y=25+48*m)
    bb0.configure(text='<- remove')
    bb0.bind('<Button-1>', lambda e: print(dele(root,lst,m)))
    
root=Tk()
root.title('3D GUI ')
root.geometry('1072x672')
ll=['00','20','40','60','80','a0','c0','e0','ff']
root.configure(bg='#'+ll[8]+ll[8]+ll[8])

root1=Frame(root)
root1.configure(bg='#ff00a0')
root1.place(width=44,height=668,x=674,y=2)

file1=readfile('./4041 colors.txt')
if len(file1) < 7:
    lst=[]
else:    
    lst=makelist(file1)
    pri_lis(root,lst)
    
root2=Canvas(root,bg='#ffffff')
root2.place(width=20,height=20,x=2,y=2)
root2.create_text(10,10,text='00')
root5=Canvas(root,bg='#ffffff')
root5.place(width=216,height=20,x=25,y=2)
root5.create_text(106,10,text='00    20    40    60    80    a0    c0    e0    ff')
root6=Canvas(root,bg='#ffffff')
root6.place(width=20,height=216,x=2,y=25)
root6.create_text(10,10,text='00')
root6.create_text(10,34,text='20')
root6.create_text(10,58,text='40')
root6.create_text(10,82,text='60')
root6.create_text(10,106,text='80')
root6.create_text(10,130,text='a0')
root6.create_text(10,154,text='c0')
root6.create_text(10,178,text='e0')
root6.create_text(10,202,text='ff')

for p in range(int(len(ll)/3)):
    for k in range(int(len(ll)/3)):
        for j in range(len(ll)):
            for i in range(len(ll)):
                color='#'+ll[k+p*3]+ll[j]+ll[i]
                create_frame(root, color, i, j, k, p)
                
for m in range(13):
    remove(m)

root.mainloop()

    

