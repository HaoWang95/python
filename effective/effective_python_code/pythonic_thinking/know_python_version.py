"""
As a programmer, developer, or a cs/software/other related university student,
it is a basic to check the version of your development environment. That can be your Java version, C# version,
C and C++ supported version(and the corresponding compiler version) or your JavaScript version.

The most convenient way to determine this is -> cmd/PowerShell/shell -> python --version

Take away note:
1. Python 3 is the most up-to-date and well-supported version
2. Avoid Python 2, because Python 2 is no longer maintained after Jan 1, 2020.
"""
import sys

if __name__ == '__main__':
    print(sys.version)
    # print(sys.version_info)
    # print(sys.path)
    # print(sys.platform)
