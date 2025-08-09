from kalkulacka import Kalkulacka
from unittest import TestCase


class TestKalkulacka(TestCase):
    kalkulacka = Kalkulacka()

    def test_scitaj(self):
        self.assertEqual(5, self.kalkulacka.scitaj(2, 3))
        self.assertEqual(100, self.kalkulacka.scitaj(-100, 200))

 #   def test_odcitaj(self):
 #       self.fail()

    def test_vydel(self):
        self.assertEqual(40, self.kalkulacka.vydel(80, 2))
        self.assertEqual(40, self.kalkulacka.vydel(120, 3))

    def test_vynasob(self):
        self.assertEqual(15, self.kalkulacka.vynasob(5, 3))
        self.assertEqual(42, self.kalkulacka.vynasob(6, 7))