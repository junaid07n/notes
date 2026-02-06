"""
Notes Manager - A simple command-line notes management system.

This module provides functionality to create, read, update, and delete notes.
Notes are stored in JSON format for easy persistence.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class NotesManager:
    """Manages notes with CRUD operations."""
    
    def __init__(self, data_file: str = "notes_data.json"):
        """
        Initialize the NotesManager.
        
        Args:
            data_file: Path to the JSON file for storing notes.
        """
        self.data_file = data_file
        self.notes = self._load_notes()
    
    def _load_notes(self) -> List[Dict]:
        """Load notes from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def _save_notes(self) -> None:
        """Save notes to the data file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.notes, f, indent=2)
    
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
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'content': content,
            'tags': tags or [],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        self.notes.append(note)
        self._save_notes()
        return note
    
    def get_all_notes(self) -> List[Dict]:
        """
        Get all notes.
        
        Returns:
            List of all notes.
        """
        return self.notes
    
    def get_note_by_id(self, note_id: int) -> Optional[Dict]:
        """
        Get a note by its ID.
        
        Args:
            note_id: The ID of the note to retrieve.
            
        Returns:
            The note if found, None otherwise.
        """
        for note in self.notes:
            if note['id'] == note_id:
                return note
        return None
    
    def update_note(self, note_id: int, title: Optional[str] = None, 
                   content: Optional[str] = None, tags: Optional[List[str]] = None) -> Optional[Dict]:
        """
        Update an existing note.
        
        Args:
            note_id: The ID of the note to update.
            title: New title (if provided).
            content: New content (if provided).
            tags: New tags (if provided).
            
        Returns:
            The updated note if found, None otherwise.
        """
        note = self.get_note_by_id(note_id)
        if note:
            if title is not None:
                note['title'] = title
            if content is not None:
                note['content'] = content
            if tags is not None:
                note['tags'] = tags
            note['updated_at'] = datetime.now().isoformat()
            self._save_notes()
            return note
        return None
    
    def delete_note(self, note_id: int) -> bool:
        """
        Delete a note by its ID.
        
        Args:
            note_id: The ID of the note to delete.
            
        Returns:
            True if the note was deleted, False otherwise.
        """
        for i, note in enumerate(self.notes):
            if note['id'] == note_id:
                self.notes.pop(i)
                self._save_notes()
                return True
        return False
    
    def search_notes(self, query: str) -> List[Dict]:
        """
        Search notes by title or content.
        
        Args:
            query: The search query string.
            
        Returns:
            List of notes matching the query.
        """
        query_lower = query.lower()
        return [
            note for note in self.notes
            if query_lower in note['title'].lower() or query_lower in note['content'].lower()
        ]
    
    def get_notes_by_tag(self, tag: str) -> List[Dict]:
        """
        Get notes by tag.
        
        Args:
            tag: The tag to filter by.
            
        Returns:
            List of notes with the specified tag.
        """
        return [note for note in self.notes if tag in note['tags']]
