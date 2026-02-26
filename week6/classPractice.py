



def greet(userName):
    print()
    print(f"Hello {userName}.")
    
def main():
    print(f"\tPlease tell me your name.")
    userName = input()
    greet(userName)

if __name__ == "__main__":
    main()