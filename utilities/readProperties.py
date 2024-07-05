import configparser
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationBaseUrl():
        BaseURL = config.get('common info','baseURL')
        return BaseURL

    @staticmethod
    def getUserName():
        userName = config.get('common info', 'username')
        return userName

    @staticmethod
    def getPassword():
        Password = config.get('common info', 'password')
        return Password
