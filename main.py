from api import app
from dal import init_db
from tests.test_basic_api import TestBasicAPI
import unittest

if __name__ == "__main__":
    init_db()  # Initialize the database on startup
    # app.run(debug=True)
    ts = unittest.defaultTestLoader.loadTestsFromTestCase(TestBasicAPI)
    unittest.TextTestRunner().run(ts)