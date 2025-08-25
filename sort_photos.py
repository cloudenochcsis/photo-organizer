#!/usr/bin/env python3
"""
Photo Sorting Script
This script sorts camera files in the current directory:
- Creates a 'RAW_Files' folder for CR2 files
- Creates a 'JPG_Files' folder for JPG files
- Moves files while preserving their original names
"""

import os
import shutil
from pathlib import Path

def sort_photos():
    """Sort photos into RAW and JPG folders"""
    
    # Get the current directory
    current_dir = Path.cwd()
    print(f"Working in directory: {current_dir}")
    
    # Create folders for organizing files
    raw_folder = current_dir / "RAW_Files"
    jpg_folder = current_dir / "JPG_Files"
    
    # Create directories if they don't exist
    raw_folder.mkdir(exist_ok=True)
    jpg_folder.mkdir(exist_ok=True)
    
    print(f"Created/verified folders:")
    print(f"  - {raw_folder}")
    print(f"  - {jpg_folder}")
    
    # Counters for statistics
    cr2_moved = 0
    jpg_moved = 0
    skipped_files = 0
    
    # Get all files in current directory
    files = [f for f in current_dir.iterdir() if f.is_file()]
    
    print(f"\nProcessing {len(files)} files...")
    
    for file_path in files:
        filename = file_path.name
        file_extension = file_path.suffix.upper()
        
        try:
            # Skip the script itself and hidden files
            if filename == 'sort_photos.py' or filename.startswith('.'):
                continue
                
            # Move CR2 files to RAW folder
            if file_extension == '.CR2':
                destination = raw_folder / filename
                if not destination.exists():
                    shutil.move(str(file_path), str(destination))
                    cr2_moved += 1
                    print(f"  Moved {filename} to RAW_Files/")
                else:
                    print(f"  Skipped {filename} (already exists in RAW_Files/)")
                    skipped_files += 1
            
            # Move JPG files to JPG folder
            elif file_extension == '.JPG' or file_extension == '.JPEG':
                destination = jpg_folder / filename
                if not destination.exists():
                    shutil.move(str(file_path), str(destination))
                    jpg_moved += 1
                    print(f"  Moved {filename} to JPG_Files/")
                else:
                    print(f"  Skipped {filename} (already exists in JPG_Files/)")
                    skipped_files += 1
            
            # Skip other file types
            else:
                print(f"  - Ignored {filename} (not a CR2/JPG file)")
                skipped_files += 1
                
        except Exception as e:
            print(f"  Error moving {filename}: {str(e)}")
            skipped_files += 1
    
    # Print summary
    print(f"\n{'='*50}")
    print("SORTING COMPLETE!")
    print(f"{'='*50}")
    print(f"CR2 files moved: {cr2_moved}")
    print(f"JPG files moved: {jpg_moved}")
    print(f"Files skipped: {skipped_files}")
    print(f"Total files processed: {cr2_moved + jpg_moved + skipped_files}")
    
    # Show folder contents
    print(f"\nFolder contents:")
    print(f"RAW_Files folder: {len(list(raw_folder.glob('*.CR2')))} CR2 files")
    print(f"JPG_Files folder: {len(list(jpg_folder.glob('*.JPG')))} JPG files")

def main():
    """Main function with error handling"""
    try:
        print("Photo Sorting Script")
        print("===================")
        
        # Ask for user confirmation
        response = input("\nThis will move all CR2 files to 'RAW_Files' folder and JPG files to 'JPG_Files' folder.\nContinue? (y/N): ")
        
        if response.lower() in ['y', 'yes']:
            sort_photos()
        else:
            print("Operation cancelled.")
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()
