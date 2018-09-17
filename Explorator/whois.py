import os

def get_whois(url):

    command = "whois " + url
    process = os.popen(command)
    #print(process.read())
    results = str(process.read())

    print("Whois Completed!!!")

    return results

#print(get_whois("https://www.facebook.com"))