import sys
from PySide6 import QtWidgets, QtCore, QtGui, QtCharts


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        self.main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.main_widget)

        # Tạo chuỗi dữ liệu biểu đồ đường cho hai phòng
        self.series_room1 = QtCharts.QSplineSeries()
        self.series_room1.setName("Room 1")
        self.series_room2 = QtCharts.QSplineSeries()
        self.series_room2.setName("Room 2")

        room1 = {"Lighting": 1000, "People": 150, "Appliances": 1200, "Roof": 300, "Floor": 0}
        room2 = {"Lighting": 1000, "People": 150, "Appliances": 1200, "Roof": 300, "Floor": 0}

        # Thêm dữ liệu vào các chuỗi
        for i, (key, value) in enumerate(room1.items()):
            self.series_room1.append(i, value)
        for i, (key, value) in enumerate(room2.items()):
            self.series_room2.append(i, value)

        # Thiết lập biểu đồ
        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series_room1)
        self.chart.addSeries(self.series_room2)
        self.chart.setTitle("Line chart example")

        # Thiết lập trục x với các danh mục
        self.categories = ["Lighting", "People", "Appliances", "Roof", "Floor"]
        self.x_axis = QtCharts.QCategoryAxis()
        for i, category in enumerate(self.categories):
            self.x_axis.append(category, i)
        self.chart.setAxisX(self.x_axis, self.series_room1)
        self.chart.setAxisX(self.x_axis, self.series_room2)

        # Thiết lập trục y với khoảng giá trị
        self.y_axis = QtCharts.QValueAxis()
        self.chart.setAxisY(self.y_axis, self.series_room1)
        self.chart.setAxisY(self.y_axis, self.series_room2)
        self.y_axis.setRange(0, 2000)

        # Thiết lập chú thích, tiêu đề trục và hiệu ứng
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.chart.axisX().setTitleText("Heat Gain Component")
        self.chart.axisY().setTitleText("Heat Gain W")
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        # Tạo và thêm QChartView vào giao diện người dùng
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.vertical_layout.addWidget(self.chart_view)


# Khởi chạy ứng dụng
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
