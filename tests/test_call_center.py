from unittest.case import TestCase
from oop.call_center import *


class TestCallHandler(TestCase):
    def test_dispatch_call(self):
        handler = CallHandler()
        call = Call(0)
        handler.dispatch_call(call)
        self.assertEqual(handler.operators[0].current_call, call)
        call = Call(2)
        handler.dispatch_call(call)
        self.assertEqual(handler.directors[0].current_call, call)
        call = Call(1)
        handler.dispatch_call(call)
        self.assertEqual(handler.managers[0].current_call, call)
        for i in range(5):
            handler.dispatch_call(Call(0))
        self.assertRaises(BusyError, handler.dispatch_call, Call(0))