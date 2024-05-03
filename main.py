from providers.data.DataProvider import DataProvider

def main ():
    data_provider = DataProvider()
    
    data_provider.add_data('test', 'test')
    print(data_provider.get_data('test'))

if __name__ == '__main__':
    main()