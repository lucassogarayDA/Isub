"""Unit tests for scanner output handling."""

import unittest

from isub.scanner import sanitize_banner


class BannerSanitizationTests(unittest.TestCase):
    def test_removes_control_characters(self):
        sample = "OpenSSH" + chr(27) + "[31m" + chr(10) + "8.9"
        self.assertEqual(sanitize_banner(sample), "OpenSSH[31m8.9")

    def test_limits_banner_length(self):
        self.assertEqual(sanitize_banner("x" * 100, limit=12), "x" * 12)

    def test_keeps_normal_unicode_text(self):
        self.assertEqual(sanitize_banner("Servicio café"), "Servicio café")


if __name__ == "__main__":
    unittest.main()
