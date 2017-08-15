class Custom:
    def __init__(self):
        print('Init method.')

    def __new__(cls,*args,**kwargs):
        print('New Instance.')
        return object.__new__(cls,*args,**kwargs)

if __name__ == '__main__':
    Custom()