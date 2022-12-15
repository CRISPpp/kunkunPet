import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import random


class CXK(QWidget):
    def __init__(self):
        super(CXK, self).__init__()
        self.initUi()
        self.tray()
        self.crazy = False
        self.crazyTimeUnit = 10
        self.timeunit = 1000
        self.is_follow_mouse = False
        self.mouse_drag_pos = self.pos()
        #计时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleAction)
        self.timer.start(self.timeunit)

        self.crazyTimer = QTimer()
        self.crazyTimer.timeout.connect(self.handleCrazyAction)

        self.jiMap = {}
    def handleCrazyAction(self):
        if self.timeKey > 4:
            self.timeKey = 1
        self.ji_url = './image/ji' + str(self.timeKey) + '.png'
        self.pm = QPixmap(self.ji_url)
        self.lbl.setPixmap(self.pm)
        self.timeKey += 1
        if self.crazy:
            self.move(random.randint(0, QDesktopWidget().availableGeometry().right()), random.randint(0, QDesktopWidget().availableGeometry().height()))
        else:
            self.crazyTimer.stop()
            self.timer.start(self.timeunit)

    def handleAction(self):
        if self.timeKey > 4:
            self.timeKey = 1
        self.ji_url = './image/ji' + str(self.timeKey) + '.png'
        self.pm = QPixmap(self.ji_url)
        self.lbl.setPixmap(self.pm)
        self.timeKey += 1
        if self.crazy:
            self.timer.stop()
            self.crazyTimer.start(self.crazyTimeUnit)



    def initUi(self):
        self.setGeometry(QDesktopWidget().availableGeometry().right() - 300, QDesktopWidget().availableGeometry().height() - 300, 240, 240)
        self.lbl = QLabel(self)
        self.timeKey = 1
        self.ji_url = './image/ji' + str(self.timeKey) + '.png'
        self.pm = QPixmap(self.ji_url)
        self.lbl.setPixmap(self.pm)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()
    # 托盘
    def tray(self):
        tp = QSystemTrayIcon(self)
        tp.setIcon(QIcon('./image/ji' + str(self.timeKey) + '.png'))
        actiontionQuit = QAction('ji', self, triggered=self.quit)
        tpMenu = QMenu(self)
        tpMenu.addAction(actiontionQuit)
        tp.setContextMenu(tpMenu)
        tp.show()

    def quit(self):
        self.close()
        sys.exit()

    def keyPressEvent(self,event):

        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_F:
            print("按下：" + 'ctrl + f')
            self.jiMap.clear()
            self.crazy = False
            mp3file = "./audio/ngm.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()

        if event.key() == Qt.Key_6:
            print("按下：" + '6666666')
            mp3file = "./audio/kg.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()

        if event.key() == Qt.Key_J:
            print("按下：" + 'j')
            mp3file = "./audio/ji.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()

        if event.key() == Qt.Key_N:
            print("按下：" + 'n')
            mp3file = "./audio/ni.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()

        if event.key() == Qt.Key_T:
            print("按下：" + 't')
            mp3file = "./audio/tai.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()

        if event.key() == Qt.Key_M:
            print("按下：" + 'm')
            mp3file = "./audio/mei.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()

        if event.key() == Qt.Key_C:
            print("按下：" + 'c')
            mp3file = "./audio/c.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()
            self.jiMap['C'] = True
            if len(self.jiMap) == 4:
                self.crazy = True
                mp3file = "./audio/ctrl.mp3"
                self.player = QMediaPlayer()
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
                self.player.play()
                self.jiMap.clear()


        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_T:
            print("按下：" + 'ctrl + t')
            mp3file = "./audio/t.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()
            self.jiMap['T'] = True
            if len(self.jiMap) == 4:
                self.crazy = True
                mp3file = "./audio/ctrl.mp3"
                self.player = QMediaPlayer()
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
                self.player.play()
                self.jiMap.clear()

        if event.key() == Qt.Key_R:
            print("按下：" + 'r')
            mp3file = "./audio/rap.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()
            self.jiMap['R'] = True
            if len(self.jiMap) == 4:
                self.crazy = True
                mp3file = "./audio/ctrl.mp3"
                self.player = QMediaPlayer()
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
                self.player.play()
                self.jiMap.clear()

        if event.key() == Qt.Key_L:
            print("按下：" + 'l')
            mp3file = "./audio/lanqiu.mp3"
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
            self.player.play()
            self.jiMap['L'] = True
            if len(self.jiMap) == 4:
                self.crazy = True
                mp3file = "./audio/ctrl.mp3"
                self.player = QMediaPlayer()
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3file)))
                self.player.play()
                self.jiMap.clear()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            xy = self.pos()
            event.accept()
    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ji = CXK()
    sys.exit(app.exec_())
