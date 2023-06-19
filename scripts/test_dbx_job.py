import os
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description='reads default arguments')
    parser.add_argument('--run_id', metavar='run_id', type=str, help='Databricks run id')
    parser.add_argument('--job_id', metavar='job_id', type=str, help='Databricks job id')

    args = parser.parse_args()
    return args.run_id, args.job_id


run_id, job_id = get_arguments()
print(f"Run id: {run_id}, job_id: {job_id}.")
print("Successfully ran test_dbx_job.py.")