from PySide2 import QtWidgets
import sys

from game import Method

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    method_curr = Method()
    method_curr.show()
    sys.exit(app.exec_())
