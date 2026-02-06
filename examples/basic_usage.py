#!/usr/bin/env python3
"""
Basic usage examples for the Notes Manager.

This script demonstrates how to use the NotesManager class
to perform common operations.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from notes_manager import NotesManager


def main():
    """Run basic usage examples."""
    
    # Initialize the manager with a custom file for this example
    print("=== Notes Manager - Basic Usage Examples ===\n")
    manager = NotesManager("example_notes.json")
    
    # Example 1: Create notes
    print("1. Creating notes...")
    note1 = manager.create_note(
        title="Python Learning Path",
        content="Start with basics, then move to OOP, and finally frameworks",
        tags=["python", "learning", "programming"]
    )
    print(f"   Created: {note1['title']} (ID: {note1['id']})")
    
    note2 = manager.create_note(
        title="Project Ideas",
        content="Build a todo app, notes manager, or a simple game",
        tags=["projects", "ideas"]
    )
    print(f"   Created: {note2['title']} (ID: {note2['id']})")
    
    note3 = manager.create_note(
        title="Meeting Notes - Feb 2026",
        content="Discussed Q1 goals, team assignments, and deadlines",
        tags=["work", "meetings"]
    )
    print(f"   Created: {note3['title']} (ID: {note3['id']})\n")
    
    # Example 2: List all notes
    print("2. Listing all notes...")
    all_notes = manager.get_all_notes()
    print(f"   Total notes: {len(all_notes)}")
    for note in all_notes:
        print(f"   - ID {note['id']}: {note['title']}")
    print()
    
    # Example 3: Get a specific note
    print("3. Getting a specific note...")
    note = manager.get_note_by_id(1)
    if note:
        print(f"   ID: {note['id']}")
        print(f"   Title: {note['title']}")
        print(f"   Content: {note['content']}")
        print(f"   Tags: {', '.join(note['tags'])}")
    print()
    
    # Example 4: Search notes
    print("4. Searching for notes containing 'python'...")
    results = manager.search_notes("python")
    print(f"   Found {len(results)} note(s):")
    for note in results:
        print(f"   - {note['title']}")
    print()
    
    # Example 5: Get notes by tag
    print("5. Getting notes with tag 'learning'...")
    tagged_notes = manager.get_notes_by_tag("learning")
    print(f"   Found {len(tagged_notes)} note(s):")
    for note in tagged_notes:
        print(f"   - {note['title']}")
    print()
    
    # Example 6: Update a note
    print("6. Updating a note...")
    updated = manager.update_note(
        note_id=1,
        title="Python Learning Path - Updated",
        tags=["python", "learning", "programming", "updated"]
    )
    if updated:
        print(f"   Updated: {updated['title']}")
        print(f"   New tags: {', '.join(updated['tags'])}")
    print()
    
    # Example 7: Delete a note
    print("7. Deleting a note...")
    if manager.delete_note(2):
        print(f"   Deleted note with ID 2")
    print()
    
    # Example 8: Final list
    print("8. Final list of notes...")
    final_notes = manager.get_all_notes()
    print(f"   Remaining notes: {len(final_notes)}")
    for note in final_notes:
        print(f"   - ID {note['id']}: {note['title']}")
    print()
    
    print("=== Examples completed! ===")
    print(f"\nNotes have been saved to: example_notes.json")
    print("You can inspect this file to see how notes are stored.")


if __name__ == '__main__':
    main()
