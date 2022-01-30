import argparse
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test.txt')


def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        file = f.read().split("\n\n")
        algo = file[0]
        image = []
        for idx, line in enumerate(file[1].split("\n")):
            image.append([])
            for pixel in line:
                image[idx].append(pixel)

        return algo, image


    return file


def main():
    read_file()


if __name__ == "__main__":
    raise SystemExit(main())
