from configparser import ConfigParser




def readConfig(section,key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\Config.ini")
    return config.get(section,key)

# print(readConfig("basic info","Basi_url"))