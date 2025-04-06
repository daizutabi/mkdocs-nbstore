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
- `visualization.ipynb` is the path to the notebook file,
  relative to the `notebook_dir` (See the directory tree above)
- `#figure-identifier` is the identifier for the specific
  figure in the notebook

For more information about using class options to control how notebook
content is displayed, see the [Class Options](class.md) page.

## Identifying Figures in the Notebook

In your Jupyter notebook, you need to mark which figures you want
to reference in your documentation. This is done using a special
comment format at the beginning of a code cell.

**Example:**

```python title="visualization.ipynb"
# #my-figure
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title('Sample Visualization')
```

The comment format has the following rules:

- It must be the first non-empty line in the cell
- It starts with a Python comment character (`#`) followed by a space
- Then comes the figure identifier, which also starts with `#`
- Example: `# #my-figure` identifies a figure with the ID `my-figure`

You can then reference this figure in your markdown:

```markdown
![Sample Chart](visualization.ipynb){#my-figure}
```

### Benefits of This Approach

This identifier method is:

- Simple to add and recognize in your notebooks
- Visible during normal notebook editing
- Doesn't require special cell tags or hidden metadata
- Maintains notebook usability for non-documentation purposes

When you look at your notebook, you can immediately identify
cells that will be referenced in the documentation by looking
for the `# #identifier` pattern at the top of the cell.

## notebook
