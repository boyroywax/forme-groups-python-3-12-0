import unittest

from tests_interface_base import TestBaseInterface


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestBaseInterface))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
