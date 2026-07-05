class Logger:
    def __init__(self, name):
        self.name = name
        self.history = []

    def log(self, level, message):
        logged_entry = f"{self.name} - {level} - {message}"
        self.history.append(logged_entry)
        
    def debug(self,message):
        self.log("Debug", message)
        
    def info(self, message):
        self.log("Info", message)
        
    def warning(self, message):
        self.log("Warning", message)
        
    def error(self, message):
        self.log("Error", message)
        
    def critical(self, message):
        self.log("Critical", message)
    
    def show_history(self):
        for entry in self.history:
            print(f"{entry}")
        
logging = Logger("SimpleLogger")

debug_logging = logging.debug("Debug message")
info_logging = logging.info("Information message")
warn_logging = logging.warning("Something went wrong!")
error_logging = logging.error("An error occurred")
critical_logging = logging.critical("A critical message occurred")

logging.show_history()
