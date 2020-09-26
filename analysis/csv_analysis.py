#! /usr/bin/env python3
# coding: utf-8

import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG)


def launch_analysis(data_file):
    try:
        mps = pd.read_csv(data_file, sep=";")
    except FileNotFoundError as e:
        logging.critical("File not found - '{}'".format(e))
    return mps
