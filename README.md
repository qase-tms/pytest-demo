# qase-pytest

If you run automated tests with pytest and want test those results available in Qase, this repository shows how to report them using the qase-pytest reporter.

---

## How It Works

The qase-pytest reporter connects your pytest suite with Qase, capturing test outcomes, execution time, and relevant metadata as tests run. These results are then sent to your Qase Workspace via the APIs.

---

## See it in action

If you already have a Qase workspace, you can get started by adding the qase-pytest reporter to your pytest test suite, setting a few environment variables, and running pytest as usual.

[Try it out now](./try_it_out.md).

---

## Quick Essentials

There are three core settings that make the reporter work:

- **API Token**: Identifies your workspace and permissions.  
- **Project Code**: Identifies which project to write results to.  
- **Mode**: Set to `testops` to enable the reporter.  

---

## How it fits into your test flow

No changes are required to how tests are written or executed in your test suite.
The reporter hooks into pytest, capturing results and sending them to Qase.
CI pipelines or local test commands will continue to operate as-is.

---

## Advanced Configuration

Beyond the basics like the API token, project code and reporter mode, there are other reporter variables that can be configured to fine tune how and where results are reported.

For example, results can be sent to a **specific test run** using the `QASE_TESTOPS_RUN_ID` environment variable. Alternatively, if you have a configuration file, you can specify the run details:

```json
{
  "testops": {
    "run": {
      "id": 123
    }
  }
}
```

Other reporter variables and options can be explored [here](./reporter_variables.md).

---

## Stay Updated

For updates on reporter features, changes, and improvements, check [this page](https://github.com/qase-tms/qase-python/blob/main/qase-pytest/changelog.md).
