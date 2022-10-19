import argparse
import os

def testfunc():
    print("this is a test function")
    os.system('ls -l')




if __name__ == '__main__':
    description_text = '''
    Useful script to help configure Ubuntu machines 
    '''

    example_text = '''
    some example text goes here
    '''

    parser = argparse.ArgumentParser(description=description_text,
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-v',
                        '--verbose',
                        help='verbose output',
                        default=None)

    args = parser.parse_args()

    testfunc()

