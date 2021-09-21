import argparse

parse = argparse.ArgumentParser()

parse.add_argument('-s', action='store', dest='simple_val', help='store simple value')
parse.add_argument('-c', action='store_const', dest='const_val', const='10000', help='store constant value')
parse.add_argument('-t', action='store_true', default=False, dest='boolean_switch',
                   help='set a switch to true')
parse.add_argument('-f', action='store_false', default=False, dest='boolean switch',
                   help='set a switch to false')
parse.add_argument('-a', action='append', dest='collection', default=[],
                   help='add repeated values to list')
parse.add_argument('-A', action='append_const', dest='const_collection',
                   const='100000', help='Add diff values to list')
parse.add_argument('--version', action='version', version='1.0')

result = parse.parse_args()
print('simple_val = ', result.simple_val)
print('const_val = ', result.const_val)
print('boolean switch= ', result.boolean_switch)
print('collection = ', result.collection)
print('const_collection = ', result.const_collection)