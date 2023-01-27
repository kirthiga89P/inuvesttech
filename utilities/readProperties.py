import configparser
config1=configparser.RawConfigParser()
config1.read(r"C:\Users\kirthiga\OneDrive\Desktop\inuvesttech\Configuration\config.ini")
class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config1.get('common info','baseURL')
        return url