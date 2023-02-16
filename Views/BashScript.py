#function to generate bash script for test server



def createCopyCommand(serverFilePath, localFilePath, testServer):
    commands = []
    localFilePath = localFilePath.split(",")
    localFilePath = [file_path.strip() for file_path in localFilePath]
    localFilePath = [file_path.trim() for file_path in localFilePath]

    testServerIp = 'root@172.16.18.22:'

    if testServer == 'Test Server 2':
        testServerIp = 'root@172.16.18.22:'


    for i in range(len(localFilePath)):
        command = 'sshpass -p "redhat" scp /'
        command += localFilePath[i]+" "
        command += testServerIp
        command += '/root/webapps'
        command += serverFilePath[i]
        commands.append(command)
    return commands

def generateScriptForTestSrvr(serverFilePath, localFilePath, testServer):
    
    



