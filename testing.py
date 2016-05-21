from rdtparser import RdtParser
import unittest
import datetime

class RdtParserTest(unittest.TestCase):
	
	def test_parse_with_hypen_dmY(self):
		self.assertEqual(
			datetime.datetime(2016, 4, 12), 
			RdtParser.parse('12-04-2016'))

	def test_parse_with_hypen_Ymd(self):
		self.assertEqual(datetime.datetime(2016, 4, 12), 
			RdtParser.parse('2016-04-12'))
	

if __name__ == '__main__':
    unittest.main()