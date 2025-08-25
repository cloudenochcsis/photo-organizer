# Photo Organizer

A collection of Python scripts designed to streamline photography workflow by organizing camera files and curating photo selections from large collections.

## Overview

This project provides tools for photographers to efficiently manage their digital photo collections, particularly useful for organizing files from DSLR cameras that produce both RAW and JPEG formats.

## Features

- **Automatic File Sorting**: Separates RAW files (CR2) and JPEG files into organized folder structures
- **Selective Photo Curation**: Move specific photos by image number to dedicated selection folders  
- **Batch Processing**: Handle hundreds of photos with a single command
- **Safety Features**: Confirmation prompts and duplicate detection prevent data loss
- **Cross-format Support**: Works with Canon CR2 RAW files and standard JPEG files

## Scripts

### sort_photos.py
Organizes photos in the current directory by file type:
- Creates `RAW_Files` folder for CR2 files
- Creates `JPG_Files` folder for JPEG files
- Moves files while preserving original names
- Provides detailed progress reporting

### move_selected.py
Moves specific photos by image number to a selection folder:
- Processes both RAW and JPEG versions of selected images
- Removes duplicate selections automatically
- Moves files from organized folders to a `SELECTED` directory
- Handles large lists of image numbers efficiently

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/photo-organizer.git
cd photo-organizer
```

2. Ensure Python 3.6+ is installed on your system

3. No additional dependencies required - uses only Python standard library

## Usage

### Basic File Organization

Navigate to your photo directory and run the sorting script:

```bash
python3 sort_photos.py
```

The script will:
1. Ask for confirmation before proceeding
2. Create `RAW_Files` and `JPG_Files` directories
3. Move all CR2 files to `RAW_Files`
4. Move all JPG files to `JPG_Files`
5. Display progress and final statistics

### Selecting Specific Photos

To move specific photos to a selection folder:

1. Edit `move_selected.py` and update the `selected_numbers` list with your desired image numbers
2. Run the selection script:

```bash
python3 move_selected.py
```

The script will:
1. Find both CR2 and JPG versions of each selected image number
2. Move them from the organized folders to a `SELECTED` directory
3. Report on successful moves and any missing files

### Organizing Selected Photos

After selecting photos, you can organize them further:

```bash
cd SELECTED
python3 ../sort_photos.py
```

This creates organized subfolders within your selection for easy access to RAW vs JPEG versions.

## Example Workflow

1. **Initial Organization**: Run `sort_photos.py` in your camera's memory card folder to separate RAW and JPEG files

2. **Photo Selection**: Review your photos and note the image numbers of your favorites

3. **Curate Selection**: Update `move_selected.py` with your chosen image numbers and run it

4. **Final Organization**: Run `sort_photos.py` in the SELECTED folder to organize your curated collection

## File Structure

After running the scripts, your directory will be organized as follows:

```
your-photo-directory/
├── RAW_Files/              # All CR2 files
├── JPG_Files/              # All JPG files
├── SELECTED/               # Curated photo selection
│   ├── RAW_Files/          # Selected CR2 files
│   └── JPG_Files/          # Selected JPG files
├── sort_photos.py
└── move_selected.py
```

## Compatibility

- **Operating Systems**: Windows, macOS, Linux
- **Python Version**: 3.6 or higher
- **File Formats**: Canon CR2 RAW files, JPEG files
- **File Systems**: Any standard file system

## Safety Features

- **Confirmation Prompts**: All operations require user confirmation
- **Duplicate Detection**: Won't overwrite existing files
- **Move Operations**: Files are moved, not copied, to save disk space
- **Error Handling**: Graceful handling of missing files or permission issues
- **Progress Reporting**: Detailed feedback on all operations

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:

- Support for additional RAW formats (NEF, ARW, etc.)
- GUI interface development
- Performance optimizations
- Additional organizational features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created for photographers who need efficient tools to manage large photo collections and streamline their digital workflow.

## Changelog

### Version 1.0
- Initial release with basic sorting functionality
- Added selective photo curation feature
- Implemented safety features and error handling
