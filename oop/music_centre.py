from abc import ABCMeta
from collections.abc import Iterable


class Storage(metaclass=ABCMeta):
    def __init__(self, artist: str, songs: Iterable):
        self.artist = artist
        self.songs = []
        self.songs.extend(songs)


class Cd(Storage):
    pass


class Flash(Storage):
    pass


class Player(metaclass=ABCMeta):
    def __init__(self):
        self._can_play_type = None
        self.current_storage = None
        self.is_playing = False

    def can_play(self, storage: Storage):
        return True if isinstance(storage, self._can_play_type) else False

    def play(self) -> str:
        self.is_playing = True
        return self.current_storage.artist

    def stop(self):
        self.is_playing = False


class FlashPlayer(Player):
    def __init__(self):
        super().__init__()
        self._can_play_type = Flash


class CdPlayer(Player):
    def __init__(self):
        super().__init__()
        self._can_play_type = Cd


class MusicCentre():
    def __init__(self):
        self._current_player = None
        self._players = [CdPlayer(), FlashPlayer()]

    def play(self, storage=None) -> str:
        self.stop()
        if storage:
            for player in self._players:
                if player.can_play(storage):
                    player.current_storage = storage
                    self._current_player = player
        return self._current_player.play()

    def stop(self):
        if self._current_player:
            self._current_player.stop()
