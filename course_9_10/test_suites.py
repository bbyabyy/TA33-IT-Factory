import unittest
import HtmlTestRunner


from Cursuri import Alerts
from Cursuri import Context_Menu
from Cursuri import Authentication_in_Firefox
from Cursuri import Keyboard

# de instalat python packages html-test-Runner, html-testRunner1005D


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Context_Menu),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
                               unittest.defaultTestLoader.loadTestsFromTestCase(Authentication_in_Firefox)])


        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True, # vrem sa ne genereze un singur raport pentru toate clasele
            report_title="Test Execution Report",
            report_name="Test Results"
        )

        runner.run(tests_to_run)