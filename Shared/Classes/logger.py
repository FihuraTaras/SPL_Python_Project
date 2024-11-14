# Classes/Logger.py
class Logger:
    def __init__(self):
        self.query_history = []

    def log_query(self, query, result):
        self.query_history.append({"query": query, "result": result})

    def show_history(self):
        if not self.query_history:
            print("No queries have been logged yet.")
        else:
            print("\nQuery History:")
            for i, entry in enumerate(self.query_history, 1):
                print(f"{i}. Query: {entry['query']}, Result: {entry['result']}")
