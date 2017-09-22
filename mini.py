import os
import tinify
import sys

tinify.key = 'L5CUibYkX6PkzMT1mkQAzOwc5WVD3fHN'


def compress(input_file):
    before_size = os.path.getsize(input_file) / 1000

    tinify.from_file(input_file).to_file(input_file)

    after_size = os.path.getsize(input_file) / 1000

    print 'convert %s %dkb =======> %dkb' % (input_file, before_size, after_size)


files = set([sys.argv[i] for i in range(1, sys.argv.__len__())])

for file in files:
    compress(file)
