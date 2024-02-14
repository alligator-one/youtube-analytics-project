import json
import os
from googleapiclient.discovery import build


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:
    """Класс для ютуб-канала"""
    api_key = 'AIzaSyD18XmtcKqilmDbM-tOqvnGAUhH8SEiFXs'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        pass

    def print_info(self, channel_id)  -> None:
        """Выводит в консоль информацию о канале."""

        self.channel_id = channel_id
        api_key = 'AIzaSyD18XmtcKqilmDbM-tOqvnGAUhH8SEiFXs'
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = 'UCwHL6WHUarjGfUM_586me8w'
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        # pass

        printj(self.channel)