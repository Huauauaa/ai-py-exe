#!/usr/bin/env python3
"""PyQt desktop app to display current local time."""

from datetime import datetime
import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class TimeWindow(QWidget):
    """Small window that refreshes and displays local time."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Time Tool")
        self.resize(420, 180)

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 24px; font-family: monospace;")

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self) -> None:
        now = datetime.now().astimezone()
        self.time_label.setText(now.strftime("%Y-%m-%d %H:%M:%S %Z"))


def main() -> int:
    app = QApplication(sys.argv)
    window = TimeWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
