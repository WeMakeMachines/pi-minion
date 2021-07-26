import datetime
import hashlib
import json
import os


class FileCacheError(Exception):
    pass


class FileCache:
    @staticmethod
    def hash_path(string: str):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()

    @staticmethod
    def check_path_exists(path: str):
        return os.path.isfile(path)

    @staticmethod
    def create_cache_dir(path: str):
        try:
            os.makedirs(path, exist_ok=True)
        except FileCacheError as error:
            raise FileCacheError(f"Directory {path} can not be created, {error}")

    def __init__(self, path: str):
        self.cache_dir = f"cache/{FileCache.hash_path(path)}"

        if not FileCache.check_path_exists(self.cache_dir):
            FileCache.create_cache_dir(self.cache_dir)

    def __get_cache_path(self):
        return f"{self.cache_dir}/data.json"

    def read(self):
        cache_exists = FileCache.check_path_exists(self.__get_cache_path())
        if not cache_exists:
            return None

        cache = None

        try:
            with open(self.__get_cache_path(), "r") as openfile:
                try:
                    cache = openfile
                except OSError as error:
                    raise OSError(f"Unable to open file, {error}")
                try:
                    return json.load(cache)
                except Exception as error:
                    raise Exception(f"Unable to read JSON cache, {error}")

        except FileCacheError as error:
            raise FileCacheError(f"Error reaching cache, {error}")

    def write(self, data):
        timestamp = datetime.datetime.now().timestamp()

        with open(self.__get_cache_path(), "w") as outfile:
            json.dump({
                "cache_timestamp": timestamp,
                "cache": data
            }, outfile)
