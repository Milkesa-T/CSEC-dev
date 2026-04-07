import unittest
import sys
import os

# Add src to the path so we can import stat_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    
    def test_mean(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertEqual(engine.get_mean(), 3.0)
        
    def test_median_odd(self):
        engine = StatEngine([1, 3, 5])
        self.assertEqual(engine.get_median(), 3.0)
        
    def test_median_even(self):
        engine = StatEngine([1, 2, 4, 10])
        self.assertEqual(engine.get_median(), 3.0)
        
    def test_mode_multimodal(self):
        engine = StatEngine([1, 1, 2, 2, 3])
        self.assertEqual(engine.get_mode(), [1.0, 2.0])
        
    def test_mode_all_unique(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_mode(), "All values are unique; no mode found.")
        
    def test_variance_sample(self):
        # Sample variance for [1, 2, 3] is 1.0 (mean=2, diffsq=[1, 0, 1], sum=2, divisor=2)
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_variance(is_sample=True), 1.0)
        
    def test_variance_population(self):
        # Population variance for [1, 2, 3] is (1+0+1)/3 = 2/3
        engine = StatEngine([1, 2, 3])
        self.assertAlmostEqual(engine.get_variance(is_sample=False), 2/3)
        
    def test_standard_deviation(self):
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_standard_deviation(is_sample=True), 1.0)
        
    def test_outliers(self):
        # Data: [1, 1, 1, 1, 1, 100]
        # Mean = 106 / 6 = 17.66
        # Variance (sample) = (sum((x-17.66)**2))/5
        # (5*(16.66**2) + (82.33**2)) / 5 = (1387.77 + 6778.22) / 5 = 1633.19
        # StdDev = approx 40.41
        # Outlier at 2 threshold would be points > 17.66 + 80.82 (98.48) or < 17.66 - 80.82
        # So 100 should be an outlier.
        engine = StatEngine([1, 1, 1, 1, 1, 100])
        outliers = engine.get_outliers(threshold=2)
        self.assertEqual(outliers, [100.0])

    def test_empty_list_error(self):
        engine = StatEngine([])
        with self.assertRaises(ZeroDivisionError):
            engine.get_mean()
            
    def test_mixed_types_cleaning(self):
        # Should clean [1, '2', 3.0, None, '4.5'] into [1.0, 2.0, 3.0, 4.5]
        engine = StatEngine([1, '2', 3.0, None, '4.5'])
        self.assertEqual(engine.data, [1.0, 2.0, 3.0, 4.5])
        
    def test_bad_types_exception(self):
        with self.assertRaisesRegex(TypeError, "Invalid data type"):
            StatEngine([1, 2, "abc"])

if __name__ == '__main__':
    unittest.main()
