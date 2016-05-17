# author : Moch Deden
# site : http://selesdepselesnul.com
import time
from datetime import date, datetime
import re

class RdtParser:

	d = '(([0-2][0-9])|(3[0-1]))'
	m = '((0[1-9])|(1[0-2]))'
	y = '((0[1-9])|([1-9][0-9]))'
	Y = '(\\d{4})'

	@staticmethod
	def parse(date_str):
		if RdtParser._is_parsed_with_pattern(date_str, 
			RdtParser.d+'-'+RdtParser.m+'-'+RdtParser.Y):
			return datetime.strptime(date_str, '%d-%m-%Y')
		elif RdtParser._is_parsed_with_pattern(date_str,
			RdtParser.Y+'-'+RdtParser.m+'-'+RdtParser.d):
			return datetime.strptime(date_str, '%Y-%m-%d')
		elif RdtParser._is_parsed_with_pattern(date_str,
			RdtParser.m+'-'+RdtParser.d+'-'+RdtParser.Y):
			return datetime.strptime(date_str, '%m-%d-%Y')
		elif RdtParser._is_parsed_with_pattern(date_str,
			RdtParser.d+'/'+RdtParser.m+'/'+RdtParser.Y):
			return datetime.strptime(date_str, '%d/%m/%Y')
		elif RdtParser._is_parsed_with_pattern(date_str,
			RdtParser.Y+'/'+RdtParser.m+'/'+RdtParser.d):
			return datetime.strptime(date_str, '%Y/%m/%d')
		elif RdtParser._is_parsed_with_pattern(date_str,
			RdtParser.m+'/'+RdtParser.d+'/'+RdtParser.Y):
			return datetime.strptime(date_str, '%m/%d/%Y')
		elif RdtParser._is_parsed_with_pattern(date_str,
			RdtParser.m+'/'+RdtParser.d+'/'+RdtParser.y):
			return datetime.strptime(date_str, '%m/%d/%y')
		else:
			return None

	@staticmethod
	def _is_parsed_with_pattern(date_str, pattern):
		regex = re.compile(pattern)
		if regex.fullmatch(date_str):
			return True
		else:
			return False


# d/m/Y
# m/d/Y
# Y/m/d
# m/d/y
print(date.today() - datetime.strptime('12/05/2016', '%d/%m/%Y').date())
print(date.today() - datetime.strptime('05/12/2016', '%m/%d/%Y').date())
print(date.today() - datetime.strptime('2016/05/12', '%Y/%m/%d').date())
print(date.today() - datetime.strptime('05/12/16', '%m/%d/%y').date())

# string localization
# string custom

# d-m-Y 
# m-d-Y
# Y-m-d (format utama)(paling banyak)
print(RdtParser.parse('31-01-2016'))
print(RdtParser.parse('01-31-2016'))
print(RdtParser.parse('2016-01-31'))

# d/m/Y
# m/d/Y
# Y/m/d
# m/d/y
print(RdtParser.parse('31/01/2016'))
print(RdtParser.parse('01/31/2016'))
print(RdtParser.parse('2016/01/31'))
print(RdtParser.parse('01/31/16'))
