# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from widgets.qlineeditadvanced import QLineEditAcceptDirectoryDrop
from widgets.qlineeditadvanced import QLineEditAcceptFileDrop

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(608, 302)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/mk_usdcat_all_64x64.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.main_VLayout = QVBoxLayout(MainWindow)
        self.main_VLayout.setSpacing(10)
        self.main_VLayout.setObjectName(u"main_VLayout")
        self.main_VLayout.setContentsMargins(6, 4, 6, 4)
        self.prerequisite_grpBx = QGroupBox(MainWindow)
        self.prerequisite_grpBx.setObjectName(u"prerequisite_grpBx")
        self.prerequisite_grpBx.setStyleSheet(u"QGroupBox{font-weight: bold;}")
        self.prerequisite_grpBx_VLayout = QVBoxLayout(self.prerequisite_grpBx)
        self.prerequisite_grpBx_VLayout.setSpacing(6)
        self.prerequisite_grpBx_VLayout.setObjectName(u"prerequisite_grpBx_VLayout")
        self.prerequisite_grpBx_VLayout.setContentsMargins(12, 8, 12, 8)
        self.preq_houdini_bin_folder_HLayout = QHBoxLayout()
        self.preq_houdini_bin_folder_HLayout.setSpacing(6)
        self.preq_houdini_bin_folder_HLayout.setObjectName(u"preq_houdini_bin_folder_HLayout")
        self.preq_houdini_bin_folder_label = QLabel(self.prerequisite_grpBx)
        self.preq_houdini_bin_folder_label.setObjectName(u"preq_houdini_bin_folder_label")

        self.preq_houdini_bin_folder_HLayout.addWidget(self.preq_houdini_bin_folder_label)

        self.preq_houdini_bin_folder_lineEdit = QLineEdit(self.prerequisite_grpBx)
        self.preq_houdini_bin_folder_lineEdit.setObjectName(u"preq_houdini_bin_folder_lineEdit")
        self.preq_houdini_bin_folder_lineEdit.setMinimumSize(QSize(320, 0))

        self.preq_houdini_bin_folder_HLayout.addWidget(self.preq_houdini_bin_folder_lineEdit)

        self.preq_houdini_bin_folder_browse_btn = QPushButton(self.prerequisite_grpBx)
        self.preq_houdini_bin_folder_browse_btn.setObjectName(u"preq_houdini_bin_folder_browse_btn")
        self.preq_houdini_bin_folder_browse_btn.setEnabled(True)
        self.preq_houdini_bin_folder_browse_btn.setMaximumSize(QSize(30, 16777215))
        font = QFont()
        font.setPointSize(8)
        self.preq_houdini_bin_folder_browse_btn.setFont(font)

        self.preq_houdini_bin_folder_HLayout.addWidget(self.preq_houdini_bin_folder_browse_btn)

        self.preq_houdini_bin_folder_validate_status_label = QLabel(self.prerequisite_grpBx)
        self.preq_houdini_bin_folder_validate_status_label.setObjectName(u"preq_houdini_bin_folder_validate_status_label")
        self.preq_houdini_bin_folder_validate_status_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.preq_houdini_bin_folder_HLayout.addWidget(self.preq_houdini_bin_folder_validate_status_label)

        self.preq_houdini_bin_folder_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.preq_houdini_bin_folder_HLayout.addItem(self.preq_houdini_bin_folder_horizontalSpacer)

        self.preq_houdini_bin_folder_open_pushButton = QPushButton(self.prerequisite_grpBx)
        self.preq_houdini_bin_folder_open_pushButton.setObjectName(u"preq_houdini_bin_folder_open_pushButton")
        self.preq_houdini_bin_folder_open_pushButton.setMaximumSize(QSize(55, 16777215))
        self.preq_houdini_bin_folder_open_pushButton.setFont(font)

        self.preq_houdini_bin_folder_HLayout.addWidget(self.preq_houdini_bin_folder_open_pushButton)


        self.prerequisite_grpBx_VLayout.addLayout(self.preq_houdini_bin_folder_HLayout)


        self.main_VLayout.addWidget(self.prerequisite_grpBx)

        self.usdcat_main_grpBx = QGroupBox(MainWindow)
        self.usdcat_main_grpBx.setObjectName(u"usdcat_main_grpBx")
        self.usdcat_main_grpBx.setStyleSheet(u"QGroupBox{font-weight: bold;}")
        self.usdcat_grpBx_VLayout = QVBoxLayout(self.usdcat_main_grpBx)
        self.usdcat_grpBx_VLayout.setSpacing(4)
        self.usdcat_grpBx_VLayout.setObjectName(u"usdcat_grpBx_VLayout")
        self.usdcat_grpBx_VLayout.setContentsMargins(12, 4, 12, 4)
        self.usdcat_HLayout = QHBoxLayout()
        self.usdcat_HLayout.setObjectName(u"usdcat_HLayout")
        self.usdcat_icon_btn = QPushButton(self.usdcat_main_grpBx)
        self.usdcat_icon_btn.setObjectName(u"usdcat_icon_btn")
        self.usdcat_icon_btn.setMinimumSize(QSize(48, 48))
        self.usdcat_icon_btn.setStyleSheet(u"border: none;")
        self.usdcat_icon_btn.setIcon(icon)
        self.usdcat_icon_btn.setIconSize(QSize(48, 48))
        self.usdcat_icon_btn.setCheckable(False)
        self.usdcat_icon_btn.setFlat(True)

        self.usdcat_HLayout.addWidget(self.usdcat_icon_btn)

        self.usdcat_output_format_grpBx = QGroupBox(self.usdcat_main_grpBx)
        self.usdcat_output_format_grpBx.setObjectName(u"usdcat_output_format_grpBx")
        self.usdcat_output_format_grpBx_HLayout = QHBoxLayout(self.usdcat_output_format_grpBx)
        self.usdcat_output_format_grpBx_HLayout.setSpacing(25)
        self.usdcat_output_format_grpBx_HLayout.setObjectName(u"usdcat_output_format_grpBx_HLayout")
        self.usdcat_output_format_grpBx_HLayout.setContentsMargins(37, 4, 37, 4)
        self.usdcat_output_binary_radioButton = QRadioButton(self.usdcat_output_format_grpBx)
        self.usdcat_output_binary_radioButton.setObjectName(u"usdcat_output_binary_radioButton")
        self.usdcat_output_binary_radioButton.setChecked(False)

        self.usdcat_output_format_grpBx_HLayout.addWidget(self.usdcat_output_binary_radioButton)

        self.usdcat_output_ascii_radioButton = QRadioButton(self.usdcat_output_format_grpBx)
        self.usdcat_output_ascii_radioButton.setObjectName(u"usdcat_output_ascii_radioButton")
        self.usdcat_output_ascii_radioButton.setChecked(True)

        self.usdcat_output_format_grpBx_HLayout.addWidget(self.usdcat_output_ascii_radioButton)


        self.usdcat_HLayout.addWidget(self.usdcat_output_format_grpBx)

        self.usdcat_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.usdcat_HLayout.addItem(self.usdcat_horizontalSpacer)

        self.usdcat_del_orig_checkBox = QCheckBox(self.usdcat_main_grpBx)
        self.usdcat_del_orig_checkBox.setObjectName(u"usdcat_del_orig_checkBox")
        self.usdcat_del_orig_checkBox.setChecked(True)

        self.usdcat_HLayout.addWidget(self.usdcat_del_orig_checkBox)


        self.usdcat_grpBx_VLayout.addLayout(self.usdcat_HLayout)

        self.usdcat_folder_grpBx = QGroupBox(self.usdcat_main_grpBx)
        self.usdcat_folder_grpBx.setObjectName(u"usdcat_folder_grpBx")
        sizePolicy.setHeightForWidth(self.usdcat_folder_grpBx.sizePolicy().hasHeightForWidth())
        self.usdcat_folder_grpBx.setSizePolicy(sizePolicy)
        self.usdcat_folder_grpBx.setStyleSheet(u"QGroupBox{border: none;}")
        self.usdcat_folder_grpBx.setFlat(True)
        self.usdcat_folder_grpBx_formLayout = QFormLayout(self.usdcat_folder_grpBx)
        self.usdcat_folder_grpBx_formLayout.setObjectName(u"usdcat_folder_grpBx_formLayout")
        self.usdcat_folder_grpBx_formLayout.setVerticalSpacing(2)
        self.usdcat_folder_to_batch_label = QLabel(self.usdcat_folder_grpBx)
        self.usdcat_folder_to_batch_label.setObjectName(u"usdcat_folder_to_batch_label")

        self.usdcat_folder_grpBx_formLayout.setWidget(0, QFormLayout.LabelRole, self.usdcat_folder_to_batch_label)

        self.usdcat_folder_to_batch_lineEdit = QLineEditAcceptDirectoryDrop(self.usdcat_folder_grpBx)
        self.usdcat_folder_to_batch_lineEdit.setObjectName(u"usdcat_folder_to_batch_lineEdit")
        self.usdcat_folder_to_batch_lineEdit.setMinimumSize(QSize(0, 20))
        self.usdcat_folder_to_batch_lineEdit.setStyleSheet(u"")

        self.usdcat_folder_grpBx_formLayout.setWidget(0, QFormLayout.FieldRole, self.usdcat_folder_to_batch_lineEdit)

        self.usdcat_instruction_label = QLabel(self.usdcat_folder_grpBx)
        self.usdcat_instruction_label.setObjectName(u"usdcat_instruction_label")
        self.usdcat_instruction_label.setEnabled(False)
        self.usdcat_instruction_label.setStyleSheet(u"font-size: 10px;")

        self.usdcat_folder_grpBx_formLayout.setWidget(1, QFormLayout.FieldRole, self.usdcat_instruction_label)


        self.usdcat_grpBx_VLayout.addWidget(self.usdcat_folder_grpBx)

        self.usdcat_batch_progressBar = QProgressBar(self.usdcat_main_grpBx)
        self.usdcat_batch_progressBar.setObjectName(u"usdcat_batch_progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.usdcat_batch_progressBar.sizePolicy().hasHeightForWidth())
        self.usdcat_batch_progressBar.setSizePolicy(sizePolicy1)
        self.usdcat_batch_progressBar.setMaximumSize(QSize(16777215, 10))
        font1 = QFont()
        font1.setPointSize(7)
        self.usdcat_batch_progressBar.setFont(font1)
        self.usdcat_batch_progressBar.setValue(0)

        self.usdcat_grpBx_VLayout.addWidget(self.usdcat_batch_progressBar)


        self.main_VLayout.addWidget(self.usdcat_main_grpBx)

        self.usdview_main_grpBx = QGroupBox(MainWindow)
        self.usdview_main_grpBx.setObjectName(u"usdview_main_grpBx")
        self.usdview_main_grpBx.setStyleSheet(u"QGroupBox{font-weight: bold;}")
        self.usdview_grpBx_VLayout = QVBoxLayout(self.usdview_main_grpBx)
        self.usdview_grpBx_VLayout.setSpacing(4)
        self.usdview_grpBx_VLayout.setObjectName(u"usdview_grpBx_VLayout")
        self.usdview_grpBx_VLayout.setContentsMargins(12, 4, 12, 4)
        self.usdview_grpBx = QGroupBox(self.usdview_main_grpBx)
        self.usdview_grpBx.setObjectName(u"usdview_grpBx")
        sizePolicy.setHeightForWidth(self.usdview_grpBx.sizePolicy().hasHeightForWidth())
        self.usdview_grpBx.setSizePolicy(sizePolicy)
        self.usdview_grpBx.setStyleSheet(u"QGroupBox{border: none;}")
        self.usdview_grpBx.setFlat(True)
        self.usdview_grpBx_formLayout = QFormLayout(self.usdview_grpBx)
        self.usdview_grpBx_formLayout.setObjectName(u"usdview_grpBx_formLayout")
        self.usdview_grpBx_formLayout.setVerticalSpacing(2)
        self.usdview_file_to_run_label = QLabel(self.usdview_grpBx)
        self.usdview_file_to_run_label.setObjectName(u"usdview_file_to_run_label")

        self.usdview_grpBx_formLayout.setWidget(0, QFormLayout.LabelRole, self.usdview_file_to_run_label)

        self.usdview_file_to_run_lineEdit = QLineEditAcceptFileDrop(self.usdview_grpBx)
        self.usdview_file_to_run_lineEdit.setObjectName(u"usdview_file_to_run_lineEdit")
        self.usdview_file_to_run_lineEdit.setMinimumSize(QSize(0, 20))

        self.usdview_grpBx_formLayout.setWidget(0, QFormLayout.FieldRole, self.usdview_file_to_run_lineEdit)

        self.usdview_instruction_label = QLabel(self.usdview_grpBx)
        self.usdview_instruction_label.setObjectName(u"usdview_instruction_label")
        self.usdview_instruction_label.setEnabled(False)
        self.usdview_instruction_label.setStyleSheet(u"font-size: 10px;")

        self.usdview_grpBx_formLayout.setWidget(1, QFormLayout.FieldRole, self.usdview_instruction_label)


        self.usdview_grpBx_VLayout.addWidget(self.usdview_grpBx)


        self.main_VLayout.addWidget(self.usdview_main_grpBx)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"mk_usdcat_all", None))
        self.prerequisite_grpBx.setTitle(QCoreApplication.translate("MainWindow", u"PREREQUISITES:  HYTHON + USDCAT", None))
        self.preq_houdini_bin_folder_label.setText(QCoreApplication.translate("MainWindow", u"Houdini bin folder:", None))
        self.preq_houdini_bin_folder_lineEdit.setText("")
        self.preq_houdini_bin_folder_browse_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.preq_houdini_bin_folder_validate_status_label.setText(QCoreApplication.translate("MainWindow", u"Validating", None))
        self.preq_houdini_bin_folder_open_pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.usdcat_main_grpBx.setTitle(QCoreApplication.translate("MainWindow", u"PERFORM USDCAT ALL", None))
        self.usdcat_icon_btn.setText("")
        self.usdcat_output_format_grpBx.setTitle("")
        self.usdcat_output_binary_radioButton.setText(QCoreApplication.translate("MainWindow", u"to Binary (Crate)", None))
        self.usdcat_output_ascii_radioButton.setText(QCoreApplication.translate("MainWindow", u"to ASCII", None))
        self.usdcat_del_orig_checkBox.setText(QCoreApplication.translate("MainWindow", u"Del Orig.", None))
        self.usdcat_folder_grpBx.setTitle("")
        self.usdcat_folder_to_batch_label.setText(QCoreApplication.translate("MainWindow", u"Folder to usdcat:", None))
        self.usdcat_instruction_label.setText(QCoreApplication.translate("MainWindow", u"Drag'n'Drop, or paste link to folder, then press Enter", None))
        self.usdview_main_grpBx.setTitle(QCoreApplication.translate("MainWindow", u"USDVIEW", None))
        self.usdview_grpBx.setTitle("")
        self.usdview_file_to_run_label.setText(QCoreApplication.translate("MainWindow", u"File to usdview:  ", None))
        self.usdview_instruction_label.setText(QCoreApplication.translate("MainWindow", u"Drag'n'Drop, or paste link to USD file, then press Enter", None))
    # retranslateUi

