from PyQt5 import QtWidgets

from log_in import LogInWindow
from admin import MainWindowAdmin
from user import MainWindowUser
from editor import MainWindowEditor


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # main_window_admin = MainWindowAdmin("duushess")
    # main_window_admin.show()
    # main_window_admin.get_data()
    log_in_window = LogInWindow()
    log_in_window.show()
    # main_window_user = MainWindowUser("blondy", 500)
    # main_window_user.show()
    # main_window_user.get_data()
    # main_window_editor = MainWindowEditor("berkutov")
    # main_window_editor.show()
    # main_window_editor.get_races_data()
    # main_window_editor.get_bets_data()
    sys.exit(app.exec_())