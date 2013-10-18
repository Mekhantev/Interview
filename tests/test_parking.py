from unittest.case import TestCase
from oop.parking import *

__author__ = 'Dmitry Mekhantev'


class TestParking(TestCase):
    def test_add(self):
        parking = Parking()
        vehicle = Car()
        parking.add(vehicle)
        self.assertEqual(vehicle, parking._parking_spots[2].vehicles[0])
        vehicle = Motorcycle()
        parking.add(vehicle)
        self.assertEqual(vehicle, parking._parking_spots[0].vehicles[0])
        for _ in range(2):
            parking.add(Car())
        self.assertRaises(Exception, parking.add, Car())

    def test_remove(self):
        parking = Parking()
        vehicle = Car()
        parking.add(vehicle)
        parking.remove(vehicle)
        self.assertEqual(0, len(parking._parking_spots[2].vehicles))
        vehicle = Motorcycle()
        parking.add(vehicle)
        parking.remove(vehicle)
        self.assertEqual(0, len(parking._parking_spots[0].vehicles))
        for _ in range(4):
            vehicle = Motorcycle()
            parking.add(vehicle)
        self.assertEqual(0, parking._parking_spots[2].empty_space)
        parking.remove(vehicle)
        self.assertEqual(1, parking._parking_spots[2].empty_space)