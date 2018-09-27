
from datetime import datetime


class Date:
    def __init__(self, date_string=None, date_format='%Y-%m-%d'):
        if date_string:
            self.date_object = datetime.strptime(date_string, date_format).date()
        else:
            self.date_object = datetime.now().date()

        self.year = self.date_object.year
        self.month = self.date_object.month
        self.month_zero_padded = self.date_object.strftime('%m')
        self.day = self.date_object.day
        self.day_zero_padded = self.date_object.strftime('%d')
        self.month_three_letter = self.date_object.strftime('%b')
        self.month_three_letter_upper_case = self.month_three_letter.upper()
        self.month_three_letter_lower_case = self.month_three_letter.lower()



    def __str__(self):
        return str(self.date_object)


