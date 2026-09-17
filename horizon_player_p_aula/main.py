import os
import sys
from PySide6.QtCore import QEvent, Qt, QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QStyle,
)

from interface_ui import Ui_MainWindow

class HorizonPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Horizon Player")

        self.playlist = []
        self.indice_atual = -1

        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)

        self.audio_output.setVolume(0.5) # Define o volume inicial 50%

        #self._configurar_icones()
        #self._conectar_sinais()
        
        def _configurar_icones(self):
            estilo = self.style()
            self.ui.btn_abrir.setIcon(estilo.standardIcon(QStyle.SP_DialogOpenButton))

            self.ui.btn_retroceder.setIcon(estilo.standardIcon(QStyle.SP_MediaSeekBackword))
            self.ui.btn_play.setIcon(estilo.standardIcon(QStyle.SP_MediaPlay))
            self.ui.btn_pause.setIcon(estilo.standardIcon(QStyle.SP_MediaPause))
            self.ui.btn_parar.setIcon(estilo.standardIcon(QStyle.SP_MediaStop))
            
            self.ui.btn_avancar.setIcon(estilo.standardIcon(QStyle.SP_MediaSeekForward))
        

        def _conectar_senais(self):

            #Clicar em Abrir chama abrir_arquivos().

            self.ui.btn_abrir.clicked.connect(self.abrir_arquivos)

            self.ui.btn_play.clicked.connect(self.player.play)
            self.ui.btn_pause.clicked.connect(self.player.pause)
            self.ui.btn_parar.clicked.connect(self.player.stop)

            self.ui.btn_avancar.clicked.connect(self.proxima_musica)
            self.ui.btn_retroceder.clicked.connect(self.musica_anterior)

            self.ui.lista_musicas.itemDoubleClicked.connect(
                self.tocar_musica_selecoinada
            )

            self.ui.slider_volume.valueChanged.connect(
                lambda v: self.audio_output.setVolume(v / 100.0)
            )

            self.ui.slider_posicao.sliderMoved.connect(
                self.player.setPosition
            )

            self.player.positionChanged.connect(self.atualizar_posicao)

            self.player.durationChanged.connect(self.atualizar_duracao)

            self.player.mediaStatusChanged.connect(
                self.verificar_fim_da_faixa
            )

        # ABRIR MÚSICAS

        def abrir_arquivos(self):

            arquivos, _ = QFileDialog.getOpenFileNames(
                self,
                "Selecionar Músicas", 
                "",
                "Arquivos de (*.mp3 *.wav *.ogg *.flac *.m4a)"
            )

            if arquivos:
                for caminho in arquivos:
                    nome_arquivo = os.path.basename(caminho)
                    # Adiciona o item da estrutura interna
                    self.playlist.append(
                        {"nome": nome_arquivo, "caminho": caminho}
                    )
                    self.ui.lista_musicas.addItem(f" {nome_arquivo}")

                if self.indice_atual == -1 and len(self.playlist) > 0:
                    self.carregar_e_tocar(0)

        def carregar_e_tocar(self, indice):
            if 0 <= indice < len(self.playlist):
                self.indice_atual = indice
                item_musica = self.playlist[indice]

                #Define a fonte de áudio no QMediaPlayer através de uma  QUrl local

                caminho_local = QUrl.fromLocalFile(item_musica["caminho"])
                self.player.setSourse(caminho_local)

                # Atualiza o rótulo de texto na interface
                self.ui.label_musica.setText(f"🎶 Tocando: {item_musica['nome']}")

                # Destacar a linha correspondente no QListWidget
                self.ui.label_musica.setText.setCurrentRow()

                # Inicia o áudio 
                self.player.play()

        def tocar_musica_selecionada(self):
            linha = self.ui.lista_musicas.currentRow()
            if linha >= 0:
                self.carregar_e_tocar(linha)



        self.ui.btn_excluir.hide()
        self.ui.lista_musicas.setSelectionMode(
            self.ui.lista_musicas.SelectionMode.ExtendedSelection
        )
        self.ui.lista_musicas.installEventFilter(self)

        
        self.setWindowTitle("🎵 Horizon Media Player")
        self.playlist = []
        self.indice_atual = -1
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(0.5)
        self._configurar_icones()
        self._conectar_sinais()

    
if __name__ == "__main__":

    
    
    
    
    app = QApplication(sys.argv)

    
    if os.path.exists("style.qss"):

        
        with open("style.qss", "r", encoding="utf-8") as f:

            
            app.setStyleSheet(f.read())

    
    
    
    janela = HorizonPlayer()

    
    janela.show()

    
    
    
    
    
    
    
    sys.exit(app.exec())
