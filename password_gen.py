import random
import string
import argparse

def generate_password(length: int, use_special: bool) -> str:
    """Generates a random password of specified length."""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
        

    try:
        rng = random.SystemRandom()
    except NotImplementedError:
        rng = random

    return ''.join(rng.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument(
        "-l", "--length", 
        type=int, 
        default=16, 
        help="Length of the password (default: 16)"
    )
    parser.add_argument(
        "--no-special", 
        action="store_true", 
        help="Exclude special characters (!@#$ etc.)"
    )
    
    args = parser.parse_args()
    
    if args.length < 4:
        print("Error: Password length should be at least 4 characters.")
        return

    password = generate_password(args.length, not args.no_special)
    
    print("\n" + "="*30)
    print(f" Generated Password: {password}")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()
