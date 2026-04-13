# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 800)
        MainWindow.setStyleSheet(u"#centralwidget { background-color: #0d0d1f; }\n"
"    QMainWindow { background-color: #0d0d1f; }\n"
"    QFrame#headerFrame { background-color: #1a1a33; border-radius: 15px; }\n"
"    QLabel { color: #a5a5cc; font-family: 'Segoe UI'; font-weight: bold; }\n"
"    QLineEdit, QComboBox { background-color: #1f1f3d; border: 1px solid #3d3d70; border-radius: 6px; color: white; padding: 8px; font-size: 12px; }\n"
"    QPushButton { border-radius: 6px; color: white; font-weight: bold; font-size: 12px; height: 40px; text-transform: uppercase; }\n"
"    QTableWidget { background-color: #161630; color: white; border: none; border-radius: 12px; gridline-color: #2d2d5a; }\n"
"    QHeaderView::section { background-color: #1e1e3f; color: #7070db; font-weight: bold; border: none; padding: 6px; }\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainV = QVBoxLayout(self.centralwidget)
        self.mainV.setSpacing(20)
        self.mainV.setObjectName(u"mainV")
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 100))
        self.headerFrame.setMaximumSize(QSize(16777215, 100))
        self.hboxLayout = QHBoxLayout(self.headerFrame)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.gym = QLabel(self.headerFrame)
        self.gym.setObjectName(u"gym")

        self.hboxLayout.addWidget(self.gym)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.manajemen_member_gym = QLabel(self.headerFrame)
        self.manajemen_member_gym.setObjectName(u"manajemen_member_gym")

        self.vboxLayout.addWidget(self.manajemen_member_gym)

        self.sistem_manajemen = QLabel(self.headerFrame)
        self.sistem_manajemen.setObjectName(u"sistem_manajemen")

        self.vboxLayout.addWidget(self.sistem_manajemen)


        self.hboxLayout.addLayout(self.vboxLayout)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem)

        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.label_total_val = QLabel(self.headerFrame)
        self.label_total_val.setObjectName(u"label_total_val")
        self.label_total_val.setAlignment(Qt.AlignCenter)

        self.vboxLayout1.addWidget(self.label_total_val)

        self.total_member = QLabel(self.headerFrame)
        self.total_member.setObjectName(u"total_member")
        self.total_member.setAlignment(Qt.AlignCenter)

        self.vboxLayout1.addWidget(self.total_member)


        self.hboxLayout.addLayout(self.vboxLayout1)


        self.mainV.addWidget(self.headerFrame)

        self.bodyH = QHBoxLayout()
        self.bodyH.setSpacing(25)
        self.bodyH.setObjectName(u"bodyH")
        self.formContainer = QFrame(self.centralwidget)
        self.formContainer.setObjectName(u"formContainer")
        self.formContainer.setMinimumSize(QSize(350, 0))
        self.formContainer.setMaximumSize(QSize(350, 16777215))
        self.vboxLayout2 = QVBoxLayout(self.formContainer)
        self.vboxLayout2.setSpacing(10)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.id_member = QLabel(self.formContainer)
        self.id_member.setObjectName(u"id_member")

        self.vboxLayout2.addWidget(self.id_member)

        self.input_id = QLineEdit(self.formContainer)
        self.input_id.setObjectName(u"input_id")

        self.vboxLayout2.addWidget(self.input_id)

        self.nama_member = QLabel(self.formContainer)
        self.nama_member.setObjectName(u"nama_member")

        self.vboxLayout2.addWidget(self.nama_member)

        self.input_nama = QLineEdit(self.formContainer)
        self.input_nama.setObjectName(u"input_nama")

        self.vboxLayout2.addWidget(self.input_nama)

        self.paket_pelanggan = QLabel(self.formContainer)
        self.paket_pelanggan.setObjectName(u"paket_pelanggan")

        self.vboxLayout2.addWidget(self.paket_pelanggan)

        self.combo_paket = QComboBox(self.formContainer)
        self.combo_paket.addItem("")
        self.combo_paket.addItem("")
        self.combo_paket.addItem("")
        self.combo_paket.setObjectName(u"combo_paket")

        self.vboxLayout2.addWidget(self.combo_paket)

        self.sisa_durasi = QLabel(self.formContainer)
        self.sisa_durasi.setObjectName(u"sisa_durasi")

        self.vboxLayout2.addWidget(self.sisa_durasi)

        self.input_durasi = QLineEdit(self.formContainer)
        self.input_durasi.setObjectName(u"input_durasi")

        self.vboxLayout2.addWidget(self.input_durasi)

        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout2.addItem(self.spacerItem1)

        self.btn_insert = QPushButton(self.formContainer)
        self.btn_insert.setObjectName(u"btn_insert")

        self.vboxLayout2.addWidget(self.btn_insert)

        self.btn_delete = QPushButton(self.formContainer)
        self.btn_delete.setObjectName(u"btn_delete")

        self.vboxLayout2.addWidget(self.btn_delete)

        self.btn_search = QPushButton(self.formContainer)
        self.btn_search.setObjectName(u"btn_search")

        self.vboxLayout2.addWidget(self.btn_search)

        self.btn_sort = QPushButton(self.formContainer)
        self.btn_sort.setObjectName(u"btn_sort")

        self.vboxLayout2.addWidget(self.btn_sort)

        self.btn_display = QPushButton(self.formContainer)
        self.btn_display.setObjectName(u"btn_display")

        self.vboxLayout2.addWidget(self.btn_display)

        self.btn_clear = QPushButton(self.formContainer)
        self.btn_clear.setObjectName(u"btn_clear")

        self.vboxLayout2.addWidget(self.btn_clear)


        self.bodyH.addWidget(self.formContainer)

        self.tableContainer = QFrame(self.centralwidget)
        self.tableContainer.setObjectName(u"tableContainer")
        self.vboxLayout3 = QVBoxLayout(self.tableContainer)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.data_member = QLabel(self.tableContainer)
        self.data_member.setObjectName(u"data_member")

        self.vboxLayout3.addWidget(self.data_member)

        self.tableWidget = QTableWidget(self.tableContainer)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"/* Style Anda */\n"
"QTableWidget {\n"
"    background-color: #24243e;\n"
"    color: #ffffff;\n"
"    gridline-color: #32325d;\n"
"    border: 1px solid #32325d;\n"
"    border-radius: 10px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    color: #7d7dbd;\n"
"    padding: 5px; /* Perkecil padding agar teks tidak sesak */\n"
"    border: none;\n"
"    border-bottom: 1px solid #32325d;\n"
"    border-right: 1px solid #32325d; \n"
"    font-weight: bold;\n"
"}\n"
"")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(222)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.vboxLayout3.addWidget(self.tableWidget)


        self.bodyH.addWidget(self.tableContainer)


        self.mainV.addLayout(self.bodyH)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Manajemen Member Gym", None))
        self.gym.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 45px; color: #5d5dfa; font-weight: 900; margin-left: 15px;", None))
        self.gym.setText(QCoreApplication.translate("MainWindow", u"\U0001f3cb\U0000fe0f\U0000200d", None))
        self.manajemen_member_gym.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 26px; color: white;", None))
        self.manajemen_member_gym.setText(QCoreApplication.translate("MainWindow", u"Manajemen Keanggotaan Gym", None))
        self.sistem_manajemen.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #6c6c9c; font-size: 12px; font-weight: normal;", None))
        self.sistem_manajemen.setText(QCoreApplication.translate("MainWindow", u"Sistem manajemen member gym dan paket pelanggan", None))
        self.label_total_val.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 45px; color: #5d5dfa; font-weight: bold;", None))
        self.label_total_val.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_member.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #6c6c9c; font-size: 11px;", None))
        self.total_member.setText(QCoreApplication.translate("MainWindow", u"Total Member", None))
        self.id_member.setText(QCoreApplication.translate("MainWindow", u"ID Member", None))
        self.input_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Masukkan ID...", None))
        self.nama_member.setText(QCoreApplication.translate("MainWindow", u"Nama Member", None))
        self.input_nama.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nama lengkap...", None))
        self.paket_pelanggan.setText(QCoreApplication.translate("MainWindow", u"Paket Langganan", None))
        self.combo_paket.setItemText(0, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.combo_paket.setItemText(1, QCoreApplication.translate("MainWindow", u"Gold", None))
        self.combo_paket.setItemText(2, QCoreApplication.translate("MainWindow", u"Platinum", None))

        self.sisa_durasi.setText(QCoreApplication.translate("MainWindow", u"Sisa Durasi (hari)", None))
        self.input_durasi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: 30", None))
        self.btn_insert.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #5d5dfa;", None))
        self.btn_insert.setText(QCoreApplication.translate("MainWindow", u"INSERT", None))
        self.btn_delete.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #f64c5d;", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.btn_search.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #2ca58d;", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.btn_sort.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #d4a017;", None))
        self.btn_sort.setText(QCoreApplication.translate("MainWindow", u"SORT", None))
        self.btn_display.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #7070db;", None))
        self.btn_display.setText(QCoreApplication.translate("MainWindow", u"DISPLAY", None))
        self.btn_clear.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: transparent; border: 1px solid #3d3d70; color: #6c6c9c;", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Bersihkan Form", None))
        self.tableContainer.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #161630; border-radius: 15px;", None))
        self.data_member.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 20px; color: white; margin-bottom: 10px;", None))
        self.data_member.setText(QCoreApplication.translate("MainWindow", u"Data Member", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID Member", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nama Member", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Paket", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Sisa Durasi (hari)", None))
    # retranslateUi

