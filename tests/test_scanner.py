"""Unit tests for scanner output handling."""

import unittest

from isub.scanner import sanitize_banner


class BannerSanitizationTests(unittest.TestCase):
    def test_removes_control_characters(self):
        self.assertEqual(sanitize_banner("OpenSSH\\x1b[31m\\n8.9"), "OpenSSH[31m8.9")

    def test_limits_banner_length(self):
        self.assertEqual(sanitize_banner("x" * 100, limit=12), "x" * 12)

    def test_keeps_normal_unicode_text(self):
        self.assertEqual(sanitize_banner("Servicio café"), "Servicio café")


if __name__ == "__main__":
    unittest.main()
