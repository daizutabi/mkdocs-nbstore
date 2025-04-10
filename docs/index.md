# mkdocs-nbstore

<strong>Connect Jupyter notebooks to your MkDocs documentation</strong>

mkdocs-nbstore is a plugin that seamlessly embeds Jupyter notebook
visualizations in your documentation, solving the disconnect between
code development and documentation.

## Why Use mkdocs-nbstore?

### The Documentation Challenge

Data scientists, researchers, and technical writers face a common dilemma:

- **Development happens in notebooks** - ideal for experimentation and visualization
- **Documentation lives in markdown** - perfect for narrative and explanation
- **Connecting the two is painful** - screenshots break, exports get outdated

### Our Solution

This plugin creates a live bridge between your notebooks and documentation by:

- **Keeping environments separate** - work in the tool best suited for each task
- **Maintaining connections** - reference specific figures from notebooks
- **Automating updates** - changes to notebooks reflect in documentation

## Key Benefits

- **True Separation of Concerns**:
  Develop visualizations in Jupyter notebooks and write documentation
  in markdown files, with each tool optimized for its purpose.

- **Intuitive Markdown Syntax**:
  Use standard image syntax with a simple extension to reference
  notebook figures: `![alt text](notebook.ipynb){#figure-id}`

- **Dynamic Notebook Execution**:
  Execute notebooks on-demand during documentation builds with the
  `.execute` option, ensuring results are always up-to-date.

- **Automatic Updates**:
  When you modify your notebooks, your documentation updates
  automatically in MkDocs serve mode.

- **Clean Source Documents**:
  Your markdown remains readable and focused on content, without
  code distractions or complex embedding techniques.

- **Enhanced Development Experience**:
  Take advantage of IDE features like code completion and syntax
  highlighting in the appropriate environment.

## Quick Start

### 1. Installation

```bash
pip install mkdocs-nbstore
```

### 2. Configuration

Add to your `mkdocs.yml`:

```yaml title="mkdocs.yml"
plugins:
  - mkdocs-nbstore:
      notebook_dir: ../notebooks
```

### 3. Mark Figures in Your Notebook

In your Jupyter notebook, identify figures with a comment:

```python title="my-notebook.ipynb"
# #my-figure
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
```

### 4. Reference in Markdown

Use standard Markdown image syntax with the figure identifier:

```markdown
![Chart description](my-notebook.ipynb){#my-figure}
```

## Advanced Usage

For more detailed information on how to use mkdocs-nbstore, see:

- [Notebook Configuration](usage/notebook.md) - Setting up notebook directories
- [Display Options](usage/class.md) - Control how notebook content is displayed
- [Execute Option](usage/execute.md) - Run notebooks during documentation builds
<!-- - [Workflow Tips](usage/workflow.md) - Best practices for documentation -->

## The Power of Separation

Creating documentation and developing visualizations involve different
workflows and timeframes. When building visualizations in Jupyter notebooks,
you need rapid cycles of execution, verification, and modification.

This plugin is designed specifically to address these separation of
concerns, allowing you to:

- **Focus on code** in notebooks without documentation distractions
- **Focus on narrative** in markdown without code interruptions
- **Maintain powerful connections** between both environments

Each environment is optimized for its purpose, while the plugin
handles the integration automatically.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
