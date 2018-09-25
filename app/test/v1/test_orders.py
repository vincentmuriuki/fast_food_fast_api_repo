import unittest
import json
import sys
sys.path.append("../")
# Local imports
# from api.v1 import *
from app.api.v1 import create_app

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()


    def test_create_order(self):
        order_data = {
            "name": "Chicken",
            "price": 1200,
            "description": "Fried"
        }

        response = self.client.post("/api/v1/orders",
            data=json.dumps(order_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], "Congratulations. Your new order has been posted. Kindly wait!")


        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)["message"], "Congratulations. Your new order has been posted. Kindly wait!")

#     def test_get_all_orders(self):

#         res = self.client.get(
#             "/api/v1/orders",
#             headers={"content-type": "application/json"}
#         )


#         self.assertEqual(res.status_code, 200)

#     def test_order_by_id(self):
#         res = self.client.get(
#             "/api/v1/orders/1",
#             headers={"content-type": "application/json"}
#         )
#         self.assertEqual(res.status_code, 200)

    
#     def test_update_order_status(self):
#         res = self.client.put(
#             "api/v1/orders/1",
#             headers={"content-type": "application/json"}
#         )
#         print(res.data)
#         self.assertEqual(res.status_code, 200)

#         self.assertEqual(json.loads(res.data)['message'], "status approved")



#     def test_non_order_by_id(self):
#         res = self.client.get(
#             "/api/v1/orders/111",
#             headers={"content-type": "application/json"}
#         )
#         self.assertEqual(res.status_code, 404)
#         self.assertEqual(json.loads(res.data)[
#                          'message'], "Order not found")


#     def test_invalid_order_delete(self):
#         # res = json.loads(res.data.decode('utf-8'))
#         res = self.client.delete(
#                 "api/v1/orders/101",
#                 headers={"content-type": "application/json"}
#                 )
#         # res = json.loads(res.decode('utf-8'))
#         self.assertEqual(res.status_code, 404)
#         self.assertEqual(json.loads(res.data)['message'],"Requested Order not found! Try a different ID!")

