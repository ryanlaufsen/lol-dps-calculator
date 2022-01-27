from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from lol_dps_calculator_gui import Ui_MainWindow
from lol_dps_calculator import calculateDPS

atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps = calculateDPS()

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps)
        self.show()


def main():
    app = QApplication([])
    w = AppWindow()

    def getDPS():
        atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps = calculateDPS()
        w.ui.retranslateUi(atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps)
        print(atk_dmg, atk_speed, crit_chance, crit_multiplier, average_dps)

    timer = QTimer(w)
    timer.timeout.connect(getDPS)
    timer.start(1000)

    w.show()
    app.exec()

if __name__ == '__main__':
    main()

