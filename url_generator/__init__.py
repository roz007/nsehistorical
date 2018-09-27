
from datetime import date
from constants import BHAV_COPY_EQUITY_URL
def generate_bhav_copy_equity_url(date_object):
    # BHAV_COPY_EQUITY = f'https://www.nseindia.com/content/historical/EQUITIES/2001/FEB/cm06FEB2001bhav.csv.zip'
    date_object = date.today()

    full_year = date_object.year
    month = date_object.strftime('%m')
    day = date_object.strftime('%d')




