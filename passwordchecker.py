import requests
import hashlib
import sys
#url = "https://api.pwnedpasswords.com/range/" + "CBFDA"
#res = requests.get(url)
#print(res) # 400-->not secured now it will say 200


def requestdata(chars):
    url= "https://api.pwnedpasswords.com/range/"+ chars
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError("Error fetching",res.status_code,"check the api again!")
    return res

def pwnedcheck(password):
    passwordsha1= (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5chars, tail = passwordsha1[:5],passwordsha1[5:]
    response=requestdata(first5chars)
    #print(first5chars,tail)
    print(response) #number of similara hash codes with first 5 chars
    return getPassword(response,tail)

#def readresponse(response):
   # print(response.text)

def getPassword(hashes,hash2check):
    hashes = (line.split(":")for line in hashes.text.splitlines() )
    for h,count in hashes:
        #print(h,count)
        if h==hash2check:
            return count
    return 0

#print(pwnedcheck("password123"))
#pwnedcheck("123")
str1="hello" #input
check=pwnedcheck(str1)

#def main(args):
    #for password in args:
        #count= pwnedcheck(password)
        #if count:
            #print(password,"was found",count,"times...you should change your password")
        #else:
            #print(password,"Was not Found!")
    #return "done!"
count= check
if count:
    print(str1,"was found",count,"times...you should change your password")
else:
    print(str1,"Was not Found!")
#main(sys.argv[1:])