# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import random
import requests

from dateutil.parser import parse


def is_date(string, fuzzy=True):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
            
def remove_unwanted_substrings_in_line(patterns_to_avoid):
    """
    Remove unwantes substring in line
    :param file: parsed file
    :param patterns_to_avoid: patterns to remove from file
    :return: list from file
    """
    
    for pattern in patterns_to_avoid:
        line = line.replace(pattern, "")


def write_list_from_file(file, patterns_to_avoid=None):
    """
    Write list from file
    :param file: parsed file
    :param patterns_to_avoid: patterns to remove from file
    :return: list from file
    """
    list_from_file = []
    with open(file, "r", encoding="utf-8") as file:
        content = file.readlines()

        for line in content:

            # Remove empty lines
            line = line.replace('\n\n', '\n').replace('\n', '')

            # Remove unwanted substrings
            if patterns_to_avoid:
                line = remove_unwanted_substrings_in_line(line)

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
    list_from_file = write_list_from_file("songs.txt")
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
    
    print("Group or Song : ", name_in_song_list)
            