# Functions/memory_functions.py
def memory_save(result):
    global memory
    memory = result
    print(f"Result {result} saved to memory.")

def memory_recall():
    global memory
    if memory is not None:
        print(f"Memory recall: {memory}")
        return memory
    else:
        print("Memory is empty.")
        return None

def memory_clear():
    global memory
    memory = None
    print("Memory cleared.")


