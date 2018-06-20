import os


def startDocker(port, image="", appPort=8765):
    command = ""

    if (image == ""):
        print("No image specified")
        return(False)
    else:
        command = "docker run -p " + str(port) + ":" + str(appPort) + " -d " + image

    try:    
        os.system(command)
    except:
        print("Docker failed to start")
        return(False)
    
    return(True)