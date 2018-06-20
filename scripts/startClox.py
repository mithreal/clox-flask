import checkPort as cP
import startDocker as sD

def startClox():
    image = "clox-test-1"
    port = 36789
    while port <= 36792:
        check = cP.checkPort(port)
        if check == True:
            sD.startDocker(port, image)
            return "Success..."
        print(port)
        port += 1
    
    
    return "Failed to bind to port"
        
        
