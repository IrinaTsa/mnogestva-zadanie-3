p=input().split()
mas=set()
for i in p:
        if i in mas:
            print('да')
        else:
            print('нет')
            mas.add(i)
