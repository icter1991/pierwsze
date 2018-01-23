# #!/usr/bin/env python

import program
import unittest




class TestingMyFunctions(unittest.TestCase):

    emp = program.User('malved.com:44000/users', 'InTest1', '1111')

    def test_function_get_users(self):

        result = program.User.get_users(self.emp)
        self.assertTrue(result, list)

    def test_adding_new_user(self):

        result = program.User.post_users(self.emp)
        self.assertEqual(result, 200)

    def test_getting_user_id_as_number(self):

        result = program.User.get_user_id(self.emp)
        self.assertTrue(result, int)

    def test_modify_user(self):

        self.emp.password = '1234'

        result = program.User.put_user_id(self.emp)
        self.assertEqual(result, 200)

    def test_z_if_user_has_been_deleted(self):

        result = program.User.delete_user(self.emp)
        self.assertEqual(result, 200)






if __name__ == '__main__':
    unittest.main()
