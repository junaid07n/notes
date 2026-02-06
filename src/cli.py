"""Command-line interface for the Notes Manager."""

import argparse
import sys
from notes_manager import NotesManager


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Notes Manager - Manage your notes from the command line')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Create note command
    create_parser = subparsers.add_parser('create', help='Create a new note')
    create_parser.add_argument('title', help='Note title')
    create_parser.add_argument('content', help='Note content')
    create_parser.add_argument('--tags', nargs='+', help='Tags for the note')
    
    # List notes command
    subparsers.add_parser('list', help='List all notes')
    
    # Get note command
    get_parser = subparsers.add_parser('get', help='Get a note by ID')
    get_parser.add_argument('id', type=int, help='Note ID')
    
    # Update note command
    update_parser = subparsers.add_parser('update', help='Update a note')
    update_parser.add_argument('id', type=int, help='Note ID')
    update_parser.add_argument('--title', help='New title')
    update_parser.add_argument('--content', help='New content')
    update_parser.add_argument('--tags', nargs='+', help='New tags')
    
    # Delete note command
    delete_parser = subparsers.add_parser('delete', help='Delete a note')
    delete_parser.add_argument('id', type=int, help='Note ID')
    
    # Search notes command
    search_parser = subparsers.add_parser('search', help='Search notes')
    search_parser.add_argument('query', help='Search query')
    
    # Filter by tag command
    tag_parser = subparsers.add_parser('tag', help='Get notes by tag')
    tag_parser.add_argument('tag', help='Tag name')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    manager = NotesManager()
    
    if args.command == 'create':
        note = manager.create_note(args.title, args.content, args.tags)
        print(f"Created note #{note['id']}: {note['title']}")
    
    elif args.command == 'list':
        notes = manager.get_all_notes()
        if not notes:
            print("No notes found.")
        else:
            for note in notes:
                tags_str = f" [{', '.join(note['tags'])}]" if note['tags'] else ""
                print(f"#{note['id']}: {note['title']}{tags_str}")
                print(f"  {note['content'][:50]}..." if len(note['content']) > 50 else f"  {note['content']}")
                print()
    
    elif args.command == 'get':
        note = manager.get_note_by_id(args.id)
        if note:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print(f"Tags: {', '.join(note['tags']) if note['tags'] else 'None'}")
            print(f"Created: {note['created_at']}")
            print(f"Updated: {note['updated_at']}")
        else:
            print(f"Note #{args.id} not found.")
    
    elif args.command == 'update':
        note = manager.update_note(args.id, args.title, args.content, args.tags)
        if note:
            print(f"Updated note #{note['id']}: {note['title']}")
        else:
            print(f"Note #{args.id} not found.")
    
    elif args.command == 'delete':
        if manager.delete_note(args.id):
            print(f"Deleted note #{args.id}")
        else:
            print(f"Note #{args.id} not found.")
    
    elif args.command == 'search':
        notes = manager.search_notes(args.query)
        if not notes:
            print(f"No notes found matching '{args.query}'.")
        else:
            print(f"Found {len(notes)} note(s):")
            for note in notes:
                print(f"#{note['id']}: {note['title']}")
    
    elif args.command == 'tag':
        notes = manager.get_notes_by_tag(args.tag)
        if not notes:
            print(f"No notes found with tag '{args.tag}'.")
        else:
            print(f"Found {len(notes)} note(s) with tag '{args.tag}':")
            for note in notes:
                print(f"#{note['id']}: {note['title']}")


if __name__ == '__main__':
    main()
