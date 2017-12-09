
#cimportはcython版のヘッダーファイルを読み込む命令
cimport numpy as np

# mindwave用に作成した値をごにょごにょする関数を呼び出しておく
cdef extern from "cython_c_code.h":
    int add(int x, int y)


# ここのdefはpythonの関数となる。c言語の関数とは名前を異なるようにつける
def py_add(a, b):
    return add(a, b)