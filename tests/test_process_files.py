import pytest

from process_files import process_files


@pytest.fixture
def empty_file(tmp_path):
    filename = tmp_path / 'empty.txt'
    with open(filename, 'w') as fp:
        fp.write('')
    return filename


@pytest.fixture
def oneline_file(tmp_path):
    filename = tmp_path / 'oneline.txt'
    with open(filename, 'w') as fp:
        fp.write('a')
    return filename


@pytest.fixture
def twoline_file_00(tmp_path):
    filename = tmp_path / 'twoline_00.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('a')
    return filename


@pytest.fixture
def twoline_file_01(tmp_path):
    filename = tmp_path / 'twoline_01.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('b')
    return filename


@pytest.fixture
def twoline_file_02(tmp_path):
    filename = tmp_path / 'twoline_02.txt'
    with open(filename, 'w') as fp:
        fp.write('b\n')
        fp.write('a')
    return filename


@pytest.fixture
def multiline_file_00(tmp_path):
    filename = tmp_path / 'multiline_00.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('b\n' * 2)
        fp.write('c\n' * 3)
        fp.write('d\n' * 4)
        fp.write('e\n' * 5)
    return filename


@pytest.fixture
def multiline_file_01(tmp_path):
    filename = tmp_path / 'multiline_01.txt'
    with open(filename, 'w') as fp:
        fp.write('e\n' * 5)
        fp.write('d\n' * 4)
        fp.write('c\n' * 3)
        fp.write('b\n' * 2)
        fp.write('a\n')
    return filename


@pytest.fixture
def multiline_file_02(tmp_path):
    filename = tmp_path / 'multiline_02.txt'
    with open(filename, 'w') as fp:
        fp.write('d\n' * 4)
        fp.write('e\n' * 3)
        fp.write('k\n' * 2)
        fp.write('n\n' * 5)
        fp.write('t\n')
        fp.write('x\n' * 3)
        fp.write('z\n' * 5)
    return filename


@pytest.fixture
def multiline_file_03(tmp_path):
    filename = tmp_path / 'multiline_03.txt'
    with open(filename, 'w') as fp:
        fp.write('z\n' * 5)
        fp.write('x\n' * 3)
        fp.write('t\n')
        fp.write('n\n' * 5)
        fp.write('k\n' * 2)
        fp.write('e\n' * 3)
        fp.write('d\n' * 4)
    return filename


@pytest.fixture
def foo_file(tmp_path):
    filename = tmp_path / 'foo.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('b\n')
        fp.write('d\n')
        fp.write('e\n' * 2)
        fp.write('t\n')
        fp.write('z\n' * 5)
    return filename


@pytest.fixture
def bar_file(tmp_path):
    filename = tmp_path / 'bar.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('b\n')
        fp.write('e\n' * 2)
        fp.write('x\n' * 5)
        fp.write('z\n' * 3)
    return filename


def test_process_files_00(empty_file, tmp_path):
    """ empty_file: ''
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(empty_file, empty_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == ''


def test_process_files_01(empty_file, oneline_file, tmp_path):
    """ empty_file: ''
        oneline_file: 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(empty_file, oneline_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == 'a\n'


def test_process_files_02(oneline_file, empty_file, tmp_path):
    """ oneline_file: 'a'
        empty_file: ''
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(oneline_file, empty_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'a\n'
        assert fp2.read() == ''


def test_process_files_03(oneline_file, tmp_path):
    """ oneline_file: 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(oneline_file, oneline_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == ''


def test_process_files_04(empty_file, twoline_file_00, tmp_path):
    """ empty_file: ''
        twoline_file_00: 'a\n' + 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(empty_file, twoline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == 'a\n' * 2


def test_process_files_05(twoline_file_00, empty_file, tmp_path):
    """ twoline_file_00: 'a\n' + 'a'
        empty_file: ''
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_00, empty_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'a\n' * 2
        assert fp2.read() == ''


def test_process_files_06(twoline_file_00, tmp_path):
    """ twoline_file_00: 'a\n' + 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_00, twoline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == ''


def test_process_files_07(empty_file, twoline_file_01, tmp_path):
    """ empty_file: ''
        twoline_file_01: 'a\n' + 'b'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(empty_file, twoline_file_01, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == 'a\n' + 'b\n'


def test_process_files_08(twoline_file_01, empty_file, tmp_path):
    """ twoline_file_01: 'a\n' + 'b'
        empty_file: ''
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_01, empty_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'a\n' + 'b\n'
        assert fp2.read() == ''


def test_process_files_09(twoline_file_01, tmp_path):
    """ twoline_file_01: 'a\n' + 'b'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_01, twoline_file_01, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == ''


def test_process_files_10(twoline_file_00, twoline_file_01, tmp_path):
    """ twoline_file_00: 'a\n' + 'a'
        twoline_file_01: 'a\n' + 'b'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_00, twoline_file_01, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == 'b\n'


def test_process_files_11(twoline_file_02, twoline_file_00, tmp_path):
    """ twoline_file_02: 'b\n' + 'a'
        twoline_file_00: 'a\n' + 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_02, twoline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'b\n'
        assert fp2.read() == ''


def test_process_files_12(empty_file, multiline_file_00, tmp_path):
    """ empty_file: ''
        multiline_file_00: 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(empty_file, multiline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5


def test_process_files_13(multiline_file_00, empty_file, tmp_path):
    """ multiline_file_00: 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5
        empty_file: ''
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_00, empty_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5
        assert fp2.read() == ''


def test_process_files_14(oneline_file, multiline_file_00, tmp_path):
    """ oneline_file: 'a'
        multiline_file_00: 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(oneline_file, multiline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5


def test_process_files_15(multiline_file_01, oneline_file, tmp_path):
    """ multiline_file_01: 'e\n'*5 + 'd\n'*4 + 'c\n'*3 + 'b\n'*2 + 'a\n'
        oneline_file: 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_01, oneline_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'e\n'*5 + 'd\n'*4 + 'c\n'*3 + 'b\n'*2
        assert fp2.read() == ''


def test_process_files_16(twoline_file_00, multiline_file_00, tmp_path):
    """ twoline_file_00: 'a\n' + 'a'
        multiline_file_00: 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_00, multiline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5


def test_process_files_17(multiline_file_01, twoline_file_00, tmp_path):
    """ multiline_file_01: 'e\n'*5 + 'd\n'*4 + 'c\n'*3 + 'b\n'*2 + 'a\n'
        twoline_file_00: 'a\n' + 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_01, twoline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'e\n'*5 + 'd\n'*4 + 'c\n'*3 + 'b\n'*2
        assert fp2.read() == ''


def test_process_files_18(twoline_file_01, multiline_file_00, tmp_path):
    """ twoline_file_01: 'a\n' + 'b'
        multiline_file_00: 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_01, multiline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == ''
        assert fp2.read() == 'c\n'*3 + 'd\n'*4 + 'e\n'*5


def test_process_files_19(multiline_file_01, twoline_file_02, tmp_path):
    """ multiline_file_01: 'e\n'*5 + 'd\n'*4 + 'c\n'*3 + 'b\n'*2 + 'a\n'
        twoline_file_02: 'b\n' + 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_01, twoline_file_02, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'e\n'*5 + 'd\n'*4 + 'c\n'*3
        assert fp2.read() == ''


def test_process_files_20(multiline_file_00, multiline_file_02, tmp_path):
    """ multiline_file_00: 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5
        multiline_file_02: 'd\n'*4 + 'e\n'*3 + 'k\n'*2 + 'n\n'*5 + 't\n' +
                           'x\n'*3 + 'z\n'*5
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_00, multiline_file_02, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'a\n' + 'b\n'*2 + 'c\n'*3
        assert fp2.read() == 'k\n'*2 + 'n\n'*5 + 't\n' + 'x\n'*3 + 'z\n'*5


def test_process_files_21(multiline_file_02, multiline_file_00, tmp_path):
    """ multiline_file_02: 'd\n'*4 + 'e\n'*3 + 'k\n'*2 + 'n\n'*5 + 't\n' +
                           'x\n'*3 + 'z\n'*5
        multiline_file_00: 'a\n' + 'b\n'*2 + 'c\n'*3 + 'd\n'*4 + 'e\n'*5
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_02, multiline_file_00, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'k\n'*2 + 'n\n'*5 + 't\n' + 'x\n'*3 + 'z\n'*5
        assert fp2.read() == 'a\n' + 'b\n'*2 + 'c\n'*3


def test_process_files_22(multiline_file_01, multiline_file_03, tmp_path):
    """ multiline_file_01: 'e\n'*5 + 'd\n'*4 + 'c\n'*3 + 'b\n'*2 + 'a\n'
        multiline_file_03: 'z\n'*5 + 'x\n'*3 + 't\n' + 'n\n'*5 + 'k\n'*2 +
                           'e\n'*3 + 'd\n'*4
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_01, multiline_file_03, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'c\n'*3 + 'b\n'*2 + 'a\n'
        assert fp2.read() == 'z\n'*5 + 'x\n'*3 + 't\n' + 'n\n'*5 + 'k\n'*2


def test_process_files_23(multiline_file_03, multiline_file_01, tmp_path):
    """ multiline_file_03: 'z\n'*5 + 'x\n'*3 + 't\n' + 'n\n'*5 + 'k\n'*2 +
                           'e\n'*3 + 'd\n'*4
        multiline_file_01: 'e\n'*5 + 'd\n'*4 + 'c\n'*3 + 'b\n'*2 + 'a\n'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_03, multiline_file_01, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'z\n'*5 + 'x\n'*3 + 't\n' + 'n\n'*5 + 'k\n'*2
        assert fp2.read() == 'c\n'*3 + 'b\n'*2 + 'a\n'


def test_process_files_24(twoline_file_01, multiline_file_02, tmp_path):
    """ twoline_file_01: 'a\n' + 'b'
        multiline_file_02: 'd\n'*4 + 'e\n'*3 + 'k\n'*2 + 'n\n'*5 + 't\n' +
                           'x\n'*3 + 'z\n'*5
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_01, multiline_file_02, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'a\n' + 'b\n'
        assert fp2.read() == 'd\n'*4 + 'e\n'*3 + 'k\n'*2 + 'n\n'*5 + 't\n' + \
                             'x\n'*3 + 'z\n'*5


def test_process_files_25(multiline_file_02, twoline_file_01, tmp_path):
    """ multiline_file_02: 'd\n'*4 + 'e\n'*3 + 'k\n'*2 + 'n\n'*5 + 't\n' +
                           'x\n'*3 + 'z\n'*5
        twoline_file_01: 'a\n' + 'b'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_02, twoline_file_01, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'd\n'*4 + 'e\n'*3 + 'k\n'*2 + 'n\n'*5 + 't\n' + \
                             'x\n'*3 + 'z\n'*5
        assert fp2.read() == 'a\n' + 'b\n'


def test_process_files_26(twoline_file_02, multiline_file_03, tmp_path):
    """ twoline_file_02: 'b\n' + 'a'
        multiline_file_03: 'z\n'*5 + 'x\n'*3 + 't\n' + 'n\n'*5 + 'k\n'*2 +
                           'e\n'*3 + 'd\n'*4
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(twoline_file_02, multiline_file_03, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'b\n' + 'a\n'
        assert fp2.read() == 'z\n'*5 + 'x\n'*3 + 't\n' + 'n\n'*5 + \
                             'k\n'*2 + 'e\n'*3 + 'd\n'*4


def test_process_files_27(multiline_file_03, twoline_file_02, tmp_path):
    """ multiline_file_03: 'z\n'*5 + 'x\n'*3 + 't\n' + 'n\n'*5 + 'k\n'*2 +
                           'e\n'*3 + 'd\n'*4
        twoline_file_02: 'b\n' + 'a'
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(multiline_file_03, twoline_file_02, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'z\n'*5 + 'x\n'*3 + 't\n' + 'n\n'*5 + \
                             'k\n'*2 + 'e\n'*3 + 'd\n'*4
        assert fp2.read() == 'b\n' + 'a\n'


def test_process_files_28(foo_file, bar_file, tmp_path):
    """ foo_file: 'a\n' + 'b\n' + 'd\n' + 'e\n'*2 + 't\n' + 'z\n'*5
        bar_file: 'a\n' + 'b\n' + 'e\n'*2 + 'x\n'*5 + 'z\n'*3
    """
    filename1 = tmp_path / 'file1.txt.out'
    filename2 = tmp_path / 'file2.txt.out'

    process_files(foo_file, bar_file, filename1, filename2)

    with open(filename1, 'r') as fp1, open(filename2, 'r') as fp2:
        assert fp1.read() == 'd\n' + 't\n'
        assert fp2.read() == 'x\n' * 5
