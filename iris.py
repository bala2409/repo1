# Data Analysis I - 5. seminar
# Download the iris dataset. For the iris data collection, implement an application that determines Euclidean distance, mean, median, total variance, standard deviation,
# and cosine similarity.

import xlrd
fileloc = "C:/Bals/Study plan/Lectures_Tutorials/DA/Task 2/iris_edited.xlsx"
wb = xlrd.open_workbook(fileloc)
sheet=wb.sheet_by_index(0)

# MEAN FOR THIS IRIS DATA
print("\n*** MEAN FOR THIS IRIS DATA ***")
#Mean_Sepal_Length
c1 =sheet.col_values(0,1)
s1en=0
for sum1 in c1:
    s1en+=sum1
sl=s1en/150
print("Sepal Length:",sl)

#Mean_Sepal_Width
c2 =sheet.col_values(1,1)
swid=0
for sum2 in c2:
    swid+=sum2
sw=swid/150
print("Sepal Width: ",sw)

#Mean_Petal_Length
c3 =sheet.col_values(2,1)
plen=0
for sum3 in c3:
    plen+=sum3
pl=plen/150
print("Petal Length:",pl)

#Mean_Petal_Width
c4 =sheet.col_values(3,1)
pwid=0
for sum4 in c4:
    pwid+=sum4
pw=pwid/150
print("Petal Width: ",pw)
#==============================================================================================
print("\n*** MEDIAN FOR THIS IRIS DATA ***")

def sepal_length_median():
    rows=sheet.nrows-1
    sortsl = sorted(sheet.col_values(0,1))
    if rows%2==0:
        a=rows/2
        b=a+1
        x=sortsl[int(a-1)]
        y=sortsl[int(b-1)]
        slm=(x+y)/2
        print("Sepal Length is:",float(slm))
sepal_length_median()

def sepal_width_median():
    rows=sheet.nrows-1
    sortsw = sorted(sheet.col_values(1,1))
    if rows%2==0:
        a=rows/2
        b=a+1
        x=sortsw[int(a-1)]
        y=sortsw[int(b-1)]
        swm=(x+y)/2
    print("Sepal Width  is:", float(swm))
sepal_width_median()

def petal_length_median():
    rows=sheet.nrows-1
    sortpl = sorted(sheet.col_values(2,1))
    if rows%2==0:
        a=rows/2
        b=a+1
        x=sortpl[int(a-1)]
        y=sortpl[int(b-1)]
        plm=(x+y)/2
    print("Petal Length is:", float(plm))
petal_length_median()

def petal_width_median():
    rows=sheet.nrows-1
    sortpw = sorted(sheet.col_values(3,1))
    if rows%2==0:
        a=rows/2
        b=a+1
        x=sortpw[int(a-1)]
        y=sortpw[int(b-1)]
        pwm=(x+y)/2
    print("Petal Width  is:", float(pwm),"\n")
petal_width_median()
#=============================================================================================
print("*** TOTAL VARIANCE OF IRIS DATA ***")
#Not Applying Bessel's correction

#def sepal_length_variance
ab1 = [(sheet.col_values(0,1)[i] - sl)**2 for i in range(len(sheet.col_values(0,1)))]
c1=sum(ab1)
d1=c1/((sheet.nrows)-1)
print("Sepal length:",d1)
#sepal_width_variance
ab2 = [(sheet.col_values(1,1)[i] - sw)**2 for i in range(len(sheet.col_values(1,1)))]
c2=sum(ab2)
d2=c2/((sheet.nrows)-1)
print("Sepal width: ",d2)
#petal_length_variance
ab3 = [(sheet.col_values(2,1)[i] - pl)**2 for i in range(len(sheet.col_values(2,1)))]
c3=sum(ab3)
d3=c3/((sheet.nrows)-1)
print("Petal length:",d3)
#petal_width_variance
ab4 = [(sheet.col_values(3,1)[i] - pw)**2 for i in range(len(sheet.col_values(3,1)))]
c4=sum(ab4)
d4=c4/((sheet.nrows)-1)
print("Petal width: ",d4)
#================================================================================================
print("\n*** STANDARD DEVIATION OF IRIS DATA ***")
def std():
    global sdsl,sdsw,sdpl,sdpw
    sdsl = (d1) ** 0.5
    sdsw = (d2) ** 0.5
    sdpl = (d3) ** 0.5
    sdpw = (d4) ** 0.5
    print("Sepal length:",sdsl)
    print("Sepal width: ",sdsw)
    print("Petal length:",sdpl)
    print("Petal width: ",sdpw)
std()
#==============================================================================================
print("\n*** EUCLIDEAN DISTANCE OF THIS IRIS DATA ***")
x=int(input("Enter the 1st row number:"))
y=int(input("Enter the 2nd row number:"))

if x and y not in range(1,len(sheet.col_values(0,1))+1):
    raise SystemExit("Not a proper row number")
def Euclidean_Distance():
    a = ((sheet.cell_value(x, 0)) - (sheet.cell_value(y, 0))) ** 2
    b = ((sheet.cell_value(x, 1)) - (sheet.cell_value(y, 1))) ** 2
    c = (a + b) ** 0.5
    print("Euclidean distance of  sepal length (", sheet.cell_value(x, 0), ",", sheet.cell_value(x, 1),
          ")  and   sepal width (", sheet.cell_value(y, 0), ",", sheet.cell_value(y, 1), ") :")
    print(c)
    a = ((sheet.cell_value(x, 2)) - (sheet.cell_value(y, 2))) ** 2
    b = ((sheet.cell_value(x, 3)) - (sheet.cell_value(y, 3))) ** 2
    c = (a + b) ** 0.5
    print("Euclidean distance of  petal length (", sheet.cell_value(x, 2), ",", sheet.cell_value(x, 3),
          ")  and   petal width (", sheet.cell_value(y, 2), ",", sheet.cell_value(y, 3), ") :")
    print(c)

Euclidean_Distance()
#=================================================================================================
def cosine_similarity_a_b():
    print("\n*** COSINE SIMILARITY OF INSTANCES **")
    x = sheet.col_values(0,1)
    y = sheet.col_values(1,1)
    z = [((x[i] * y[i])) for i in range(150)]
    nom=(sum(z))
####
    a=[ ((x[i])**2) for i in range(150)]
    b=[ ((y[i])**2) for i in range(150)]
    d1=(sum(a))**0.5
    d2=(sum(b))**0.5
    denom=d1*d2
####
    cs=nom/denom
    print("Sepal Length(a) and Sepal width(b)  : ",cs)
cosine_similarity_a_b()

def cosine_similarity_a_c():
    x = sheet.col_values(0,1)
    y = sheet.col_values(2,1)
    z = [((x[i] * y[i])) for i in range(150)]
    nom=(sum(z))
####
    a=[ ((x[i])**2) for i in range(150)]
    b=[ ((y[i])**2) for i in range(150)]
    d1=(sum(a))**0.5
    d2=(sum(b))**0.5
    denom=d1*d2
####
    cs=nom/denom
    print("Sepal Length(a) and Petal length(c) : ",cs)
cosine_similarity_a_c()

def cosine_similarity_a_d():
    x = sheet.col_values(0,1)
    y = sheet.col_values(3,1)
    z = [((x[i] * y[i])) for i in range(150)]
    nom=(sum(z))
####
    a=[ ((x[i])**2) for i in range(150)]
    b=[ ((y[i])**2) for i in range(150)]
    d1=(sum(a))**0.5
    d2=(sum(b))**0.5
    denom=d1*d2
####
    cs=nom/denom
    print("Sepal Length(a) and Petal Width(d)  : ",cs)
cosine_similarity_a_d()

def cosine_similarity_b_c():
    x = sheet.col_values(1,1)
    y = sheet.col_values(2,1)
    z = [((x[i] * y[i])) for i in range(150)]
    nom=(sum(z))
####
    a=[ ((x[i])**2) for i in range(150)]
    b=[ ((y[i])**2) for i in range(150)]
    d1=(sum(a))**0.5
    d2=(sum(b))**0.5
    denom=d1*d2
####
    cs=nom/denom
    print("Sepal Width(b)  and Petal Length(c) : ",cs)
cosine_similarity_b_c()

def cosine_similarity_b_d():
    x = sheet.col_values(1,1)
    y = sheet.col_values(3,1)
    z = [((x[i] * y[i])) for i in range(150)]
    nom=(sum(z))
####
    a=[ ((x[i])**2) for i in range(150)]
    b=[ ((y[i])**2) for i in range(150)]
    d1=(sum(a))**0.5
    d2=(sum(b))**0.5
    denom=d1*d2
####
    cs=nom/denom
    print("Sepal Width(b)  and Petal Width(d)  : ",cs)
cosine_similarity_b_d()

def cosine_similarity_c_d():
    x = sheet.col_values(2,1)
    y = sheet.col_values(3,1)
    z = [((x[i] * y[i])) for i in range(150)]
    nom=(sum(z))
####
    a=[ ((x[i])**2) for i in range(150)]
    b=[ ((y[i])**2) for i in range(150)]
    d1=(sum(a))**0.5
    d2=(sum(b))**0.5
    denom=d1*d2
####
    cs=nom/denom
    print("Petal Length(c) and Petal Width(d)  : ",cs)
cosine_similarity_c_d()

""""
def cosine_similarity_a_b_c():
    x = sheet.col_values(0,1)
    y = sheet.col_values(1,1)
    z = sheet.col_values(2,1)
    zz = [((x[i] * y[i] * z[i])) for i in range(150)]
    nom=(sum(zz))
####
    a=[ ((x[i])**2) for i in range(150)]
    b=[ ((y[i])**2) for i in range(150)]
    c=[ ((z[i])**2) for i in range(150)]
    d1=(sum(a))**0.5
    d2=(sum(b))**0.5
    d3=(sum(c))**0.5
    denom=d1*d2*d3
####
    cs=nom/denom
    print("Sepal Length(a) and Sepal width(b) and Petal Length : ",cs)
cosine_similarity_a_b_c()

def counter():
    a=sheet.col_values(0,1)
    b=sorted(a)
    count = 0
    i = 0
    while i <= 150:
        if b[i]==b[i+1]:
            count=count+1
        else:
            count=1
    i = i + 1
    print(count)
counter()
"""
# Data Analysis I - 6. seminar
# For the iris data collection, for all attributes, specify the frequency of attribute values, their relative and cumulative frequencies.
# Verify that the probability distribution of all attributes corresponds to the normal distribution (using mean and standard deviation)

a = sheet.col_values(0,1)
b = sheet.col_values(1,1)
c = sheet.col_values(2,1)
d = sheet.col_values(3,1)

print("\nFrequencies of instances from Sepal length:")
sl_dict = {i:a.count(i) for i in a}
print(sl_dict)

print("Frequencies of instances from Sepal width:")
sw_dict = {i:b.count(i) for i in b}
print(sw_dict)

print("Frequencies of instances from Petal length:")
pl_dict = {i:c.count(i) for i in c}
print(pl_dict)

print("Frequencies of instances from Petal Width:")
pw_dict = {i:d.count(i) for i in d}
print(pw_dict)

i=0
ii= [(sl_dict[i])/150 for i in sl_dict]
jj= [(sw_dict[i])/150 for i in sw_dict]
kk= [(pl_dict[i])/150 for i in pl_dict]
ll= [(pw_dict[i])/150 for i in pw_dict]
print("\nRelative frequency for Sepal length:")
print(ii)
print("Relative frequency for Sepal width:")
print(jj)
print("Relative frequency for Petal length:")
print(kk)
print("Relative frequency for Petal width:")
print(ll)

print("\nCumulative frequency for Sepal length:")
c=[0]
i,d=0,0
for i in range(len(ii)):
    d=ii[i]+c[i]
    c.append(d)
del(c[0])
print(c)

print("Cumulative frequency for Sepal width:")
c=[0]
i,d=0,0
for i in range(len(jj)):
    d=jj[i]+c[i]
    c.append(d)
del(c[0])
print(c)

print("Cumulative frequency for Petal length:")
c=[0]
i,d=0,0
for i in range(len(kk)):
    d=kk[i]+c[i]
    c.append(d)
del(c[0])
print(c)

print("Cumulative frequency for Petal width:")
c=[0]
i,d=0,0
for i in range(len(ll)):
    d=ll[i]+c[i]
    c.append(d)
del(c[0])
print(c)

print("\n**** Normal distribution ****")
print("|_for Sepal Length:")
ndsl= [((sheet.col_values(0,1)[i]-sl)/sdsl)for i in range(150)]
print(ndsl)

print("|_for Sepal Width:")
ndsw= [((sheet.col_values(1,1)[i]-sw)/sdsw)for i in range(150)]
print(ndsw)

print("|_for Petal Length:")
ndpl= [((sheet.col_values(2,1)[i]-sl)/sdpl)for i in range(150)]
print(ndpl)

print("|_for Petal Width:")
ndpw= [((sheet.col_values(3,1)[i]-sw)/sdpw)for i in range(150)]
print(ndpw)

# Data Analysis I - 7. seminar #
# Review tasks from previous seminars.
# Preparing for the lecture and the next seminar - read these documents: Lecture 0, Lecture 1.
