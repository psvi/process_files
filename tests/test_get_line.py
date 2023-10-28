import pytest

from process_files import get_line, Line


def test_empty_file(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('')

    lines = get_line(filename)

    with pytest.raises(StopIteration):
        next(lines)


def test_file_00(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('\n')

    lines = get_line(filename)

    assert next(lines) == Line('', 1)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_01(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('\n')
        fp.write('\n')

    lines = get_line(filename)

    assert next(lines) == Line('', 2)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_02(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')

    lines = get_line(filename)

    assert next(lines) == Line('a', 1)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_03(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('a')

    lines = get_line(filename)

    assert next(lines) == Line('a', 1)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_04(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('a\n')

    lines = get_line(filename)

    assert next(lines) == Line('a', 2)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_05(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('a')

    lines = get_line(filename)

    assert next(lines) == Line('a', 2)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_06(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('b\n')

    lines = get_line(filename)

    assert next(lines) == Line('a', 1)
    assert next(lines) == Line('b', 1)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_07(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('a\n')
        fp.write('b\n')

    lines = get_line(filename)

    assert next(lines) == Line('a', 2)
    assert next(lines) == Line('b', 1)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_08(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('a\n')
        fp.write('b\n')
        fp.write('b\n')

    lines = get_line(filename)

    assert next(lines) == Line('a', 2)
    assert next(lines) == Line('b', 2)
    with pytest.raises(StopIteration):
        next(lines)


def test_file_09(tmp_path):
    filename = tmp_path / 'file.txt'
    with open(filename, 'w') as fp:
        fp.write('a\n')
        fp.write('b\n')
        fp.write('b\n')

    lines = get_line(filename)

    assert next(lines) == Line('a', 1)
    assert next(lines) == Line('b', 2)
    with pytest.raises(StopIteration):
        next(lines)
