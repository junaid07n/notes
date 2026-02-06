# Notes Manager 📝

A simple and elegant command-line notes management system written in Python. Organize your thoughts, ideas, and tasks with ease!

## Features ✨

- **Create, Read, Update, Delete (CRUD)** - Full management of your notes
- **Tag Support** - Organize notes with custom tags
- **Search Functionality** - Quickly find notes by title or content
- **Persistent Storage** - Notes are saved in JSON format
- **Command-Line Interface** - Easy-to-use CLI for all operations
- **Type Hints** - Full type annotations for better code quality

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/junaid07n/notes.git
cd notes
```

2. Install dependencies (optional, for testing):
```bash
pip install -r requirements.txt
```

## Usage 💻

### Command-Line Interface

Create a new note:
```bash
python src/cli.py create "Meeting Notes" "Discussed project timeline and deliverables" --tags work meeting
```

List all notes:
```bash
python src/cli.py list
```

Get a specific note:
```bash
python src/cli.py get 1
```

Update a note:
```bash
python src/cli.py update 1 --title "Updated Title" --content "Updated content"
```

Delete a note:
```bash
python src/cli.py delete 1
```

Search notes:
```bash
python src/cli.py search "project"
```

Filter by tag:
```bash
python src/cli.py tag work
```

### Python API

You can also use the NotesManager class directly in your Python code:

```python
from src.notes_manager import NotesManager

# Initialize the manager
manager = NotesManager()

# Create a note
note = manager.create_note(
    title="My First Note",
    content="This is the content of my note",
    tags=["personal", "ideas"]
)

# Get all notes
all_notes = manager.get_all_notes()

# Search notes
results = manager.search_notes("first")

# Get notes by tag
personal_notes = manager.get_notes_by_tag("personal")
```

## Project Structure 📁

```
notes/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── notes_manager.py     # Core NotesManager class
│   └── cli.py               # Command-line interface
├── tests/
│   ├── __init__.py
│   └── test_notes_manager.py  # Unit tests
├── docs/
│   └── API.md               # API documentation
├── examples/
│   └── basic_usage.py       # Usage examples
├── .gitignore               # Git ignore rules
├── LICENSE                  # MIT License
├── README.md                # This file
└── requirements.txt         # Python dependencies
```

## Running Tests 🧪

Run the test suite using pytest:

```bash
pytest tests/
```

Run with coverage:
```bash
pytest --cov=src tests/
```

## API Documentation 📚

See [docs/API.md](docs/API.md) for detailed API documentation.

## Examples 💡

Check out the [examples](examples/) directory for more usage examples.

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author ✍️

**Junaid Alam** - [@junaid07n](https://github.com/junaid07n)

## Acknowledgments 🙏

- Thanks to all contributors who have helped improve this project
- Inspired by the need for a simple, lightweight notes management system

---

Made with ❤️ by Junaid Alam