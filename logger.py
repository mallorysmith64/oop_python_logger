import csv
class Logger:
    def __init__(self, name, filename="log.csv"):
        self.name = name
        self.filename = filename
        self.history = []

    def log(self, level, message):
        formatted_entry = f"{self.name} - {level} - {message}"
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
            writer.writerow(["logger", "level", "message"])
            writer.writerows(self.history)
   
    def entry_count(self):
        count = 0
        for _ in self.history:
            count += 1
        print(f"Total log entries: {count}")
        return count

logging = Logger("SimpleLogger")

debug_logging = logging.debug("Debug message")
info_logging = logging.info("Information message")
warn_logging = logging.warning("Something went wrong!")
error_logging = logging.error("An error occurred")
critical_logging = logging.critical("A critical message occurred")

logging.show_history()
writer_logging = logging.to_csv()
entry_count_logging = logging.entry_count()
