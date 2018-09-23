import unittest

import facial_recog.tests.test_app

suite = unittest.TestLoader().loadTestsFromModule(facial_recog.tests.test_app)
unittest.TextTestRunner(verbosity=2).run(suite)
