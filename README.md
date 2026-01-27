# qase-pytest

This is an example repository with tests in the `tests/examples/` directory. To run the tests :

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

5. Create a `qase.config.json` in the root of the repository:
   - Copy the example file: `cp qase.config.json.example qase.config.json`
   - Edit `qase.config.json` and replace `<your_api_token_here>` with your Qase API token
   - Replace `<your_project_code_here>` with your Qase project code
   
   **Note:** `qase.config.json` is gitignored for security (contains sensitive credentials). 
   Use `qase.config.json.example` as a template.

6. Run `pytest`.
