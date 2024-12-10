import os
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox, QVBoxLayout, QWidget, QTextEdit, QComboBox, QCheckBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class RenameWorker(QThread):
    progress = pyqtSignal(str)

    def __init__(self, directory, pattern, target_format, remove_duplicates):
        super().__init__()
        self.directory = directory
        self.pattern = pattern
        self.target_format = target_format
        self.remove_duplicates = remove_duplicates

    def run(self):
        try:
            files = [
                f for f in os.listdir(self.directory)
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))
            ]

            if not files:
                self.progress.emit("선택된 디렉토리에 이미지 파일이 없습니다.")
                return

            if self.remove_duplicates:
                files = self.remove_duplicate_files(files)

            for i, file in enumerate(files):
                old_path = os.path.join(self.directory, file)
                creation_time = os.path.getctime(old_path)
                creation_date = datetime.fromtimestamp(creation_time).strftime('%Y%m%d')

                # 새로운 이름 생성
                new_name = f"{self.pattern}_{creation_date}_{i:06d}"
                ext = {
                    "PNG": ".png",
                    "JPG": ".jpg",
                    "WEBP": ".webp"
                }.get(self.target_format, os.path.splitext(file)[1])
                new_name += ext

                new_path = os.path.join(self.directory, new_name)

                # 기존 파일 삭제 처리
                if os.path.exists(new_path):
                    os.remove(new_path)
                    self.progress.emit(f"기존 파일 삭제: {new_name}")

                os.rename(old_path, new_path)
                self.progress.emit(f"{file} -> {new_name}")

            self.progress.emit("모든 파일의 이름 변경 작업이 완료되었습니다.")

        except Exception as e:
            self.progress.emit(f"오류 발생: {str(e)}")

    def remove_duplicate_files(self, files):
        import hashlib
        unique_files = {}
        for file in files:
            file_path = os.path.join(self.directory, file)
            file_hash = self.get_file_hash(file_path)
            if file_hash in unique_files:
                os.remove(file_path)
                self.progress.emit(f"중복 파일 삭제: {file}")
            else:
                unique_files[file_hash] = file

        return list(unique_files.values())

    @staticmethod
    def get_file_hash(file_path):
        import hashlib
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


class PhotoRenamerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("사진 이름 변경기")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.dir_label = QLabel("선택된 디렉토리: 없음")
        layout.addWidget(self.dir_label)

        self.select_dir_button = QPushButton("디렉토리 선택")
        self.select_dir_button.clicked.connect(self.select_directory)
        layout.addWidget(self.select_dir_button)

        self.pattern_label = QLabel("변경할 이름 패턴 입력 (예: 'photo'): ")
        layout.addWidget(self.pattern_label)

        self.pattern_input = QLineEdit()
        layout.addWidget(self.pattern_input)

        self.format_label = QLabel("변경할 파일 유형 선택: ")
        layout.addWidget(self.format_label)

        self.format_combo = QComboBox()
        self.format_combo.addItems(["원본 유지", "PNG", "JPG", "WEBP"])
        layout.addWidget(self.format_combo)

        self.duplicate_checkbox = QCheckBox("중복 파일 제거")
        layout.addWidget(self.duplicate_checkbox)

        self.rename_button = QPushButton("사진 이름 변경")
        self.rename_button.clicked.connect(self.start_rename)
        layout.addWidget(self.rename_button)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        layout.addWidget(self.log_output)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "디렉토리 선택")
        if directory:
            self.selected_directory = directory
            self.dir_label.setText(f"선택된 디렉토리: {directory}")
            self.log_output.append(f"디렉토리 선택: {directory}")

    def start_rename(self):
        directory = getattr(self, 'selected_directory', None)
        if not directory:
            QMessageBox.warning(self, "오류", "먼저 디렉토리를 선택하세요.")
            return

        pattern = self.pattern_input.text()
        if not pattern:
            QMessageBox.warning(self, "오류", "이름 패턴을 입력하세요.")
            return

        target_format = self.format_combo.currentText()
        remove_duplicates = self.duplicate_checkbox.isChecked()

        self.worker = RenameWorker(directory, pattern, target_format, remove_duplicates)
        self.worker.progress.connect(self.update_log)
        self.worker.start()

    def update_log(self, message):
        self.log_output.append(message)


if __name__ == "__main__":
    app = QApplication([])
    window = PhotoRenamerApp()
    window.show()
    app.exec_()
