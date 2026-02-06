# Contributing to Notes Manager

First off, thank you for considering contributing to Notes Manager! It's people like you that make this tool better for everyone.

## Code of Conduct

This project and everyone participating in it is governed by respect, kindness, and professionalism. Please be courteous to all contributors.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples** to demonstrate the steps
* **Describe the behavior you observed** and what you expected to see
* **Include Python version** and operating system information

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

* **Use a clear and descriptive title**
* **Provide a detailed description** of the suggested enhancement
* **Provide specific examples** to demonstrate the use case
* **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repository
2. Create a new branch from `main`:
   ```bash
   git checkout -b feature/my-feature
   ```

3. Make your changes:
   * Write clear, readable code
   * Follow the existing code style
   * Add tests for new functionality
   * Update documentation as needed

4. Test your changes:
   ```bash
   pytest tests/
   ```

5. Commit your changes:
   ```bash
   git commit -m "Add feature: description of feature"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/my-feature
   ```

7. Open a Pull Request

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/notes.git
   cd notes
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests to ensure everything works:
   ```bash
   pytest tests/
   ```

## Coding Standards

* Follow PEP 8 style guide for Python code
* Use type hints for function parameters and return values
* Write docstrings for all classes and functions
* Keep functions focused and small
* Write meaningful variable names

### Code Style Example

```python
def create_note(self, title: str, content: str, tags: Optional[List[str]] = None) -> Dict:
    """
    Create a new note.
    
    Args:
        title: The title of the note.
        content: The content of the note.
        tags: Optional list of tags for categorization.
        
    Returns:
        The created note as a dictionary.
    """
    # Implementation
```

## Testing Guidelines

* Write tests for all new features
* Ensure all tests pass before submitting PR
* Aim for high test coverage
* Use descriptive test names that explain what is being tested

### Test Example

```python
def test_create_note(notes_manager):
    """Test creating a new note."""
    note = notes_manager.create_note("Test Title", "Test Content", ["tag1"])
    
    assert note['title'] == "Test Title"
    assert note['content'] == "Test Content"
    assert note['tags'] == ["tag1"]
```

## Documentation

* Update README.md if you change functionality
* Update API.md for API changes
* Add examples for new features
* Keep documentation clear and concise

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
