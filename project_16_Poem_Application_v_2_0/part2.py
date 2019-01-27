import threading
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) $(message)')


def move_1():
    logging.debug("start")
    time.sleep(random.randint(1, 5))
    logging.debug("exiting")


def move_2():
    logging.debug("start")
    time.sleep(random.randint(1, 3))
    logging.debug("exiting")
    return


def main():
    t_1 = threading.Thread(name='office client', target=move_1)
    t_2 = threading.Thread(name='parking client', target=move_2)

    t_3 = threading.Thread(target=move_1)

    t_1.start()
    t_2.start()
    t_3.start()


if __name__ == "__main__":
    main()
