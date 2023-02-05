def make_shirt(size='L', message='I love python'):
    print(f'T-shirt size:{size}\nT-shirt message:{message}')


def describe_city(city_name, country='India'):
    print(f'{city_name} is in {country}')


# positional arguments
make_shirt('L', 'Mambu')

# keyword arguments
make_shirt(size='M', message='Mambu 2.0')

make_shirt()
make_shirt(size='M')
make_shirt()

describe_city('Trichy')
describe_city('Brisbane', 'Australia')
