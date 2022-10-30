import logging


class LogGen:




    @staticmethod
    def log_gen():

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("D:\\Python_Selenium\\nopCommerceApp\\Logs\\automation.log")
        formatter = logging.Formatter("'%(asctime)s - %(levelname)s : %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

# LogGen.log_gen().error("error")
