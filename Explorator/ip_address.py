import os

def get_ip_address(url):

    command = "host " + url

    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12


    print("IP Address completed!")

    # return results[marker:].splitlines()[0]
    return results[marker:].splitlines()[1]
    # res = res.split(":")
    # return res[1]


#print(get_ip_address("https://www.facebook.com"))