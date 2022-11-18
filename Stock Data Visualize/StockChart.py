import pygal

class StockChart:
    def __init__(self, user_data, stock_data):
        self.user_data = user_data
        self.stock_data = stock_data
        self.date_list = []
        self.open_list = []
        self.close_list = []
        self.high_list = []
        self.low_list = []
        self.__populate_chart_lists()

    def __populate_chart_lists(self):
        for key, value in self.stock_data.data_dictionary.items():
            self.date_list.append(key)
            for datapoint_key, datapoint_value in value.items():
                if "open" in datapoint_key:
                    datapoint_number = float(datapoint_value)
                    self.open_list.append(datapoint_number)
                if "close" in datapoint_key:
                    datapoint_number = float(datapoint_value)
                    self.close_list.append(datapoint_number)
                if "high" in datapoint_key:
                    datapoint_number = float(datapoint_value)
                    self.high_list.append(datapoint_number)
                if "low" in datapoint_key:
                    datapoint_number = float(datapoint_value)
                    self.low_list.append(datapoint_number)

    def display_chart(self):
        # Reverse the order so the dates are in ascending order.
        self.date_list.reverse()

        # Build chart
        if self.user_data.chart_type == 1:
            chart = pygal.Bar(x_label_rotation=45)
        else:
            chart = pygal.Line(x_label_rotation=45)
        chart.title = f"Stock Data for {self.user_data.stock_symbol}:  {self.user_data.start_date} to {self.user_data.end_date}"
        chart.x_labels = self.date_list
        chart.add("Open", self.open_list)
        chart.add("High", self.high_list)
        chart.add("Low", self.low_list)
        chart.add("Close", self.close_list)
        chart.render_in_browser()