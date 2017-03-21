from tkinter import *
from tkinter.messagebox import *
import socket,_thread,pickle,threading
root=Tk()
root.geometry("600x600")
frame=Frame(root)
frame.pack(fill=BOTH)
can=Canvas(frame,bg="green",relief=SUNKEN)
can.config(width=600,height=500)
can.config(scrollregion=(0,0,300,1000))
can.config(highlightthickness=0)

sbar=Scrollbar(frame)
sbar.config(command=can.yview)
can.config(yscrollcommand=sbar.set)
sbar.pack(side=RIGHT, fill=Y)
can.pack(side=LEFT, expand=YES, fill=BOTH)
i=0
s=None


def entr():
    global s
    if s._closed :
        print(_thread._count())
        if askyesno("Reconnect","Connection closed! Do you want to reconnect?"):
            _thread.start_new_thread(listen, ())
    else:
        s.send(pickle.dumps(textinputbox.get(index1="1.0", index2=END)))


def print_received(txt):
    global i
    can.create_text(0,i,text=txt,anchor=NW)
    i+=20

textinputbox = Text(root, height=5, insertofftime=0)
sendbutton=Button(root,text="Send",command=entr)
sendbutton.pack(side=BOTTOM)
textinputbox.pack(fill=X,side=BOTTOM)

def ip():
    return "127.0.0.1"

def port():
    return 3000


def listen():
    global s
    while True:
        try:
            s = socket.socket()
            s.connect((ip(),port()))
            while True:
                receive=pickle.loads(s.recv(1024))
                print(receive)
                if receive=="close":
                    s.close()
                    showinfo('Close', 'Connection closed by Server!')
                else:
                    print_received(receive)
        except Exception as e:
            print("error: %s" %e)
            if askyesno("Failed", "Connection failed! Do you want to retry?"):
                continue
            else:
                s.close()
                _thread.exit_thread()


_thread.start_new_thread(listen,())
#bitmap = BitmapImage(file="newmsg.bmp")
print("Thread called")
mainloop()
