# -*- coding: utf-8 -*-
"""
    tests/__init__.py

"""
import unittest

import trytond.tests.test_tryton

from tests.test_views_depends import TestViewsDepends
from tests.test_product import TestProduct
from tests.test_pagination import TestPagination


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestViewsDepends),
        unittest.TestLoader().loadTestsFromTestCase(TestProduct),
        unittest.TestLoader().loadTestsFromTestCase(TestPagination),
    ])
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
