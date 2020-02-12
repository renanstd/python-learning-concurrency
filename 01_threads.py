#!python3

import threading

def my_task():
    print('Hello world: {}'.format(threading.current_thread()))

def main():
    my_thread = threading.Thread(target=my_task())
    my_thread.start()

if __name__ == "__main__":
    main()
