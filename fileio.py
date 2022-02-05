import json
import io

try:
  to_unicode = unicode
except NameError:
  to_unicode = str

def writeFile(fileName, data):
  with io.open(fileName, 'w', encoding='utf-8') as writeFile:
    str_ = json.dumps(data, indent=4, sort_keys=True,
                        separators=(',', ': '), ensure_ascii=False)
    writeFile.write(to_unicode(str_))


def readFile(fileName):
  try:
    f = io.open(fileName, 'r', encoding='utf-8')
  except OSError:
    return []
  with f as readFile:
      data = json.load(readFile)
      return data
   