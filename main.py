#! /usr/bin/env python3
# coding: utf-8

import argparse
import analysis.csv_analysis as csv
import analysis.xml_analysis as xml
import parliamentMembers

from os import path


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""
                        type of file to analyses. Can be CSV or XML""")
    parser.add_argument("-f", "--file", help="""
    the location of the file to be parsed
    """)
    return parser.parse_args()


def parse_csv(file):
    print("parsing as CSV")
    data = csv.launch_analysis(file)
    pms = parliamentMembers.SetOfParliamentMembers("")
    pms.data_from_dataframe(data)
    result = pms.split_by_politcal_parties()
    pms.display_chart()
    return result


def main():
    args = parse_arguments()
    directory = path.dirname(__file__)
    path_to_file = path.join(directory, "data", args.file)
    if args.extension.upper() == 'XML':
        print("parsing as XML")
        xml.launch_analysis(path_to_file)
    elif args.extension.upper() == 'CSV':
        print(parse_csv(path_to_file))


if __name__ == "__main__":
    main()
