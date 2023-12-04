import unittest
import self

from userAuthentication.registrationAndLogin import UserManager, openRegistrationWindow, displayLogin


class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.authManager = UserManager()

    def tearDown(self):
        del self.authManager

    def testRegisterUser(self):
        # Test successful registration
        result = self.authManager.registerCheck("testUser", "testPassword", "testUser@gmail.com", "student") # make email and usernamd rnadom
        self.assertTrue(result)

        # Test registration with duplicate email
        resultExistingEmail = self.authManager.registerCheck("anotherUser", "testPassword", "testUser@gmail.com", "student")
        self.assertFalse(resultExistingEmail)

    def testLogin(self):
        # Test successful login
        self.authManager.registerCheck("testUser2", "testPassword", "testUser2@gmail.com", "student")
        userType, success = self.authManager.authenticateUser("testUser2", "testPassword")
        self.assertTrue(success)
        self.assertEqual(userType, "student")

        # Test unsuccessful login
        userTypeFail, fail = self.authManager.authenticateUser("nonExistentUser", "testPassword")
        self.assertFalse(fail)
        self.assertIsNone(userTypeFail)

if __name__ == "__main__":
    unittest.main()
