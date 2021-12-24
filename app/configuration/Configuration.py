from configparser import ConfigParser

path_to_configuration_file = "config.ini"


class Configuration:
    api_key = ""
    api_secret = ""
    subaccount_name = ""
    bot_base_url = ""

    def __init__(self):
        config_init = ConfigParser()
        config_init.read(path_to_configuration_file)
        config = config_init["DEFAULT"]
        self.api_key = config["api_key"]
        self.api_secret = config["api_secret"]
        self.subaccount_name = config["subaccount_name"]
        self.bot_base_url = config["bot_base_url"]
