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
    list_from_file = []
    with open(file, encoding="utf-8", mode="r") as file:
        content = file.readlines()

        for line in content:

            # Remove lines
            line = line.replace('\n\n', '\n').replace('\n', '')

            # Remove unwanted patterns
            if patterns_to_avoid is not None:
                for pattern in patterns_to_avoid:
                    line = line.replace(pattern, "")

            # Add the line if :
            # - not empty
            # - not a date
            if line != '' and not is_date(line):
                list_from_file.append(line)

    return list_from_file


def get_list_from_file():
    """
    Get songs
    :return: songs
    """
    list_from_file = write_list_from_file("songs.txt", patterns_to_avoid=["chords", "ago"])
    lines = []
    for i in range(0, len(list_from_file), 1):
        line = list_from_file[i]
        lines.append(line)
    return lines


if __name__ == '__main__':
    
    # Name in the song list can be :
    #  the group's 
    #  the title 
    name_in_song_list = random.choice(get_list_from_file())
    
    # Choose another line because this one is not a song title
    while any(ele in name_in_song_list for ele in ["Official", "Chords", "Tab"]):
        name_in_song_list = random.choice(get_list_from_file())

    print("Group or Song : ", name_in_song_list)