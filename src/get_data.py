# Read the params
# Process it
# Return dataframe

import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path, "r") as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    # print(df.head())
    return df
    # extra comment to trigger dvc workflow again as it will make changes in md5 & size of file wrt dvc.lock
    # and retrigger workflow using cmd: dvc repro
    # running again after making changes in split_data.py file


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)
