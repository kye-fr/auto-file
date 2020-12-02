# auto-file
#### Organize a specified directory by auto-creating subdirectories from filetypes
### Specifying the directory
Specify the path for the directory to be sorted:
```python
root = '/Users/you/yourDirectory/'
```
This will be the default parent directory of the resulting file structure.

### Adding new filetypes
To add filetypes that do not exist, add the extension to the appropriate list:
```python
media = ['.mp3', '.mp4', '.wmv', '.newFileType']
```
