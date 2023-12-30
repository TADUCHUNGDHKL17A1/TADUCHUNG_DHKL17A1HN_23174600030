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

