"""
    Copyright (C) 2015 Tuomas Airaksinen.
    See LICENCE.txt
"""


def get_verse_ranges():
    """ get data for CHAPTER_LST_VERSES and LAST_CHAPTERS from ESVS osis file"""
    from bs4 import BeautifulSoup
    from .bibleref import Ref

    bs = BeautifulSoup(open('esvs.osis').read(), 'xml')
    print 'reading done'
    verse_nums = {}
    chap_nums = {}
    for v in bs.find_all('verse'):
        ref = Ref(v['osisID'])
        chapref = '%s.%s' % (BOOKREFS[ref.numref[0]], ref.numref[1])
        verse_nums[chapref] = max(ref.numref[2], verse_nums.get(chapref, 0))
        bookref = BOOKREFS[ref.numref[0]]
        chap_nums[bookref] = max(ref.numref[1], chap_nums.get(bookref, 0))
    return chap_nums, verse_nums


TAGS_NONE = 0
TAGS_BOOK = 1
TAGS_CHAPTES = 2
TAGS_VERSES = 3

BOOKREFS = ['Gen', 'Exod', 'Lev', 'Num', 'Deut', 'Josh', 'Judg', 'Ruth', '1Sam', '2Sam', '1Kgs', '2Kgs', '1Chr',
            '2Chr', 'Ezra', 'Neh', 'Esth', 'Job', 'Ps', 'Prov', 'Eccl', 'Song', 'Isa', 'Jer', 'Lam', 'Ezek', 'Dan',
            'Hos', 'Joel', 'Amos', 'Obad', 'Jonah', 'Mic', 'Nah', 'Hab', 'Zeph', 'Hag', 'Zech', 'Mal', 'Matt', 'Mark',
            'Luke', 'John', 'Acts', 'Rom', '1Cor', '2Cor', 'Gal', 'Eph', 'Phil', 'Col', '1Thess', '2Thess', '1Tim',
            '2Tim', 'Titus', 'Phlm', 'Heb', 'Jas', '1Pet', '2Pet', '1John', '2John', '3John', 'Jude', 'Rev']

CHAPTER_LAST_VERSES = {'Rev.10': 11, 'Matt.2': 23, '1Kgs.8': 66, '1Kgs.9': 28, 'Matt.3': 17, '1Kgs.2': 46, '1Kgs.3': 28,
                       '1Kgs.1': 53, '1Kgs.6': 38, '1Kgs.7': 51, '1Kgs.4': 34, '1Kgs.5': 18, '2Chr.7': 22, '2Chr.6': 42,
                       '2Chr.5': 14, '2Chr.4': 22, '2Chr.3': 17, '2Chr.2': 18, '2Chr.1': 17, 'Rev.19': 21, 'Isa.8': 22,
                       'Matt.6': 34, 'Rev.14': 20, 'Rev.15': 8, 'Luke.20': 47, 'Rev.13': 18, '2Chr.9': 31, '2Chr.8': 18,
                       'Jonah.4': 11, 'Isa.18': 7, 'Isa.19': 25, 'Isa.14': 32, 'Isa.15': 9, 'Isa.16': 14, 'Isa.17': 14,
                       'Isa.10': 34, 'Isa.11': 16, 'Isa.12': 6, 'Isa.13': 22, '1Thess.4': 18, '1Thess.5': 28,
                       '1Thess.2': 20, '1Thess.3': 13, 'Isa.9': 21, 'Job.22': 30, 'Acts.7': 60, 'Acts.6': 15,
                       'Acts.5': 42, 'Song.8': 14, 'Acts.3': 26, 'Matt.8': 34, 'Acts.1': 26, 'Isa.59': 21, 'Song.3': 11,
                       'Luke.2': 52, 'Jer.23': 40, 'Jer.5': 31, 'Song.2': 17, 'John.21': 25, 'Jer.36': 32, 'Amos.2': 16,
                       'Jer.37': 21, 'Ps.135': 21, 'Rev.20': 15, '1Tim.1': 20, 'Song.7': 13, '1Tim.3': 16, 'Ps.134': 3,
                       '1Tim.5': 25, '1Tim.4': 16, 'Song.6': 13, 'Jas.3': 18, 'Jer.22': 30, 'Ps.104': 35, 'Song.5': 16,
                       'Song.4': 16, 'Amos.3': 15, 'Rev.1': 20, '1John.2': 29, '1John.5': 21, 'Jer.21': 14,
                       '2Chr.31': 21, '2Chr.30': 27, '2Chr.33': 25, '2Chr.32': 33, '2Chr.35': 27, '2Chr.34': 33,
                       '2Chr.36': 23, '1John.3': 24, 'Amos.4': 13, 'Isa.22': 25, 'Rev.16': 21, 'Jer.7': 34,
                       'Rev.22': 21,
                       'Lev.6': 30, 'Lev.7': 38, 'Lev.4': 35, 'Lev.5': 19, 'Lev.2': 16, 'Lev.3': 17, 'Lev.1': 17,
                       'Num.35': 34, 'Num.34': 29, 'Num.36': 13, 'Num.31': 54, 'Num.30': 16, 'Lev.8': 36, 'Num.32': 42,
                       'Ps.46': 11, 'Ps.47': 9, 'Ps.44': 26, 'Ps.45': 17, 'Ps.42': 11, 'Ps.43': 5, 'Ps.40': 17,
                       'Ps.41': 13, 'Rev.4': 11, 'Deut.29': 29, 'Rev.6': 17, 'Jer.27': 22, 'Num.5': 31, 'Ps.48': 14,
                       'Deut.28': 68, 'Ps.138': 8, 'Eph.4': 32, 'Num.4': 49, 'Jonah.3': 10, 'Jonah.2': 10,
                       'Jonah.1': 17,
                       'Eph.1': 23, 'Acts.23': 35, 'Hag.1': 15, 'Judg.4': 24, 'Judg.5': 31, 'Judg.6': 40, 'Judg.7': 25,
                       'Judg.1': 36, 'Judg.2': 23, 'Judg.3': 31, 'Jer.26': 24, 'Judg.8': 35, 'Judg.9': 57, 'Neh.6': 19,
                       'Amos.7': 17, '2Pet.1': 21, 'Neh.7': 73, 'Neh.4': 23, 'Job.29': 25, 'Job.28': 28, 'Jer.18': 23,
                       'Neh.5': 19, '1Chr.8': 40, 'Jer.25': 38, 'Job.21': 34, 'Neh.2': 20, 'Job.23': 17, '1Chr.9': 44,
                       'Job.25': 6, 'Job.24': 25, 'Job.27': 23, 'Neh.3': 32, 'Heb.6': 20, 'Ezek.24': 27, 'Heb.4': 16,
                       'Heb.5': 14, 'Heb.2': 18, 'John.7': 53, 'Heb.1': 14, 'Neh.1': 11, 'Heb.8': 13, 'Heb.9': 28,
                       'Jer.24': 10, 'Ezek.20': 49, 'Ezek.21': 32, 'Rom.4': 25, 'Ezek.11': 25, 'Isa.6': 13, 'Rom.1': 32,
                       'Isa.5': 30, 'Neh.8': 18, 'Neh.9': 38, 'Obad.1': 21, 'Acts.9': 43, 'Ezek.28': 26, 'Acts.8': 40,
                       'Ezek.29': 21, 'Ps.91': 16, 'Ps.90': 17, 'Ps.93': 5, 'Ps.92': 15, 'Ps.95': 11, 'Ps.94': 23,
                       'Ps.97': 12, 'Ps.96': 13, 'Ps.99': 9, 'Ps.98': 9, 'Isa.58': 14, 'Isa.47': 15, 'Isa.46': 13,
                       'Isa.45': 25, 'Isa.44': 28, 'Isa.43': 28, 'Isa.42': 25, 'Isa.41': 29, 'Isa.40': 31, 'Ps.1': 6,
                       'Rom.3': 31, 'Isa.49': 26, 'Isa.48': 22, '1Chr.6': 81, '1Chr.7': 40, '1Chr.4': 43, '1Chr.5': 26,
                       '1Chr.2': 55, '1Chr.3': 24, '1Chr.1': 54, 'Deut.25': 19, 'Deut.24': 22, 'Deut.27': 26,
                       'Deut.26': 19, 'Deut.21': 23, 'Deut.20': 20, 'Deut.23': 25, 'Deut.22': 30, 'Isa.4': 6,
                       'Ezek.25': 17, 'Ezek.26': 21, 'Ezek.27': 36, 'Prov.28': 28, 'Prov.29': 27, 'Ezek.22': 31,
                       'Ezek.23': 49, 'Prov.24': 34, 'Prov.25': 28, 'Prov.26': 28, 'Prov.27': 27, 'Prov.20': 30,
                       'Prov.21': 31, 'Prov.22': 29, 'Prov.23': 35, 'Gen.28': 22, 'Gen.29': 35, 'Gen.24': 67,
                       'Gen.25': 34, 'Gen.26': 35, 'Gen.27': 46, 'Gen.20': 18, 'Gen.21': 34, 'Gen.22': 24, 'Gen.23': 20,
                       'Matt.25': 46, 'Matt.24': 51, 'Matt.27': 66, 'Matt.26': 75, 'Matt.21': 46, 'Matt.20': 34,
                       'Matt.23': 39, 'Matt.22': 46, 'Ps.3': 8, 'Rom.5': 21, '1Cor.8': 13, 'Matt.28': 20, 'Hab.1': 17,
                       'Exod.6': 30, 'Exod.7': 25, 'Exod.4': 31, 'Exod.5': 23, 'Exod.2': 25, 'Exod.3': 22, 'Exod.1': 22,
                       'Jas.1': 27, 'Gal.2': 21, 'Jas.2': 26, 'Acts.4': 37, 'Jas.4': 17, 'Exod.8': 32, 'Exod.9': 35,
                       'Matt.1': 25, '2Cor.8': 24, 'Ps.128': 6, 'Ps.129': 8, 'Jer.19': 15, 'Ps.124': 8, 'Ps.125': 5,
                       'Ps.126': 6, 'Ps.127': 5, 'Ps.120': 7, 'Ps.121': 8, 'Ps.122': 9, 'Ps.123': 4, 'Rom.10': 21,
                       '1Thess.1': 10, 'Rom.7': 25, 'Heb.11': 40, 'Zech.8': 23, 'Zech.9': 17, 'Acts.21': 40,
                       'Zech.2': 13, 'Zech.3': 10, 'Zech.1': 21, 'Zech.6': 15, 'Zech.7': 14, 'Zech.4': 14, 'Zech.5': 11,
                       'Dan.9': 27, 'Rom.6': 23, 'Zech.12': 14, 'Matt.4': 25, 'Col.2': 23, '1Tim.2': 15, 'Mic.2': 13,
                       'Ps.142': 7, 'Zeph.1': 18, 'Exod.40': 38, 'Mic.6': 16, 'Mic.7': 20, 'Mic.4': 13, 'Mic.5': 15,
                       'Jer.45': 5, 'Jer.44': 30, 'Jer.47': 7, 'Jer.46': 28, 'Jer.41': 18, 'Jer.40': 16, 'Jer.43': 13,
                       'Jer.42': 22, 'Matt.5': 48, '1Tim.6': 21, 'Jer.49': 39, 'Jer.48': 47, '1Sam.10': 27,
                       '1Sam.11': 15, '1Sam.12': 25, '1Sam.13': 23, '1Sam.14': 52, '1Sam.15': 35, '1Sam.16': 23,
                       '1Sam.17': 58, '1Sam.18': 30, '1Sam.19': 24, '2Cor.4': 18, '2Cor.5': 21, '2Cor.2': 17,
                       '2Cor.3': 18, '2Cor.1': 24, 'Rev.7': 17, 'Jer.12': 17, 'Mark.6': 56, 'John.9': 41, 'Heb.7': 28,
                       'Jer.13': 27, 'Titus.3': 15, 'Luke.12': 59, 'Luke.15': 32, 'Luke.14': 35, 'Luke.17': 37,
                       'Jer.10': 25, '1Chr.14': 17, '1Chr.15': 29, '1Chr.16': 43, '1Chr.17': 27, '1Chr.10': 14,
                       '1Chr.11': 47, '1Chr.12': 40, '1Chr.13': 14, '1Chr.18': 17, '1Chr.19': 19, 'Matt.9': 38,
                       'Jer.34': 22, 'John.20': 31, 'Jer.11': 23, 'John.6': 71, '2Chr.28': 27, '2Chr.29': 36,
                       '2Chr.26': 23, '2Chr.27': 9, '2Chr.24': 27, '2Chr.25': 28, '2Chr.22': 12, '2Chr.23': 21,
                       '2Chr.20': 37, '2Chr.21': 20, 'Jer.16': 21, '1John.4': 21, '2Thess.3': 18, 'Prov.8': 36,
                       'Mark.13': 37, 'Mark.12': 44, 'Mark.11': 33, 'Mark.10': 52, 'Mark.16': 20, 'Mark.15': 47,
                       'Mark.14': 72, 'Dan.10': 21, 'Matt.7': 29, 'Acts.2': 47, 'Ps.139': 24, 'Ps.73': 28, 'Ps.72': 20,
                       'Ps.71': 24, 'Ps.70': 5, 'Ps.77': 20, 'Ps.76': 12, 'Ps.75': 10, 'Ps.74': 23, 'Ps.79': 13,
                       'Ps.78': 72, 'John.4': 54, 'Prov.6': 35, '2Cor.10': 18, 'Acts.27': 44, '2Cor.11': 33,
                       '2Cor.12': 21, 'Job.6': 30, '2Cor.13': 14, 'Job.7': 21, 'Job.14': 22, 'Job.15': 35, 'Job.16': 22,
                       'Job.17': 16, 'Job.10': 22, 'Job.11': 20, 'Job.12': 25, 'Job.13': 28, 'Dan.8': 27, 'Jer.30': 24,
                       'Job.18': 21, 'Job.19': 29, 'Esth.10': 3, 'Jer.15': 21, 'Mal.1': 14, 'Dan.12': 13, 'Eccl.6': 12,
                       'Job.8': 22, 'Job.9': 35, 'Jer.6': 30, 'Jer.31': 40, 'Acts.25': 27, 'Isa.23': 18, 'Mal.4': 6,
                       'Isa.50': 11, 'Ps.82': 8, 'Isa.51': 23, 'Ezra.10': 44, 'John.1': 51, 'Rom.13': 14, 'Rom.12': 21,
                       'Rom.15': 33, 'Rom.14': 23, '2Tim.2': 26, 'Isa.24': 23, 'Exod.14': 31, 'Exod.15': 27,
                       'Exod.16': 36, 'Exod.17': 16, 'Exod.10': 29, 'Exod.11': 10, 'Exod.12': 51, 'Exod.13': 22,
                       'Acts.22': 30, 'John.8': 59, 'Exod.18': 27, 'Exod.19': 25, 'Isa.29': 24, 'Isa.28': 29,
                       'Phil.4': 23, 'Phil.3': 21, 'Phil.2': 30, 'Phil.1': 30, 'Jer.33': 26, 'John.19': 42,
                       'John.18': 40, 'John.17': 26, 'John.3': 36, 'John.15': 27, 'John.14': 31, 'John.13': 38,
                       'John.12': 50, 'John.11': 57, 'John.2': 25, 'Josh.4': 24, 'Josh.5': 15, 'Josh.6': 27,
                       'Josh.7': 26, 'Ps.86': 17, 'Josh.1': 18, 'Josh.2': 24, 'Josh.3': 17, '2Tim.3': 17, 'Luke.9': 62,
                       'Ps.88': 18, 'Ps.89': 52, 'Josh.8': 35, 'Josh.9': 27, 'Luke.8': 56, 'Isa.32': 20, 'Isa.33': 24,
                       'Isa.30': 33, 'Isa.31': 9, 'Isa.36': 22, 'Isa.37': 38, 'Isa.34': 17, 'Isa.35': 10, 'Hag.2': 23,
                       'Isa.38': 22, 'Isa.39': 8, 'Luke.4': 44, 'Deut.32': 52, 'Deut.33': 29, 'Deut.30': 20,
                       'Deut.31': 30, 'Deut.34': 12, '2John.1': 13, 'Prov.19': 29, 'Prov.18': 24, 'Ezek.13': 23,
                       'Ezek.12': 28, 'Ezek.15': 8, 'Ezek.14': 23, 'Ezek.17': 24, 'Ezek.16': 63, 'Prov.11': 31,
                       'Prov.10': 32, 'Prov.13': 25, 'Prov.12': 28, 'Prov.15': 33, 'Prov.14': 35, 'Prov.17': 28,
                       'Prov.16': 33, 'Ezek.5': 17, 'Ezek.4': 17, 'Gen.39': 23, 'Gen.38': 30, 'Ezek.1': 28,
                       'Ezek.39': 29, 'Ezek.3': 27, 'Jer.35': 19, 'Gen.33': 20, 'Gen.32': 32, 'Gen.31': 55,
                       'Gen.30': 43,
                       'Gen.37': 36, 'Gen.36': 43, 'Gen.35': 29, 'Gen.34': 31, 'Ps.37': 40, 'Ps.36': 12, 'Ps.35': 28,
                       'Ps.34': 22, 'Ps.33': 22, 'Ps.32': 11, 'Ps.31': 24, 'Ps.30': 12, 'Lam.5': 22, 'Lam.4': 22,
                       'Joel.1': 20, 'Lam.1': 22, 'Ps.39': 13, 'Ps.38': 22, 'Hab.2': 20, 'Hab.3': 19, 'Col.3': 25,
                       '2Chr.17': 19, '2Chr.16': 14, '2Chr.15': 19, '2Chr.14': 15, '2Chr.13': 22, '2Chr.12': 16,
                       '2Chr.11': 23, '2Chr.10': 19, 'Ps.133': 3, 'Ps.132': 18, 'Ps.131': 3, 'Ps.130': 8, 'Ps.137': 9,
                       'Ps.136': 26, '2Chr.19': 11, '2Chr.18': 34, 'Lev.25': 55, 'Lev.24': 23, 'Lev.27': 34,
                       'Lev.26': 46, 'Lev.21': 24, 'Lev.20': 27, 'Lev.23': 44, 'Lev.22': 33, 'Lev.9': 24, 'Rev.2': 29,
                       'Ps.83': 18, 'Rev.9': 21, 'Gen.48': 22, 'Gen.49': 33, 'Gen.46': 34, 'Gen.47': 31, 'Gen.44': 34,
                       'Gen.45': 28, 'Gen.42': 38, 'Gen.43': 34, 'Gen.40': 23, 'Gen.41': 57, 'Phlm.1': 25,
                       'Matt.12': 50,
                       'Jer.39': 18, '1Cor.16': 24, '1Cor.15': 58, 'Rom.16': 27, '1Cor.13': 13, '1Cor.12': 31,
                       '1Cor.11': 34, '1Cor.10': 33, 'Rom.11': 36, 'Gal.6': 18, 'Eph.6': 24, 'Ps.148': 14, 'Ps.149': 9,
                       'Ps.146': 10, 'Ps.147': 20, 'Ps.144': 15, 'Ps.145': 21, 'Ps.81': 16, 'Ps.143': 12, 'Ps.140': 13,
                       'Ps.141': 10, 'Luke.19': 48, 'Luke.18': 43, '2Pet.3': 18, '2Pet.2': 22, 'Luke.11': 54,
                       'Luke.10': 42, 'Luke.13': 35, 'Ruth.4': 22, 'Ruth.3': 18, 'Ruth.2': 23, 'Ruth.1': 22,
                       'Luke.16': 31, 'Hos.1': 11, 'Hos.3': 5, 'Hos.2': 23, 'Hos.5': 15, 'Hos.4': 19, 'Hos.7': 16,
                       'Hos.6': 11, 'Hos.9': 17, 'Hos.8': 14, 'Ps.49': 20, 'Job.42': 17, 'Job.41': 34, 'Job.40': 24,
                       'Job.2': 13, 'Job.3': 26, 'Job.1': 22, '1Sam.29': 11, '1Sam.28': 25, 'Job.4': 21, 'Job.5': 27,
                       '1Sam.25': 44, '1Sam.24': 22, '1Sam.27': 12, '1Sam.26': 25, '1Sam.21': 15, '1Sam.20': 42,
                       '1Sam.23': 29, '1Sam.22': 23, 'Heb.10': 39, 'Ps.2': 12, 'Eph.2': 22, 'Eph.3': 21, 'Ezek.42': 20,
                       '2Thess.2': 17, 'Ezek.43': 27, 'Hos.11': 12, 'Hos.10': 15, 'Hos.13': 16, 'Hos.12': 14,
                       'Hos.14': 9, 'Dan.2': 49, 'Rev.3': 22, 'Dan.3': 30, 'Neh.10': 39, 'Neh.11': 36, 'Neh.12': 47,
                       'Neh.13': 31, 'Ps.5': 12, 'Ps.4': 8, 'Ps.7': 17, 'Ps.6': 10, 'Ps.9': 20, 'Ps.8': 9, 'Dan.1': 21,
                       'Dan.6': 28, 'Dan.7': 28, 'Dan.4': 37, 'Dan.5': 31, 'Joel.2': 32, 'Joel.3': 21, 'Ezek.48': 35,
                       '1Chr.21': 30, '1Chr.20': 8, '1Chr.23': 32, '1Chr.22': 19, '1Chr.25': 31, '1Chr.24': 31,
                       '1Chr.27': 34, '1Chr.26': 32, '1Chr.29': 30, '1Chr.28': 21, 'Jer.17': 27, 'Acts.17': 34,
                       'Matt.15': 39, 'Nah.2': 13, '1Cor.6': 20, 'Matt.16': 28, 'Mic.3': 12, 'Isa.65': 25, 'Isa.64': 12,
                       'Isa.66': 24, 'Isa.61': 11, 'Isa.60': 22, 'Isa.63': 19, 'Isa.62': 12, 'Mic.1': 16, 'Judg.18': 31,
                       'Judg.19': 30, 'Judg.16': 31, 'Judg.17': 13, 'Judg.14': 20, 'Judg.15': 20, 'Judg.12': 15,
                       'Judg.13': 25, 'Judg.10': 18, 'Judg.11': 40, 'Num.17': 13, 'Num.16': 50, 'Num.15': 41,
                       'Num.14': 45, 'Num.13': 33, 'Num.12': 16, 'Num.11': 35, 'Num.10': 36, 'Mal.3': 18, 'Luke.23': 56,
                       'Num.19': 22, 'Num.18': 32, 'Eccl.11': 10, 'Eccl.10': 20, 'Eccl.12': 14, 'Rev.21': 27,
                       'Eph.5': 33, 'Ps.68': 35, 'Ps.69': 36, 'John.16': 33, 'Ps.64': 10, 'Ps.65': 13, 'Ps.66': 20,
                       'Ps.67': 7, 'Ps.60': 12, 'Ps.61': 8, 'Ps.62': 12, 'Ps.63': 11, 'Ps.102': 28, 'Ps.103': 22,
                       'Ps.100': 5, 'Ps.101': 8, 'Ps.106': 48, 'Ps.107': 43, 'Josh.18': 28, 'Josh.19': 51,
                       'Josh.16': 10,
                       'Josh.17': 18, 'Josh.14': 15, 'Josh.15': 63, 'Josh.12': 24, 'Josh.13': 33, 'Josh.10': 43,
                       'Josh.11': 23, '1Kgs.10': 29, '1Kgs.11': 43, '1Kgs.12': 33, '1Kgs.13': 34, '1Kgs.14': 31,
                       '1Kgs.15': 34, '1Kgs.16': 34, '1Kgs.17': 24, '1Kgs.18': 46, '1Kgs.19': 21, 'John.10': 42,
                       'Luke.3': 38, 'Luke.21': 38, 'Ezra.2': 70, 'Ezra.3': 13, 'Song.1': 17, 'Ezra.1': 11,
                       'Ezra.6': 22,
                       'Ezra.7': 28, 'Ezra.4': 24, 'Ezra.5': 17, 'Rom.9': 33, 'Rom.8': 39, 'Ezra.8': 36, 'Ezra.9': 15,
                       'Jer.38': 28, 'Ps.80': 19, '1John.1': 10, 'Num.33': 56, 'Esth.4': 17, 'Esth.5': 14, 'Esth.6': 14,
                       'Esth.7': 10, 'Mal.2': 17, 'Esth.1': 22, 'Esth.2': 23, 'Esth.3': 15, 'Luke.22': 71, 'Esth.8': 17,
                       'Esth.9': 32, 'Ps.87': 7, 'Ps.84': 12, 'Acts.26': 32, '1Cor.14': 40, 'Ps.85': 13, '1Cor.9': 27,
                       'Amos.1': 15, '2Sam.24': 25, '2Sam.22': 51, '2Sam.23': 39, '2Sam.20': 26, '2Sam.21': 22,
                       'Exod.21': 36, 'Exod.20': 26, 'Exod.23': 33, 'Exod.22': 31, 'Exod.25': 40, 'Exod.24': 18,
                       'Exod.27': 21, 'Exod.26': 37, 'Exod.29': 46, 'Exod.28': 43, '2Cor.9': 15, 'Amos.5': 27,
                       '2Cor.6': 18, '1Sam.8': 22, '1Sam.9': 27, '2Cor.7': 16, '1Sam.2': 36, '1Sam.3': 21, '1Sam.1': 28,
                       '1Sam.6': 21, '1Sam.7': 17, '1Sam.4': 22, '1Sam.5': 12, '2Kgs.3': 27, 'Luke.24': 53,
                       '2Sam.6': 23,
                       '1Pet.4': 19, '1Pet.5': 14, '2Sam.5': 25, '1Pet.2': 25, '1Pet.3': 22, 'Eccl.9': 18, 'Eccl.8': 17,
                       'Jer.20': 18, 'Job.20': 29, 'Eccl.1': 18, '2Sam.3': 39, 'Eccl.3': 22, 'Eccl.2': 26, 'Eccl.5': 20,
                       'Eccl.4': 16, 'Eccl.7': 29, '2Sam.2': 32, 'Isa.21': 17, 'Isa.20': 6, 'Deut.8': 20, 'Deut.9': 29,
                       'Isa.25': 12, '2Sam.1': 27, 'Isa.27': 13, 'Isa.26': 21, 'Deut.2': 37, 'Deut.3': 29, 'John.5': 47,
                       'Deut.1': 46, 'Deut.6': 25, 'Deut.7': 26, 'Deut.4': 49, 'Deut.5': 33, 'Nah.3': 19, 'Jer.14': 22,
                       'Job.26': 14, 'Jer.29': 32, 'Gen.9': 29, 'Gen.8': 22, 'Jer.28': 17, '1Cor.7': 40, 'Gen.1': 31,
                       'Gen.3': 24, 'Gen.2': 25, 'Gen.5': 32, 'Gen.4': 26, 'Gen.7': 24, 'Gen.6': 22, 'Acts.15': 41,
                       'Jas.5': 20, 'Heb.3': 19, 'Ps.20': 9, 'Ps.21': 13, 'Ps.22': 31, 'Ps.23': 6, 'Ps.24': 10,
                       'Ps.25': 22, 'Ps.26': 12, 'Ps.27': 14, 'Ps.28': 9, 'Ps.29': 11, 'Nah.1': 15, 'Ezek.9': 11,
                       '2Tim.1': 18, 'Rev.8': 13, 'Judg.21': 25, 'Judg.20': 48, 'Ezek.8': 18, 'Matt.18': 35,
                       'Lev.10': 20, 'Lev.11': 47, 'Lev.12': 8, 'Lev.13': 59, 'Lev.14': 57, 'Lev.15': 33, 'Lev.16': 34,
                       'Lev.17': 16, 'Lev.18': 30, 'Lev.19': 37, 'Rev.18': 24, 'Num.28': 31, 'Num.29': 40, 'Num.26': 65,
                       'Num.27': 23, 'Num.24': 25, 'Num.25': 18, 'Num.22': 41, 'Gen.50': 26, 'Num.20': 29, 'Num.21': 35,
                       'Ps.55': 23, 'Ps.54': 7, 'Ps.57': 11, 'Ps.56': 13, 'Ps.51': 19, 'Ps.50': 23, 'Ps.53': 6,
                       'Ps.52': 9, 'Ps.59': 17, 'Ps.58': 11, 'Titus.1': 16, '2Kgs.22': 20, '2Kgs.23': 37, '2Kgs.20': 21,
                       'Josh.24': 33, 'Josh.23': 16, 'Josh.22': 34, 'Josh.21': 45, 'Josh.20': 9, 'Col.1': 29,
                       'Num.23': 30, 'Matt.10': 42, 'Mark.9': 50, 'Mark.8': 38, 'Acts.19': 41, 'Acts.18': 28,
                       'Mark.3': 35, 'Mark.2': 28, 'Mark.1': 45, 'Acts.14': 28, 'Mark.7': 37, 'Ps.150': 6, 'Mark.5': 43,
                       'Mark.4': 41, 'Matt.11': 30, 'Ezek.19': 14, 'Job.38': 41, 'Job.39': 30, 'Rev.17': 18,
                       'Rom.2': 29,
                       'Ezek.18': 32, 'Job.32': 22, 'Job.33': 33, 'Job.30': 31, 'Job.31': 40, 'Job.36': 33,
                       'Job.37': 24,
                       'Job.34': 37, 'Job.35': 16, 'Jer.32': 44, 'Num.9': 23, 'Num.8': 26, 'Num.7': 89, 'Num.6': 27,
                       '1Sam.30': 31, '1Sam.31': 13, 'Num.3': 51, 'Num.2': 34, 'Num.1': 54, '2Sam.17': 29,
                       '2Sam.16': 23,
                       '2Sam.15': 37, '2Sam.14': 33, '2Sam.13': 39, '2Sam.12': 31, '2Sam.11': 27, '2Sam.10': 19,
                       'Isa.2': 22, 'Isa.3': 26, 'Isa.1': 31, 'Ps.105': 45, 'Isa.7': 25, '2Sam.19': 43, '2Sam.18': 33,
                       'Titus.2': 15, 'Matt.13': 58, '3John.1': 15, 'Ezek.7': 27, 'Matt.19': 30, 'Ezek.6': 14,
                       '1Pet.1': 25, 'Zech.10': 12, 'Zech.11': 17, 'Ezek.38': 23, 'Zech.13': 9, 'Zech.14': 21,
                       'Acts.24': 27, 'Matt.14': 36, 'Ezek.2': 10, 'Rev.12': 17, '2Kgs.21': 26, 'Zeph.3': 20,
                       'Acts.20': 38, 'Acts.12': 25, 'Prov.9': 18, '2Kgs.24': 20, '2Thess.1': 12, 'Prov.5': 23,
                       'Prov.4': 27, 'Prov.7': 27, '2Kgs.25': 30, 'Prov.1': 33, 'Prov.3': 35, 'Prov.2': 22,
                       'Deut.10': 22, 'Deut.11': 32, 'Deut.12': 32, 'Deut.13': 18, 'Deut.14': 29, 'Deut.15': 23,
                       'Deut.16': 22, 'Deut.17': 20, 'Deut.18': 22, 'Deut.19': 21, 'Isa.52': 15, 'Isa.53': 12,
                       'Isa.54': 17, 'Isa.55': 13, 'Isa.56': 12, 'Isa.57': 21, 'Ezek.37': 28, 'Ezek.36': 38,
                       'Ezek.35': 15, 'Ezek.34': 31, 'Ezek.33': 33, 'Ezek.32': 32, 'Ezek.31': 18, 'Ezek.30': 26,
                       'Luke.5': 39, 'Ezek.10': 22, 'Luke.7': 50, 'Luke.6': 49, 'Luke.1': 80, 'Prov.31': 31,
                       'Prov.30': 33, 'Gen.11': 32, 'Gen.10': 32, 'Gen.13': 18, 'Gen.12': 20, 'Gen.15': 21,
                       'Gen.14': 24,
                       'Gen.17': 27, 'Gen.16': 16, 'Gen.19': 38, 'Gen.18': 33, '1Cor.5': 13, '1Cor.4': 21, '1Cor.3': 23,
                       '1Cor.2': 16, '1Cor.1': 31, 'Matt.17': 27, 'Zeph.2': 15, 'Rev.11': 19, 'Ps.19': 14, 'Ps.18': 50,
                       'Ezek.40': 49, 'Ezek.41': 26, 'Ezek.46': 24, 'Ezek.47': 23, 'Ezek.44': 31, 'Ezek.45': 25,
                       'Ps.11': 7, 'Ps.10': 18, 'Ps.13': 6, 'Ps.12': 8, 'Ps.15': 5, 'Ps.14': 7, 'Ps.17': 15,
                       'Ps.16': 11,
                       'Ps.111': 10, 'Ps.110': 7, 'Ps.113': 9, 'Ps.112': 10, 'Ps.115': 18, 'Ps.114': 8, 'Ps.117': 2,
                       'Ps.116': 19, 'Ps.119': 176, 'Ps.118': 29, 'Gal.5': 26, 'Gal.4': 31, 'Gal.3': 29, 'Jer.2': 37,
                       'Gal.1': 24, 'Amos.8': 14, 'Amos.9': 15, 'Jer.3': 25, 'Lam.3': 66, 'Acts.16': 40, 'Jer.4': 31,
                       'Dan.11': 45, 'Lam.2': 22, '1Kgs.21': 29, '1Kgs.20': 43, 'Amos.6': 14, '1Kgs.22': 53,
                       '2Sam.7': 29, '2Kgs.2': 25, '2Kgs.1': 18, '2Sam.4': 12, '2Kgs.7': 20, '2Kgs.6': 33, '2Kgs.5': 27,
                       '2Kgs.4': 44, 'Acts.13': 52, '2Kgs.9': 37, '2Kgs.8': 29, '2Sam.9': 13, '2Sam.8': 18,
                       '2Tim.4': 22,
                       'Jer.8': 22, 'Heb.12': 29, 'Heb.13': 25, 'Acts.11': 30, 'Jer.9': 26, 'Acts.10': 48, 'Ps.108': 13,
                       'Ps.109': 31, 'Jer.1': 19, '2Kgs.19': 37, '2Kgs.18': 37, 'Acts.28': 31, '2Kgs.13': 25,
                       '2Kgs.12': 21, '2Kgs.11': 21, '2Kgs.10': 36, '2Kgs.17': 41, '2Kgs.16': 20, '2Kgs.15': 38,
                       '2Kgs.14': 29, 'Jude.1': 25, 'Exod.38': 31, 'Exod.39': 43, 'Exod.36': 38, 'Exod.37': 29,
                       'Exod.34': 35, 'Exod.35': 35, 'Exod.32': 35, 'Exod.33': 23, 'Exod.30': 38, 'Exod.31': 18,
                       'Col.4': 18, 'Jer.52': 34, 'Jer.50': 46, 'Jer.51': 64, 'Rev.5': 14}

LAST_CHAPTERS = {'Jer': 52, 'Ps': 150, 'Matt': 28, 'Obad': 1, 'Phlm': 1, 'Neh': 13, 'Ezek': 48, 'Prov': 31, '1Sam': 31,
                 'Acts': 28, 'Josh': 24, 'Jas': 5, 'Hag': 2, 'Hos': 14, 'Heb': 13, 'Deut': 34, 'Ruth': 4, 'Titus': 3,
                 'Lam': 5, '2Sam': 24, '2Tim': 4, '2Cor': 13, 'Song': 8, 'Luke': 24, 'Dan': 12, '1Cor': 16, 'Jonah': 4,
                 'Gal': 6, 'Job': 42, '2Chr': 36, '3John': 1, 'Lev': 27, '1Pet': 5, '1Kgs': 22, '2Thess': 3, 'Gen': 50,
                 'Exod': 40, 'Col': 4, '1John': 5, 'Rev': 22, 'Joel': 3, 'Phil': 4, 'Judg': 21, '1Tim': 6, 'Jude': 1,
                 '2John': 1, 'Mic': 7, 'Hab': 3, 'John': 21, 'Eph': 6, 'Amos': 9, 'Isa': 66, 'Mark': 16, 'Eccl': 12,
                 'Nah': 3, 'Ezra': 10, 'Rom': 16, '2Kgs': 25, '2Pet': 3, 'Esth': 10, 'Mal': 4, 'Num': 36, 'Zech': 14,
                 '1Thess': 5, '1Chr': 29, 'Zeph': 3}
