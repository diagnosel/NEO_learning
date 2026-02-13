from joke import get_random_joke

def main():
    name = input("Please input your name: ")
    print(f"Hello, {name}")
    
    while True:
        user_response = input(f"{name}, do you want the joke? (yes/no): ").lower()
        if user_response == "yes":
            print(get_random_joke())
        elif user_response == "no":
            print(f"Goodbye {name}")
            break
        
if __name__ == "__main__":
    main()