# Data Analysis I - 9. seminar
# Network data analysis: Download (read) this data Karate Cluband implement an application
# which reads this data (this graph) and stores it in adjacency matrix and in adjacency list (in list of vertices and their neighbours).
# This matrix and list will be printed into standard output (console). Specify min, max and mean degree of nodes.
# Specify the frequency and relative frequency of occurrences of nodes with a given degree and create a histogram of these frequencies

import pprint,xlrd, matplotlib.pyplot as plt
global inf
inf=99999
fileloc="E:\Bals\Study plan\Lectures_Tutorials\Sem 1\DA\kctest.xlsx"
wb=xlrd.open_workbook(fileloc)
sheet=wb.sheet_by_index(0)

def adjacency_list():
    adj_list={}
    a=sheet.col_values(0,0)
    b=sheet.col_values(1,0)
    i=0
    while i<len(sheet.col_values(0,0)):
        adj_list.setdefault(int(a[i]),[])
        adj_list[int(a[i])].append(int(b[i]))
        adj_list.setdefault(int(b[i]), [])
        adj_list[int(b[i])].append(int(a[i]))
        i=i+1
    print("\nAdjacency list:")
    pprint.pprint(adj_list)
    print("\n")
adjacency_list()
#-------------------------------------
#Converting two columns in a list
a1=[]
b1=[]
i=0
while i<len(sheet.col_values(0,0)):
    a1.append(int(sheet.cell_value(i,0)))
    i=i+1

i=0
while i<len(sheet.col_values(0,0)):
    b1.append(int(sheet.cell_value(i,1)))
    i=i+1

r,c = 34,34
Matrix = [[0 for x in range(r)] for y in range(c)]
i=0
while i<78:
    Matrix[a1[i]-1][b1[i]-1] = 1
    Matrix[b1[i]-1][a1[i]-1] = 1
    i=i+1
print("Adjacency Matrix:")
print(' 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34')# numbers for vertices
print(*Matrix,sep="\n") #prints as matrix
#============================
print("\nMin degree of nodes:")
s,i=sum(Matrix[0]),0
while i<len(Matrix):
    if s>sum(Matrix[i]):
        s=sum(Matrix[i])
    i=i+1
print(s)
#============================
print("\nMax degree of nodes:")
s,i=sum(Matrix[0]),0
while i<len(Matrix):
    if s<sum(Matrix[i]):
        s=sum(Matrix[i])
    i=i+1
print(s)
#============================
print("\nMean of nodes:")
s=0
i=0
while i<34:
    s=s+sum(Matrix[i])
    i=i+1
print((s)/len(Matrix))
#============================
print("\nDegree matrix:")
i =0
j =1
aa=[]
while i <= len(Matrix) and j<35:
    print(j,sum(Matrix[i]))
    aa.append(sum(Matrix[i]))
    i = i + 1
    j=j+1

print("\nSorted List of frequency values:")
bb=sorted(aa)
print(sorted(bb))
freq= {i:bb.count(i) for i in bb}
print("\nFrequency")
print(freq)
# plt.title("Histogram for frequency")
# plt.xlabel("Number")
# plt.ylabel("Frequency")
# plt.xlim(0,18)
# plt.ylim(0,12)
# plt.bar(list(freq.keys()), freq.values(), color='g')
# plt.legend()
# plt.show()
#=============================
print("\nRelative frequency:")
i=0
ii= [(freq[i])/len(Matrix) for i in freq]
print(ii)
print("\nSum of Relative frequencies which is always equal to 1")
print(sum(ii),"\n")
plt.xlabel("Number")
plt.ylabel("Relative frequency")
x=list(freq.keys())
y=ii
print("Freq:","\n",x)
print("Rel Freq","\n",y)
# plt.bar(x,y,color="b")
# plt.xlim(0,18)
# plt.ylim(0,0.5)
# plt.title("Histogram for Relative frequency")
# plt.legend()
# plt.show()
#=============================
# Data Analysis I - 10. seminar
# For data from the Karate Club Karate Club specify the distance (the shortest path length) between all pairs of nodes, mean distance and diameter.
# You'll need Floyd's algorithm. Next, determine the frequency and relative frequency of occurrences of distances, create a histogram.

#Next matrix creation
next=[]
i=0
while i<34:
    next.append(list(range(1,35)))
    i=i+1
i=0
j=0
while i<34: #Loop to change diagonally 0's
    if i==j:
        next[i][j]=0
        j=j+1
    i=i+1

r,c = 34,34
dist = [[0 for x in range(r)] for y in range(c)]
for i in range(0,34):
    for j in range(0,34):
        if(i!=j) and Matrix[i][j]==0:
            dist[i][j]=inf
        elif(i==j):
            dist[i][j]=0
        elif(Matrix[i][j]==1):
            dist[i][j]=1

for k in range(0,34):
    for i in range(0,34):
        for j in range(0,34):
            if dist[i][j]>dist[i][k]+dist[k][j]:
                dist[i][j]=dist[i][k]+dist[k][j]
                next[i][j]=next[i][k]
print("\n*** Distance Matrix using 'Floyd Warshall Algorithm' ***")
print("    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34")
i=0
while i<34:
    if i in range(0,9): #if else just to sort the distance matrix while printing
        print(i+1,'',dist[i])
    else:
        print(i+1,dist[i])
    i+=1

print("\nPairs  |  Distance")
a=[]
kkk=range(1,35)
for i in range(0,34):
    for j in range(0,34):
        print(i+1,"<-->",j+1,": ",dist[i][j])
        a.append(dist[i][j])

sum1=0
i=0
while i<len(dist):
    sum1=sum1+sum(dist[i])
    i=i+1
print("\nMean Distance:",sum1/(len(dist)*len(dist)))
#============================
maxi=0
for j in range(0,len(dist)):
    for i in dist[j]:
        if i>maxi:
            maxi=i
print("\nDiameter:",maxi)

print("\n*** Frequencies of Distances ***")
print("Distance | Frequency |    Relative frequency")
print("--------------------------------------------------")
d=list(range(6))
f=[]
rf=[]
for i in range(0,6):
    f.append(a.count(i))
    rf.append(f[i]/len(a))
    if i in range(1,5): #Used if else for printing like a proper column (i.e from relative frequency to 1.0)
        print(i, "        ", a.count(i),"          ",f[i] / len(a))
    else:
        print(i, "        ", a.count(i),"           ",f[i] / len(a))
    c=[f[i]/len(a) for i in range(0,len(f))]
print("--------------------------------------------------")
print("Total:    ",len(a),"         ",sum(c))
print("--------------------------------------------------")

# x,y,z=d,f,rf
# plt.bar(x,y,color='b')
# plt.title("Histogram for frequency")
# plt.xlabel('Distance')
# plt.ylabel('Frequencies')
# plt.xlim(-1,6)
# plt.ylim(0,600)
# plt.legend('Frequency')
# plt.show()
#===============================================
# plt.bar(x,z,color='r')
# plt.title("Histogram for Relative frequency")
# plt.xlabel('Distance')
# plt.ylabel('Relative Frequencies')
# plt.xlim(-1,6)
# plt.ylim(0,0.6)
# plt.legend('Relative Frequency')
# plt.show()
#===============================================
# Data Analysis I - 11. seminar
# For data from the Karate Club Karate Club, determine the clustering coefficient of each vertex and determine the network transitivity
# (i.e., the mean clustering coefficient for whole graph)

a=sheet.col_values(0,1)
b=sheet.col_values(1,1)
g=[]
i=0
while i<=len(sheet.col_values(0,1)):
    c=tuple((int(sheet.cell_value(i,0)),int(sheet.cell_value(i,1))))
    i=i+1
    g.append(c)

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

G = {}
for (x,y) in g: make_link(G,x,y)

def clustering_coefficient(G,v):
    neighbors = G[v].keys()
    if len(neighbors) == 1: return -1.0
    links = 0
    for w in neighbors:
        for u in neighbors:
            if u in G[w]: links =links+ 0.5
    return 2.0*(links/(len(neighbors)*(len(neighbors)-1)))

print("\n*** Clustering coefficient ***")
print("Vertices | Coefficients")
a=[]
i=1
while i<=34:
    a.append([i,clustering_coefficient(G,i)])
    i=i+1
print(*a,sep="\n")

total = 0
for v in G.keys():
    total =total+ clustering_coefficient(G,v)

print("\n*** Mean-clustering coefficient of the graph ***")
print(total/len(G))

#---END---#
