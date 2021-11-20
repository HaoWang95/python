"""
    This is the module documentation for use_docstr.py
"""

class DocTest:
    """
    This is a doc string testing for class DocTest
    """
    pass


def docfunc():
    """
    This is a doc string testing for function docfunc
    :return: None
    """
    pass


if __name__ == '__main__':
    print(__doc__)
    print(DocTest.__doc__)
    print(docfunc.__doc__)