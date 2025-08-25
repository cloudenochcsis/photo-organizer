# Photo Organizer

![Version](https://img.shields.io/github/v/tag/cloudenochcsis/photo-organizer?label=version)
![License](https://img.shields.io/github/license/cloudenochcsis/photo-organizer)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)

A collection of Python scripts designed to streamline photography workflow by organizing camera files and curating photo selections from large collections.

## Overview

This project provides tools for photographers to efficiently manage their digital photo collections, particularly useful for organizing files from DSLR cameras that produce both RAW and JPEG formats. Perfect for processing hundreds of photos from photo shoots, events, or travel photography.

## Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/cloudenochcsis/photo-organizer.git
cd photo-organizer
```

2. **Copy scripts to your photo directory:**
```bash
cp *.py /path/to/your/photos/
cd /path/to/your/photos/
```

3. **Organize your photos:**
```bash
python3 sort_photos.py
```

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

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

### Method 1: Clone Repository
```bash
git clone https://github.com/cloudenochcsis/photo-organizer.git
cd photo-organizer
```

### Method 2: Download Scripts
Download the latest release from [GitHub Releases](https://github.com/cloudenochcsis/photo-organizer/releases) and extract to your desired location.

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

## Sample Output

### sort_photos.py Output
```
Photo Sorting Script
===================

This will move all CR2 files to 'RAW_Files' folder and JPG files to 'JPG_Files' folder.
Continue? (y/N): y
Working in directory: /Users/photographer/photos
Created/verified folders:
  - /Users/photographer/photos/RAW_Files
  - /Users/photographer/photos/JPG_Files

Processing 628 files...
  Moved IMG_8439.CR2 to RAW_Files/
  Moved IMG_8439.JPG to JPG_Files/
  [... processing continues ...]

==================================================
SORTING COMPLETE!
==================================================
CR2 files moved: 314
JPG files moved: 314
Files skipped: 0
Total files processed: 628

Folder contents:
RAW_Files folder: 314 CR2 files
JPG_Files folder: 314 JPG files
```

## Troubleshooting

### Common Issues

**Permission Errors**
- Ensure you have write permissions to the directory
- On macOS/Linux, you might need to run with appropriate permissions

**Files Not Found**
- Verify file extensions match (CR2, JPG) - case sensitive on some systems
- Check that files haven't already been moved or organized

**Script Won't Run**
- Confirm Python 3.6+ is installed: `python3 --version`
- Try running with full path: `/usr/bin/python3 script_name.py`

### Getting Help

- Check the [Issues](https://github.com/cloudenochcsis/photo-organizer/issues) page for known problems
- Create a new issue if you encounter a bug or need help

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

Contributions are welcome! Here's how you can help:

### Reporting Issues
- Use the [GitHub Issues](https://github.com/cloudenochcsis/photo-organizer/issues) page
- Include your Python version and operating system
- Provide steps to reproduce the problem

### Suggesting Features
- Open a feature request on GitHub Issues
- Describe the use case and expected behavior
- Consider submitting a pull request if you can implement it

### Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit with clear messages: `git commit -m "Add feature description"`
5. Push to your fork and submit a pull request

### Development Ideas
- Support for additional RAW formats (NEF, ARW, ORF, etc.)
- GUI interface using tkinter or PyQt
- Configuration file support
- Batch renaming capabilities
- Duplicate photo detection
- Integration with photo management software

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### Version 1.0.0 (2025-08-25)
- Initial release with basic sorting functionality
- Added selective photo curation feature
- Implemented safety features and error handling
- Professional documentation and GitHub setup
- Comprehensive .gitignore for photography projects

## Author

Created by [cloudenochcsis](https://github.com/cloudenochcsis) for photographers who need efficient tools to manage large photo collections and streamline their digital workflow.

---

**Star this repository** if you find it useful! 
**Report issues** on the [GitHub Issues page](https://github.com/cloudenochcsis/photo-organizer/issues).
