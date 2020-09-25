#! /usr/bin/env python3
# coding: utf-8


def launch_analysis(data_file):
    try:
        with open(data_file, "r") as f:
            print(f.readline())
    except FileNotFoundError as e:
        print("File not found - '{}'".format(e))
        return


if __name__ == "__main__":
    launch_analysis('current_mps.csv')