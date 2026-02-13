import sys
import os
# Add the 5_files directory to the path so we can import fake_user_generator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '5_files'))

from fake_user_generator import generate_fake_data

def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])
    print(generate_fake_data())
    

if __name__ == "__main__":
    main()