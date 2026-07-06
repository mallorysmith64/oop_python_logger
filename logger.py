import csv
from datetime import datetime
class Logger:
    def __init__(self, name, filename="log.csv"):
        self.name = name
        self.filename = filename
        self.history = []
        
    def getDateTime(self):
        timestamp = datetime.now().replace(microsecond=0).isoformat()
        return timestamp

    def log(self, level, message):
        timestamp = self.getDateTime()
        formatted_entry = f"{self.name} - {level} - {message} - {timestamp}"
        self.history.append([formatted_entry])
        
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
    
    #using generator to show history of log entries to avoid loading all entries into memory at once
    def show_history(self):
        for entry in self.history:
            yield entry
            
    def to_csv(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["logger", "level", "message", "timestamp"])
            writer.writerows(self.history)
   
    def entry_count(self):
        count = 0
        for _ in self.history:
            count += 1
        return f"Total log entries: {count}"

logging = Logger("SimpleLogger")

name = logging.name
filename = logging.filename

logging.debug("Debug message")
logging.info("Information message")
logging.warning("Something went wrong!")
logging.error("An error occurred")
logging.critical("A critical message occurred")

logging.show_history()
logging.to_csv()
print(logging.entry_count())
