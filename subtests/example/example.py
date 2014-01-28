"""
Call superclass during each stage
"""

from dockertest import subtest

# Use pylint from top-level test directory like this:
# pylint -rn --init-hook="sys.path.append('$PWD')" subtests/example/example.py

class example(subtest.Subtest):
    version = "1.2.3"  #  Used to track when setup() should run
    iterations = 3
    config_section = 'example'

    def setup(self):
        """
        Called once per version change
        """
        super(example, self).setup() # Prints out basic info
        # Do Something useful here

    def initialize(self):
        """
        Called every time the test is run.
        """
        super(example, self).initialize() # Prints out basic info
        # Do Something useful here

    def run_once(self):
        """
        Called to run test
        """
        super(example, self).run_once() # Prints out basic info
        # Do Something useful here

    def postprocess_iteration(self):
        """
        Called to process each iteration
        """
        super(example, self).postprocess_iteration() # Prints out basic info
        # Do Something useful here

    def postprocess(self):
        """
        Called to process all results
        """
        super(example, self).postprocess()  # Prints out basic info
        # Do Something useful here

    def cleanup(self):
        """
        Called after all other methods
        """
        super(example, self).cleanup() # Prints out basic info
        # Do Something useful here
