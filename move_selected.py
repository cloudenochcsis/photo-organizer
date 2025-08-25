#!/usr/bin/env python3
"""
Selected Photos Script
This script moves specific photos (both CR2 and JPG) to the SELECTED folder
based on their image numbers.
"""

import os
import shutil
from pathlib import Path

def move_selected_photos():
    """Move selected photos to SELECTED folder"""
    
    # Get the current directory
    current_dir = Path.cwd()
    print(f"Working in directory: {current_dir}")
    
    # Define folder paths
    raw_folder = current_dir / "RAW_Files"
    jpg_folder = current_dir / "JPG_Files"
    selected_folder = current_dir / "SELECTED"
    
    # Check if source folders exist
    if not raw_folder.exists():
        print(f"Error: RAW_Files folder not found at {raw_folder}")
        return
    
    if not jpg_folder.exists():
        print(f"Error: JPG_Files folder not found at {jpg_folder}")
        return
    
    # Create SELECTED folder if it doesn't exist
    selected_folder.mkdir(exist_ok=True)
    print(f"Target folder: {selected_folder}")
    
    # List of selected image numbers
    selected_numbers = [
        # Column 1
        8442, 8439, 8440, 8443, 8449, 8455, 8457, 8460, 8462, 8463, 8464, 8465, 8467, 8469, 8472, 8473, 8474, 8475, 8476, 8482, 8485, 8486,
        # Column 2
        8474, 8476, 8498, 8502, 8506, 8507, 8508, 8512, 8447, 8490, 8518, 8523, 8523, 8525, 8526, 8530, 8533, 8537, 8542,
        # Column 3
        8544, 8548, 8552, 8556, 8561, 8564, 8565, 8566, 8581, 8579, 8584, 8583, 8585, 8587, 8591, 8592, 8595,
        # Column 4
        8597, 8598, 8601, 8603, 8605, 8613, 8618, 8621, 8623, 8627, 8629, 8630, 8633, 8636, 8638, 8641,
        # Column 5
        8643, 8644, 8648, 8650, 8652, 8654, 8658, 8662, 8663, 8667, 8668, 8669, 8670, 8671, 8673, 8681, 8684,
        # Column 6
        8685, 8689, 8691, 8702, 8703, 8704, 8705, 8706, 8719, 8725, 8728, 8732, 8736, 8737, 8738, 8742, 8743,
        # Column 7
        8748, 8751, 8752, 8754, 8755, 8756, 8758, 8761, 8762, 8766, 8771, 8772, 8773, 8776, 8777, 8778, 8779, 8780,
        # Column 8
        8782, 8783, 8785, 8787, 8790, 8791, 8793, 8794, 8795, 8796, 8797, 8801, 8806, 8809, 8810, 8812, 8815,
        # Column 9
        8816, 8818, 8821, 8824, 8825, 8829
    ]
    
    # Remove duplicates and sort
    unique_numbers = sorted(set(selected_numbers))
    print(f"Moving {len(unique_numbers)} unique image numbers...")
    
    # Counters for statistics
    cr2_moved = 0
    jpg_moved = 0
    cr2_not_found = 0
    jpg_not_found = 0
    errors = 0
    
    print("\nProcessing selected images...")
    
    for img_number in unique_numbers:
        # Generate filenames
        cr2_filename = f"IMG_{img_number}.CR2"
        jpg_filename = f"IMG_{img_number}.JPG"
        
        # Source paths
        cr2_source = raw_folder / cr2_filename
        jpg_source = jpg_folder / jpg_filename
        
        # Destination paths
        cr2_destination = selected_folder / cr2_filename
        jpg_destination = selected_folder / jpg_filename
        
        # Move CR2 file
        try:
            if cr2_source.exists():
                if not cr2_destination.exists():
                    shutil.move(str(cr2_source), str(cr2_destination))
                    cr2_moved += 1
                    print(f"  Moved {cr2_filename} to SELECTED/")
                else:
                    print(f"  Skipped {cr2_filename} (already exists in SELECTED/)")
            else:
                print(f"  CR2 not found: {cr2_filename}")
                cr2_not_found += 1
        except Exception as e:
            print(f"  Error moving {cr2_filename}: {str(e)}")
            errors += 1
        
        # Move JPG file
        try:
            if jpg_source.exists():
                if not jpg_destination.exists():
                    shutil.move(str(jpg_source), str(jpg_destination))
                    jpg_moved += 1
                    print(f"  Moved {jpg_filename} to SELECTED/")
                else:
                    print(f"  Skipped {jpg_filename} (already exists in SELECTED/)")
            else:
                print(f"  JPG not found: {jpg_filename}")
                jpg_not_found += 1
        except Exception as e:
            print(f"  Error moving {jpg_filename}: {str(e)}")
            errors += 1
    
    # Print summary
    print(f"\n{'='*60}")
    print("SELECTION COMPLETE!")
    print(f"{'='*60}")
    print(f"CR2 files moved: {cr2_moved}")
    print(f"JPG files moved: {jpg_moved}")
    print(f"CR2 files not found: {cr2_not_found}")
    print(f"JPG files not found: {jpg_not_found}")
    print(f"Errors encountered: {errors}")
    print(f"Total images processed: {len(unique_numbers)}")
    
    # Show final folder contents
    selected_cr2_count = len(list(selected_folder.glob('*.CR2')))
    selected_jpg_count = len(list(selected_folder.glob('*.JPG')))
    
    print(f"\nSELECTED folder contents:")
    print(f"CR2 files: {selected_cr2_count}")
    print(f"JPG files: {selected_jpg_count}")
    print(f"Total files in SELECTED: {selected_cr2_count + selected_jpg_count}")

def main():
    """Main function with error handling"""
    try:
        print("Selected Photos Moving Script")
        print("============================")
        
        # Ask for user confirmation
        response = input("\nThis will move selected CR2 and JPG files to the 'SELECTED' folder.\nContinue? (y/N): ")
        
        if response.lower() in ['y', 'yes']:
            move_selected_photos()
        else:
            print("Operation cancelled.")
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()
