def is_balanced(expression: str) -> bool:
    """Checks whether a string of parentheses, brackets, and braces is balanced."""
    stack = ()
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top_elem = stack.pop()
            if top_elem != matching_pairs[char]:
                return False
                
    return stack.is_empty()


class PrintJob:
    """Represents a document print job."""
    def __init__(self, job_id: str, pages: int):
        self.job_id = job_id
        self.pages = pages

    def __str__(self):
        return f"Job ID: {self.job_id}, Pages: {self.pages}"


def simulate_print_queue():
    """Simulates a printer spooler using a FIFO queue."""
    print("\n--- Print Queue Simulation ---")
    print_queue = ()

    # Enqueue jobs
    jobs = [
        PrintJob("Doc1.pdf", 5),
        PrintJob("Report.docx", 12),
        PrintJob("Photo.png", 1)
    ]

    for job in jobs:
        print(f"Enqueuing: {job}")
        print_queue.enqueue(job)

    print("\nProcessing Print Jobs in FIFO Order:")
    while not print_queue.is_empty():
        current_job = print_queue.dequeue()
        print(f"-> Printing... [{current_job}] completed.")

