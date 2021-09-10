__author__ = "Robert van der Leeuw"
__date__ = "11/9/2021"

from datetime import datetime


def CheckTime(strtime: str):
	try:
		dtime = datetime.strptime(strtime, '%d %B %Y %H:%M')
		if (dtime - datetime.now()).seconds < 0:
			print('That time already passed.')
			return None

		return dtime
	except ValueError:
		print('Invalid time argument')
		return None
