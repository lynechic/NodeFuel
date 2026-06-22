# test_nodefuel.py
"""
Tests for NodeFuel module.
"""

import unittest
from nodefuel import NodeFuel

class TestNodeFuel(unittest.TestCase):
    """Test cases for NodeFuel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeFuel()
        self.assertIsInstance(instance, NodeFuel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeFuel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
