from datetime import datetime


class DateUtils:
    def is_curr_time_less_than_given(self,date_stamp_to_check):
        current_timestamp = datetime.timestamp(datetime.now())

        return date_stamp_to_check>current_timestamp