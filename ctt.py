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
    p = argparse.ArgumentParser(description='Convert a .cue file into a text tracklist (v{0})'.format(_VERSION))
    p.add_argument("directory", help="recursively search this directory for .cue files to translate")
    args = p.parse_args()

    print("\r\n>> ctt.py —— Xander Jones —— v" + _VERSION)

    cue = cueparse.Cuefile(args.file)
    for track in cue.tracks:
        print("{0}: {1} - {2}".format(track.index, track.performer, track.title))

else:
    print("Error: This script should be invoked directly")
