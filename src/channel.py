import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv('.env')
class Channel:
    """Класс для ютуб-канала"""
    # api_key = 'AIzaSyD18XmtcKqilmDbM-tOqvnGAUhH8SEiFXs'
    api_key: str = os.getenv('SECRET_KEY')
    print(api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)


