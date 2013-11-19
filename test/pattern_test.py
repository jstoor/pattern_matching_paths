from base import BaseTestCase


class PatternTestCase(BaseTestCase):
	def test_pattern_non_ascii(self):
		self.assertTrue(False)

	def test_patterns_unique(self):
		self.assertTrue(False)

	def test_patterns_not_unique(self):
		self.assertTrue(False)

	def test_pattern_invalid_format(self):
		# A pattern is a comma-separated sequence of non-empty fields.
		self.assertTrue(False)

	def test_pattern_no_match(self):
		self.assertTrue(False)

	def test_pattern_basic_match(self):
		self.assertTrue(False)

	def test_pattern_basic_no_match(self):
		self.assertTrue(False)

	def test_pattern_ignore_leading_slashes(self):
		self.assertTrue(False)

	def test_pattern_ignore_trailing_slashes(self):
		self.assertTrue(False)

	def test_patterm_ignore_leading_trailing_slashes(self):
		self.assertTrue(False)

	# For example, the pattern `A,*,B,*,C` consists of five fields: three
	# strings and two wildcards. It will successfully match the paths
	# `A/foo/B/bar/C` and `A/123/B/456/C`, but not `A/B/C`,
	# `A/foo/bar/B/baz/C`, or `foo/B/bar/C`.

	def test_pattern_wildcard_match(self):
		# Patterns can also contain a special field consisting of a *single
		# asterisk*, which is a wildcard and can match any string in the path.
		self.assertTrue(False)

	def test_patterm_wildcard_no_match(self):
		self.assertTrue(False)


	def test_pattern_best_matching(self):
		# For each path encountered in the input, print the *best-matching
		# pattern*. The best-matching pattern is the one which matches the path
		# using the fewest wildcards.

		# If there is a tie (that is, if two or more patterns with the same number
		# of wildcards match a path), prefer the pattern whose leftmost wildcard
		# appears in a field further to the right. If multiple patterns' leftmost
		# wildcards appear in the same field position, apply this rule recursively
		# to the remainder of the pattern.

		# For example: given the patterns `*,*,c` and `*,b,*`, and the path
		# `/a/b/c/`, the best-matching pattern would be `*,b,*`.
		self.assertTrue(False)