# Execute

The `execute` class option is used to control whether a
notebook should be executed when it is referenced in a markdown file.

To execute a notebook, nbconvert must be installed.

```bash
pip install nbconvert
```

Executing a notebook will not overwrite the existing notebook.

mkdocs-nbstore cannot execute each cell but only the whole notebook.
