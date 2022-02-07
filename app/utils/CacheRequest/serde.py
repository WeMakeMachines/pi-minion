import datetime
import json


class JsonCacheSerializeDeserialize(object):
    def serialize(self, key, data):
        if isinstance(data, str):
            return data.encode("utf-8"), 1

        timestamp = datetime.datetime.now().timestamp()
        cache = {"cache_timestamp": timestamp, "cache": data}

        return json.dumps(cache).encode("utf-8"), 2

    def deserialize(self, key, value, flags):
        if flags == 1:
            return value.decode("utf-8")
        if flags == 2:
            return json.loads(value.decode("utf-8"))
        raise Exception("Unknown serialization format")
