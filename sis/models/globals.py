
import time

year = 0


class Globals():


    def get_year(a):
        # prefetch
        global year
        if year == 0:
            year = time.strftime('%Y')
            res = int(year)
            return res
        else:
            return year
