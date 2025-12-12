# qase-pytest

Capture your pytest test results along with all relevant metadata in Qase automatically using the qase-pytest reporter.

## Try It Out Now

Want to see it in action? It only takes **3 minutes**! [Try it out now](./try_it_out.md)   

---

## Quick Essentials

Here’s what makes it work:  

- **API Token**: Identifies your workspace and permissions.  
- **Project Code**: Identifies which project to write results to.  
- **Mode**: Set to `testops` to enable the reporter.  

---

## How It Works

The qase-pytest reporter acts as a bridge between pytest and Qase. It listens to pytest’s test runner, captures each test result along with relevant metadata, and then uses the Qase API to send this information to your project.

---

## Advanced Configuration

Along with the essentials like the API token and project code, there are other options and variables that can be configured.

For example, results can be sent to a **specific test run** using the `QASE_RUN_ID` variable.  

Other reporter variables and options can be explored [here](YOUR_VARIABLES_LINK).

---

## Stay Updated

Want to keep up with the latest reporter updates and features? Check out [this page](YOUR_UPDATES_LINK) to stay in the loop.  
