from datetime import datetime, timedelta
from calendar import monthrange

from PyQt6.QtWidgets import QGridLayout, QComboBox, QCalendarWidget
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt
from PyQt6.QtCharts import QChartView, QChart, QBarSet, QStackedBarSeries, QBarCategoryAxis, QValueAxis

from functions.db_Helper import Db_helper

class Statistic_widget(QGridLayout):
    def __init__(self):
        super().__init__()
        self.helper_beta = Db_helper("Beta.db")
        self.helper_alpha = Db_helper("Alpha.db")
        self.chartView = None
        self.date_of_calendar = ''
        self.text_of_graphic = ''
        self.period = QComboBox()
        self.period.currentTextChanged.connect(self.period_text_changed)
        period = ["day", "month", "year"]
        for i in period:
            self.period.addItem(i)
        self.enter_data = QCalendarWidget()
        self.enter_data.clicked.connect(self.show_day_statistic)
        self.addWidget(self.period, 2, 0, 1, 2)
        self.addWidget(self.enter_data, 0, 7, 3, 13 )

    def period_text_changed(self, e):
        self.date_of_calendar = ''
        if e == "day":
            self.axisX, self.set0, self.set1 = self.show_todays_statistic(time_start_="start of day", group_="%Y%m%d %H", time_size="hour", plus_time = timedelta(hours=1))
        elif e == "month":
            self.axisX, self.set0, self.set1 = self.show_todays_statistic(time_start_="start of month", group_="%Y%m%d", time_size="day", plus_time = timedelta(days=1))
        elif e == "year":
            self.axisX, self.set0, self.set1 = self.show_todays_statistic(time_start_="start of year", group_="%Y%m", time_size="month", plus_time = timedelta(weeks=5))
        self.drow_statistic()

    def show_todays_statistic(self, time_start_, group_, time_size, plus_time):
            set0 = QBarSet("cash")
            set1 = QBarSet("card")
            axisX =QBarCategoryAxis()
            info, first_date = self.get_categories(time_start=time_start_, group=group_)
            first_date_datetime = datetime.fromisoformat(first_date)
            counter = 0
            time_size_func = {"day" : self.get_max_month_days(first_date_datetime), "hour": 24, "month": 12}
            time_label_graphic = {"hour": f"{first_date_datetime.year}-{first_date_datetime.month}-{first_date_datetime.day}",
                                  "day": f"{first_date_datetime.year}-{first_date_datetime.month}",
                                  "month": f"{first_date_datetime.year}"}
            self.text_of_graphic = time_label_graphic[time_size]
            for b in range(time_size_func[time_size]):
                if info!= [] and  f"{getattr(datetime.fromisoformat(info[counter][2]), time_size)}" == f"{getattr(first_date_datetime, time_size)}":
                    axisX.append([f"{getattr(first_date_datetime, time_size)}"])
                    set0.append(info[counter][0])
                    set1.append(info[counter][1])
                    if counter < len(info)-1:
                        counter += 1
                else:
                    set0.append(0)
                    set1.append(0)
                    axisX.append([f"{getattr(first_date_datetime, time_size)}"])
                first_date_datetime += plus_time
            return axisX, set0, set1

    def get_categories(self, group, time_start):
        info1 = self.helper_alpha.get_list(f"""SELECT sum(cash), sum(card), time_close 
                                            FROM "ClosedOrder"
                                            WHERE time_close LIKE '%{self.date_of_calendar}%'
                                            GROUP BY strftime('{group}', time_close); """)

        info2 = self.helper_beta.get_list(f"""SELECT sum(cash), sum(card), time_close 
                                            FROM "HistoryTable"
                                            WHERE time_close LIKE '%{self.date_of_calendar}%'
                                            GROUP BY strftime('{group}', time_close); """)
        if self.date_of_calendar == '':
            first_date = self.helper_alpha.select_magic(selector=f"datetime('now', '{time_start}')")
        else:
            first_date = self.helper_alpha.select_magic(selector=f"datetime('{self.date_of_calendar}', '{time_start}')")
        if time_start == "start of day":
            info = info1 + info2
        else:
            info = info2 + info1
        return info, str(first_date[0][0])
    
    def show_day_statistic(self, e):
        self.period.setCurrentText("day")
        dat = self.enter_data.selectedDate()
        day = str(dat.day())
        month = str(dat.month())
        year = str(dat.year())
        if len(day) == 1:
            day = "0" + day
        if len(month) == 1:
            month = "0" + month
        self.date_of_calendar = f"{year}-{month}-{day}"
        self.axisX, self.set0, self.set1 = self.show_todays_statistic(time_start_="start of day", group_="%Y%m %H", time_size="hour", plus_time = timedelta(hours=1))
        self.drow_statistic()    

    def get_max_month_days(self, date):
        return monthrange(date.year, date.month)[1] 
    
    def drow_statistic(self):
        if self.chartView != None:
            self.removeWidget(self.chartView)
        self.series = QStackedBarSeries()
        self.chart = QChart()
        self.axisY = QValueAxis()
        self.chartView = QChartView(self.chart)
        self.chart.setTitle(self.text_of_graphic)
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chartView.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.series.append(self.set0)
        self.series.append(self.set1)
        self.chart.addSeries(self.series)
        self.chart.addAxis(self.axisX, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(self.axisY, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)
        self.addWidget(self.chartView, 3, 0, 16, 20) 