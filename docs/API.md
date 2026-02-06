# Notes Manager API Documentation

## NotesManager Class

The `NotesManager` class is the core of the notes management system, providing all CRUD operations and search functionality.

### Constructor

```python
NotesManager(data_file: str = "notes_data.json")
```

**Parameters:**
- `data_file` (str, optional): Path to the JSON file for storing notes. Defaults to "notes_data.json".

**Example:**
```python
manager = NotesManager()  # Uses default file
manager = NotesManager("my_notes.json")  # Custom file
```

### Methods

#### create_note

```python
create_note(title: str, content: str, tags: Optional[List[str]] = None) -> Dict
```

Create a new note.

**Parameters:**
- `title` (str): The title of the note
- `content` (str): The content of the note
- `tags` (List[str], optional): List of tags for categorization

**Returns:**
- Dict: The created note with id, title, content, tags, created_at, and updated_at fields

**Example:**
```python
note = manager.create_note(
    title="Shopping List",
    content="Buy groceries for the week",
    tags=["personal", "todo"]
)
print(note['id'])  # 1
```

#### get_all_notes

```python
get_all_notes() -> List[Dict]
```

Get all notes.

**Returns:**
- List[Dict]: List of all notes

**Example:**
```python
notes = manager.get_all_notes()
for note in notes:
    print(f"{note['id']}: {note['title']}")
```

#### get_note_by_id

```python
get_note_by_id(note_id: int) -> Optional[Dict]
```

Get a note by its ID.

**Parameters:**
- `note_id` (int): The ID of the note to retrieve

**Returns:**
- Dict or None: The note if found, None otherwise

**Example:**
```python
note = manager.get_note_by_id(1)
if note:
    print(note['title'])
else:
    print("Note not found")
```

#### update_note

```python
update_note(note_id: int, title: Optional[str] = None, 
           content: Optional[str] = None, tags: Optional[List[str]] = None) -> Optional[Dict]
```

Update an existing note.

**Parameters:**
- `note_id` (int): The ID of the note to update
- `title` (str, optional): New title
- `content` (str, optional): New content
- `tags` (List[str], optional): New tags

**Returns:**
- Dict or None: The updated note if found, None otherwise

**Example:**
```python
# Update only the title
updated = manager.update_note(1, title="New Title")

# Update multiple fields
updated = manager.update_note(
    1,
    title="Updated Title",
    content="Updated content",
    tags=["updated", "modified"]
)
```

#### delete_note

```python
delete_note(note_id: int) -> bool
```

Delete a note by its ID.

**Parameters:**
- `note_id` (int): The ID of the note to delete

**Returns:**
- bool: True if the note was deleted, False otherwise

**Example:**
```python
if manager.delete_note(1):
    print("Note deleted successfully")
else:
    print("Note not found")
```

#### search_notes

```python
search_notes(query: str) -> List[Dict]
```

Search notes by title or content (case-insensitive).

**Parameters:**
- `query` (str): The search query string

**Returns:**
- List[Dict]: List of notes matching the query

**Example:**
```python
results = manager.search_notes("meeting")
print(f"Found {len(results)} notes")
for note in results:
    print(note['title'])
```

#### get_notes_by_tag

```python
get_notes_by_tag(tag: str) -> List[Dict]
```

Get notes by tag.

**Parameters:**
- `tag` (str): The tag to filter by

**Returns:**
- List[Dict]: List of notes with the specified tag

**Example:**
```python
work_notes = manager.get_notes_by_tag("work")
for note in work_notes:
    print(note['title'])
```

## Note Structure

Each note is a dictionary with the following structure:

```python
{
    'id': 1,                          # Unique identifier
    'title': 'Note Title',            # Note title
    'content': 'Note content here',   # Note content
    'tags': ['tag1', 'tag2'],        # List of tags
    'created_at': '2026-02-06T...',  # ISO format timestamp
    'updated_at': '2026-02-06T...'   # ISO format timestamp
}
```

## Error Handling

The NotesManager handles common errors gracefully:

- **Missing file**: Creates a new empty notes list
- **Corrupt JSON**: Returns an empty list and starts fresh
- **Non-existent note**: Returns None for get operations, False for delete

## Data Persistence

Notes are automatically saved to the data file after every create, update, or delete operation. The file is in JSON format for easy inspection and manual editing if needed.

## Thread Safety

The current implementation is not thread-safe. If you need concurrent access, consider implementing file locking or using a proper database backend.
