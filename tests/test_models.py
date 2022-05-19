import unittest
from app.models import User, Post


class UserModelTest(unittest.TestCase):
    """this class sets upt the test suite for the application models"""

    def setUp(self):
        """Set up value that executes before each test suite runs"""
        self.new_user = User(
            username='billy', email='billy@code.dev', bio='writing some bugs')

    def test_set_password(self):
        """test the password setter"""
        self.new_user.set_password('password')
        self.assertTrue(self.new_user.password_hash is not None)

    def test_check_password(self):
        """test the password hashing"""
        self.new_user.set_password('password')
        self.assertTrue(self.new_user.check_password('password'))
        self.assertFalse(self.new_user.check_password('wrong_password'))


class TestPostModel(unittest.TestCase):
    """this class sets up the test suite for the application models"""

    def setUp(self):
        """Set up value that executes before each test suite runs"""
        self.new_post = Post(title='unittest', body='Unit testing is kinda sweet!')

    def test_instance(self):
        """test if the object is an instance of the class"""
        self.assertTrue(isinstance(self.new_post, Post))

    def test_check_instance(self):
        """test if the object is an instance of the class"""
        self.assertTrue(self.new_post.title == 'unittest')
        self.assertTrue(self.new_post.body == 'Unit testing is kinda sweet!')


if __name__ == '__main__':
    unittest.main()
