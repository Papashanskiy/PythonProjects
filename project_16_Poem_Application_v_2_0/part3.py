import threading, time, random, logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) $(message)s')


def demon_func():
    logging.debug("Start")
    time.sleep(4)
    with open('part3.txt', 'w') as f:
        f.write("Hello :)")
        f.close()
    logging.debug("Exiting")


def non_demon_func():
    logging.debug("Start")
    time.sleep(2)
    logging.debug("Exiting")


def main():
    t_1 = threading.Thread(target=demon_func)
    t_2 = threading.Thread(target=non_demon_func)

    t_1.setDaemon(True)

    t_1.start()
    t_2.start()

    t_1.join()


if __name__ == "__main__":
    main()