import os
import sys
import re
from itertools import islice, dropwhile

# Note : Let's make use of Pythons buffered IO and memory management,
#  	     in case we're dealing with an exceptionally large file.


class PatternPathParser(object):
	"""
	Parses source data to find paths that match given patterns.
	Patterns must be supplied as the initial block from source with the first line, 
	being a count of number of patterns following.
	Followed by count of number of paths and the actual path lines. 
	"""
	def __init__(self):
		pass


	def _parse_counter(self, raw_counter):
		"""
		Parses the raw value, validating and returning the integer result.
		"""
		if not raw_counter.isdigit() or int(raw_counter) <= 0:
			raise TypeError('Expecting non-zero, numeric value.')

		result = int(raw_counter)
		return result


	def _get_patterns(self, file_object):
		"""
		Reads the patterns block from the file, into an array and returns the result.
		"""
		raw_counter = file_object.readline().strip()
		pattern_count = self._parse_counter(raw_counter)

		# Read x number of lines from the file, corresponding to the patterns block.
		# Note : File position will be moved, as part of this process.
		patterns = map(lambda x: x.strip(), list(islice(file_object, pattern_count)))

		if len(patterns) != pattern_count:
			raise IndexError('Number of patterns, does not match pattern count value.')

		return patterns


	def _convert_pattern(self, raw_pattern):
		return raw_pattern.replace(',', '/').replace('*', '\w*')


	def _convert_patterns_to_regex_format(self, patterns):
		"""
		Converts the input patterns into a regular expression format,
		returning a list of tuples i.e. original pattern and converted pattern.	
		"""
		result = [(p, self._convert_pattern(p)) for p in patterns]
		return result


	def _read_paths(self, file_object):
		"""
		Generator yielding one path at a time from the input source.
		First return value, will be the path counter.
		"""
		# Data should be starting at offset from pattern section,
		# i.e. beginning of path block.
		raw_counter = file_object.next().strip()
		pattern_count = self._parse_counter(raw_counter)

		yield pattern_count

		for line in file_object:
			yield line


	def process_paths(self, file_object):
		"""
		Loads the patterns from the source data,
		then iterates over the paths, looking for macthes.
		Results of processing, written to stdout.
		"""
		raw_patterns = self._get_patterns(file_object)
		patterns = self._convert_patterns_to_regex_format(raw_patterns)

		path_gen = self._read_paths(file_object)
		number_of_paths = path_gen.next()

		for line in path_gen:
			for p in patterns:
				if re.search(p[1], line, re.IGNORECASE):
					sys.stdout.write(p[0] + '\n')
					break
			else:
				sys.stdout.write("NO MATCH\n")




