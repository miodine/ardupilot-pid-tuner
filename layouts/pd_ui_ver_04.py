# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_rel_v4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 866)
        MainWindow.setWindowOpacity(0.95)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 410, 281, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout_regulation_quality = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_regulation_quality.setContentsMargins(0, 0, 0, 0)
        self.layout_regulation_quality.setObjectName("layout_regulation_quality")
        self.label_ref_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ref_value.setObjectName("label_ref_value")
        self.layout_regulation_quality.addWidget(self.label_ref_value, 2, 0, 1, 1)
        self.var_ref_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.var_ref_value.setObjectName("var_ref_value")
        self.layout_regulation_quality.addWidget(self.var_ref_value, 2, 1, 1, 1)
        self.label_act_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_act_value.setObjectName("label_act_value")
        self.layout_regulation_quality.addWidget(self.label_act_value, 3, 0, 1, 1)
        self.var_act_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.var_act_value.setObjectName("var_act_value")
        self.layout_regulation_quality.addWidget(self.var_act_value, 3, 1, 1, 1)
        self.var_reg_error = QtWidgets.QLabel(self.gridLayoutWidget)
        self.var_reg_error.setObjectName("var_reg_error")
        self.layout_regulation_quality.addWidget(self.var_reg_error, 4, 1, 1, 1)
        self.label_reg_error = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_reg_error.setObjectName("label_reg_error")
        self.layout_regulation_quality.addWidget(self.label_reg_error, 4, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 620, 601, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.layout_rate_tuning = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.layout_rate_tuning.setContentsMargins(0, 0, 0, 0)
        self.layout_rate_tuning.setObjectName("layout_rate_tuning")
        self.label_rate_I = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_rate_I.setObjectName("label_rate_I")
        self.layout_rate_tuning.addWidget(self.label_rate_I, 0, 3, 1, 1)
        self.var_spinbox_rate_D = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.var_spinbox_rate_D.sizePolicy().hasHeightForWidth())
        self.var_spinbox_rate_D.setSizePolicy(sizePolicy)
        self.var_spinbox_rate_D.setDecimals(3)
        self.var_spinbox_rate_D.setSingleStep(0.01)
        self.var_spinbox_rate_D.setObjectName("var_spinbox_rate_D")
        self.layout_rate_tuning.addWidget(self.var_spinbox_rate_D, 0, 8, 1, 1)
        self.label_rate_D = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_rate_D.setObjectName("label_rate_D")
        self.layout_rate_tuning.addWidget(self.label_rate_D, 0, 7, 1, 1)
        self.label_rate_P = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_rate_P.setObjectName("label_rate_P")
        self.layout_rate_tuning.addWidget(self.label_rate_P, 0, 0, 1, 1)
        self.var_spinbox_rate_I = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.var_spinbox_rate_I.sizePolicy().hasHeightForWidth())
        self.var_spinbox_rate_I.setSizePolicy(sizePolicy)
        self.var_spinbox_rate_I.setDecimals(3)
        self.var_spinbox_rate_I.setSingleStep(0.01)
        self.var_spinbox_rate_I.setObjectName("var_spinbox_rate_I")
        self.layout_rate_tuning.addWidget(self.var_spinbox_rate_I, 0, 5, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.layout_rate_tuning.addWidget(self.line_12, 0, 6, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.layout_rate_tuning.addWidget(self.line_10, 0, 2, 1, 1)
        self.var_spinbox_rate_P = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.var_spinbox_rate_P.sizePolicy().hasHeightForWidth())
        self.var_spinbox_rate_P.setSizePolicy(sizePolicy)
        self.var_spinbox_rate_P.setDecimals(3)
        self.var_spinbox_rate_P.setSingleStep(0.01)
        self.var_spinbox_rate_P.setObjectName("var_spinbox_rate_P")
        self.layout_rate_tuning.addWidget(self.var_spinbox_rate_P, 0, 1, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.layout_rate_tuning.addWidget(self.line_11, 0, 4, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 580, 601, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 390, 601, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(10, 740, 601, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 370, 601, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.layout_operation_state = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.layout_operation_state.setContentsMargins(0, 0, 0, 0)
        self.layout_operation_state.setObjectName("layout_operation_state")
        self.label_monit = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_monit.sizePolicy().hasHeightForWidth())
        self.label_monit.setSizePolicy(sizePolicy)
        self.label_monit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_monit.setObjectName("label_monit")
        self.layout_operation_state.addWidget(self.label_monit)
        self.var_monit = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.var_monit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.var_monit.setObjectName("var_monit")
        self.layout_operation_state.addWidget(self.var_monit)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 360, 601, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 90, 601, 261))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.layout_signal_viz = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.layout_signal_viz.setContentsMargins(0, 0, 0, 0)
        self.layout_signal_viz.setObjectName("layout_signal_viz")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 760, 601, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.layout_tuning_apply = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.layout_tuning_apply.setContentsMargins(0, 0, 0, 0)
        self.layout_tuning_apply.setObjectName("layout_tuning_apply")
        self.button_upload_tuning = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.button_upload_tuning.setEnabled(True)
        self.button_upload_tuning.setObjectName("button_upload_tuning")
        self.layout_tuning_apply.addWidget(self.button_upload_tuning)
        self.button_download_tuning = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.button_download_tuning.setEnabled(True)
        self.button_download_tuning.setObjectName("button_download_tuning")
        self.layout_tuning_apply.addWidget(self.button_download_tuning)
        self.button_upload_default_tuning = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.button_upload_default_tuning.setEnabled(True)
        self.button_upload_default_tuning.setObjectName("button_upload_default_tuning")
        self.layout_tuning_apply.addWidget(self.button_upload_default_tuning)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 694, 601, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.layout_stabilization_tuning = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.layout_stabilization_tuning.setContentsMargins(0, 0, 0, 0)
        self.layout_stabilization_tuning.setObjectName("layout_stabilization_tuning")
        self.label_stabilization_P = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_stabilization_P.setObjectName("label_stabilization_P")
        self.layout_stabilization_tuning.addWidget(self.label_stabilization_P, 0, 0, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.layout_stabilization_tuning.addWidget(self.line_16, 0, 2, 1, 1)
        self.label_stabilization_accel_max = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_stabilization_accel_max.setObjectName("label_stabilization_accel_max")
        self.layout_stabilization_tuning.addWidget(self.label_stabilization_accel_max, 0, 4, 1, 1)
        self.var_spinbox_stabilization_Accel = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.var_spinbox_stabilization_Accel.setDecimals(3)
        self.var_spinbox_stabilization_Accel.setSingleStep(0.01)
        self.var_spinbox_stabilization_Accel.setObjectName("var_spinbox_stabilization_Accel")
        self.layout_stabilization_tuning.addWidget(self.var_spinbox_stabilization_Accel, 0, 5, 1, 1)
        self.var_spinbox_stabilization_P = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.var_spinbox_stabilization_P.setDecimals(3)
        self.var_spinbox_stabilization_P.setMinimum(3.0)
        self.var_spinbox_stabilization_P.setMaximum(12.0)
        self.var_spinbox_stabilization_P.setSingleStep(0.001)
        self.var_spinbox_stabilization_P.setObjectName("var_spinbox_stabilization_P")
        self.layout_stabilization_tuning.addWidget(self.var_spinbox_stabilization_P, 0, 1, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.layout_stabilization_tuning.addWidget(self.line_17, 0, 3, 1, 1)
        self.label_rate_tuning = QtWidgets.QLabel(self.centralwidget)
        self.label_rate_tuning.setGeometry(QtCore.QRect(10, 594, 291, 21))
        self.label_rate_tuning.setObjectName("label_rate_tuning")
        self.label_stabilization_tuning = QtWidgets.QLabel(self.centralwidget)
        self.label_stabilization_tuning.setGeometry(QtCore.QRect(10, 670, 291, 21))
        self.label_stabilization_tuning.setObjectName("label_stabilization_tuning")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(300, 410, 121, 112))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.layout_tuning_axis_selection = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.layout_tuning_axis_selection.setContentsMargins(0, 0, 0, 0)
        self.layout_tuning_axis_selection.setObjectName("layout_tuning_axis_selection")
        self.radio_yaw = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.radio_yaw.setObjectName("radio_yaw")
        self.layout_tuning_axis_selection.addWidget(self.radio_yaw, 3, 0, 1, 1)
        self.radio_roll = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.radio_roll.setObjectName("radio_roll")
        self.layout_tuning_axis_selection.addWidget(self.radio_roll, 1, 0, 1, 1)
        self.radio_alt = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.radio_alt.setObjectName("radio_alt")
        self.layout_tuning_axis_selection.addWidget(self.radio_alt, 5, 0, 1, 1)
        self.radio_pitch = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.radio_pitch.setObjectName("radio_pitch")
        self.layout_tuning_axis_selection.addWidget(self.radio_pitch, 2, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(440, 410, 171, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_image_prompt = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_image_prompt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image_prompt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image_prompt.setObjectName("frame_image_prompt")
        self.verticalLayout.addWidget(self.frame_image_prompt)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 546, 601, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_tuning_options = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_tuning_options.setContentsMargins(0, 0, 0, 0)
        self.layout_tuning_options.setObjectName("layout_tuning_options")
        self.checkbox_combine_pi_values = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkbox_combine_pi_values.setObjectName("checkbox_combine_pi_values")
        self.layout_tuning_options.addWidget(self.checkbox_combine_pi_values)
        self.checkbox_combine_roll_pitch_axes = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkbox_combine_roll_pitch_axes.setObjectName("checkbox_combine_roll_pitch_axes")
        self.layout_tuning_options.addWidget(self.checkbox_combine_roll_pitch_axes)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 530, 601, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(10, 60, 601, 20))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 601, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layout_ip_input = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_ip_input.setContentsMargins(0, 0, 0, 0)
        self.layout_ip_input.setObjectName("layout_ip_input")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.layout_ip_input.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.layout_ip_input.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Poldrone APQP PID Tuning Utility"))
        self.label_ref_value.setText(_translate("MainWindow", "Reference value:"))
        self.var_ref_value.setText(_translate("MainWindow", "__sys_input__"))
        self.label_act_value.setText(_translate("MainWindow", "Actual value:"))
        self.var_act_value.setText(_translate("MainWindow", "__sys_output__"))
        self.var_reg_error.setText(_translate("MainWindow", "__sys_regerror__"))
        self.label_reg_error.setText(_translate("MainWindow", "Regulation error:"))
        self.label_rate_I.setText(_translate("MainWindow", "Int. Gain (I)"))
        self.label_rate_D.setText(_translate("MainWindow", "Der. Gain (D)"))
        self.label_rate_P.setText(_translate("MainWindow", "Prop. Gain (P)"))
        self.label_monit.setText(_translate("MainWindow", "MONIT:"))
        self.var_monit.setText(_translate("MainWindow", "__monit__"))
        self.button_upload_tuning.setText(_translate("MainWindow", "Upload Tuning"))
        self.button_download_tuning.setText(_translate("MainWindow", "Download Tuning"))
        self.button_upload_default_tuning.setText(_translate("MainWindow", "Upload Default Tuning"))
        self.label_stabilization_P.setText(_translate("MainWindow", "Prop. Gain (P)"))
        self.label_stabilization_accel_max.setText(_translate("MainWindow", "Acceleration Max"))
        self.label_rate_tuning.setText(_translate("MainWindow", "Angular Rate Control Loop Tunings"))
        self.label_stabilization_tuning.setText(_translate("MainWindow", "Stabilization Control Loop Tunings"))
        self.radio_yaw.setText(_translate("MainWindow", "Yaw (OZ)"))
        self.radio_roll.setText(_translate("MainWindow", "Roll (OX)"))
        self.radio_alt.setText(_translate("MainWindow", "Altitude (Z)"))
        self.radio_pitch.setText(_translate("MainWindow", "Pitch (OY)"))
        self.checkbox_combine_pi_values.setText(_translate("MainWindow", "Combine P and I Values"))
        self.checkbox_combine_roll_pitch_axes.setText(_translate("MainWindow", "Combine Roll and Pitch Axes"))
        self.label.setText(_translate("MainWindow", "Target Platform IP:"))
