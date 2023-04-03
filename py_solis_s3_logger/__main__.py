# SPDX-FileCopyrightText: 2023-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == '__main__':
    from .cli import py_solis_s3_logger

    sys.exit(py_solis_s3_logger())
