class Logger:
    def __init__(self, name):
        self.name = name
        self.history = []

    def log(self, message):
        self.message = message
        print(f"Log Message: {message}")
        self.history.append(message)
        print(f"History: {self.history}")

    def levels(self, level):
        self.level = level
        print(f"Warning Level: {level}")
        
    def info(self, level):
        self.level = level
        print(f"Info Level: {level}")
        
    def warning(self, level):
        self.level = level
        print(f"Warning Level: {level}")
        
    def error(self, level):
        self.level = level
        print(f"Error Level: {level}")
        
    def format(self, name, level, message):
        self.name = name
        self.level = level
        self.message = message
        print(f"{name} - {level} - {message}")
        
logging = Logger("SimpleLogger")
log_message = logging.log("Error: Something went wrong!")
level_logging = logging.levels("Warning")
info_logging = logging.info("Info")
warn_logging = logging.warning("Warning")
error_logging = logging.error("Error")
formatted_message = logging.format("SimpleLogger", "INFO", "Formatted log message")