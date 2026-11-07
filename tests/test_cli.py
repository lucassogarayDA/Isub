"""Unit tests for CLI argument parsing."""

import unittest

from isub.cli import parse_ports


class ParsePortsTests(unittest.TestCase):
    def test_parses_single_ports_and_ranges(self):
        self.assertEqual(parse_ports("22,80,443"), [22, 80, 443])
        self.assertEqual(parse_ports("80,1-3,3"), [1, 2, 3, 80])

    def test_trims_whitespace(self):
        self.assertEqual(parse_ports(" 22, 80 - 81 "), [22, 80, 81])

    def test_rejects_empty_specification(self):
        for value in ("", "   ", ",", "22,,80"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_ports(value)

    def test_rejects_malformed_ranges(self):
        for value in ("1-", "-10", "1-2-3", "10-1", "abc"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_ports(value)

    def test_accepts_tcp_port_boundaries(self):
        self.assertEqual(parse_ports("1,65535"), [1, 65535])

    def test_rejects_ports_outside_tcp_range(self):
        for value in ("0", "65536", "1-65536"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_ports(value)


if __name__ == "__main__":
    unittest.main()
