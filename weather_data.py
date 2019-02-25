#This is to check merge between master and issue

import xlrd
fileloc = "C:/Bals/Study plan/Lectures_Tutorials/DA/Task 1/Weather.xlsx"
wb = xlrd.open_workbook(fileloc)
sheet=wb.sheet_by_index(1)
k,l,kk,ll=24,48,47,71
outlook=['sunny','overcast','rainy']
temperature=["hot","mild","cool"]
humidity=["high","normal"]
windy=["F","T"]
play=["yes","no"]

x = [[a+"', '"+b+"', '"+c+"', '" +d+"', '" +e] for a in outlook for b in temperature for c in humidity for d in windy for e in play]

i=1
while True:
    playing=[(sheet.row_values(i,0)) for i in  range(1,15)]
    break

playing1 = [playing[i][4] for i in range(0,14)]
#print(playing)

#print("\nPlaying yes conditions-Excel:")
i = 0
s1=[]
while i<len(playing):
     if "yes" in playing[i][4]:
          z = s1.append(playing[i])
     i=i+1
#print(*s1,sep="\n")

#print("\nPlaying no conditions-Excel:")
i = 0
no = []
while i < len(playing):
     if "no" in playing[i][4]:
          z = no.append(playing[i])
     i = i + 1
#print(*no,sep="\n")

#print("\n",len(playing))
print("\n")

j=0
sun1=[]
while j<=23:
    z=[sun1.append(x[j])]
    j=j+1
#print(sun1)

ovr1=[]
while k<=kk:
    zz = ovr1.append(x[k])
    k=k+1
#print(*ovr1,sep="\n")
for i in range (0,24,2):
    print(*ovr1[i],sep="\n")

rai=[]
while l<=ll:
    zzz = rai.append(x[l])
    l = l + 1
#print(rai)

import xlrd

fileloc = "C:/Bals/Study plan/Lectures_Tutorials/DA/Task 1/Weather.xlsx"
wb = xlrd.open_workbook(fileloc)
sheet = wb.sheet_by_index(0)
out = sheet.col(0, 1)
tmp = sheet.col(1, 1)
hum = sheet.col(2, 1)
win = sheet.col(3, 1)

outlook1 = ["sunny", "overcast", "rainy"]
temperature1 = list(range(60, 70))
temperature2 = list(range(70, 80))
temperature3 = list(range(80, 100))
humidity1 = list(range(81, 100))
humidity2 = list(range(61, 100))
windy = ["false", "true"]
play = ["Yes", "No"]

print("\nFINDING PLAYING CONDITIONS:")

# outlook module
outlook2 = input("ENTER CLIMATE OUTLOOK:\n")
if outlook2 == outlook1[1]:
    print("Rule3: Play: Yes", "we can play\n")
    exit()
elif outlook2 == outlook1[2]:
    print("Entered outlook is: rainy\n")
elif outlook2 == outlook1[0]:
    print("Entered outlook is: sunny\n")
else:
    print("you have entered something out of the weather outlook")
    exit()

# finding temperature:
temp = input("ENTER THE TEMPERATURE IN VALUES:\n")
if int(temp) in temperature1:
    print("temp is cool")
    if int(temp) in list(sheet.col_values(1, 1)):
        print("Yes, the value is in the Excel sheet\n")
elif int(temp) in temperature2:
    print("temp is mild")

if int(temp) in list(sheet.col_values(1, 1)):
    print("Yes, the value is in the Excel sheet\n")
elif int(temp) in temperature3:
    print("temp is hot")
    if int(temp) in list(sheet.col_values(1, 1)):
        print("Yes, the value is in the Excel sheet\n")
else:
    print("you have entered out of suitable range")
    exit()

# finding humidity:
humid = input("ENTER THE HUMIDITY IN VALUES:\n")
if int(humid) in humidity1:
    print("humidity is high")
    if int(humid) in list(sheet.col_values(2, 1)):
        print("Yes, the value is in the Excel sheet\n")
elif int(humid) in humidity2:
    print("humidity is normal")
    if int(humid) in list(sheet.col_values(2, 1)):
        print("Yes, the value is in the Excel sheet\n")
else:
    print("\nyou have entered wrong parameter in humidity")
    exit()

# finding windy values:
wind = input("ENTER WINDY TRUE OF FALSE:\n")
if wind in windy[1]:
    print("Windy: ", "True")
elif wind in windy[0]:
    print("Windy: ", "False")
else:
    print("you have entered something else")
    exit()

# Applying some rules:
if outlook2 == outlook1[0] and int(humid) in humidity1:
    print("Rule1: Play = no, we cannot play")
elif outlook2 == outlook1[2] and wind == windy[1]:
    print("Rule2: Play = no, we cannot play")
elif humid in humidity2:
    print("Rule4: Play = yes", " we can play")
else:
    print("Rule99: Play = yes", " we can play")
