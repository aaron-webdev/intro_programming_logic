



def greet(userName, greeting = "hello", punc = "!"):
    print()
    print(f"{greeting} {userName}{punc}")
    
def main():
    print(f"\tPlease tell me your name.")
    userName = input()
    print("Input a greeting")
    greeting = input()
    print("Input a punctuation")
    punc = input()

    greet(userName,greeting,punc)

if __name__ == "__main__":
    main()