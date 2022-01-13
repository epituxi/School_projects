# -*- coding: utf-8 -*-
# Nimi: Viljami Riihimäki
# Opiskelijanumero: 910048

import unittest
import unittest.mock as mock
import io
import random

from passwords import xkcd_passwords


PASSWORD_FILENAME = "words.txt"
MOCK_FILE_ROWS = {
    "one",
    "two",
    "three",
    "four",
}
MOCK_FILE_CONTENTS = "\n".join(MOCK_FILE_ROWS)
EXPECTED_PASSWORD_COUNT = 20
EXPECTED_WORD_COUNT = 4


#​​‌‌‌‌‌‌​​‌‌​​‌ Nopeutetaan testejä korvaamalla testien ajaksi passwords-moduulin open-funktio
#​​‌‌‌‌‌‌​​‌‌​​‌ "mockilla", joka lukee tekstiä kuvitteellisesta tiedostosta,
#​​‌‌‌‌‌‌​​‌‌​​‌ joka sisältää vain 4 riviä.
@mock.patch("passwords.open", mock.mock_open(read_data=MOCK_FILE_CONTENTS))
class TestPasswords(unittest.TestCase):

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_file_is_opened(self, mock_stdout):
        """Funktion xkcd_passwords tulostamat salasanat on luettu tiedostosta nimeltä 'words.txt'."""
        xkcd_passwords()
        for line in mock_stdout.getvalue().splitlines():
            for word in line.split(" "):
                self.assertIn(
                    word,
                    MOCK_FILE_ROWS,
                    "Funktiosi tulostama rivi:\n'{}'\nsisältää sanan '{}',\njoka ei ollut tiedostossa '{}' kun sen sisältö oli:\n{}"
                    .format(line, word, PASSWORD_FILENAME, MOCK_FILE_CONTENTS))

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_correct_password_count(self, mock_stdout):
        xkcd_passwords()
        printed_lines = mock_stdout.getvalue().splitlines()
        self.assertEqual(
            len(printed_lines),
            EXPECTED_PASSWORD_COUNT,
            "Funktiosi tulosti yhteensä {} salasanaa, vaikka funktiosi tulisi tulostaa täsmälleen {} salasanaa."
            .format(len(printed_lines), EXPECTED_PASSWORD_COUNT))

    test_correct_password_count.__doc__ = (
        """Funktio xkcd_passwords tulostaa täsmälleen {} riviä."""
        .format(EXPECTED_PASSWORD_COUNT))

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_correct_password_length(self, mock_stdout):
        xkcd_passwords()
        for line_i, line in enumerate(mock_stdout.getvalue().splitlines(), start=1):
            words = line.split(" ")
            self.assertEqual(
                len(words),
                EXPECTED_WORD_COUNT,
                "Funktiosi tulosti {}. riville salasanan joka koostuu {} sanasta:\n\n'{}'.\n\nFunktiosi tulostamat salasanat tulee koostua täsmälleen {} sanasta."
                .format(line_i, len(words), line, EXPECTED_WORD_COUNT))

    test_correct_password_length.__doc__ = (
            """Kaikilla funktion xkcd_passwords tulostamilla riveillä on tasan {} sanaa."""
            .format(EXPECTED_WORD_COUNT))

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_random_module_is_used(self, mock_stdout):
        """Funktio xkcd_passwords käyttää random-moduulia."""
        state_a = random.getstate()
        xkcd_passwords()
        state_b = random.getstate()
        if state_a == state_b:
            self.fail("Funktion xkcd_passwords tulisi käyttää random-moduulin jotain toiminnallisuutta satunnaisuuden aikaansaamiseksi.")


if __name__ in ("__main__", "tests"):
    from sys import version_info
    if version_info.major < 3:
        raise Exception("Testit yritettiin ajaa Python-tulkilla {:d}.{:d}, ole hyvä ja vaihda tilalle versio 3.".format(version_info.major, version_info.minor))
    else:
        unittest.main(verbosity=2)

