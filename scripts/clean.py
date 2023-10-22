import os

PKL_DIR = './data/pkls/'

def main():
    files = os.listdir(PKL_DIR)

    for file in files: 
        os.remove(PKL_DIR + file)

if __name__ == '__main__':
    main()
