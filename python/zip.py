import os
import zipfile
from tkinter import Tk, filedialog, Label, Button, StringVar, Entry, messagebox


def scan_and_zip_photos(source_dir, target_dir, max_size_mb=499):
    """스캔한 사진 파일을 ZIP 파일로 분할 저장"""
    max_size = max_size_mb * 1024 * 1024  # MB to bytes
    zip_file_paths = []

    # 소스 디렉토리 스캔
    photo_files = [os.path.join(source_dir, f) for f in os.listdir(source_dir)
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

    if not photo_files:
        raise ValueError("No image files found in the selected directory.")

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for photo in photo_files:
        file_size = os.path.getsize(photo)
        if file_size <= max_size:
            # 파일 크기가 기준 이하일 경우 단일 ZIP
            zip_name = os.path.join(target_dir, f"{os.path.splitext(os.path.basename(photo))[0]}.zip")
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(photo, os.path.basename(photo))
            zip_file_paths.append(zip_name)
        else:
            # 파일 크기가 기준 초과일 경우 분할 처리
            with open(photo, 'rb') as f:
                part_num = 1
                while True:
                    chunk = f.read(max_size)
                    if not chunk:
                        break
                    part_file_name = os.path.join(target_dir,
                                                  f"{os.path.splitext(os.path.basename(photo))[0]}_part{part_num}.zip")
                    with zipfile.ZipFile(part_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        zipf.writestr(os.path.basename(photo), chunk)
                    zip_file_paths.append(part_file_name)
                    part_num += 1

    return zip_file_paths


def select_source_dir():
    dir_path = filedialog.askdirectory(title="Select Source Directory")
    if dir_path:
        source_dir.set(dir_path)


def select_target_dir():
    dir_path = filedialog.askdirectory(title="Select Target Directory")
    if dir_path:
        target_dir.set(dir_path)


def start_processing():
    try:
        source = source_dir.get()
        target = target_dir.get()
        if not source or not target:
            raise ValueError("Both source and target directories must be selected.")
        
        zip_files = scan_and_zip_photos(source, target, max_size_mb=int(max_size.get()))
        messagebox.showinfo("Success", f"ZIP files created successfully:\n{len(zip_files)} files.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI 설정
root = Tk()
root.title("Photo Zipper")
root.geometry("500x300")

# 입력 및 버튼
source_dir = StringVar()
target_dir = StringVar()
max_size = StringVar(value="499")

Label(root, text="Source Directory:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
Entry(root, textvariable=source_dir, width=50).grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Browse", command=select_source_dir).grid(row=0, column=2, padx=10, pady=10)

Label(root, text="Target Directory:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
Entry(root, textvariable=target_dir, width=50).grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Browse", command=select_target_dir).grid(row=1, column=2, padx=10, pady=10)

Label(root, text="Max Size (MB):").grid(row=2, column=0, padx=10, pady=10, sticky='w')
Entry(root, textvariable=max_size, width=10).grid(row=2, column=1, padx=10, pady=10, sticky='w')

Button(root, text="Start", command=start_processing, bg="green", fg="white").grid(row=3, column=1, padx=10, pady=20)

root.mainloop()
