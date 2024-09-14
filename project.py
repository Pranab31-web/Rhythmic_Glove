import requests
import pymsgbox as a
import serial
import time


# Send a GET request to the desired API URL
response = requests.get('http://localhost:3000/current')

# Parse the response as JSON
data = response.json()

output = a.confirm('Arduino project', 'Are you want to play music',["ok","cancel"])

print(output)


arduino = serial.Serial(port='COM3', baudrate=9600)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    num = input("Enter a number: ") 
    value = write_read(num)




import math

def find_root():
    # here we find the value of the polynomial at a certial point
    def get_value(v,num):
        deg = len(v)-1
        i = 0
        ans = 0
        while(deg>=0):
            c = math.pow(num,deg)
            c = c* v[i]
            deg = deg - 1
            i = i+1
            ans = ans +c
        return ans
        
# here we spilt the portion where roots are present in 100000 parts and minimize the function value
    def minimize(l,m,v):
        division = 100000
        ans_list = []
        ans_list.append(l)
        put = (1/division)
        for i in range(division):
            value = round(l + put,len(str(division)))
            ans_list.append(value)
            put = (1/division) + put
        
        #print(ans_list)
       
        root = ans_list[0]
        min_ans = abs(get_value(v, ans_list[0]))
        for i in range(1,len(ans_list)):
            q = abs(get_value(v,ans_list[i]))
            if(q<min_ans):
                root = ans_list[i]
                min_ans = min(min_ans,q)            
       # print("root")
        print(root)
        return root            
       
    n = int(input("Enter the degree of polynomail "))
    
    coeff = list(map(int,input("\n enter your coefficinet : ").strip().split()))[:n+1]
    
    check_list = []
    no_of_roots = 0
    final_ans = []
    for i in range(0,10000):
        a = get_value(coeff,i)
        b = get_value(coeff,i+1)
        #print(a," ",b)
        if(no_of_roots==n):
            break
        
        if(a==0):
            final_ans.append(i)
            no_of_roots = no_of_roots + 1
        if((a*b)<0):
            check_list.append([i,i+1])
            no_of_roots = no_of_roots + 1

    for i in range(-10000,1):
        a = get_value(coeff,i)
        b = get_value(coeff,i+1)
        #print(a," ",b)
        if(no_of_roots==n):
            break
        
        if(a==0):
            final_ans.append(i)
            no_of_roots = no_of_roots + 1
        if((a*b)<0):
            check_list.append([i,i+1])
            no_of_roots = no_of_roots + 1


    #print(check_list)
    #print(final_ans)
    for i in range(len(check_list)):
        a = minimize(check_list[i][0],check_list[i][1],coeff)
        final_ans.append(a)
    
    print("the final roots are")
    print(final_ans)

find_root()    
    




