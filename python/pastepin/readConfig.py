import configparser

def readConfig(filename,part):
    config = configparser.ConfigParser()
    config.read(filenames=filename)
    return config[part]
