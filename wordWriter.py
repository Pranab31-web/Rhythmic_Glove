import requests
firstMode = True
secondMode = False
string = ""
inputRes1 = 0
inputRes2 = 0
def send_request(url,mode,string):
# string = str(input("Enter your character "))
    requestUrl = f"{url}/{mode}/{string}"
    print(requestUrl)        
    response = requests.get(requestUrl)
    print(response.status_code)
    print(response.content)
            
charater = ""
charArray = ["abcde","fghij","klmno","pqrst","uvwxy","z"]
url = 'http://localhost:3000'
while True:
    space = int(input("is space"))
    app = int(input("Enter to append"))
    
    if space==1:
        send_request(url,"spaceMode"," ")
        
        charater = ""
    if app>0:
        send_request(url,"thirdMode",app)  
        charater = ""  
      
    if firstMode:
        # string = str(input("Enter your character "))
        # requestUrl = f"{url}/firstMode/{string}"
        # print(requestUrl)        
        # response = requests.get(requestUrl)
        # print(response.status_code)
        # print(response.content)
        i = int(input("enter the charArry elemet"))
        send_request(url,"firstMode/suggestion",i)
        inputRes = i
        firstMode = False
        secondMode = True
    if secondMode:
        print("choose from the ",charArray[inputRes-1])
        inputRes2 = int(input(""))
        charater = charater + charArray[inputRes-1][inputRes2-1]
        print(f"you selected {charArray[inputRes-1][inputRes2-1]}")
        send_request(url,"secondMode/suggestion",charater)
        send_request(url,'secondMode',charArray[inputRes-1][inputRes2-1])
        requestUrl = f"{url}/firstMode/{charArray[inputRes-1][inputRes2-1]}"
        # print(requestUrl)        
        # response = requests.get(requestUrl)
        # print(response.status_code)
        # print(response.content)
        firstMode = True
        secondMode = False
        

            
