#! /bin/python3
import unittest
import helloworld

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(helloworld.hello_world(), "Hello, world!")
