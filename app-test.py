from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from lol_dps_calculator_gui import Ui_MainWindow
from lol_dps_calculator import calculate_dps

stats = calculate_dps()

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(
            stats.attack_damage,
            stats.attack_speed,
            stats.crit_chance,
            stats.crit_multiplier,
            stats.average_dps,
        )
        self.show()


def main():
    app = QApplication([])
    w = AppWindow()

    def getDPS():
        data = calculate_dps()
        w.ui.retranslateUi(
            data.attack_damage,
            data.attack_speed,
            data.crit_chance,
            data.crit_multiplier,
            data.average_dps,
        )
        print(
            data.attack_damage,
            data.attack_speed,
            data.crit_chance,
            data.crit_multiplier,
            data.average_dps,
        )

    timer = QTimer(w)
    timer.timeout.connect(getDPS)
    timer.start(1000)

    w.show()
    app.exec()

if __name__ == '__main__':
    main()

