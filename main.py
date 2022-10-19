import argparse
import subprocess



def run_a_command(arguments):
    print('running command: %s' % arguments)
    process = subprocess.run(arguments, 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
    print(process)


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

    run_a_command(['ls', '-l'])

