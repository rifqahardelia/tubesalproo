import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QCalendarWidget, QListWidget, QInputDialog, QMessageBox
import re

catatan_per_tanggal = {}

def tambah_tugas():
    input_nama, ok1 = QInputDialog.getText(window, "ToDoList", "Nama tugas")
    if ok1:
        nama_tugas = input_nama 

        input_dosen, ok2 = QInputDialog.getText(window, "ToDoList", "Nama dosen")
        if ok2:
            nama_dosen = input_dosen

            input_jam, ok3 = QInputDialog.getText(window, "ToDoList", "Jam deadline (HH:MM)")
            if ok3:
             jam_deadline = input_jam
            if re.match(r'^\d{2}:\d{2}$', jam_deadline):
                print("Valid input:", jam_deadline)
            else:
                QMessageBox.critical(window, "Invalid Input", "Format input tidak valid, silahkan input sesuai format HH:MM.")
                return

            selected_date = calendar.selectedDate()
            tanggal = selected_date.day()
            bulan = selected_date.month()
            tahun = selected_date.year()

            tanggal_str = f"{tanggal}-{bulan}-{tahun}"
            history_text = f"{tanggal_str}: {nama_tugas} (Deadline: {jam_deadline})"
            all_tasks_list.addItem(history_text)

            if tanggal_str not in catatan_per_tanggal:
                catatan_per_tanggal[tanggal_str] = []

            catatan_per_tanggal[tanggal_str].append(history_text)

def hapus_catatan():
    selected_item = all_tasks_list.currentItem()
    if selected_item:
        selected_text = selected_item.text()
        for tanggal, catatan in catatan_per_tanggal.items():
            if selected_text in catatan:
                catatan.remove(selected_text)
        all_tasks_list.takeItem(all_tasks_list.currentRow())

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()

button_input = QPushButton("tambah Tugas")
button_input.setStyleSheet("background-color: #008CBA; color: white; border: 2px solid #008CBA; border-radius: 5px")
layout.addWidget(button_input)

calendar = QCalendarWidget()
layout.addWidget(calendar)

all_tasks_list = QListWidget()
layout.addWidget(all_tasks_list)

button_hapus_catatan = QPushButton("Hapus Tugas")
button_hapus_catatan.setStyleSheet("background-color: #000000; color: white; border: 2px solid #000000; border-radius: 5px")
layout.addWidget(button_hapus_catatan)

window.setLayout(layout)

button_input.clicked.connect(tambah_tugas)
button_hapus_catatan.clicked.connect(hapus_catatan)

window.setWindowTitle('ToDoList')
window.setGeometry(100, 100, 400, 400)
window.show()

sys.exit(app.exec_())
