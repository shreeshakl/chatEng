import socket,pickle,_thread

grp_dic={1:[]}
serverobj=socket.socket()
serverobj.bind(("127.0.0.1",3000))
serverobj.listen(50)
dic_track=2

def message_receive(s,gid):
    global grp_dic
    print("message_receive called %d" %gid)
    print(grp_dic[1])
    while True:
        msg=pickle.loads(s.recv(1024))
        print(msg+" %d"%gid)
        print("Message receipients" )
        print(grp_dic[gid])
        for i in grp_dic[gid]:
            if not i._closed:
                print(i._closed)
                print("Pushing")
                i.send(pickle.dumps(msg))
            else:
                print(i._closed)


def connection_accept():
    print("2")
    global grp_dic,dic_track,serverobj
    while True:
        print("Waiting for connection")
        connection, address = serverobj.accept()
        print(" connected %d"%len(grp_dic))
        for i in range(1,len(grp_dic)+1):
            print(" %d i in connection accept" %i)
            if len(grp_dic[i])<5 :
                grp_dic[i].append(connection)
                print("appended")
                break
        else:
            grp_dic[dic_track]=[connection]
            dic_track+=1
            print("appeded2")
        _thread.start_new_thread(message_receive, (connection,dic_track-1))
print("1")

_thread.start_new_thread(connection_accept(),())

print("hai")
