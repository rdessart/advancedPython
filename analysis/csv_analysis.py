#! /usr/bin/env python3
# coding: utf-8

import logging

logging.basicConfig(level=logging.DEBUG)


def launch_analysis(data_file):
    try:
        with open(data_file, "r") as f:
            logging.debug(f.readline())
    except FileNotFoundError as e:
        logging.critical("File not found - '{}'".format(e))
        return
