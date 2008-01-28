import os
import sys

if not os.getcwd() in sys.path:
    sys.path.append(os.getcwd())

import UnitTests

from TestUtils.testutils import MakeSuite, RunTests

tests = MakeSuite(UnitTests)
RunTests(suite=tests, verbosity=2)
