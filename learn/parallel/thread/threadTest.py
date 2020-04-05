import threading, time


def test():
    print('thread %s is running ...' % threading.current_thread().name)
    time.sleep(5)
    print('thread %s done !' % threading.current_thread().name)


if __name__ == '__main__':
    t = threading.Thread(target=test, name='testFunc')
    t.start()
    # t.join()
    print('main thread done !')
