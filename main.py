import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtCore import Qt

from ui_main import Ui_MainWindow
from tubeskel4 import DoublyLinkedList

class GymApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dll = DoublyLinkedList()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.btn_insert.clicked.connect(self.tambah)
        self.ui.btn_delete.clicked.connect(self.hapus)
        self.ui.btn_search.clicked.connect(self.cari)
        self.ui.btn_sort.clicked.connect(self.sortir)
        self.ui.btn_display.clicked.connect(self.tampilkan_semua)
        self.ui.btn_clear.clicked.connect(self.bersihkan_form)

    def refresh_table(self, data_list=None):
        """Menampilkan data ke tabel."""
        nodes = data_list if data_list is not None else self.dll.display()
        self.ui.tableWidget.setRowCount(0)

        for i, node in enumerate(nodes):
            self.ui.tableWidget.insertRow(i)
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(node.id_member))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(node.nama))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(node.paket))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(node.sisa_durasi)))

        self.ui.label_total_val.setText(str(self.dll.size))

    def tampilkan_semua(self):
        self.refresh_table()

    def bersihkan_form(self):
        self.ui.input_id.clear()
        self.ui.input_nama.clear()
        self.ui.input_durasi.clear()

    def tambah(self):
        try:
            id_m   = self.ui.input_id.text().strip()
            nama   = self.ui.input_nama.text().strip()
            paket  = self.ui.combo_paket.currentText()
            durasi = self.ui.input_durasi.text().strip()

            if not id_m or not nama or not durasi:
                QMessageBox.warning(self, "Peringatan", "Isi semua data!")
                return

            if not durasi.isdigit():
                QMessageBox.warning(self, "Peringatan", "Sisa durasi harus berupa angka!")
                return

            self.dll.insert(id_m, nama, paket, int(durasi))
            self.refresh_table()
            self.bersihkan_form()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def hapus(self):
        id_m = self.ui.input_id.text().strip()
        if not id_m:
            QMessageBox.warning(self, "Peringatan", "Masukkan ID Member yang ingin dihapus!")
            return

        if self.dll.delete(id_m):
            self.refresh_table()
            QMessageBox.information(self, "Sukses", f"Member {id_m} berhasil dihapus.")
        else:
            QMessageBox.warning(self, "Gagal", "ID Member tidak ditemukan.")

    def cari(self):
        id_m = self.ui.input_id.text().strip()
        if not id_m:
            QMessageBox.warning(self, "Peringatan", "Masukkan ID Member yang ingin dicari!")
            return

        res = self.dll._find_node(id_m)
        if res:
            self.refresh_table([res])
        else:
            self.ui.tableWidget.setRowCount(0)
            QMessageBox.warning(self, "Tidak Ditemukan", "Member tidak ditemukan.")

    def sortir(self):
        self.dll.sort_by_sisa_durasi()
        self.refresh_table()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GymApp()
    window.show()
    sys.exit(app.exec())