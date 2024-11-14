from UTest.test_weather import TestWeatherFunctions
import unittest

def run_weather_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__('UTest.test_weather'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    unittest.main()