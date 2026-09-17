# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 450)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.layout_principal = QVBoxLayout(self.centralwidget)
        self.layout_principal.setObjectName(u"layout_principal")

        self.label_musica = QLabel(self.centralwidget)
        self.label_musica.setObjectName(u"label_musica")
        self.label_musica.setAlignment(Qt.AlignCenter)
        self.layout_principal.addWidget(self.label_musica)

        self.lista_musicas = QListWidget(self.centralwidget)
        self.lista_musicas.setObjectName(u"lista_musicas")

        # Permite selecionar várias músicas usando Ctrl/Shift.
        self.lista_musicas.setSelectionMode(
            QListWidget.SelectionMode.ExtendedSelection
        )

        self.layout_principal.addWidget(self.lista_musicas)

        self.linha_progresso = QHBoxLayout()
        self.linha_progresso.setObjectName(u"linha_progresso")

        self.label_tempo_atual = QLabel(self.centralwidget)
        self.label_tempo_atual.setObjectName(u"label_tempo_atual")
        self.linha_progresso.addWidget(self.label_tempo_atual)

        self.slider_posicao = QSlider(self.centralwidget)
        self.slider_posicao.setObjectName(u"slider_posicao")
        self.slider_posicao.setOrientation(Qt.Horizontal)
        self.slider_posicao.setMaximum(0)
        self.linha_progresso.addWidget(self.slider_posicao)

        self.label_tempo_total = QLabel(self.centralwidget)
        self.label_tempo_total.setObjectName(u"label_tempo_total")
        self.linha_progresso.addWidget(self.label_tempo_total)

        self.layout_principal.addLayout(self.linha_progresso)

        self.barra_botoes = QHBoxLayout()
        self.barra_botoes.setObjectName(u"barra_botoes")

        self.spacer_esquerda = QSpacerItem(
            40, 20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )
        self.barra_botoes.addItem(self.spacer_esquerda)

        self.btn_abrir = QPushButton(self.centralwidget)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.barra_botoes.addWidget(self.btn_abrir)

        self.btn_retroceder = QPushButton(self.centralwidget)
        self.btn_retroceder.setObjectName(u"btn_retroceder")
        self.barra_botoes.addWidget(self.btn_retroceder)

        self.btn_play = QPushButton(self.centralwidget)
        self.btn_play.setObjectName(u"btn_play")
        self.barra_botoes.addWidget(self.btn_play)

        self.btn_pause = QPushButton(self.centralwidget)
        self.btn_pause.setObjectName(u"btn_pause")
        self.barra_botoes.addWidget(self.btn_pause)

        self.btn_parar = QPushButton(self.centralwidget)
        self.btn_parar.setObjectName(u"btn_parar")
        self.barra_botoes.addWidget(self.btn_parar)

        self.btn_avancar = QPushButton(self.centralwidget)
        self.btn_avancar.setObjectName(u"btn_avancar")
        self.barra_botoes.addWidget(self.btn_avancar)

        # Novo botão para excluir músicas selecionadas.
        self.btn_excluir = QPushButton(self.centralwidget)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.barra_botoes.addWidget(self.btn_excluir)

        self.spacer_direita = QSpacerItem(
            40, 20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )
        self.barra_botoes.addItem(self.spacer_direita)

        self.layout_principal.addLayout(self.barra_botoes)

        self.linha_volume = QHBoxLayout()
        self.linha_volume.setObjectName(u"linha_volume")

        self.label_volume = QLabel(self.centralwidget)
        self.label_volume.setObjectName(u"label_volume")
        self.linha_volume.addWidget(self.label_volume)

        self.slider_volume = QSlider(self.centralwidget)
        self.slider_volume.setObjectName(u"slider_volume")
        self.slider_volume.setOrientation(Qt.Horizontal)
        self.slider_volume.setMaximum(100)
        self.slider_volume.setValue(50)
        self.linha_volume.addWidget(self.slider_volume)

        self.layout_principal.addLayout(self.linha_volume)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                u"\U0001f3b5 Horizon Media Player",
                None
            )
        )

        self.label_musica.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Nenhuma música carregada",
                None
            )
        )

        self.label_tempo_atual.setText(
            QCoreApplication.translate("MainWindow", u"00:00", None)
        )

        self.label_tempo_total.setText(
            QCoreApplication.translate("MainWindow", u"00:00", None)
        )

        self.btn_abrir.setText(
            QCoreApplication.translate("MainWindow", u" Abrir", None)
        )

        self.btn_abrir.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"Abrir músicas",
                None
            )
        )

        self.btn_retroceder.setText("")
        self.btn_retroceder.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"Música anterior",
                None
            )
        )

        self.btn_play.setText("")
        self.btn_play.setToolTip(
            QCoreApplication.translate("MainWindow", u"Play", None)
        )

        self.btn_pause.setText("")
        self.btn_pause.setToolTip(
            QCoreApplication.translate("MainWindow", u"Pause", None)
        )

        self.btn_parar.setText("")
        self.btn_parar.setToolTip(
            QCoreApplication.translate("MainWindow", u"Parar", None)
        )

        self.btn_avancar.setText("")
        self.btn_avancar.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"Próxima música",
                None
            )
        )

        self.btn_excluir.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Excluir",
                None
            )
        )

        self.btn_excluir.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"Excluir música(s) selecionada(s)",
                None
            )
        )

        self.label_volume.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"\U0001f50a Volume:",
                None
            )
        )
