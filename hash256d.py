from hashlib import sha256 
import sys 

def hash_iterations(data, iterations=2): 
    hashed_data = data

    for i in range(iterations): 
        hashed_data = sha256(hashed_data).digest() 

    return hashed_data.hex()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'usage: python {sys.argv[0]} <password> <iterations>')
        sys.exit(1)

    password = bytes(sys.argv[1], 'utf-8') 
    iterations = int(sys.argv[2])

    hashed_password = hash_iterations(password, iterations)
    print(hashed_password)
