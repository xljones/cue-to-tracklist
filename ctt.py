#
# ctt.py
# Cue to Tracklist
#
# Xander Jones [2020]
#
import argparse
import os
import cueparse

_VERSION = "1.0.0"

'''
    Entry point to script. This is not designed to be imported into another
    script. Alert the user if this happens.
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a .cue file into a text tracklist')
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-f', '--file', help='The .cue file to convert to tracklist', required=True)
    optional_args = parser.add_argument_group('optional arguments')
    args = parser.parse_args()

    print("\r\n>> ctt.py —— Xander Jones —— v" + _VERSION)

    cue = cueparse.Cuefile(args.file)
    for track in cue.tracks:
        print("{0}: {1} - {2}".format(track.index, track.performer, track.title))

else:
    print("Error: This script should be invoked directly")
