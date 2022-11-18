from datetime import datetime

class UserData:
    def __init__(self):
        self.stock_symbol = input("\nEnter the stock symbol you are looking for:  ")
        self.chart_type = self.__get_chart_type()
        self.requested_function = self.__get_requested_function()
        self.start_date = self.__get_formatted_date_str()
        self.end_date = self.__get_formatted_date_str("end", self.start_date)

    def __get_chart_type(self):
        chart_type = 0
        error_msg = "\n💥ERROR:  Please enter one of the availabe options (1 or 2).💥"
        while True:
            print("\nChart Types")
            print("-------------")
            print("1. Bar")
            print("2. Line")
            chart_type_str = input("\nEnter the chart type you want (1, 2):  ")
            try:
                chart_type = int(chart_type_str)
            except:
                print(error_msg)
            else:
                if chart_type == 1 or chart_type == 2:
                    break
                else:
                    print(error_msg)
        return chart_type

    def __get_requested_function(self):
        requested_function = 0
        error_msg = "\n💥ERROR:  Please enter one of the availabe options (1, 2, 3, or 4).💥"
        while True:
            print("\nSelect the Time Series of the chart you want to Generate")
            print("----------------------------------------------------------")
            print("1. Intraday")
            print("2. Daily")
            print("3. Weekly")
            print("4. Monthly")
            requested_function_str = input("\nEnter the time series option (1, 2, 3, or 4):  ")

            try:
                requested_function = int(requested_function_str)
            except:
                print(error_msg)
            else:
                if requested_function == 1 or requested_function == 2 or requested_function == 3 or requested_function == 4:
                    break
                else:
                    print(error_msg)
        return requested_function

    def __get_formatted_date_str(self, date_name: str = "start", start_date: str = ""):
        date_str = ""
        error_msg = "\n💥ERROR:  Please enter the date in the following format (YYYY-MM-DD).💥"
        while True:
            user_date_str = input(f"\nEnter the {date_name} Date (YYYY-MM-DD):  ")
            try:
                str_list = user_date_str.split("-")
            except:
                print(error_msg)
            else:
                if self.__is_valid_date_string(str_list):
                    try:
                        new_date = self.__get_valid_date(str_list)
                    except Exception as ex:
                        print(ex)
                    else:
                        if date_name == "end":
                            if new_date > datetime.strptime(start_date, "%Y-%m-%d"):
                                date_str = "-".join(str_list)
                                break
                            else:
                                print("\n💥ERROR:  The end date must be greater than the start date.💥")
                        else:
                            date_str = "-".join(str_list)
                            break
                else:
                    print(error_msg)
        return date_str

    def __is_valid_date_string(self, str_list):
        if len(str_list[0]) == 4 and len(str_list[1]) == 2 and len(str_list[2]) == 2:
            if str_list[0].isdigit() and str_list[1].isdigit() and str_list[2].isdigit():
                return True
        return False

    def __get_valid_date(self, str_list):
        try:
            new_date = datetime(year=int(str_list[0]), month=int(str_list[1]), day=int(str_list[2]))
        except:
            raise Exception(f'\n💥ERROR:  {"-".join(str_list)} is not a valid date. Please try again.💥')
        else:
            return new_date