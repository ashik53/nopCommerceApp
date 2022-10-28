import configparser

config = configparser.ConfigParser()
config.read('D:/Python_Selenium/nopCommerceApp/Configurations/config.ini')

class ReadConfig():
    @staticmethod
    def get_application_url():
        url = config.get("common info", 'baseURL')
        #print(url)
        return url

    @staticmethod
    def get_application_username():
        userName = config.get('common info', 'userName')
        return userName

    @staticmethod
    def get_application_password():
        password = config.get('common info', 'password')
        return password

