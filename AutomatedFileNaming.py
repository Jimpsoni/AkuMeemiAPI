import os

PATH = "./images"


def index_images(path: str) -> None:
    """
    :param path: path to images folder
    :return: None
    """
    index = 1

    os.chdir(path)

    for image in os.listdir():
        os.rename(image, f"{index:03d}.png")
        index += 1


if __name__ == "__main__":

    index_images(PATH)
