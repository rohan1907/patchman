#function to generate bash script for test server

# sshpass -p "redhat" scp /home/eshwar/insta-hms/instahms/target/classes/com/insta/hms/core/billing/BillRepository.class root@testsvr4:~/webapps/instahms/WEB-INF/classes/com/insta/hms/core/billing/BillRepository.class

def generateScriptForTestSrvr(serverFilePath, localFilePath, testServer):
    commands = []
    localFilePath = localFilePath.split(",")
    localFilePath = [file_path.strip() for file_path in localFilePath]

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
    



