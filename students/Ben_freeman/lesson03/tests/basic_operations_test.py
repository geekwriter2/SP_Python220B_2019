# pylint: disable=unused-import, unused-wildcard-import,
# pylint: disable=too-few-public-methods, too-many-arguments, wildcard-import
# pylint: disable=logging-format-interpolation, pointless-string-statement
import sys
import unittest
sys.path.append("../src/")
import basic_operations as b_o
import customers


class TestFunctions(unittest.TestCase):

    def test_add_customer(self):
        b_o.add_customer("Test_id",
                         "Test_name",
                         "Test_last_name",
                         "Test_home_address",
                         1234567890,
                         "Test_email_address",
                         True,
                         9001)
        self.assertEqual(customers.Customer.get(customers.Customer.customer_id == "Test_id").name, "Test_name")

    def test_search_customer(self):
        test = b_o.search_customer("Test_id")
        self.assertEqual(test, {"Name":"Test_name",
                                "Last Name": "Test_last_name",
                                "Email Address": "Test_email_address",
                                "Phone number": 1234567890})

    def test_update_customer_credit(self):
        b_o.update_customer_credit("Test_id", 9002)
        self.assertEqual(customers.Customer.get(customers.Customer.customer_id == "Test_id").credit_limit, 9002)

    def test_list_active_customers(self):
        number = b_o.list_active_customers()
        self.assertEqual(number, 1)

    def test_zdelete_customer(self):
        b_o.delete_customer("Test_id")
        number = b_o.list_active_customers()
        self.assertEqual(number, 0)


class TestFailures(unittest.TestCase):

    def test_fail_add_customer(self):
        with self.assertRaises(TypeError):
            b_o.add_customer("Customer_id")

    def test_fail_search_customer(self):
        test_dict = b_o.search_customer("WillyWonka")
        self.assertEqual(test_dict, {})

    def test_fail_update_customer_credit(self):
        with self.assertRaises(ValueError):
            b_o.update_customer_credit("Santa", 123)

    def test_fail_delete_customer(self):
        with self.assertRaises(NameError):
            b_o.delete_customer("BrotherBear")



