#
# cueparse.py
# .cue file parser
#
# Xander Jones [2020]
#
class Cuetrack:
    title = None
    performer = None
    file = None
    index = None

    def __init__(self, track_title, track_performer, track_file, track_index):
        self.title = track_title
        self.performer = track_performer
        self.file = track_file
        self.index = track_index

class Cuefile:
    date = None
    recorded_by = None
    title = None
    performer = None
    file = None
    tracks = []
    input_file = None

    def _parse_file(self, file):
        with open(file, 'r') as f:
            track_title = None
            track_performer = None
            track_file = None
            track_index = None
            for index, line in enumerate(f):
                if line[:8] == "REM DATE":
                    self.date = line[9:].strip().replace("\"","")
                elif line[:15] == "REM RECORDED_BY":
                    self.recorded_by = line[16:].strip().replace("\"","")
                elif line[:5] == "TITLE":
                    self.title = line[6:].strip().replace("\"","")
                elif line[:9] == "PERFORMER":
                    self.performer = line[10:].strip().replace("\"","")
                elif line[:4] == "FILE":
                    self.file = line[5:-5].strip().replace("\"","")
                elif line[:7] == "		TITLE":
                    track_title = line[8:].strip().replace("\"","")
                elif line[:11] == "		PERFORMER":
                    track_performer = line[12:].strip().replace("\"","")
                elif line[:6] == "		FILE":
                    track_file = line[7:].strip().replace("\"","")
                elif line[:7] == "		INDEX":
                    track_index = line[10:].strip().replace("\"","")
                    self.tracks.append(Cuetrack(track_title, track_performer, track_file, track_index))
                    track_title = None
                    track_performer = None
                    track_file = None
                    track_index = None

    def __init__(self, input_file):
        self._parse_file(input_file)
