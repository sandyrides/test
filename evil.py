import sys
import StringIO

s = StringIO.StringIO()

sys.stdout = s

sys.stderr.write('It actually went to a StringIO object, I will show you now:\n')
sys.stderr.write(s.getvalue())