from unittest.case import TestCase
from oop.music_centre import *

__author__ = 'Dmitry Mekhantev'


class TestMusicCentre(TestCase):
    def test_play(self):
        mc = MusicCentre()
        cd = Cd('Judas Priest', (
            'Painkiller',
            'All Guns Blazing',
            'One Shot at Glory'
        ))
        flash = Flash('Black Sabbath', (
            'Neon Knights',
            'Heaven and Hell',
            'Die Young'
        ))
        artist = mc.play(cd)
        self.assertEqual(cd.artist, artist)
        self.assertEqual(type(mc._current_player), CdPlayer)
        artist = mc.play(flash)
        self.assertEqual(flash.artist, artist)
        self.assertEqual(type(mc._current_player), FlashPlayer)
