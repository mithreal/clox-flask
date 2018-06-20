import socket, errno

def checkPort(portN):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p = False
    try:
        s.bind(("127.0.0.1", portN))
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            response = "Port " + str(portN) + " is already in use."
            print(response)
            p = False
        else:
            # something else raised the socket.error exception
            print(e)
            p = False
    else:
        print("Port free")
        p = True
    s.close()
    return(p)

