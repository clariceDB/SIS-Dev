
import time

year = 0


class Globals():


    def get_year(a):
        """This method computes and returns the current year using the time package"""
        # prefetch
        global year
        if year == 0:
            year = time.strftime('%Y')
            res = int(year)
            return res
        else:
            return year