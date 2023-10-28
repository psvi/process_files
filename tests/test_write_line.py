from process_files import write_line, Line


def test_write_lines_00(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        write_line(fp, Line('', 0))

    with open(filename, 'r') as fp:
        assert fp.read() == ''


def test_write_lines_01(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        write_line(fp, Line('', 1))

    with open(filename, 'r') as fp:
        assert fp.read() == '\n'


def test_write_lines_02(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        write_line(fp, Line('', 2))

    with open(filename, 'r') as fp:
        assert fp.read() == '\n' * 2


def test_write_lines_03(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        write_line(fp, Line('a', 1))

    with open(filename, 'r') as fp:
        assert fp.read() == 'a\n'


def test_write_lines_04(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        write_line(fp, Line('a', 2))

    with open(filename, 'r') as fp:
        assert fp.read() == 'a\n' * 2


def test_write_lines_05(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        write_line(fp, Line('a', 1))
        write_line(fp, Line('b', 2))
        write_line(fp, Line('c', 3))

    with open(filename, 'r') as fp:
        assert fp.read() == 'a\n'*1 + 'b\n'*2 + 'c\n'*3
