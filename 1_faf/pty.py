import os
import hashlib
import shutil
import threading
from tkinter import Tk, Label, Button, Entry, Text, Frame, filedialog, messagebox

def log(msg):
    log_text.insert("end", msg + "\n")
    log_text.see("end")

def 선택_폴더(entry):
    폴더 = filedialog.askdirectory()
    if 폴더:
        entry.delete(0, "end")
        entry.insert(0, 폴더)
        log(f"선택된 폴더: {폴더}")

def 파일_해시_계산(파일_경로):
    hash_algo = hashlib.sha256()
    try:
        with open(파일_경로, 'rb') as f:
            while chunk := f.read(8192):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()
    except Exception as e:
        log(f"해시 계산 실패: {파일_경로}, 오류: {e}")
        return None

def GUI_작업_실행(task):
    thread = threading.Thread(target=task)
    thread.start()

def 이미지_이름_변경():
    def 작업():
        폴더 = source_entry.get().strip()
        새이름 = rename_entry.get().strip()
        if not 폴더 or not 새이름:
            messagebox.showerror("오류", "폴더와 새 이름을 모두 입력하세요.")
            return
        try:
            files = [f for f in os.listdir(폴더) if f.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tif'))]
            if not files:
                raise Exception("이미지 파일이 없습니다.")
            for i, file in enumerate(files, 1):
                확장자 = os.path.splitext(file)[1]
                새파일 = f"{새이름}_{i:07}{확장자}"
                os.rename(os.path.join(폴더, file), os.path.join(폴더, 새파일))
                log(f"{file} -> {새파일}")
            messagebox.showinfo("완료", "이미지 이름 변경 완료!")
        except Exception as e:
            log(f"오류: {e}")
            messagebox.showerror("오류", str(e))
    GUI_작업_실행(작업)

def 파일_이동():
    def 작업():
        소스 = source_entry.get().strip()
        대상 = dest_entry.get().strip()
        if not 소스 or not 대상:
            messagebox.showerror("오류", "소스와 대상 폴더를 모두 입력하세요.")
            return
        try:
            if not os.path.exists(대상):
                os.makedirs(대상)
            files = os.listdir(소스)
            if not files:
                raise Exception("이동할 파일이 없습니다.")
            for file in files:
                shutil.move(os.path.join(소스, file), os.path.join(대상, file))
                log(f"{file} -> {대상}로 이동")
            messagebox.showinfo("완료", "파일 이동 완료!")
        except Exception as e:
            log(f"오류: {e}")
            messagebox.showerror("오류", str(e))
    GUI_작업_실행(작업)

def 중복_이미지_삭제():
    def 작업():
        폴더 = source_entry.get().strip()
        if not 폴더:
            messagebox.showerror("오류", "폴더를 선택하세요.")
            return
        try:
            파일_목록 = [os.path.join(폴더, f) for f in os.listdir(폴더) if f.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tif', 'gif'))]
            if not 파일_목록:
                log("이미지 파일이 없습니다.")
                messagebox.showinfo("결과", "이미지 파일이 없습니다.")
                return
            해시_데이터 = {}
            삭제된_파일 = 0
            for 파일 in 파일_목록:
                파일_해시 = 파일_해시_계산(파일)
                if 파일_해시 is None:
                    continue
                if 파일_해시 in 해시_데이터:
                    os.remove(파일)
                    삭제된_파일 += 1
                    log(f"중복 파일 삭제: {파일}")
                else:
                    해시_데이터[파일_해시] = 파일
            if 삭제된_파일 == 0:
                log("중복된 파일이 없습니다.")
                messagebox.showinfo("결과", "중복된 파일이 없습니다.")
            else:
                log(f"{삭제된_파일}개의 중복 파일이 삭제되었습니다.")
                messagebox.showinfo("완료", f"{삭제된_파일}개의 중복 파일이 삭제되었습니다.")
        except Exception as e:
            log(f"오류: {e}")
            messagebox.showerror("오류", str(e))
    GUI_작업_실행(작업)

# GUI 생성
root = Tk()
root.title("파일 관리 도구")
root.geometry("700x800")

Label(root, text="파일 관리 도구", font=("Arial", 18, "bold")).pack(pady=10)

folder_frame = Frame(root)
folder_frame.pack(pady=10, fill="x")
Label(folder_frame, text="소스 폴더", width=15, anchor="w").grid(row=0, column=0, padx=5, pady=5)
source_entry = Entry(folder_frame, width=50)
source_entry.grid(row=0, column=1, padx=5, pady=5)
Button(folder_frame, text="선택", command=lambda: 선택_폴더(source_entry)).grid(row=0, column=2, padx=5, pady=5)

Label(folder_frame, text="대상 폴더", width=15, anchor="w").grid(row=1, column=0, padx=5, pady=5)
dest_entry = Entry(folder_frame, width=50)
dest_entry.grid(row=1, column=1, padx=5, pady=5)
Button(folder_frame, text="선택", command=lambda: 선택_폴더(dest_entry)).grid(row=1, column=2, padx=5, pady=5)

rename_frame = Frame(root)
rename_frame.pack(pady=10, fill="x")
Label(rename_frame, text="새 이름 입력", width=15, anchor="w").grid(row=0, column=0, padx=5, pady=5)
rename_entry = Entry(rename_frame, width=50)
rename_entry.grid(row=0, column=1, padx=5, pady=5)

button_frame = Frame(root)
button_frame.pack(pady=20, fill="x")
Button(button_frame, text="이미지 이름 변경", command=이미지_이름_변경, width=20, bg="lightblue").grid(row=0, column=0, padx=10, pady=5)
Button(button_frame, text="파일 이동", command=파일_이동, width=20, bg="lightgreen").grid(row=0, column=1, padx=10, pady=5)
Button(button_frame, text="중복 이미지 삭제", command=중복_이미지_삭제, width=20, bg="orange").grid(row=1, column=0, padx=10, pady=5)

Label(root, text="작업 로그", font=("Arial", 12, "bold")).pack(pady=5)
log_text = Text(root, height=20, wrap="word")
log_text.pack(fill="both", padx=10, pady=10)

root.mainloop()
