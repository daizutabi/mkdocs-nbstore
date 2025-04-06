# Notebook Configuration

This page explains how to configure mkdocs-nbstore to work with
your Jupyter notebooks.

## Setting the Notebook Directory

The first step is to specify where your Jupyter notebooks are
located. This is done using the `notebook_dir` option in your
`mkdocs.yml` configuration file.

**Example:**

```yaml title="mkdocs.yml"
plugins:
  - mkdocs-nbstore:
      notebook_dir: ../notebooks
```

The `notebook_dir` path is relative to your `docs` directory.
For example, with the configuration above and the following
project structure:

```text
project/
├─ docs/
│  └─ index.md
├─ notebooks/    <- notebook_dir points here
│  ├─ data-analysis.ipynb
│  └─ visualization.ipynb
└─ mkdocs.yml
```

All notebooks in the `notebooks` directory will be available
to reference in your markdown files.

## Referencing Notebooks in Markdown

Once you've configured the notebook directory, you can reference
notebooks using the standard Markdown image syntax with attributes:

```markdown
![Alt text](visualization.ipynb){#figure-identifier}
```

Where:

- `Alt text` is the alternative text for the image
- `notebook-name.ipynb` is the path to the notebook file,
  relative to the `notebook_dir` (See the directory tree above)
- `#figure-identifier` is the identifier for the specific
  figure in the notebook

For more information about using class options to control how notebook
content is displayed, see the [Class Options](class.md) page.

## Identifying Figures in the Notebook

To identify a figure in the notebook, you can use the normal Python
commenting syntax. For example:

```python
# #figure-identifier
plt.plot([1, 2, 3, 4])
```

The comment must be the first non-empty line in the cell.
The first `#` is the comment character, and the second `#` is the
identifier prefix. One space is required between these two `#`s.
This will create a figure with the identifier `#figure-identifier`.
When you work with the notebook in the browser or editor,
you can easily add this identifier as a comment.
There are no hidden structures in the notebook that you need to
work around, for example, by adding a cell tag or metadata.
You can always recognize whether a figure has an identifier by
checking whether the cell starts with `# #figure-identifier`.
