import datetime
import time
import calendar


class TimeHelper:
    input_time_format = '%d.%m.%Y - %H:%M:%S'
    clock_time_format = '%H:%M:%S'

    @staticmethod
    def get_time_in_s(json_time):
        d = time.mktime(datetime.datetime.strptime(json_time, TimeHelper.input_time_format).timetuple())
        return int(d)

    @staticmethod
    def get_time_string(time_in_ms):
        return datetime.datetime.fromtimestamp(time_in_ms).strftime(TimeHelper.input_time_format)

    @staticmethod
    def get_stopwatch_time_string(time_in_ms):
        return str(time.strftime(TimeHelper.clock_time_format, time.gmtime(time_in_ms)))

    @staticmethod
    def get_weekday(time_in_ms):
        return str(calendar.day_name[datetime.datetime.fromtimestamp(time_in_ms).weekday()])
