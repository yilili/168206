"""
A：我没有偷钻石。
B：D就是罪犯。
C：B是盗窃这块钻石的罪犯。
D：B有意诬陷我。
假定只有一个人说的是真话，编程序判断谁偷走了钻石。
"""
arr= [ 'A', 'B', 'C', 'D' ]#分别装凶手的四种情况

def jiashe():
    for i in range(ord('A'),ord('D')+1):#从A到D一个一个假设是小偷
        print("假设",chr(i),"为真，那么：")
        if i==ord('A'):
            print("A为真，A没偷\nB为假，D没偷\nC为假，B没偷\nD为假，B为真，D偷了\n\n")
        elif i==ord('B'):
            print("A为假，A偷了\nB为真，D偷了\nC为假，B没偷\nD为假，B为真，D偷了\n\n")
        elif i==ord('C'):
            print("A为假，A偷了\nB为假，D没偷\nC为真，B偷了\nD为假，B为真，D偷了\n\n")
        elif i==ord('D'):
            print("A为假，A偷了\nB为假，D没偷\nC为假，B没偷\nD为真，B为假，D没偷\n\n")
def zhaoxiaotou():
    flag=0
    for j in arr:  
        if (j!='A')+(j=='D')+(j=='B')+(j!='D')==1:
            flag=1
            print("根据以上假设，说明是",j,"偷走了钻石\n\n")

    if(flag==0):
        print("没有找到小偷")

jiashe()
zhaoxiaotou()
