def test_error_handling():
    print("\n--- Testing Error Handling ---")
    # Stack Overflow & Underflow
    s = (2)
    try:
        s.pop()
    except IndexError as e:
        print(f"Caught expected error: {e}")
    
    s.push("A")
    s.push("B")
    try:
        s.push("C")
    except OverflowError as e:
        print(f"Caught expected error: {e}")

    # Queue Overflow & Underflow
    q =(2)
    try:
        q.dequeue()
    except IndexError as e:
        print(f"Caught expected error: {e}")
        
    q.enqueue(1)
    q.enqueue(2)
    try:
        q.enqueue(3)
    except OverflowError as e:
        print(f"Caught expected error: {e}")


def main():
    while True:
        print("\n=== Module 5 Lab: Stacks and Queues ===")
        print("1. Test ArrayStack")
        print("2. Test LinkedStack")
        print("3. Test Circular ArrayQueue (with wrap-around)")
        print("4. Test LinkedQueue")
        print("5. Test Error Handling (Underflow/Overflow)")
        print("6. Run Application: Balanced Parentheses Checker")
        print("7. Run Application: Print Queue Simulation")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            stk =(3)
            stk.push(10)
            stk.push(20)
            print(f"Pushed 10, 20. Peek: {stk.peek()}")
            print(f"Popped: {stk.pop()}")
            print(f"Is empty? {stk.is_empty()}")
            
        elif choice == '2':
            stk =()
            stk.push("X")
            stk.push("Y")
            print(f"Pushed X, Y. Peek: {stk.peek()}")
            print(f"Popped: {stk.pop()}")
            
        elif choice == '3':
            q =(3)
            q.enqueue("A")
            q.enqueue("B")
            print(f"Enqueued A, B. Dequeued: {q.dequeue()}")
            q.enqueue("C")
            q.enqueue("D")  # Wrap around test
            print("Enqueued C and D (wrap-around demonstrated).")
            print(f"Peek front: {q.peek_front()}")
            
        elif choice == '4':
            q = ()
            q.enqueue(100)
            q.enqueue(200)
            print(f"Enqueued 100, 200. Peek front: {q.peek_front()}")
            print(f"Dequeued: {q.dequeue()}")
            
        elif choice == '5':
            test_error_handling()
            
        elif choice == '6':
            expr = input("Enter an expression with parentheses (e.g., {[()]}): ")
            if is_balanced(expr):
                print("Result: Balanced!")
            else:
                print("Result: Not balanced!")
                
        elif choice == '7':
            simulate_print_queue()
            
        elif choice == '8':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if == "_main_":
    main()

