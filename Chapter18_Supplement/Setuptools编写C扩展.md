# Setuptools编写C扩展

## 源文件准备

palindrome.c, palindrome.i, setup.py

## 运行 Setuptools

    ```bash
    python setup.py build_ext --inplace
    ```

生成文件:_palindrome.cpython-38-aarch64-linux-gnu.so,palindrome.py,palindrome_wrap.c
生成文件夹:
build __pycache__

## 模块测试

test.ipynb
