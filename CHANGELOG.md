# Changelog

All notable changes to this project will be documented in this file.

## [0.1.2] - 2026-08-28

### Fixed
- Fix: decode() Raises a descriptive ValueError instead of an IndexError for short mov instructions.
- Fix: save() It eliminates the path traversal risk by sanitizing the file name using os.path.basename.

## [0.1.1] - 2026-07-26

### Added
- Added `decode()` function for decoding generated machine code.
- Exported `decode` in the public API.

### Fixed
- Fixed an import issue that prevented the package from being imported correctly.
- Improved package structure.

### Compatibility
- Verified compatibility with Python 3.13.
- Verified compatibility with Python 3.14.

## [0.1.0] - 2026-07-08

### Added
- Initial release.
- x86 machine code generation.
- `mov`, `ret`, and `nop` instructions.