import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help = "Your name: ")
    parser.add_argument("email", help = "Your name: ")
    parser.add_argument("--phone", help = "Your name: ")
    parser.add_argument("test")
    args = parser.parse_args()
    
    print(args)
    