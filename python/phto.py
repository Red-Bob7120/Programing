import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# 이미지 파일 복사 및 이름 변경 함수
def copy_and_rename_files(source_folder, destination_folder, extensions, rename_pattern, log_widget):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    copied_count = 0
    for root, dirs, files in os.walk(source_folder):
        for index, file in enumerate(files):
            if file.lower().endswith(tuple(extensions)):
                source_path = os.path.join(root, file)
                album_name = os.path.basename(source_folder)
                new_name = f"{rename_pattern}_{album_name}_{index + 1:06d}{os.path.splitext(file)[1]}" if rename_pattern else file
                destination_path = os.path.join(destination_folder, new_name)
                try:
                    shutil.copy2(source_path, destination_path)
                    log_widget.insert(tk.END, f"복사 완료: {file} -> {new_name}\n")
                    log_widget.yview(tk.END)  # 스크롤 자동 이동
                    copied_count += 1
                except Exception as e:
                    log_widget.insert(tk.END, f"복사 실패: {file} - {e}\n")
                    log_widget.yview(tk.END)

    log_widget.insert(tk.END, f"총 {copied_count}개의 파일이 복사되었습니다.\n")
    log_widget.yview(tk.END)

# 소스 폴더 선택 함수
def select_source_folder():
    folder = filedialog.askdirectory()
    if folder:
        source_var.set(folder)

# 대상 폴더 선택 함수
def select_destination_folder():
    folder = filedialog.askdirectory()
    if folder:
        destination_var.set(folder)

# 복사 실행 함수
def start_copy():
    source_folder = source_var.get()
    destination_folder = destination_var.get()
    rename_pattern = rename_var.get()
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    if not source_folder or not destination_folder:
        messagebox.showerror("오류", "사진이 있는 폴더와 저장할 폴더를 선택해주세요!")
        return

    log_text.delete(1.0, tk.END)  # 로그 초기화

    # 파일 복사를 별도의 스레드에서 실행
    copy_thread = threading.Thread(target=copy_and_rename_files, args=(source_folder, destination_folder, extensions, rename_pattern, log_text))
    copy_thread.start()

# GUI 생성
app = tk.Tk()
app.title("사진 복사 및 이름 변경")
app.geometry("600x500")

# 폴더 경로 변수
source_var = tk.StringVar()
destination_var = tk.StringVar()
rename_var = tk.StringVar()

# 소스 폴더 선택 UI
source_label = tk.Label(app, text="사진이 있는 폴더:")
source_label.pack(anchor="w", padx=10, pady=5)
source_frame = tk.Frame(app)
source_frame.pack(fill="x", padx=10)
source_entry = tk.Entry(source_frame, textvariable=source_var, width=50)
source_entry.pack(side="left", fill="x", expand=True)
source_button = tk.Button(source_frame, text="폴더 선택", command=select_source_folder)
source_button.pack(side="right")

# 대상 폴더 선택 UI
destination_label = tk.Label(app, text="저장할 폴더:")
destination_label.pack(anchor="w", padx=10, pady=5)
destination_frame = tk.Frame(app)
destination_frame.pack(fill="x", padx=10)
destination_entry = tk.Entry(destination_frame, textvariable=destination_var, width=50)
destination_entry.pack(side="left", fill="x", expand=True)
destination_button = tk.Button(destination_frame, text="폴더 선택", command=select_destination_folder)
destination_button.pack(side="right")

# 파일 이름 변경 옵션 UI
rename_label = tk.Label(app, text="새 파일 이름 (예: Photo):")
rename_label.pack(anchor="w", padx=10, pady=5)
rename_entry = tk.Entry(app, textvariable=rename_var, width=50)
rename_entry.pack(fill="x", padx=10)
rename_note = tk.Label(app, text="* 새 이름 뒤에 앨범 이름과 번호가 자동으로 붙습니다. 비워두면 원래 이름이 유지됩니다.", fg="gray")
rename_note.pack(anchor="w", padx=10)

# 실행 버튼
start_button = tk.Button(app, text="복사 및 저장 시작", command=start_copy, bg="lightblue")
start_button.pack(pady=10)

# 로그 출력 UI
log_label = tk.Label(app, text="작업 로그:")
log_label.pack(anchor="w", padx=10)
log_text = scrolledtext.ScrolledText(app, wrap="word", height=15)
log_text.pack(fill="both", padx=10, pady=5, expand=True)

# 프로그램 실행
app.mainloop()
