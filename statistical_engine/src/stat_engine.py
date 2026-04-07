import math
from typing import List, Tuple, Union, Any

class StatEngine:
    """
    A pure-Python statistical engine for processing 1D numerical data.
    """
    
    def __init__(self, data: List[Any]):
        """
        Initializes the StatEngine with a list of data points.
        Cleans data or raises descriptive TypeErrors for mixed/invalid types.
        """
        if not data:
            self.data = []
        else:
            self.data = self._clean_data(data)
        
        if not self.data:
            # Handle empty list case (after cleaning)
            self._is_empty = True
        else:
            self._is_empty = False

    def _clean_data(self, data: List[Any]) -> List[float]:
        """
        Filters out non-numeric values and ensures everything is a float.
        If a value cannot be converted, it raises a TypeError.
        """
        cleaned = []
        for i, val in enumerate(data):
            if val is None:
                continue # Skip None values like Slide 25
            try:
                numeric_val = float(val)
                cleaned.append(numeric_val)
            except (ValueError, TypeError):
                raise TypeError(f"Invalid data type at index {i}: '{val}' is not a number.")
        return cleaned

    def _check_empty(self):
        """
        Prevents ZeroDivisionError by checking if data is empty.
        """
        if self._is_empty:
            raise ZeroDivisionError("StatEngine cannot perform calculations on an empty dataset.")

    def get_mean(self) -> float:
        """
        Calculates the arithmetic mean.
        """
        self._check_empty()
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        """
        Calculates the median value. Logic handles even and odd constraints.
        """
        self._check_empty()
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 1:
            # Odd number of elements
            return sorted_data[mid]
        else:
            # Even number of elements: average of the two middle elements
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def get_mode(self) -> Union[List[float], str]:
        """
        Calculates the mode(s) of the dataset.
        Handles multimodal distributions and unique values.
        """
        self._check_empty()
        frequency = {}
        for x in self.data:
            frequency[x] = frequency.get(x, 0) + 1
        
        max_freq = max(frequency.values())
        
        # If max frequency is 1 and more than 1 value exists, all values are unique
        if max_freq == 1 and len(self.data) > 1:
            return "All values are unique; no mode found."
        
        modes = [k for k, v in frequency.items() if v == max_freq]
        return sorted(modes)

    def get_variance(self, is_sample: bool = True) -> float:
        """
        Calculates the variance.
        is_sample=True: Sample Variance (Bessel's correction n-1)
        is_sample=False: Population Variance (n)
        """
        self._check_empty()
        n = len(self.data)
        if is_sample and n <= 1:
            raise ZeroDivisionError("Sample variance requires at least 2 data points.")
        
        mean = self.get_mean()
        sum_sq_diff = sum((x - mean) ** 2 for x in self.data)
        
        divisor = (n - 1) if is_sample else n
        return sum_sq_diff / divisor

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        """
        Calculates the standard deviation (Square root of variance).
        """
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold: float = 2.0) -> List[float]:
        """
        Returns data points that are greater than `threshold` standard deviations away from the mean.
        Uses sample standard deviation by default.
        """
        self._check_empty()
        if len(self.data) <= 1:
            return [] # No outliers in a single point dataset
            
        mean = self.get_mean()
        std_dev = self.get_standard_deviation(is_sample=True)
        
        if std_dev == 0:
            return [] # Constant dataset has no outliers
            
        outliers = [x for x in self.data if abs(x - mean) > (threshold * std_dev)]
        return outliers
