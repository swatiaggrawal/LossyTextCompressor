import json

notebook_path = "LossyTextCompressor.ipynb"
backup_path = notebook_path.replace(".ipynb", "_backup.ipynb")

# Backup first
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

with open(backup_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print(f"Backup saved as {backup_path}")

# Recursive fix function
def fix_widgets_in_dict(d):
    if isinstance(d, dict):
        if "widgets" in d and isinstance(d["widgets"], dict):
            if "state" not in d["widgets"]:
                d["widgets"]["state"] = {}
        for k, v in d.items():
            fix_widgets_in_dict(v)
    elif isinstance(d, list):
        for item in d:
            fix_widgets_in_dict(item)

fix_widgets_in_dict(nb)

# Save fixed notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Notebook fixed for GitHub rendering!")
