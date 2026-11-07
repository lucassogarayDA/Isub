"""Unit tests for Isub's rotating logger."""

import logging
import os
import tempfile
import unittest

from isub.logger import setup_logger


class LoggerTests(unittest.TestCase):
    def test_reuses_handler_for_same_path(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "first.log")
            logger = setup_logger(path)
            handlers_before = list(logger.handlers)
            self.assertIs(setup_logger(path), logger)
            self.assertEqual(logger.handlers, handlers_before)
            logger.info("test entry")
            for handler in logger.handlers:
                handler.flush()
            with open(path, encoding="utf-8") as stream:
                self.assertIn("test entry", stream.read())

    def test_switches_to_a_new_path_without_duplicate_handlers(self):
        with tempfile.TemporaryDirectory() as directory:
            first = os.path.join(directory, "first.log")
            second = os.path.join(directory, "second.log")
            logger = setup_logger(first)
            setup_logger(second)
            file_handlers = [
                handler for handler in logger.handlers
                if hasattr(handler, "baseFilename")
            ]
            self.assertEqual(len(file_handlers), 1)
            self.assertEqual(file_handlers[0].baseFilename, second)
            logger.info("second entry")
            file_handlers[0].flush()
            with open(second, encoding="utf-8") as stream:
                self.assertIn("second entry", stream.read())


if __name__ == "__main__":
    unittest.main()
