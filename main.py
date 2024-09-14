import pyttsx3
from pygame import mixer
from serial import Serial
from requests import get

url = 'http://localhost:3000'
char = ''
string = ""

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def playsound(filename):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(1.0)
    mixer.music.play()

def send_request(url,mode,string):
# string = str(input("Enter your character "))
    requestUrl = f"{url}/{mode}/{string}"
    print(requestUrl)        
    response = get(requestUrl)
    print(response.status_code)
    print(response.content)

response = get("http://localhost:3000/current")
data = response.json()
speakData = data["word"]
reader = Serial(port='COM6', baudrate=9600)
print(data)
conversationCheck  = False
if(data['conversation']=='yes'):
    conversationCheck = True
if data['instrument'] != "":
    isMusic = True
else:
    isMusic = False

firstMode = True
secondMode = False
thirdMode = False
current = 0
firstModeSelect = ""
charArray = ["abcde","fghij","klmno","pqrst","uvwxy","z"]


print(conversationCheck)

if conversationCheck:
    while True:    
        if firstMode:
            firstMode = False
            secondMode = True
            thirdMode = False
            print("check firstmode")
            while True:
                serialInput = reader.readline()
                if current == serialInput:
                    continue
                else:
                    current = serialInput
                if serialInput == b'1\r\n':
                    print("first pin")
                    send_request(url,"firstMode/suggestion",1)
                    string = charArray[0]
                    firstModeSelect = 1
                    break
                elif serialInput == b'2\r\n':
                    send_request(url,"firstMode/suggestion",2)
                    string = charArray[1]
                    firstModeSelect = 2
                    break
                elif serialInput == b'3\r\n':
                    send_request(url,"firstMode/suggestion",3)
                    string = charArray[2]
                    firstModeSelect = 3
                    break
                elif serialInput == b'4\r\n':
                    send_request(url,"firstMode/suggestion",4)
                    string = charArray[3]
                    firstModeSelect = 4
                    
                    break
                elif serialInput == b'5\r\n':
                    send_request(url,"firstMode/suggestion",5)
                    string = charArray[4]
                    firstModeSelect = 5
                    break
                elif serialInput == b'6\r\n':
                    send_request(url,"firstMode/suggestion",6)
                    string = charArray[5]
                    firstModeSelect = 6
                    break
        if secondMode:
            while True:
                serialInput = reader.readline()
                if current == serialInput:
                    continue
                else:
                    current = serialInput
                if serialInput == b'1\r\n':
                    char = char + string[0]
                    send_request(url,"secondMode/suggestion",char)
                    send_request(url,'secondMode',string[0])
                elif serialInput == b'2\r\n':
                    char = char + string[1]
                    send_request(url,"secondMode/suggestion",char)
                    send_request(url,'secondMode',string[1])
                elif serialInput == b'3\r\n':
                    char = char + string[2]
                    send_request(url,"secondMode/suggestion",char)
                    send_request(url,'secondMode',string[2])
                elif serialInput == b'4\r\n':
                    char = char + string[3]
                    send_request(url,"secondMode/suggestion",char)
                    send_request(url,'secondMode',string[3])
                elif serialInput == b'5\r\n':
                    char = char + string[4]
                    send_request(url,"secondMode/suggestion",char)
                    send_request(url,'secondMode',string[4])
                elif serialInput == b'6\r\n':
                    print("sixth pin")
                    firstMode,secondMode,thirdMode = True,False,False
                    send_request(url,"firstMode/suggestion",firstModeSelect)
                    break
                
                elif serialInput == b'7\r\n':
                    send_request(url,"spaceMode"," ")
                    speak(char)
                    char = ''
                    firstMode,secondMode,thirdMode = True,False,False
                    break
                elif serialInput == b'8\r\n':
                    firstMode,secondMode,thirdMode = False,False,True
                    send_request(url,"secondMode/suggestion",char)
                    break
        if thirdMode:
            while True:
                serialInput = reader.readline()
                if current == serialInput:
                    continue
                else:
                    current = serialInput
                if serialInput == b'1\r\n':
                    send_request(url,"thirdMode",1)
                    firstMode,secondMode,thirdMode = True,False,False
                    speak(char)
                    char = ''
                    break
                elif serialInput == b'2\r\n':
                    send_request(url,"thirdMode",2)
                    firstMode,secondMode,thirdMode = True,False,False
                    speak(char)
                    char = ''
                    break
                elif serialInput == b'3\r\n':
                    send_request(url,"thirdMode",3)
                    firstMode,secondMode,thirdMode = True,False,False
                    speak(char)
                    char = ''
                    break
                elif serialInput == b'4\r\n':
                    send_request(url,"thirdMode",4)
                    firstMode,secondMode,thirdMode = True,False,False
                    speak(char)
                    char = ''
                    break
                elif serialInput == b'5\r\n':
                    send_request(url,"thirdMode",5)
                    firstMode,secondMode,thirdMode = True,False,False
                    speak(char)
                    char = ''
                    break
                    

                


elif isMusic:
    while True:
        serialInput = reader.readline()
        # print(serialInput)
        if current == serialInput:
            continue
        else:
            current = serialInput
        
        if serialInput == b'1\r\n':
            playsound(f"{data['instrument']}/C.wav")
        if serialInput == b'2\r\n':
            playsound(f"{data['instrument']}/D.wav")
        if serialInput == b'3\r\n':
            playsound(f"{data['instrument']}/E.wav")
        if serialInput == b'4\r\n':
            playsound(f"{data['instrument']}/F.wav")
        elif serialInput == b'5\r\n':
            playsound(f"{data['instrument']}/G.wav")
        elif serialInput == b'6\r\n':
            playsound(f"{data['instrument']}/A.wav")
        elif serialInput == b'7\r\n':
            playsound(f"{data['instrument']}/B.wav")
        elif serialInput == b'8\r\n':
            playsound(f"{data['instrument']}/C2.wav")
        elif serialInput == b'100\r\n':
            print("EXIT")
            break

else:
    while True:
        serialInput = reader.readline()
        # print(serialInput)
        if current == serialInput:
            continue
        else:
            current = serialInput
        
        if serialInput == b'1\r\n':
            speak(speakData[0])
        elif serialInput == b'2\r\n':
            speak(speakData[1])
        elif serialInput == b'3\r\n':
            speak(speakData[2])
        elif serialInput == b'4\r\n':
            speak(speakData[3])
        elif serialInput == b'100\r\n':
            print("EXIT")
            break

reader.close()



# if conversationCheck:
#     while True:
#         serialInput = reader.readline()
#         print(serialInput)
#         if current == serialInput:
#             continue
#         else:
#             current = serialInput
        
#         if serialInput == b'7\r\n':
#             send_request(url,"spaceMode"," ")
#             char = ''
#             firstMode, secondMode, thirdMode = True, False, False
#         elif serialInput == b'8\r\n':
#             firstMode, secondMode, thirdMode = False, False, True
#             send_request(url,"secondMode/suggestion",char)

#         if firstMode:
#             firstMode = False
#             secondMode = True
#             thirdMode = False
#             print("check firstmode")
#             while True:
#                 if serialInput == b'1\r\n':
#                     print("first pin")
#                     send_request(url,"firstMode/suggestion",1)
#                     string = charArray[0]
#                     break
#                 elif serialInput == b'2\r\n':
#                     send_request(url,"firstMode/suggestion",2)
#                     string = charArray[1]
#                     break
#                 elif serialInput == b'3\r\n':
#                     send_request(url,"firstMode/suggestion",3)
#                     string = charArray[2]
#                     break
#                 elif serialInput == b'4\r\n':
#                     send_request(url,"firstMode/suggestion",4)
#                     string = charArray[3]
#                     break
#                 elif serialInput == b'5\r\n':
#                     send_request(url,"firstMode/suggestion",5)
#                     string = charArray[4]
#                     break
#                 elif serialInput == b'6\r\n':
#                     send_request(url,"firstMode/suggestion",6)
#                     string = charArray[5]
#                     break
        
#         if secondMode:
#             if serialInput == b'1\r\n':
#                 char = char + string[0]
#                 send_request(url,"secondMode/suggestion",char)
#             elif serialInput == b'2\r\n':
#                 char = char + string[1]
#                 send_request(url,"secondMode/suggestion",char)
#             elif serialInput == b'3\r\n':
#                 char = char + string[2]
#                 send_request(url,"secondMode/suggestion",char)
#             elif serialInput == b'4\r\n':
#                 char = char + string[3]
#                 send_request(url,"secondMode/suggestion",char)
#             elif serialInput == b'5\r\n':
#                 char = char + string[4]
#                 send_request(url,"secondMode/suggestion",char)
        
#         if thirdMode:
#             firstMode,secondMode,thirdMode = True,False,False
#             if serialInput == b'1\r\n':
#                 send_request(url,"thirdMode",1)
#                 char=''
#             elif serialInput == b'2\r\n':
#                 send_request(url,"thirdMode",2)
#                 char=''
#             elif serialInput == b'3\r\n':
#                 send_request(url,"thirdMode",3)
#                 char=''
#             elif serialInput == b'4\r\n':
#                 send_request(url,"thirdMode",4)
#                 char=''
#             elif serialInput == b'5\r\n':
#                 send_request(url,"thirdMode",5)
#                 char=''
                
            
            


            

