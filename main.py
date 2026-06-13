import logging

from src.config import LOG_FILE

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
    ],
)


def main():
    print("Hello from kitforge!")


if __name__ == "__main__":
    main()
