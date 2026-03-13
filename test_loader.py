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

        fake_location2 = Mock()
        fake_location2.latitude = 30.684373
        fake_location2.longitude = -88.015316
        fake_location2.geo_type = "Park"

        #fake geolocator
        fake_geo = Mock()
        fake_geo.geocode.side_effect = [fake_location, fake_location2]

        #function call 
        result = fetch_location_data(fake_geo, "MoMa")
        result2 = fetch_location_data(fake_geo, "USS Alabama Battleship Park")

        self.assertEqual(result["location"], "MoMa")
        self.assertEqual(result["latitude"], 40.7618552)
        self.assertEqual(result["longitude"], -73.9782438)
        self.assertEqual(result["type"], "Museum")

        self.assertEqual(result2["location"], "USS Alabama Battleship Park")
        self.assertEqual(result2["latitude"], 30.684373)
        self.assertEqual(result2["longitude"], -88.015316)
        self.assertEqual(result2["type"], "Park")

        

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertIsNone(result, 
                          "A nonexistent location should have an empty result.")

if __name__ == "__main__":
    unittest.main()
