import calendar

year = 2017

val = calendar.isleap(year)
if val == true:
	calendar.prmonth(year,4,2,1)
else:
	print("% s is not a leap year" % year)