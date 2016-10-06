import datetime
import time


class TimeHelper:
    input_time_format = '%d.%m.%Y - %H:%M:%S'
    clock_time_format = '%H:%M:%S'

    @staticmethod
    def get_time_in_ms(json_time):
        d = time.mktime(datetime.datetime.strptime(json_time, TimeHelper.input_time_format).timetuple())
        print(int(d))
        return int(d)

    @staticmethod
    def get_time_string(time_in_ms):
        return datetime.date.fromtimestamp(time_in_ms).strftime(TimeHelper.input_time_format)

    @staticmethod
    def get_stopwatch_time_string(time_in_ms):
        return str(time.strftime(TimeHelper.clock_time_format, time.gmtime(time_in_ms)))
