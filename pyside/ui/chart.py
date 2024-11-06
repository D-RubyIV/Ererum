import sys

from PySide6 import QtWidgets, QtCore, QtGui, QtCharts


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        self.main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.main_widget)

        # Tạo các bộ dữ liệu cho hai phòng
        self.set0 = QtCharts.QBarSet("Room 1")
        self.set1 = QtCharts.QBarSet("Room 2")

        room1 = {"Lighting": 1000, "People": 150, "Appliances": 1200, "Roof": 300, "Floor": 0}
        room2 = {"Lighting": 1000, "People": 150, "Appliances": 1200, "Roof": 300, "Floor": 0}

        # Thêm dữ liệu vào các bộ dữ liệu
        self.set0.append(list(room1.values()))
        self.set1.append(list(room2.values()))

        # Tạo chuỗi dữ liệu biểu đồ thanh và thêm các bộ dữ liệu
        self.bar_series = QtCharts.QBarSeries()
        self.bar_series.append(self.set0)
        self.bar_series.append(self.set1)

        # Thiết lập biểu đồ
        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.bar_series)
        self.chart.setTitle("Bar chart example")

        # Thiết lập trục x với các danh mục
        self.categories = ["Lighting", "People", "Appliances", "Roof", "Floor"]
        self.x_axis = QtCharts.QBarCategoryAxis()
        self.x_axis.append(self.categories)
        self.chart.setAxisX(self.x_axis, self.bar_series)

        # Thiết lập trục y với khoảng giá trị
        self.y_axis = QtCharts.QValueAxis()
        self.chart.setAxisY(self.y_axis, self.bar_series)
        self.y_axis.setRange(0, 2000)

        # Thiết lập chú thích, tiêu đề trục và hiệu ứng
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.chart.axisX().setTitleText("Heat Gain Component")
        self.chart.axisY().setTitleText("Heat Gain W")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        # Tạo và thêm QChartView vào giao diện người dùng
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.vertical_layout.addWidget(self.chart_view)


# Khởi chạy ứng dụng
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
