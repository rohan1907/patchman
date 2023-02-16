#function to generate bash script for test server

def createBackupComman(serverFilePath):
    commandList = []
    bkpCommandList = [], revertCommandList = []
    for file in serverFilePath:
        bkpCommandList.append(f"cp {file} {file}.bkp")
        revertCommandList.append(f"mv {file}.bkp {file}")

    commandList.append(bkpCommandList)
    commandList.append(revertCommandList)
    return commandList

def createCopyCommand(serverFilePath, localFilePath, testServer):
    commands = []
    localFilePath = localFilePath.split(",")
    localFilePath = [file_path.strip() for file_path in localFilePath]
    localFilePath = [file_path.replace("\n","") for file_path in localFilePath]

    testServerIp = 'root@172.16.18.22:'

    if testServer == 'Test Server 2':
        testServerIp = 'root@172.16.18.22:'


    for i in range(len(localFilePath)):
        command = 'sshpass -p "redhat" scp /'
        command += localFilePath[i]+" "
        command += testServerIp
        command += '/root/webapps'
        command += serverFilePath[i]
        command += "\n"
        commands.append(command)
    return commands

def generateScriptForTestSrvr(serverFilePath, localFilePath, testServer, typeOfPatch, tomcatRestart):
    commandsList = None
    if typeOfPatch == "testsvr":
        commandsList = createCopyCommand(serverFilePath, localFilePath, testServer)
        loginCommand = "sshpass -p 'redhat' ssh root@172.16.18.2"
        if tomcatRestart:
            loginCommand += testServer[-1]
            commandsList.append(loginCommand)

        script_command = "".join(commandsList)
        with open("bash_script.sh", "w") as file:
            file.write(script_command)
    
    
        
    
    



