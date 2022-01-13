# -*- coding: utf-8 -*-
# Nimi: Viljami Riihimäki
# Opiskelijanumero: 910048

import unittest
import unittest.mock as mock
import io

from palindrome import palindromi


class TestPalindrome(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_palindromes(self, mock_out):
        """Funktio palindromi palauttaa True kun sille annetaan parametrina merkkijono joka on palindromi."""
        palindromes = (
            "a",
            "aa",
            "aba",
            "abba",
            "abcba",
            "ab c ba",
            "a b cb  a",
            "A BCb a ",
        )
        for p in palindromes:
            self.assertTrue(
                palindromi(p),
                "{!r} on palindromi mutta funktiosi palautti False."
                .format(p))

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_not_palindromes(self, mock_out):
        """Funktio palindromi palauttaa False kun sille annetaan parametrina merkkijono joka ei ole palindromi."""
        not_palindromes = (
            "ab",
            "abb",
            "ba",
            "bba",
            "abcbba",
        )
        for np in not_palindromes:
            self.assertFalse(
                palindromi(np),
                "{!r} ei ole palindromi mutta funktiosi palautti True."
                .format(np))

    def test_correct_output(self):
        """Funktio palindromi tulostaa parametrinsa oikein kahdelle riville."""
        params_and_output = (
            ("a", "a", "a"),
            ("A", "a", "a"),
            ("  A  ", "a", "a"),
            ("ab", "ab", "ba"),
            ("abba", "abba", "abba"),
            ("ab Ba", "abba", "abba"),
            ("abcd", "abcd", "dcba"),
            ("Innostunut sonni", "innostunutsonni", "innostunutsonni"),
        )
        for parameter, line1, line2 in params_and_output:
            with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_out:
                palindromi(parameter)
                out_value = mock_out.getvalue()
                lines = out_value.splitlines()
                self.assertEqual(
                    len(lines),
                    2,
                    "Funktiosi pitäisi tulostaa 2 riviä, mutta se tulosti {} riviä:\n{}"
                    .format(len(lines), out_value))
                self.assertEqual(
                    lines[0],
                    line1,
                    "Funktiosi pitäisi tulostaa ensimmäiselle riville {}, mutta se tulosti {}."
                    .format(line1, lines[0]))
                self.assertEqual(
                    lines[1],
                    line2,
                    "Funktiosi pitäisi tulostaa toiselle riville {}, mutta se tulosti {}."
                    .format(line2, lines[1]))



if __name__ in ("__main__", "tests"):
    from sys import version_info
    if version_info.major < 3:
        raise Exception("Testit yritettiin ajaa Python-tulkilla {:d}.{:d}, ole hyvä ja vaihda tilalle versio 3.".format(version_info.major, version_info.minor))
    else:
        unittest.main(verbosity=2)

