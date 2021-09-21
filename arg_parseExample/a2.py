import argparse

parse = argparse.ArgumentParser(description='example')

parse.add_argument('count', action='store', type=int)
parse.add_argument('units', action='store')
parse.add_argument('calories', action='store', type=int)

print(parse.parse_args())