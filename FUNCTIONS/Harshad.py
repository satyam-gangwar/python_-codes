def harshad(b):
    for i in b:
        j=i
        sum=0
        while j>0:
            rem = j%10
            sum+=rem
            j//=10
        if i%sum==0:
            print(f'{i} is a harshad number')
        else:
            print(f'{i} is not harshad number')
a=eval(input('enter the list'))
harshad(a)
