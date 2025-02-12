# Playwright Automation Project

This project uses Playwright to automate browser interactions. The script loads environment variables, launches a browser, navigates to a specified URL, interacts with elements on the page, and manages cookies.

## Prerequisites

- Python 3.7+
- Playwright
- dotenv

## Setup

1. Clone the repository:

```sh
$ git clone <repository-url>
$ cd <repository-directory>
```

2. Install the required packages:

```sh
$ pip install playwright python-dotenv
$ playwright install
```

3. Create a `.env` file in the root directory and add the following variables:

```env
BROWERS_EXECUTABLE_PATH=<path-to-browser-executable>
SITE_URL_ONE=<url-to-navigate>
```

4. Create a `cookies.json` file in the root directory. This file will be used to store and load cookies.

## Usage

Run the script:

```sh
$ python main.py
```

The script will launch the browser, navigate to the specified URL, interact with elements on the page, and save the cookies to `cookies.json`.

## Project Structure

```
<project-root>
│
├── .env
├── cookies.json
├── main.py
└── README.md
```

## License

This project is licensed under the MIT License.
