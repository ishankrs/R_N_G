from funkybob import UniqueRandomNameGenerator
print("random name generator with 16k random names")
numbers_of= int(input("how many random names"))

def print_names(generator, count=numbers_of):
    for name in generator[:count]:
        print('  -', name)
    print()


print('Random names:')
generator = UniqueRandomNameGenerator()
print_names(generator)
