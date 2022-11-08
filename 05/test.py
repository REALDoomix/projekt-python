import files as f
import sys

text = f.textfile_read(sys.argv[1])
print(text)
f.textfile_write(sys.argv[2], text=text)