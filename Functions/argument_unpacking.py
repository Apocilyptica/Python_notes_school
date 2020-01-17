# Default unpacking is *args, it get returned as a Tuple
def greeting(*args):
    print('Hi ' + ' '.join(args))
    print(args)


greeting('Tiffany', 'Hudgens')
greeting('Kristine', 'M', 'Hudgens')

def greeting(time_of_day, *args):
    print(f"Hi {'-'.join(args)}, I hope that you are having a good {time_of_day}")
    print(args)


greeting('Morning', 'Tiffany', 'Hudgens')
greeting('Afternoon', 'Kristine', 'M', 'Hudgens')