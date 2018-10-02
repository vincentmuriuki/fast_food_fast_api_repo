# import os
# import unittest

# from flask import current_app
# from app.api.v2 import create_app
# from app.api.v2.database.tables import drop_tables, fastfood_tables

# # local imports
# from .base_test import BaseTests

# class BasicsTestCase(BaseTests):
#     def setUp(self):
#         self.app = create_app('testing')
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         with self.app_context:
#             fastfood_tables()

#     def tearDown(self):
#         drop_tables()
#         self.app_context.pop()

#     def test_app_exists(self):
#         self.assertFalse(current_app is None)

#     def test_app_is_testing(self):
#         self.assertTrue(create_app('testing'))


# if __name__ == '__main__':
#     unittest.main()