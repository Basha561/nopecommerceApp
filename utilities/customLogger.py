import logging
class LogGenerator:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(".\\Logs\\automation.log")
        formatter = logging.Formatter('%(asctime)s : %(levelname)s :%(message)s',datefmt='%m/%d/%Y %I : %M : %S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger