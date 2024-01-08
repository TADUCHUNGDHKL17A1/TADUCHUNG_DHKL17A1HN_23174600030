#bài 4.1
so = float(input(" Nhập giá trị: "))
if so > 0:
    binh_phuong = so ** 2
    print(f"Bình phương của {so} là {binh_phuong}")
else:
    print("Số không phải là số dương.")
#bài 4.2
N = int(8)
if N > 0:
   for i in range(1, N + 1):
    print(i)    
else:
  print("N phải là số tự nhiên dương")
#bài
m = eval(input("Nhập giá trị m: "))
n = eval(input("Nhập giá trị n: "))
if n <= m:
   print("Vui lòng nhập giá trị m nhỏ hơn n")
else:
      print(f"các số chia hết trong khoảng từ {m} đến {n} là :")
      for x in range(1 , n+1):
         if x % m == 0:
            print(x)
#
A = int(input("nhập số 1: "))
B = int(input("nhập số 2: "))
C = int(input("nhập số 3: "))
#tìm max
Max = A
if A > B:
   print("Max trong 3 số là: ", A)
#bài 4.5
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
result = bcnn(so1, so2)
print(f"BCNN của {so1} và {so2} là: {result}")
#bài 4.7
def tinh_tong_chu_so(N):
    chuoi_so = str(N)
    tong = 0
    for chu_so in chuoi_so:
        tong += int(chu_so)
    return tong
so_nguyen = int(input("Nhập một số nguyên: "))
tong_chu_so = tinh_tong_chu_so(so_nguyen)
print(f"Tổng các chữ số của {so_nguyen} là: {tong_chu_so}")

#bài 5.1 
print("** ** ****** **    **    ****")
print("** ** **     **    **    *  *")
print("***** ****** **    **    *  *")
print("** ** **     **    **    *  *")
print("***** ****** ****  ****  ****")
#bài 5.2
x=10
y=5
tong=x+y
hieu=x-y
thuong=x/y
tich=x*y
print(tong)
print(hieu)
print(thuong)
print(tich)
#bài 5.3
ten_hang="hộp sữa Vina Milk"
so_luong=5
don_gia=25000
tien_phai_tra=so_luong*don_gia
print("tên hàng",":",ten_hang)
print("số lượng",":",so_luong)
print("đơn giá",":",don_gia)
print("tiền phải trả",":",tien_phai_tra)
#bài 5.4
import math
a=int(input("nhập số đo cạnh a:"));
b=int(input("nhập số đo cạnh b:"));
c=int(input("nhập số đo cạnh c:"));
chuvi=a+b+c
p=chuvi/2
dien_tich=math.sqrt((p*(p-a)*(p-b)*(p-c)))
print("diện tích=", dien_tich)
#bài 6.1
print('**    **  ******  **      **      ******')
print('**    **  **      **      **      **  **')
print('********  ******  **      **      **  **')
print('**    **  **      **      **      **  **')
print('**    **  ******  ******  ******  ******')
#bài 6.2
x=10
y=5
print('x=10')
print('y=5')
print('tổng=',x+y)
print('Hiệu=',x-y)
print('Tích=',x*y)
print('thương=',x/y)
#bài 6.3
soluong=5
dongia=25000
thanhtien=soluong*dongia
print('tên hàng : sữa hộp vinamilk')
print('số lương',soluong)
print('dơn giá',dongia)
print('thành tiền',thanhtien)
#bài 6.4
a=(5-3)//2
b=8-(3*2)-(1+1)
print(a)
print(b)
#bài 6.5
a = int(input("nhập số lượng:"))
# nhap sl = 100
b = int(input("nhập đơn giá: "))
# nhap don gia = 5000
thanh_tien= a * b
print("thành tiền là :","\n",thanh_tien)
#bài 6.7
def c_to_f(DOC):
    DOF = (DOC * 9/5) + 32
    return DOF
DOC = float(input("Nhập nhiệt độ độ C: "))
DOF = c_to_f(DOC)
print(f"Nhiệt độ tương ứng ở độ F là: {DOF}°F")
#bài 6.8
a=(input("nhập chuỗi s1:"))
b=(input("nhập chuỗi s2:"))
c=(input("nhập chuỗi s3:"))
d=int(input("nhập index:"))
print("chiều dài chuỗi s1=",a)
print("chiều dài chuỗi s2=",b)
print("chiều dài chuỗi s3=",c)
print("chuỗi s4=",a[d:])
print("chuỗi s2 lặp lại 2 lần",b*2)
#bài 6.6
a=int(input("số kẹo alice có:",))
b=int(input("số kẹo bob có:",))
c=int(input("số kẹo carol có",))
print("số kẹo thừa:",(a+b+c)%3)
#bài 6.9
a=float(input("lãi suất 1 năm(%):"))
b=float(input("số tiền gửi:"))
c=float(input("số tháng gửi:"))
d=(b*c)*(a/100/12)
print("tiền lãi=",d)
print("tiền vốn+lãi",d+b)
#bài 7.1
x=int(input("nhập giá trị của x:"));
s=1+x+x**3/3+x**5/5
print("giá trị biểu thức s=1+x+x^3/3+x^5/5 là:",s)
#bài 7.2
result = 1+2
print('result=',result)
original_result = result
result = result - 1
print('result=',result)
original_result = result
result = result*2
original_result = result 
print('result=',result)
result = result**3
original_result = result
print('result=',result)
result = result+8
original_result = result
print('result=',result)
result = result % 7
original_result = result
print('result=',result)
result = result//2
original_result = result
print('result=',result)
#bài 7.3
result = 5
print('result=',result)
result -=1
print('result=',result)
result +=3
print('result=',result)
result = -result
print('result=',result)
result = True
print('not result=', not result)
#bài 7.4
x=10
y=4
print('x=%d,y=%d'%(x,y))
equivelence=x==y
print('x==y is',equivelence)
equivelence=x!=y
print('x!=y is',equivelence)
equivelence=x>y
print('x>y is',equivelence)
x=8
x=9
print('x=%d ,y=%d'%(x,y))
equivelence=x>=y
print('x>=y is',equivelence)
equivelence=x<y 
print('x<y is',equivelence)
equivelence=x<=y
print('x<=y is',equivelence)
#bài 7.5
x=15
y=12
print('Binary of x=', bin(x),',Binary of y=', bin(y))
print('x & y', bin(x&y))
print('x / y', bin(x|y))
print('x ^ y', bin(x^y))
print('~x=', bin(~x))
print('x << 2', bin(x<<2))
print('y >> 2', bin(y>>2))
#bài 7.6
x = True
y = False
print('x and y:',x and y)
print('x or y:',x or y)
print('not x:',not x)
print('x is y:',x is y)
print(' x is not y:', x is not y)
#bài 7.7 
x=int(input("nhập số tiền muốn đổi :"));
so_to1=x//500000
tien_con_lai=x%500000
print("số tờ 500k :",so_to1)
so_to2=tien_con_lai//200000
tien_con_lai=tien_con_lai%200000
print("số tờ 200k :",so_to2)
so_to3=tien_con_lai//100000
tien_con_lai=tien_con_lai%100000
print("số tờ 100k :",so_to3)
so_to4=tien_con_lai//50000
tien_con_lai=tien_con_lai%50000
print("số tờ 50k :",so_to4)
print("tiền còn lại ",tien_con_lai)

#bài 8.1
a = eval(input("nhập giá trị a:"))
b = eval(input("nhập giá trị b:"))
c = eval(input("nhập giá trị c:"))
d = eval(input("nhập giá trị d:"))
max_valua = max(a,b,c,d)
min_valua = min(a,b,c,d)
print("đây là số lớn  nhất:", max_valua)
print("đây là số nhỏ  nhất:", min_valua)
#bài 8.2
x = int(input("nhập giá trị của x:"))
abs_x = abs(x)
print("giá trị tuyệt đối của x là:",abs_x)
#bài 8.3
a=int(input("nhập a"));
b=int(input("nhập b"));
print("giải phương trình bậc nhât ax+b=0")
if(a==0 and b!=0):
    print(" phương trình vô nghiệm")
elif(a==0 and b==0):
    print("phương trình vô số nghiệm")
else:
    x=(-b)/a
    print("phương trinh có nghiệm x",x)
#bài 8.4
import math
a=float(input("nhập cạnh a :"));
b=float(input("nhập cạnh b :"));
c=float(input("nhập cạnh c :"));
p=(a+b+c)/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("diện tích tam giác ",p)
#bài 8.5
x=int(input("nhập năm :"));
if ((x%4==0 and x%100!=0)or(x%400==0)):
    print("đây là năm nhuận")
else:
    print("đây không phải năm nhuận")
#bài 8.6
loaixe=int(input("nhập loại xe 4 chỗ hoặc 7 chỗ :"));
sokm=int(input("nhập số km :"));
tgtro=int(input("nhập thời gian chờ :"));
if (tgtro >=5):
    tientro=(tgtro-5)*800
    print("tiền chờ ",tientro)
else:
    tientro=800*0
    print("05 phút đầu được miễn phí tiền trờ",tientro)
if(loaixe ==4):
    if(sokm<=20):
        tiendichuyen=12100*sokm
        tiencuoc=(tiendichuyen+tientro)
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
    else:
        tiendichuyen=(20*12100)+((sokm-20)*10000)
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
if(loaixe==7):
    if(sokm<=30):
        tiendichuyen=14100*sokm
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
    else:
        tiendichuyen=(30*14100)+((sokm-30)*12000)
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
#bài 8.7
x=int(input("nhập số điện :"));
if(x>0 and x<=50):
    td=x*1.678
    print("số tiền điện là :",td )
elif(x>=51 and x<=100):
    td=(50*1.678)+((x-50)*1.734)
    print("số tiền điện là :",td )
elif(x>=101 and x<=200):
    td=(50*1.678)+(50*1.734)+((x-100)*2.014)
    print("số tiền điện là :",td )
elif(x>=201 and x<=300):
    td=(50*1.678)+(50*1.734)+(100*2.014)+((x-200)*2.536)
    print("số tiền điện là :",td )
elif(x>=301 and x<=400):
    td=(50*1.678)+(50*1.734)+(100*2.014)+(100*2.536)+((x-300)*2.834)
    print("số tiền điện là :",td )
else:
    td=(50*1.678)+(50*1.734)+(100*2.014)+(100*2.536)+(100*2.834)+((x-400)*2.927)
    print("số tiền điện là :",td )
#bài 8.8
lp=int(input("nhập loại phòng từ 1-8:"));
sd=int(input(" nhập số đêm "));
if (lp ==1 ):
    print(" tên phòng Standard")
    if (sd >=2 and sd <= 3):
        tt=(1260000-(1260000*0.25))*sd
        print(" thành tiền =",tt)
    elif (sd >= 4):
        tt=(1260000-(1260000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=sd*1260000
        print(" thành tiên =",tt)
if (lp ==2):
    print(" tên phòng superior Garden View")
    if (sd>=2 and sd <=3):
        tt=(1550000-(1550000*0.25))*sd
        print(" thành tiên =",tt)
    elif(sd>=4):
        tt=(1550000-(1550000*0.3))*sd
        print(" thành tiên =",tt)
    else:
        tt=1550000*sd
        print(" thành tiền =",tt)
if(lp ==3):
    print("tên phòng Super Ocean View")
    if (sd >=2 and sd <=3):
        tt=(1830000-(1830000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd >=4):
        tt=(1830000-(1830000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=1830000*sd
        print(" thành tiền =",tt)
if(lp ==4):
    print("tên phòng Garden View Bungalow")
    if (sd >=2 and sd <=3):
        tt=(1830000-(1830000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd >=4):
        tt=(1830000-(1830000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=1830000*sd
        print(" thành tiền =",tt)
if(lp==5):
    print("tên phòng Pool View Bungalow")
    if (sd>=2 and sd<=3):
        tt=(2120000-(2120000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd>=4):
        tt=(2120000-(2120000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=2120000*sd
        print(" thành tiền =",tt)
if(lp==6):
     print("tên phòng Family Room ")
     if (sd>=2 and sd<=3):
            tt=(2120000-(2120000*0.25))*sd
            print(" thành tiền =",tt)
     elif(sd>=4):
            tt=(2120000-(2120000*0.3))*sd
            print(" thành tiền =",tt)
     else:
            tt=2120000*sd
            print(" thành tiền =",tt)
if (lp==7):
    print("tên phòng Beach Front Bungalow")
    if(sd>=2 and sd<=3):
        tt=(2540000-(2540000*0.25))*sd
        print(" thanh tiền =",tt)
    elif(sd>=4):
        tt=(2540000-(2540000*0.3))*sd
        print("  thành tiền =",tt)
    else:
        tt=2540000*sd
        print(" thành tiền =",tt)
if(lp==8):
    print("tên phòng VIP sea View")
    if (sd>=2 and sd<=3):
        tt=(4800000-(4800000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd>=4):
        tt=(4800000-(4800000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=4800000*sd
        print(" thành tiền =",tt)     
#bài 8.9
import time
def countdown (seconds) :
    while seconds > 0 :
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Countdown finished!")
countdown(10)
#bài 8.10
n=float(input("nhập số n :"));
x=float(input("nhập số x :"));
print(" tính giá trị biểu thức s=(x^2 + 1)^n ")
s=(x*x + 1)**n
print(" giá trị biểu thức :",s)
#bài 8.11
n=float(input("nhập số n:"));
x=float(input("nhập số x:"));
A=(x**x + x + 1)**n +(x**x - x +1)**n
print("giá trị của biểu thức A :", A)
#bài 8.12
def is_prime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True
n=int(input("nhập số tự nhiên "));
if is_prime(n):
    print(f"{n} là số nguyên tố ")
else:
    print(f"{n} không phải là số nguyên tố ")
#8.13
# A = tổng các số lẻ nhỏ hơn hoặc bằng n
# B = tổng các số chẵn nhỏ hơn hay bằng n
# C = tích các số từ 1 đến n
# D = tích các số chia hết cho 3
# E = tổng các cố nguyên tố nhỏ hơn hay bằng n
# F = tổng chuỗi đan dấu
import math
n = int(input("nhập số N: "))
def A(n):
    j = []
    a = 0
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a + v
    return print("A = ",a)
def B(n):
    j = []
    a = 0
    for i in range(1,n):
        if i%2==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("B = ",a)
def C(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a*v
    return print("C = ",a)
def D(n):
    j = []
    a = 1
    for i in range(1,n):
        if i%3==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("D = ",a)
def E(n):
    j = []
    a = 0
    for i in range(2,n+1):
        if i>0:
            for k in range(2,int(math.sqrt(i))+1):
                if i%k ==0:
                    break
            else:
                j.append(i)
    for v in j:
        a = a + v
    print("E = ",a)    
def F(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i**-1)
    for v in j:
        if i%2==0:
            a = a + v
        else:
            a = a - v 
    return print("F = ",a - 1)
A(n)
B(n)
C(n)
D(n)
E(n)
F(n)
#bài 8.14
a = int(input("nhập số nguyên thứ 1:"))
b = int(input("nhập số nguyên thứ 2:"))
c = int(input("nhập số nguyên thứ 3:"))
S = a + b + c
print(f"S = {S}")
#bài 8.15
total = 0
while True:
    try:
        num = int(input("Nhập số nguyên (nhập 0 để kết thúc):"))
        if num == 0:
            break
        total += num
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ")
print("S=:", total)
#bài 8.16
def find_gcd(a,b):
    while b:
        a, b = b, a % b
    return a
a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
gdc = find_gcd(a,b)
print(f"UCLN của {a} và {b} là: {find_gcd}")
#bài 8.17
def tim_ucln(a,b):
    while b:
        a,b = b,a%b
    return a
def tim_bcnn(a, b):
    return a* b// tim_ucln(a,b)
a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
print(f"BCLN của {a} và {b} là {tim_bcnn(a,b)}")
#bài 8.18
def kiem_tra_so_hoan_hao(x):
    tong = 0
    for i in range(1,x):
        if x % i == 0:
            tong +=i
    return tong == x 
x = int(input("Nhập một số x:"))
if kiem_tra_so_hoan_hao(x):
    pritn(f"{x} là số hoàn hảo.")
else:
    print(f"{x} không phải là số hoàn hảo")
#bài 8.19
def dao_nguoc_day_so_so_le(n):
    day_so = list(range(1,2*n, 2))
    day_so_dao_nguoc = day_so[::-1]
    return day_so_dao_nguoc 
so_luong = int(input("Nhập số lượng số trong dãy:"))
ket_qua = dao_nguoc_day_so_so_le(so_luong)
print("Dãy số đâỏ ngược:", ket_qua)
#bài 8.20
import math
x=int(input("Nhap x:"))
ex=1
n=1
t=x
while math.fabs(t)>=0.0001:
    ex +=t
    n +=1
    t *=(x/n)
print("Gia tri gan dung cua e mu x la:",ex)
# bài 9.1
def tinh_nam_am_lich(nam_duong_lich):
    can = ["Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm"]
    chi = ["Hợi", "Tí", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất"]

    can_index = (nam_duong_lich - 4) % 10
    chi_index = (nam_duong_lich - 4) % 12

    nam_am_lich = "{} {}".format(can[can_index], chi[chi_index])

    return nam_am_lich

# Ví dụ sử dụng hàm
nam_duong_lich = 2023
nam_am_lich = tinh_nam_am_lich(nam_duong_lich)

print("Năm âm lịch tương ứng với năm {} là: {}".format(nam_duong_lich, nam_am_lich))
# bài 9.1
def tinh_nam_am_lich(nam_duong_lich):
    can = ["Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm"]
    chi = ["Hợi", "Tí", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất"]

    can_index = (nam_duong_lich - 4) % 10
    chi_index = (nam_duong_lich - 4) % 12

    nam_am_lich = "{} {}".format(can[can_index], chi[chi_index])

    return nam_am_lich

# Ví dụ sử dụng hàm
nam_duong_lich = int(input("nhập năm :"))
nam_am_lich = tinh_nam_am_lich(nam_duong_lich)

print("Năm âm lịch tương ứng với năm {} là: {}".format(nam_duong_lich, nam_am_lich))

# 9.3
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/(chieu_cao*chieu_cao)
    if bmi < 18.5:
        print("chỉ số bmi cua bạn là", bmi ,"(gầy)")
    elif (bmi>=18.5 and bmi<=24.99):
        print("chỉ số bmi của bạn là", bmi ," (bình thường)" )
    else:
        print("chỉ số bmi của bạn là", bmi ,"(thừa cân)" )
    return bmi
w=float(input("cho biết cân nặng của bạn :"))
h=float(input("cho biết chiều cao của bạn :"))
tinh_bmi(can_nang=w,chieu_cao=h)
    
#bài 9.4
n=int(input(" nhập n :"))
x=int(input("nhập x :"))
s=(x**2 +1)**n
print(s)
#bài 9.5
n=int(input(" nhập n :"))
x=int(input("nhập x :"))
A=((x**2+x+1)**n +(x**2-x+1)**n)
print(A)
# bài 9.6
# hàm kiểm tra số nguyên tố
def tinh_so_nt(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
n=int(input("nhập số tự nhiên :"))
if tinh_so_nt(n):
    print(n,"là số nguyên tố ")
else:
    print(n,"không phải là số nguyên tố ")

# bài 9.7
def phan_nguyen_phep_chia(a, b):
    if b == 0:
        return "Lỗi: Không thể chia cho 0"
    
    ket_qua = a // b
    return ket_qua

# Ví dụ sử dụng hàm
so_chia = int(input("nhập số chia :"))
so_bi_chia = int(input("nhập số bị chia"))

ket_qua_phep_chia = phan_nguyen_phep_chia(so_chia, so_bi_chia)
print("Phần nguyên của {}/{} là: {}".format(so_chia, so_bi_chia, ket_qua_phep_chia))
# Bài 9.8
def la_so_hoan_hao(so):
    if so <= 0:
        return False

    tong_uoc_so = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc_so += i

    return tong_uoc_so == so

# Ví dụ sử dụng hàm
so_kiem_tra = int(input("nhập số kiểm tra :"))
ket_qua = la_so_hoan_hao(so_kiem_tra)

if ket_qua:
    print("{} là số hoàn hảo.".format(so_kiem_tra))
else:
    print("{} không phải là số hoàn hảo.".format(so_kiem_tra))
# Bài 9.9
# Hàm tính diện tích và chu vi của hình tròn
tinh_dien_tich_chu_vi_hinh_tron = lambda r: (3.14159 * r**2, 2 * 3.14159 * r)

# Hàm tính diện tích và chu vi của hình chữ nhật
tinh_dien_tich_chu_vi_hinh_chu_nhat = lambda a, b: (a * b, 2 * (a + b))

# Ví dụ sử dụng hàm cho hình tròn
ban_kinh_hinh_tron = int(input("nhập bán kính r :"))
dien_tich_hinh_tron, chu_vi_hinh_tron = tinh_dien_tich_chu_vi_hinh_tron(ban_kinh_hinh_tron)
print("Diện tích hình tròn:", dien_tich_hinh_tron)
print("Chu vi hình tròn:", chu_vi_hinh_tron)

# Ví dụ sử dụng hàm cho hình chữ nhật
chieu_dai_hinh_chu_nhat = int(input("nhập chiêu dài hình chữ nhật :"))
chieu_rong_hinh_chu_nhat = int(input("nhập chiều rộng hình chữ nhật :"))
dien_tich_hinh_chu_nhat, chu_vi_hinh_chu_nhat = tinh_dien_tich_chu_vi_hinh_chu_nhat(chieu_dai_hinh_chu_nhat, chieu_rong_hinh_chu_nhat)
print("Diện tích hình chữ nhật:", dien_tich_hinh_chu_nhat)
print("Chu vi hình chữ nhật:", chu_vi_hinh_chu_nhat)
# 10.1
a,b,c,d=eval(input("Nhập  a,b,c,d :"))
print("giá trị lớn nhất là :",max(a,b,c,d))
# 10.2
x=int(input(" Nhập x :"))
print("|x| = ",abs(x))
# 10.3
import math
n=int(input("Nhập giá trị của n :"))
x=int(input("Nhập giá trị của x :"))
s=(math.pow(x,2)+1)*n
print(s)
# 10.4
import math
n=int(input("Nhập giá trị của n :"))
x=int(input("Nhập giá trị của x :"))
A=(math.pow((math.pow(x,2)+x+1),n)+math.pow(math.pow(x,2)-x+1,n))
print(A)
# 10.5
def kiem_tra_zip_code(zip_code):
    """
    Kiểm tra dữ liệu ZIP code ở Việt Nam.

    Parameters:
    - zip_code (str): Mã vùng cần kiểm tra.

    Returns:
    - True nếu ZIP code hợp lệ, False nếu không hợp lệ."
    """
    if not isinstance(zip_code, str):
        return False
    
    # Kiểm tra độ dài của ZIP code (mã vùng Việt Nam có độ dài 6 ký tự)
    if len(zip_code) != 6:
        return False

    # Kiểm tra xem tất cả các ký tự có phải là số không
    if not zip_code.isdigit():
        return False

    return True

# Sử dụng hàm kiểm tra
zip_code = "700000"
if kiem_tra_zip_code(zip_code):
    print(f"{zip_code} là mã vùng hợp lệ.")
else:
    print(f"{zip_code} không phải là mã vùng hợp lệ.")

# 10.6
import math
 
print("Giải phương trình bậc 2: ax2 + bx + c = 0 (a, b khác 0)")

# Nhập số a, b và kiểm tra điều kiện khác 0
a = float(input("Mời bạn nhập hệ số a: "))
while True:
    if a == 0:
        a = float(input("Số a phải khác 0. Mời nhập lại số a: "))
    else:
        break
    
b = float(input("Mời bạn nhập hệ số b: "))
while True:
    if b == 0:
        b = float(input("Số b phải khác 0. Mời nhập lại số b: "))
    else:
        break
    
# Nhập số c
c = float(input("Mời bạn nhập hệ số c: "))

# Tính Delta
delta = b**2 - 4 * a * c

# Tìm nghiệm của phương trình
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) )
# 10.7
import string

def xu_ly_chuoi(chuoi):
    """
    Xử lý chuỗi theo yêu cầu:
    - Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
    - In chuỗi với ký tự đầu viết hoa.
    - Đếm và in ra số lần chuỗi con xuất hiện trong chuỗi.
    - Nhập từ muốn thay thế và từ thay thế, in ra chuỗi đã thay thế.

    Parameters:
    - chuoi (str): Chuỗi cần xử lý.

    Returns:
    - None.
    """
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    chuoi = chuoi.strip()

    # In chuỗi với ký tự đầu viết hoa
    chuoi_in_hoa = chuoi.capitalize()
    print(f"Chuỗi sau khi in hoa: {chuoi_in_hoa}")

    # Đếm và in ra số lần chuỗi con xuất hiện trong chuỗi
    chuoi_con = input("Nhập chuỗi con cần kiểm tra: ")
    so_lan_xuat_hien = chuoi.count(chuoi_con)
    print(f"Số lần chuỗi con '{chuoi_con}' xuất hiện trong chuỗi: {so_lan_xuat_hien}")

    # Nhập từ muốn thay thế và từ thay thế
    tu_thay_the = input("Nhập từ muốn thay thế: ")
    tu_thay_the_bang = input(f"Nhập từ thay thế '{tu_thay_the}' bằng: ")

    # Thực hiện thay thế và in ra chuỗi đã thay thế
    chuoi_thay_the = chuoi.replace(tu_thay_the, tu_thay_the_bang)
    print(f"Chuỗi sau khi thay thế: {chuoi_thay_the}")

# Sử dụng hàm
chuoi_input = input("Nhập chuỗi cần xử lý: ")
xu_ly_chuoi(chuoi_input)
import string

def xu_ly_chuoi(chuoi):

    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    chuoi = chuoi.strip()

    # In chuỗi với ký tự đầu viết hoa
    chuoi_in_hoa = chuoi.capitalize()
    print(f"Chuỗi sau khi in hoa: {chuoi_in_hoa}")

    # Đếm và in ra số lần chuỗi con xuất hiện trong chuỗi
    chuoi_con = input("Nhập chuỗi con cần kiểm tra: ")
    so_lan_xuat_hien = chuoi.count(chuoi_con)
    print(f"Số lần chuỗi con '{chuoi_con}' xuất hiện trong chuỗi: {so_lan_xuat_hien}")

    # Nhập từ muốn thay thế và từ thay thế
    tu_thay_the = input("Nhập từ muốn thay thế: ")
    tu_thay_the_bang = input(f"Nhập từ thay thế '{tu_thay_the}' bằng: ")

    # Thực hiện thay thế và in ra chuỗi đã thay thế
    chuoi_thay_the = chuoi.replace(tu_thay_the, tu_thay_the_bang)
    print(f"Chuỗi sau khi thay thế: {chuoi_thay_the}")

# Sử dụng hàm
chuoi_input = input("Nhập chuỗi cần xử lý: ")
xu_ly_chuoi(chuoi_input)
# Bài 11.1
a=[1,2,3]
b=[1,[2,3]]
c=[]
d=[1,2,3][1:]
print("Độ dài danh sách a là :",len(a))
print("Độ dài danh sách b là :",len(b))
print("Độ dài danh sách c là :",len(c))
print("Độ dài danh sách d là :",len(d))
# Bài 11.2
teams=[['Steven','Neena','Lex','Alexander','Bruce'],['David','jack','Bill','Tom','Mike','Daniel'],['Alexander','Adam','Payam','Kevin','Sigal','Mike']]
print("Đội trưởng tệ nhất là Adam ")
# Bài 11.3
List_of_animal =['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("List of animal :",List_of_animal)
print("Number of animal :",len(List_of_animal))
n=input("I want to find :")
for animal in List_of_animal:
    if animal==n :
        print("there is ",animal,'in List of animal ')
# Bài 11.4
def nhap_list():
    danh_sach_list=[]
    while True :
        gia_tri_list=input("Nhập giá trị :")
        danh_sach_list.append(gia_tri_list)

        n=int(input("Tiếp tục nhập giá trị ? (1: có , 0: không) :"))
        if n!=1 :
            break
    return danh_sach_list

nhap_gia_tri=nhap_list()
print("List :",nhap_gia_tri)
x=input("nhập vào số x")
for num in nhap_gia_tri :
    if num==x:
        print(x,"có xuất hiện trong list ")
        print(x," xuất hiện ",nhap_gia_tri.count(x)," lần trông list ")
    else:
        print(x,"không xuất hiện trong list ")
        break

for num in nhap_gia_tri:
    if x < num :
        list_lon=[]
        list_lon.append(num)
        print("các số lớn hơn ",num,"trong list là ",list_lon)
    else: 
        print("không có số nào lớn hơn x")
# Bài 11.5
      
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def xu_ly_list():
    danh_sach = []
    so_luong = int(input("Nhập số lượng phần tử trong list: "))

    for _ in range(so_luong):
        phan_tu = int(input("Nhập phần tử mới: "))
        danh_sach.append(phan_tu)

    print("Danh sách ban đầu:", danh_sach)

    while True:
        tiep_tuc = int(input("Bạn muốn nhập tiếp không? (1: Có, 0: Không): "))
        if tiep_tuc == 0:
            break
        elif tiep_tuc == 1:
            phan_tu_moi = int(input("Nhập phần tử mới: "))
            danh_sach.append(phan_tu_moi)

    so_nguyen_to = [x for x in danh_sach if la_so_nguyen_to(x)]
    print("Các số nguyên tố trong danh sách:", so_nguyen_to)

    phan_tu_am = [x for x in danh_sach if x < 0]
    phan_tu_duong = [x for x in danh_sach if x >= 0]

    trung_binh_am = sum(phan_tu_am) / len(phan_tu_am) if phan_tu_am else 0
    trung_binh_duong = sum(phan_tu_duong) / len(phan_tu_duong) if phan_tu_duong else 0

    print(f"Trung bình cộng các phần tử âm: {trung_binh_am}")
    print(f"Trung bình cộng các phần tử dương: {trung_binh_duong}")

    max_value = max(danh_sach, default=None)
    min_value = min(danh_sach, default=None)

    print(f"Giá trị lớn nhất trong danh sách: {max_value}")
    print(f"Giá trị nhỏ nhất trong danh sách: {min_value}")

    danh_sach.sort()
    print("Danh sách sau khi sắp xếp tăng dần:", danh_sach)

# Sử dụng hàm
xu_ly_list()

# bài 11.6
def inch_to_meter(height_inch):
    return height_inch * 0.0254

def xu_ly_list_chieu_cao():
    chieu_cao_inch = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]

    # Chuyển đổi inch sang mét
    chieu_cao_met = [inch_to_meter(chieu) for chieu in chieu_cao_inch]

    # In 3 chiều cao đầu tiên
    print("3 chiều cao đầu tiên:", chieu_cao_met[:3])

    # In 3 chiều cao cuối cùng
    print("3 chiều cao cuối cùng:", chieu_cao_met[-3:])

    # In chiều cao trung bình
    chieu_cao_trung_binh = sum(chieu_cao_met) / len(chieu_cao_met)
    print(f"Chiều cao trung bình: {chieu_cao_trung_binh:.2f} mét")

    # In chiều cao lớn nhất và nhỏ nhất
    chieu_cao_lon_nhat = max(chieu_cao_met)
    chieu_cao_nho_nhat = min(chieu_cao_met)
    print(f"Chiều cao lớn nhất: {chieu_cao_lon_nhat:.2f} mét")
    print(f"Chiều cao nhỏ nhất: {chieu_cao_nho_nhat:.2f} mét")

    # Sắp xếp list theo thứ tự tăng dần và giảm dần
    chieu_cao_met_tang_dan = sorted(chieu_cao_met)
    chieu_cao_met_giam_dan = sorted(chieu_cao_met, reverse=True)

    print("Danh sách sau khi sắp xếp tăng dần:", chieu_cao_met_tang_dan)
    print("Danh sách sau khi sắp xếp giảm dần:", chieu_cao_met_giam_dan)

# Sử dụng hàm
xu_ly_list_chieu_cao()

# Bài 11.7
L =[1,2,3,4]
thresh =2
print(elementwise_greater_than(L,thresh)) 

# Bài 11.8
def has_lucky_numbers(nums):
    return any(num % 7 == 0 for num in nums)
danh_sach = [2, 14, 8, 5, 21, 6]
ket_qua = has_lucky_numbers(danh_sach)

if ket_qua:
    print("Danh sách có chứa số may mắn.")
else:
    print("Danh sách không chứa số may mắn.")
 # Bài 11.9
# Bài 11.11
def xu_ly_tuple():
    # Tạo một tuple có 10 phần tử chuỗi bất kỳ
    my_tuple = ("red", "green", "yellow", "blue", "black", "while", "pink", "orange", "red", "blue")

    # In ra tuple
    print("Tuple:", my_tuple)

    # Nhập index dương
    index_duong = int(input("Nhập một index dương (0 <= index < 10): "))
    if 0 <= index_duong < 10:
        print(f"Phần tử tại index {index_duong}: {my_tuple[index_duong]}")
    else:
        print("Index không hợp lệ.")

    # Nhập index âm
    index_am = int(input("Nhập một index âm (-1 >= index >= -9): "))
    if -10 <= index_am <= -1:
        print(f"Phần tử tại index {index_am}: {my_tuple[index_am]}")
    else:
        print("Index không hợp lệ.")

    # Nhập chuỗi cần tìm
    s_find = input("Nhập chuỗi cần tìm: ")

    # Tìm và in ra vị trí của chuỗi trong tuple (nếu có)
    vi_tri = [i for i, item in enumerate(my_tuple) if s_find in item]
    if vi_tri:
        print(f"Chuỗi '{s_find}' xuất hiện ở vị trí: {vi_tri}")
        print(f"Số lần xuất hiện của '{s_find}' trong tuple: {len(vi_tri)}")
    else:
        print(f"Chuỗi '{s_find}' không xuất hiện trong tuple.")

# Sử dụng hàm
xu_ly_tuple()

# Bài 11.12
# Tạo tuple a chứa 4 số nguyên dương đầu tiên
a = (3, 1, 2, 4)

# Tạo tuple b chứa 4 số nguyên dương tiếp theo
b = (5, 7, 6, 8)

# Tạo tuple c là sự kết hợp của các phần tử trong tuple a và tuple b
c = a + b

# Tạo tuple d từ tuple c với các phần tử được xắp xếp
d = tuple(sorted(c))

# In ra phần tử thứ 3 của d
print(f"Phần tử thứ 3 của d: {d[2]}")

# In ra 3 phần tử cuối cùng của d
print(f"3 phần tử cuối cùng của d: {d[-3:]}")
# 13.1
try:
    # Nhập tên tập tin từ người dùng
    ten_tap_tin = input("Nhập tên tập tin muốn đọc: ")

    # Mở tập tin trong chế độ đọc
    with open(ten_tap_tin, 'r', encoding='utf-8') as file:
        # Đọc nội dung của tập tin
        noi_dung = file.read()

        # In nội dung
        print("Nội dung của tập tin:")
        print(noi_dung)

except FileNotFoundError:
    print(f"Tập tin '{ten_tap_tin}' không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

# 13.2
import re

try:
    # Nhập tên tập tin từ người dùng
    ten_tap_tin = input("Nhập tên tập tin muốn đọc: ")

    # Mở tập tin trong chế độ đọc
    with open(ten_tap_tin, 'r', encoding='utf-8') as file:
        # Đọc nội dung của tập tin
        noi_dung = file.read()

        # Đếm số dòng
        so_dong = noi_dung.count('\n') + 1

        # Đếm số ký tự
        so_ky_tu = len(noi_dung)

        # Đếm số từ
        so_tu = len(re.findall(r'\b\w+\b', noi_dung))

        # In thông tin
        print(f"Số dòng: {so_dong}")
        print(f"Số ký tự: {so_ky_tu}")
        print(f"Số từ: {so_tu}")

except FileNotFoundError:
    print(f"Tập tin '{ten_tap_tin}' không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

# Bài 13.3
tep_tep=input("Nhập tên tập tin :")
with open(tep_tep,'w',encoding='utf-8') as file:
    a=input("Nhập nội dung cần nhập ")
    file.write(a)
    print("Đã ghi nội dung nhập vào tập tin ",tep_tep,"là \n",a)
file.close()

# Bài 13.4

try:
    # Nhập tên tập tin từ người dùng
    ten_tap_tin = input("Nhập tên tập tin muốn tạo hoặc ghi đè: ")

    # Nhập nội dung từ người dùng
    print("Nhập nội dung (Nhấn Enter để kết thúc nhập):")
    noi_dung = []
    while True:
        dong = input()
        tieptuc=int(input("Bạn có muốn tiếp tục nhập nội dung vào file ? (1:Có , 0:Không) "))
        if tieptuc!=1 :
            break
        noi_dung.append(dong)

    # Ghi nội dung vào tập tin
    with open(ten_tap_tin, 'w', encoding='utf-8') as file:
        file.write('\n'.join(noi_dung))

    print(f"Tập tin '{ten_tap_tin}' đã được tạo hoặc ghi đè thành công.")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

# Bài 13.5
# đọc file csv 
import csv

def doc_tep_csv(ten_tep):
    try:
        with open(ten_tep, 'r', newline='', encoding='utf-8') as file_csv:
            doc_csv = csv.reader(file_csv)
            for hang in doc_csv:
                print(hang)
    except FileNotFoundError:
        print(f"Tệp {ten_tep} không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Nhập tên tệp CSV từ người dùng
ten_tep_csv = input("Nhập tên tệp CSV: ")

# Gọi hàm để đọc và in ra nội dung tệp CSV
doc_tep_csv(ten_tep_csv)

# Bài 13.6 
import csv

def ghi_danh_sach_sdt(ten_tep, danh_sach_sdt):
    try:
        with open(ten_tep, 'a', newline='', encoding='utf-8') as file_csv:
            ghi_csv = csv.writer(file_csv)
            ghi_csv.writerow(danh_sach_sdt)
        print("Ghi danh sách số điện thoại thành công.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Nhập tên tệp CSV từ người dùng
ten_tep_csv = input("Nhập tên tệp CSV: ")

# Nhập danh sách số điện thoại từ người dùng (các số cách nhau bằng dấu phẩy)
danh_sach_sdt = input("Nhập danh sách số điện thoại (cách nhau bằng dấu phẩy): ").split(',')

# Gọi hàm để ghi danh sách số điện thoại vào tệp CSV
ghi_danh_sach_sdt(ten_tep_csv, danh_sach_sdt)
# Bài 14.1
def kiem_tra_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài các cạnh phải là số dương và khác 0.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Độ dài các cạnh không thỏa mãn là một tam giác.")

    # Nếu không có ngoại lệ, thông báo là tam giác hợp lệ
    print("Đây là một tam giác hợp lệ.")

try:
    # Nhập độ dài các cạnh từ người dùng
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))

    # Gọi hàm kiểm tra tam giác
    kiem_tra_tam_giac(a, b, c)

except ValueError as ve:
    print(f"Lỗi: {ve}")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

# Bài 14.2
class InputError(Exception):
    pass

def nhap_so_nguyen_duong():
    while True:
        try:
            so_nguyen = int(input("Nhập một số nguyên dương (nhập 0 để kết thúc): "))
            
            if so_nguyen == 0:
                break  # Kết thúc khi nhập 0
            
            if so_nguyen < 0:
                raise InputError("Lỗi: Số không được là số nguyên âm.")
            
            if 'prev_input' in locals() and so_nguyen == prev_input:
                raise InputError("Lỗi: Bạn đã nhập 4 số nguyên dương giống nhau liên tiếp.")
            
            prev_input = so_nguyen
            
            print("Nhập thành công:", so_nguyen)

        except ValueError:
            print("Lỗi: Bạn đã nhập một chuỗi không phải số nguyên.")
        
        except InputError as ie:
            print(ie)

        



