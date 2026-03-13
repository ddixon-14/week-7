import unittest
from unittest.mock import Mock
import pandas as pd
from loader import *
class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        #creates a fake location object
        fake_location = Mock()
        fake_location.latitude = 40.4
        fake_location.longitude = 79.9
        fake_location.geo_type = "city"

        #fake geolocator
        fake_geo = Mock()
        fake_geo.geocode.return_value = fake_location

        #function call 
        result = fetch_location_data(fake_geo, "Indiana")

        self.assertEqual(result["location"], "Indiana")
        self.assertEqual(result["latitude"], 40.4)
        self.assertEqual(result["longitude"], 79.9)
        self.assertEqual(result["type"], "city")

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertIsNone(result, 
                          "A nonexistent location should have an empty result.")

if __name__ == "__main__":
    unittest.main()
