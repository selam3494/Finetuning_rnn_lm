import nbformat

nb = nbformat.read("AI_agent_setup.ipynb", as_version=nbformat.NO_CONVERT)
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

for cell in nb.cells:
    if "widgets" in cell.get("metadata", {}):
        del cell.metadata["widgets"]

nbformat.write(nb, "AI_agent_setup.ipynb")
print("Removed all 'metadata.widgets' while keeping outputs intact.")
