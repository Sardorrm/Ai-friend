import unittest

from ai_friend import generate_response


class AiFriendTests(unittest.TestCase):
    def test_greeting(self):
        self.assertIn("hello", generate_response("hello").lower())

    def test_mood_support(self):
        response = generate_response("I am sad")
        self.assertTrue(any(keyword in response.lower() for keyword in ["sorry", "feeling", "okay", "strong"]))

    def test_default_response(self):
        response = generate_response("tell me a joke")
        self.assertTrue(len(response) > 0)


if __name__ == "__main__":
    unittest.main()
