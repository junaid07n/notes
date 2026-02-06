"""Tests for the NotesManager class."""

import pytest
import os
import sys
import json
from pathlib import Path

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from notes_manager import NotesManager


@pytest.fixture
def temp_notes_file(tmp_path):
    """Create a temporary notes data file."""
    return str(tmp_path / "test_notes.json")


@pytest.fixture
def notes_manager(temp_notes_file):
    """Create a NotesManager instance with a temporary data file."""
    return NotesManager(temp_notes_file)


def test_create_note(notes_manager):
    """Test creating a new note."""
    note = notes_manager.create_note("Test Title", "Test Content", ["tag1", "tag2"])
    
    assert note['id'] == 1
    assert note['title'] == "Test Title"
    assert note['content'] == "Test Content"
    assert note['tags'] == ["tag1", "tag2"]
    assert 'created_at' in note
    assert 'updated_at' in note


def test_get_all_notes(notes_manager):
    """Test getting all notes."""
    notes_manager.create_note("Note 1", "Content 1")
    notes_manager.create_note("Note 2", "Content 2")
    
    notes = notes_manager.get_all_notes()
    assert len(notes) == 2
    assert notes[0]['title'] == "Note 1"
    assert notes[1]['title'] == "Note 2"


def test_get_note_by_id(notes_manager):
    """Test getting a note by ID."""
    note = notes_manager.create_note("Test Note", "Test Content")
    
    retrieved_note = notes_manager.get_note_by_id(note['id'])
    assert retrieved_note is not None
    assert retrieved_note['title'] == "Test Note"
    
    # Test non-existent note
    assert notes_manager.get_note_by_id(999) is None


def test_update_note(notes_manager):
    """Test updating a note."""
    note = notes_manager.create_note("Original Title", "Original Content")
    
    updated_note = notes_manager.update_note(
        note['id'], 
        title="Updated Title", 
        content="Updated Content",
        tags=["new_tag"]
    )
    
    assert updated_note is not None
    assert updated_note['title'] == "Updated Title"
    assert updated_note['content'] == "Updated Content"
    assert updated_note['tags'] == ["new_tag"]
    
    # Test partial update
    notes_manager.update_note(note['id'], title="Another Title")
    retrieved = notes_manager.get_note_by_id(note['id'])
    assert retrieved['title'] == "Another Title"
    assert retrieved['content'] == "Updated Content"


def test_delete_note(notes_manager):
    """Test deleting a note."""
    note = notes_manager.create_note("To Delete", "Content")
    
    assert notes_manager.delete_note(note['id']) is True
    assert notes_manager.get_note_by_id(note['id']) is None
    
    # Test deleting non-existent note
    assert notes_manager.delete_note(999) is False


def test_search_notes(notes_manager):
    """Test searching notes."""
    notes_manager.create_note("Python Tutorial", "Learn Python programming")
    notes_manager.create_note("JavaScript Guide", "Learn JavaScript")
    notes_manager.create_note("Python Advanced", "Advanced Python concepts")
    
    results = notes_manager.search_notes("Python")
    assert len(results) == 2
    
    results = notes_manager.search_notes("JavaScript")
    assert len(results) == 1
    
    results = notes_manager.search_notes("Ruby")
    assert len(results) == 0


def test_get_notes_by_tag(notes_manager):
    """Test getting notes by tag."""
    notes_manager.create_note("Note 1", "Content 1", ["python", "tutorial"])
    notes_manager.create_note("Note 2", "Content 2", ["javascript"])
    notes_manager.create_note("Note 3", "Content 3", ["python", "advanced"])
    
    python_notes = notes_manager.get_notes_by_tag("python")
    assert len(python_notes) == 2
    
    js_notes = notes_manager.get_notes_by_tag("javascript")
    assert len(js_notes) == 1
    
    ruby_notes = notes_manager.get_notes_by_tag("ruby")
    assert len(ruby_notes) == 0


def test_persistence(temp_notes_file):
    """Test that notes are persisted to disk."""
    manager1 = NotesManager(temp_notes_file)
    manager1.create_note("Persisted Note", "This should persist")
    
    # Create a new manager instance with the same file
    manager2 = NotesManager(temp_notes_file)
    notes = manager2.get_all_notes()
    
    assert len(notes) == 1
    assert notes[0]['title'] == "Persisted Note"


def test_empty_notes_file(temp_notes_file):
    """Test handling of non-existent notes file."""
    manager = NotesManager(temp_notes_file)
    assert manager.get_all_notes() == []


def test_corrupt_notes_file(temp_notes_file):
    """Test handling of corrupted notes file."""
    # Create a corrupted JSON file
    with open(temp_notes_file, 'w') as f:
        f.write("{ invalid json }")
    
    manager = NotesManager(temp_notes_file)
    assert manager.get_all_notes() == []


def test_id_generation_after_deletion(notes_manager):
    """Test that ID generation works correctly after notes are deleted."""
    # Create notes with IDs 1, 2, 3
    note1 = notes_manager.create_note("Note 1", "Content 1")
    note2 = notes_manager.create_note("Note 2", "Content 2")
    note3 = notes_manager.create_note("Note 3", "Content 3")
    
    assert note1['id'] == 1
    assert note2['id'] == 2
    assert note3['id'] == 3
    
    # Delete note 2
    notes_manager.delete_note(2)
    
    # Create a new note - it should get ID 4, not 3
    note4 = notes_manager.create_note("Note 4", "Content 4")
    assert note4['id'] == 4
    
    # Verify note 3 still exists
    assert notes_manager.get_note_by_id(3) is not None
