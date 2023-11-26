#!/usr/bin/env python

"""
fake_text
----------

Tests for the `fake_text` module.
"""

import unittest
import fake_text


class TestFakeText(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sentence_001(self):
        self.assertTrue(fake_text.sentence()[0].isupper())

    def test_sentence_002(self):
        self.assertEqual(fake_text.sentence()[-1], ".")


if __name__ == "__main__":
    import sys
    sys.exit(unittest.main())
