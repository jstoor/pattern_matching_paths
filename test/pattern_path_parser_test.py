import sys
from base import BaseTestCase
from cStringIO import StringIO

from scooby.pattern_path_parser import PatternPathParser

class PatternPathParserTestCase(BaseTestCase):
	def test_parse_counter(self):
		self.assertEqual(5, PatternPathParser()._parse_counter('5'))

	def test_parse_counter_raises_exception(self):
		self.assertRaises(TypeError, PatternPathParser()._parse_counter, 'abc')

	def test_get_patterns(self):
		with open('test/file_01.txt') as f:
			patterns = PatternPathParser()._get_patterns(f)
			self.assertTrue(patterns)
			self.assertEqual(len(patterns), 6)

	def test_number_of_patterns_omitted(self):
		with open('test/file_pattern_count_ommitted.txt') as f:
			self.assertRaises(TypeError, PatternPathParser()._get_patterns, f)

	def test_convert_pattern(self):
		source = '*,ABC,*,X'
		expected = '\w*/ABC/\w*/X'
		self.assertEqual(expected, PatternPathParser()._convert_pattern(source))

	def test_convert_patterns_to_regex_format(self):
		source = ['*,ABC,*,X', 'foo,bar']
		expected = [('*,ABC,*,X', '\w*/ABC/\w*/X'), ('foo,bar', 'foo/bar')]
		self.assertEqual(expected, PatternPathParser()._convert_patterns_to_regex_format(source))

	def test_read_paths(self):
		with open('test/file_paths_only.txt') as f:
			path_gen = PatternPathParser()._read_paths(f)
			number_of_paths = path_gen.next()
			self.assertEqual(5, number_of_paths)
			self.assertEqual(5, len(list(path_gen)))
			
	def test_process_paths(self):
		expected = "w,x,*,*\n*,b,*\nNO MATCH\nNO MATCH\nfoo,bar,baz\n"
		result = None
		backup = sys.stdout
		with open('test/file_01.txt') as f:
			try:
				sys.stdout = StringIO()
				PatternPathParser().process_paths(f)
				result = sys.stdout.getvalue()
			finally:
				sys.stdout.close() 
				sys.stdout = backup
		self.assertEqual(expected, result)
