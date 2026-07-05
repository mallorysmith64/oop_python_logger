class Logger:
    def __init__(self, name):
        self.name = name
        self.history = []

    def log(self, level, message):
        print(f"Log Message: {level} - {message}")
        self.history.append(message)
        print(f"History: {self.history}")
        
    def debug(self,level):
        print(f"Debug: {level}")
        
    def info(self, level):
        print(f"Info: {level}")
        
    def warning(self, level):
        print(f"Warning: {level}")
        
    def error(self, level):
        print(f"Error: {level}")
        
    def critical(self, level):
        print(f"Critical: {level}")
        
    def format(self, name, level, message):
        return f"{name} - {level} - {message}"
    
    def show_history(self):
        for entry in self.history:
            print(f"{entry}")
        
logging = Logger("SimpleLogger")
log_message = logging.log("Warning", "Error: Something went wrong!")
debug_logging = logging.debug("Debug")
info_logging = logging.info("Info")
warn_logging = logging.warning("Warning")
error_logging = logging.error("Error")
critical_logging = logging.critical("Critical")
formatted_message = logging.format("SimpleLogger", "INFO", "Formatted log message")

logging.show_history()
