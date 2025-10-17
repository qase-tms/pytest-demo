# qase-pytest

This is an example repository with tests in the `tests/examples/` directory. To run the tests :

### Compatibility

As of this release, Python 3.7 and 3.8 are no longer supported.
The supported Python versions are:
3.9, 3.10, 3.11, 3.12, and 3.13.

1. Clone the repository with `git clone https://github.com/cskmnrpt/qase-pytest.git`.
   To clone a different branch, other than `main`, use this command - <br> `git clone --single-branch --branch <branch-name> https://github.com/cskmnrpt/qase-pytest.git`

2. Create and use a virtual environment:
   a. Create a virtual environment with `virtualenv venv`, and activate it with `source venv/bin/activate`.
      Run `pip install -r requirements.txt` from the root of this repository to install dependencies.
 
   b. Or, use [pipenv](https://realpython.com/pipenv-guide/) to handle dependencies: Install `pipenv` with homebrew: 
      $ `brew install pipenv`
      $ `pipenv shell`
      $ `pipenv install`

3. Install the latest version of `chromedriver` with brew: $ `brew install chromedriver`
 
4. Install browsers, if you are using the `playwright` library: `playwright install`.

5. Create a `qase.config.json` in the root of the repository, and add your token, and project code.

6. Run `pytest`.

## New Features & Configuration
### Test Run Tags
You can now add tags to test runs. Update your `qase.config.json` or pass tags via CLI:

```json
{
  "testops": {
    "tags": ["smoke", "regression"]
  }
}
```
#### Environment variable example:
```bash
export QASE_TESTOPS_RUN_TAGS="smoke,regression"
```
#### CLI flag example:
```bash
pytest --qase-testops-run-tags "smoke,regression"
```
### Excluding Parameters from Results

Specify parameters to exclude from results:
```json
{
  "testops": {
    "exclude_parameters": ["browser", "environment"]
  }
}
```
#### Environment variable example:
```bash
export QASE_EXCLUDE_PARAMS="browser,environment"
```
#### CLI flag example:
```bash
pytest --qase-exclude-params "browser,environment"
```
### Test Run Configurations
You can specify configurations for test runs via `qase.config.json`, environment variables, or CLI flags.
Example `qase.config.json`:
```json
{
  "testops": {
    "configurations": {
      "values": [
        {
          "name": "browser",
          "value": "chrome"
        },
        {
          "name": "environment",
          "value": "staging"
        }
      ],
      "createIfNotExists": true
    }
  }
}
```

#### Environment variable example:
```bash
export QASE_TESTOPS_CONFIGURATIONS_VALUES="browser=chrome,environment=staging"
```
#### CLI flag example:
```bash
pytest --qase-testops-configurations-values "browser=chrome,environment=staging"
```
`Notes:`
- Format: "group1=value1,group2=value2"
- Use createIfNotExists: true in your config file to automatically create configurations in Qase if they don’t exist.
- If not set, no configurations will be added.

### Filtering Test Results by Status
```json
{
  "testops": {
    "statusFilter": ["passed", "failed"]
  }
}
```
#### Environment variable example:
```bash
export QASE_TESTOPS_STATUS_FILTER="passed,failed"
```
#### CLI flag example:
```bash
pytest --qase-testops-status-filter "passed,failed"
```
### Status Mapping
You can filter which results to send based on status:
```json
{
  "statusMapping": {
    "invalid": "failed",
    "skipped": "passed"
  }
}
```
#### Environment variable example:
```bash
export QASE_STATUS_MAPPING="invalid=failed,skipped=passed"
```
#### CLI flag example:
```bash
pytest --qase-status-mapping="invalid=failed,skipped=passed"
```
More details: Status Mapping [Docs](https://github.com/qase-tms/qase-python/blob/main/qase-python-commons/docs/STATUS_MAPPING.md)

---
