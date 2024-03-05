from configparser import RawConfigParser

config_obj = RawConfigParser()
config_obj.read(r".\Configuration\config.ini")

class ReadProperty:
    @staticmethod
    def GetUser():
        return config_obj.get("common data", "user")

    @staticmethod
    def GetPassword():
        return config_obj.get("common data", "password")

    @staticmethod
    def GetBaseURL():
        return config_obj.get("common data", "url")