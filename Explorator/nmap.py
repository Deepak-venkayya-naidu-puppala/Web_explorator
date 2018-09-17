import os

def get_nmap(options,ip):

    command = "nmap "+options +" "+ip
 
    process = os.popen(command)
    results = str(process.read())

    print("Nmap Scan Completed")
    return results

# print(get_nmap("-F","192.168.43.1"))