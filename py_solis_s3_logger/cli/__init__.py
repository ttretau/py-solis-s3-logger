# SPDX-FileCopyrightText: 2023-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT
import click
import logging
import os
from ..__about__ import __version__
from ..publisher import publish_loop
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='Py Solis S3 Logger')
@click.pass_context
def py_solis_s3_logger(ctx: click.Context):
    click.echo('Publish Solis power..')
    publish_loop()