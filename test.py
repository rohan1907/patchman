import subprocess

# Replace the command below with the command you want to execute
command = "ls -al"

# Execute the command in the terminal and capture the output
output = subprocess.check_output(command, shell=True)

# Print the output to the console
print(output.decode())
