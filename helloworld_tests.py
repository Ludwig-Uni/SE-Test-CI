#! /bin/python3
import unittest
import helloworld


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertTrue(helloworld.hello_world().startswith("Hello, world!"))
