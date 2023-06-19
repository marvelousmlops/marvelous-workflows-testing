# GSO ML Toolkit Testing

Integration testing for gso-ml-toolkit repository: https://github.com/RoyalAholdDelhaize/gso-ml-toolkit

Since gso-ml-toolkit workflows and actions are meant to be used in other repository,
the only way to do proper integration testing is by running the workflows in other repository.

We test number of input options and check whether those resulted in succesful Databricks run.

## Workflows

### test_gso_ml_toolkit.yml 

This workflow is intended to run on workflow dispatch. 
It is used to test databricks_job.yml workflow from gso-ml-toolkit repository.
Per default it uses master branch of gso-ml-toolkit.
Unfortunately, it is not possible to parametritize the branch of gso-ml-toolkit that we want to test.
To test any other branch of gso-ml-toolkit rather than master, a feature branch of gso-ml-toolkit-testing 
should be created with a different branch reference for the gso-ml-toolkit workflows.

### test_gso_ml_toolkit_by_ref.yml

This workflow is intended to run on workflow dispatch or can be triggered
via dispatch_testing.yml workflow of gso-ml-toolkit:
https://github.com/RoyalAholdDelhaize/gso-ml-toolkit/blob/master/.github/workflows/dispatch_testing.yml


This workflow is intended to test reusable actions from gso-ml-toolkit and not the workflows.
To test the workflows, test_gso_ml_toolkit.yml should be used.

## What exactly do we test?
There are 4 python files that need to run succesfully on Databricks for workflows mentioned above to be succesful:
- test_no_extra_input.py
- test_single_input.py
- test_multiple_input.py
- test_setup_file.py

When one of the gso-ml-toolkit-testing workflows is dispatched, 
run of those python files is triggered via the following Databricks job definitions:
- test_no_extra_input.json
- test_single_input.json
- test_multiple_input.json
- test_setup_file.json

Gso-ml-toolkit uploads python scripts, extra files (config.yml, config2.yml) to dbfs,
build and uploads the wheels for RoyalAholdDelhaize packages to dbfs, 
adjusts Databricks job definition by adding libraries, 
adding arguments to python scripts ({{run_id}}, {{job_id}}) 
and environment variables: GIT_TAG, PROJECT_NAME + environment variables defined in the workflow call

In gso-ml-toolkit we test whether arguments, environment variables, packages and extra files are accessible during the run.
