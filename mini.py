import os
import tinify
import sys

tinify.key = 'L5CUibYkX6PkzMT1mkQAzOwc5WVD3fHN'

input_file = sys.argv[1]

before_size = os.path.getsize(input_file) / 1000

tinify.from_file(sys.argv[1]).to_file(sys.argv[1])

after_size = os.path.getsize(input_file) / 1000

print 'convert %s %dkb =======> %dkb' %(input_file, before_size, after_size)