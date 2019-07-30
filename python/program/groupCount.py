# 抓檔案到放進data
with open("groupCount.txt",'r') as f:
    data = f.read().rsplit('\n')

# num:人數 group:組數
num = int(data[0])
friend = list(map(int,data[1].split()))
used = []
group = 0

def find(x):
    if x not in used:
        used.append(x)
        find(friend[x])

for i in range(num):
    if i not in used:
        group += 1
        find(i)

print('總共有' + str(group) + '組')