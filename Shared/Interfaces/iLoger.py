# Interfaces/ILogger.py
# strategy  patern beha

from abc import ABC, abstractmethod

class ILogger(ABC):
    @abstractmethod
    def log_query(self, query, result):
        pass

# Concrete implementations
class FileLogger(ILogger):
    def log_query(self, query, result):
        with open("log.txt", "a") as file:
            file.write(f"Query: {query}, Result: {result}\n")

class ConsoleLogger(ILogger):
    def log_query(self, query, result):
        print(f"Query: {query}, Result: {result}")

# Usage with dependency injection
class QueryProcessor:
    def __init__(self, logger: ILogger):
        self.logger = logger

    def process_query(self, query):
        # Process the query and get the result (dummy result here for example)
        result = f"Result for {query}"
        self.logger.log_query(query, result)
        return result

# Injecting different logging strategies
# file_logger = FileLogger()
# console_logger = ConsoleLogger()
#
# processor1 = QueryProcessor(file_logger)
# processor1.process_query("SELECT * FROM table")
#
# processor2 = QueryProcessor(console_logger)
# processor2.process_query("SELECT * FROM table")
