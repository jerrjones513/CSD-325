import unittest 
from city_functions import country_info

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = country_info("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()