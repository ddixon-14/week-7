import unittest
from unittest.mock import Mock
import pandas as pd
from loader import *
class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        #creates a fake location object
        fake_location = Mock()
        fake_location.latitude = 40.7618552
        fake_location.longitude = -73.9782438
        fake_location.geo_type = "Museum"

        #fake geolocator
        fake_geo = Mock()
        fake_geo.geocode.return_value = fake_location

        #function call 
        result = fetch_location_data(fake_geo, "MoMa")

        self.assertEqual(result["location"], "MoMa")
        self.assertEqual(result["latitude"], 40.7618552)
        self.assertEqual(result["longitude"], -73.9782438)
        self.assertEqual(result["type"], "Museum")

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertIsNone(result, 
                          "A nonexistent location should have an empty result.")

if __name__ == "__main__":
    unittest.main()
