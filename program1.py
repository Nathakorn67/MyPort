num1 = int(input("first number: ")) #เลขตัวที่1
num2 = int(input("Second number: ")) #เลขตัวที่2
Ans = (num1**num2)**0.5 #ยกกำลัง+ถอดรากที่2
if Ans > 0:
    print("เต็มบวก :", Ans)
elif Ans < 0:
    print("เต็มลบ :", Ans)
else:
    print("เต็มลบ :", Ans)