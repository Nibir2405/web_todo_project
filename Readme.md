# Streamlit Todo App

A simple web-based Todo application built with [Streamlit](https://streamlit.io/) and Python. This app allows you to add and remove todo items, helping you stay productive.

## Features

- Add new todo items
- Mark items as completed to remove them from the list
- Todos are persisted in a text file (`todos.txt`)
- Displays the current date and time

## Project Structure

```
functions.py         # Functions for reading/writing todos
web.py               # Streamlit web app
todos.txt            # Stores the todo items
requirements.txt     # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone this repository or download the source code.
2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

### Running the App

Start the Streamlit app with:

```sh
streamlit run web.py
```

The app will open in your browser.

## Usage

- Add a new todo by typing in the input box and pressing Enter.
- Mark a todo as completed by checking its box; it will be removed from the list.

## File Descriptions

- [`functions.py`](functions.py): Contains [`read_todos`](functions.py) and [`write_todos`](functions.py) for file operations.
- [`web.py`](web.py): Main Streamlit app logic and UI.
- [`todos.txt`](todos.txt): Stores the list of todos, one per line.
- [`requirements.txt`](requirements.txt): List of required Python packages.

## License

This project is licensed under the MIT License.