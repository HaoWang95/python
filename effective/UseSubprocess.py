import subprocess

if __name__ == '__main__':
    '''
    For running under Windows, shell=True must be set.
    '''
    result = subprocess.run('dir', shell=True, capture_output= True, text= True)
    print(result.stdout)
