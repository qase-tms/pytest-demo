# Qase Pytest Reporter Variables

This page lists all available variables for the Qase pytest reporter. These variables can be configured using either the `qase.config.json` file or environment variables.

---

## Common

| Description | Config file | Environment variable | Default value | Required | Possible values |
|-------------|------------|--------------------|---------------|----------|----------------|
| Mode of reporter | mode | QASE_MODE | off | No | testops, report, off |
| Fallback mode of reporter | fallback | QASE_FALLBACK | off | No | testops, report, off |
| Environment | environment | QASE_ENVIRONMENT | undefined | No | Any string |
| Root suite | rootSuite | QASE_ROOT_SUITE | undefined | No | Any string |
| Enable debug logs | debug | QASE_DEBUG | False | No | True, False |
| Enable capture logs from stdout and stderr | testops.defect | QASE_CAPTURE_LOGS | False | No | True, False |
| Map test result statuses to different values (format: fromStatus=toStatus) | statusMapping | QASE_STATUS_MAPPING | undefined | No | Object mapping statuses (e.g., {"invalid": "failed", "skipped": "passed"}) |

---

## Logging configuration

| Description | Config file | Environment variable | Default value | Required | Possible values |
|-------------|------------|--------------------|---------------|----------|----------------|
| Enable/disable console output for reporter logs | logging.console | QASE_LOGGING_CONSOLE | True | No | True, False |
| Enable/disable file output for reporter logs | logging.file | QASE_LOGGING_FILE | Same as debug setting | No | True, False |

---

## Qase Report configuration

| Description | Config file | Environment variable | Default value | Required | Possible values |
|-------------|------------|--------------------|---------------|----------|----------------|
| Driver used for report mode | report.driver | QASE_REPORT_DRIVER | local | No | local |
| Path to save the report | report.connection.path | QASE_REPORT_CONNECTION_PATH | ./build/qase-report | No | Any string |
| Local report format | report.connection.format | QASE_REPORT_CONNECTION_FORMAT | json | No | json, jsonp |

---

## Qase TestOps configuration

| Description | Config file | Environment variable | Default value | Required | Possible values |
|-------------|------------|--------------------|---------------|----------|----------------|
| Token for API access | testops.api.token | QASE_TESTOPS_API_TOKEN | undefined | Yes | Any string |
| Qase API host. For enterprise users, specify address: example.qase.io | testops.api.host | QASE_TESTOPS_API_HOST | qase.io | No | Any string |
| Qase enterprise environment | testops.api.enterprise | QASE_TESTOPS_API_ENTERPRISE | False | No | True, False |
| Code of your project, which you can take from the URL: https://app.qase.io/project/DEMOTR - DEMOTR is the project code | testops.project | QASE_TESTOPS_PROJECT | undefined | Yes | Any string |
| Qase test run ID | testops.run.id | QASE_TESTOPS_RUN_ID | undefined | No | Any integer |
| Qase test run title | testops.run.title | QASE_TESTOPS_RUN_TITLE | Automated run <Current date and time> | No | Any string |
| Qase test run description | testops.run.description | QASE_TESTOPS_RUN_DESCRIPTION | <Framework name> automated run | No | Any string |
| Qase test run complete | testops.run.complete | QASE_TESTOPS_RUN_COMPLETE | True | No | True, False |
| Array of tags to be added to the test run | testops.run.tags | QASE_TESTOPS_RUN_TAGS | [] | No | Array of strings |
| External link to associate with test run (e.g., Jira ticket) | testops.run.externalLink | QASE_TESTOPS_RUN_EXTERNAL_LINK | undefined | No | JSON object with type (jiraCloud or jiraServer) and link (e.g., PROJ-123) |
| Qase test plan ID | testops.plan.id | QASE_TESTOPS_PLAN_ID | undefined | No | Any integer |
| Size of batch for sending test results | testops.batch.size | QASE_TESTOPS_BATCH_SIZE | 200 | No | Any integer |
| Enable defects for failed test cases | testops.defect | QASE_TESTOPS_DEFECT | False | No | True, False |
| Enable/disable attachment uploads | testops.uploadAttachments | QASE_TESTOPS_UPLOAD_ATTACHMENTS | true | No | True, False |
| Filter test results by status (comma-separated list of statuses to exclude from reporting) | testops.statusFilter | QASE_TESTOPS_STATUS_FILTER | undefined | No | Array of strings (passed, failed, skipped, invalid) |
| Configuration values to create/find in groups (format: group1=value1,group2=value2) | testops.configurations.values | QASE_TESTOPS_CONFIGURATIONS_VALUES | undefined | No | Comma-separated key=value pairs |
| Create configuration groups if they don't exist | testops.configurations.createIfNotExists | QASE_TESTOPS_CONFIGURATIONS_CREATE_IF_NOT_EXISTS | false | No | True, False |
| Enable public report link generation and display after test run completion | testops.showPublicReportLink | QASE_TESTOPS_SHOW_PUBLIC_REPORT_LINK | False | No | True, False |

---

## Example `qase.config.json`

```json
{
  "mode": "testops",
  "fallback": "off",
  "environment": "undefined",
  "rootSuite": "undefined",
  "debug": false,
  "captureLogs": false,
  "statusMapping": {
    "invalid": "failed",
    "skipped": "passed"
  },
  "logging": {
    "console": true,
    "file": false
  },
  "report": {
    "driver": "local",
    "connection": {
      "path": "./build/qase-report",
      "format": "json"
    }
  },
  "testops": {
    "api": {
      "token": "YOUR_QASE_API_TOKEN",
      "host": "qase.io",
      "enterprise": false
    },
    "project": "YOUR_PROJECT_CODE",
    "run": {
      "id": 123,
      "title": "Automated run <Current date and time>",
      "description": "<Framework name> automated run",
      "complete": true,
      "tags": ["smoke", "regression"],
      "externalLink": {
        "type": "jiraCloud",
        "link": "PROJ-123"
      }
    },
    "plan": {
      "id": 456
    },
    "batch": {
      "size": 200
    },
    "defect": false,
    "uploadAttachments": true,
    "statusFilter": ["skipped", "invalid"],
    "configurations": {
      "values": "env=prod,version=1.0",
      "createIfNotExists": false
    },
    "showPublicReportLink": false
  }
}