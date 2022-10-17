import argparse
import os
from mutagen.easyid3 import EasyID3

argparser = argparse.ArgumentParser(description='Rename files based on ID3 tags.')
argparser.add_argument('path', type=str, help='Path of the folder containing MP3s')
args = argparser.parse_args()


def main():
    os.chdir(args.path)
    for root, dirs, files in os.walk(args.path):
        for file in files:
            if file.endswith('.mp3'):
                print(f'Processing file {file}...')
                id3data = EasyID3(file)
                id3artist = id3data['artist'][0]
                id3title = id3data['title'][0]
                id3tracknum = id3data['tracknumber'][0]
                # TODO: Fix this so it works properly on Redmond OSes as well
                new_filename = f'{id3tracknum}. {id3artist.replace("/", "-")} - {id3title.replace("/", "-")}'
                print(f'New filename: {new_filename}')
                os.rename(os.path.abspath(file), f'{args.path}{new_filename}')
    print('--- Done! ---')


if __name__ == '__main__':
    main()
