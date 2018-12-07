
import unittest
from selenium_basics.test_class1 import TestClass1
from selenium_basics.test_class2 import TestClass2
from selenium_basics.switch_to_window import SwitchWindow

# get all tests from test_class1 and test_class2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(SwitchWindow)

# create a test suite combining TestClass1 and TestClass2
smoke_test = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smoke_test)

