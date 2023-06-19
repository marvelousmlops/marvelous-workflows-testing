# Reusable workflows testing

Integration testing for marvelous-workflows repository: https://github.com/marvelousmlops/marvelous-workflows

Since marvelous-workflows workflows and actions are meant to be used in other repository,
the only way to do proper integration testing is by running the workflows in other repository.


## Workflows

### test_dbx_reusableworkflow.yml 

This workflow is intended to run on workflow dispatch. 
It is used to test databricks_job_dbx.yml workflow from marvelous-workflows repository.
Per default it uses master branch of marvelous-workflows.
Unfortunately, it is not possible to parametritize the branch of marvelous-workflows that we want to test.
To test any other branch of marvelous-workflows rather than master, a feature branch of marvelous-workflows-testing 
should be created with a different branch reference for the marvelous-workflows workflows.

## What exactly do we test?
There is a python file that need to run succesfully on Databricks for workflows mentioned above to be succesful:
- scripts/test_dbx_job.py

When one of the marvelous-workflows-testing workflows is dispatched, 
run of those python files is triggered via the following Databricks job definitions:
- scripts/test_dbx_job.py

marvelous-workflows uploads python scripts, wheels to dbfs,
adjusts Databricks job definition by adding libraries, 
adding arguments to python scripts ({{run_id}}, {{job_id}}) 
and environment variables: GIT_TAG, PROJECT_NAME
