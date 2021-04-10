# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import random


def is_date(string):
    """
    Check if string is a date
    :param string: the parsed string
    :return: boolean (is a date or not)
    """

    try:
        datetime.datetime.strptime(string, '%b %d, %Y')
        return True
    except ValueError:
        return False


def write_list_from_file(file, patterns_to_avoid=None):
    """
    Write list from file
    :param file: parsed file
    :param patterns_to_avoid: patterns to remove from file
    :return: list from file
    """
    list = []
    with open(file, encoding="utf-8", mode="r") as file:
        content = file.readlines()

        for line in content:

            # Remove lines
            line = line.replace('\n\n', '\n').replace('\n', '')

            # Remove unwanted patterns
            if patterns_to_avoid is not None:
                for pattern in patterns_to_avoid:
                    line = line.replace(pattern, "")

            if line != '' and not is_date(line):
                list.append(line)

    return list


def get_songs():
    """
    Get songs
    :return: songs
    """
    song_list = write_list_from_file("songs.txt", patterns_to_avoid=["chords"])
    songs = []
    for i in range(0, len(song_list), 2):
        song = {"artist": song_list[i], "name": song_list[i + 1]}
        songs.append(song)
    return songs


if __name__ == '__main__':
    songs = get_songs()
    print(random.choice(songs))
