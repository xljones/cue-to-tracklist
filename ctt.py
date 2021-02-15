#
# ctt.py
# Cue to Tracklist
#
# Xander Jones [2020]
#
import argparse
import os
import cueparse

_VERSION = "1.1.0"

'''
    Entry point to script. This is not designed to be imported into another
    script. Alert the user if this happens.
'''
if __name__ == "__main__":
    p = argparse.ArgumentParser(description='Convert a .cue file into a text tracklist (v{0})'.format(_VERSION))
    p.add_argument("directory", help="recursively search this directory for .cue files to translate")
    args = p.parse_args()

    print("\r\n>> ctt.py —— Xander Jones —— v" + _VERSION)

    if os.path.isdir(args.directory):
        for root, dir, files in os.walk(args.directory):
            print("root '{0}', dir '{1}', file '{2}'".format(root, dir, files))
            for file in files:
                if file.endswith('.cue'):
                    new_filename = file.replace(".cue", ".txt")
                    f = open(os.path.join(root, new_filename), "w")
                    cue = cueparse.Cuefile(os.path.abspath(file))
                    for track in cue.tracks:
                        f.write("{0}: {1} - {2}".format(track.index, track.performer, track.title))
                    f.close()

    else:
        raise FileNotFoundError("Directory '{0}' does not exist".format(args.directory))

    #cue = cueparse.Cuefile(args.file)
    #for track in cue.tracks:
    #    print("{0}: {1} - {2}".format(track.index, track.performer, track.title))

else:
    print("Error: This script should be invoked directly")
