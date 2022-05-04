import subprocess


# use subprocess

def run_subprocess(command):
    result = subprocess.run(
        [command],
        capture_output=True,
        encoding='utf-8'
    )
    result.check_returncode()
    print(result.stdout)


if __name__ == '__main__':
    run_subprocess('whoami')
