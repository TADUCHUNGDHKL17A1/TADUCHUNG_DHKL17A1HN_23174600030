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
