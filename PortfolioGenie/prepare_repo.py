import os
import shutil

root_dir = r"C:\Users\elsay\.gemini\antigravity\scratch\portfoliogenie"
subfolder = os.path.join(root_dir, "PortfolioGenie")

# Create subfolder
if not os.path.exists(subfolder):
    os.makedirs(subfolder)
    print(f"Created subfolder: {subfolder}")

items_to_move = [
    "src",
    "public",
    "docs",
    "package.json",
    "package-lock.json",
    "vite.config.js",
    "eslint.config.js",
    "index.html",
    "vercel.json"
]

for item in items_to_move:
    src_path = os.path.join(root_dir, item)
    dst_path = os.path.join(subfolder, item)
    if os.path.exists(src_path):
        print(f"Moving {item} to subfolder...")
        shutil.move(src_path, dst_path)

# Create a clean root .gitignore
root_gitignore_content = """# Root Git Ignore
.venv/
.venv
node_modules/
node_modules
PortfolioGenie/node_modules/
PortfolioGenie/dist/
*.log
~$*
"""

root_gitignore_path = os.path.join(root_dir, ".gitignore")
with open(root_gitignore_path, "w") as f:
    f.write(root_gitignore_content)
print("Created root .gitignore")

# Create a local .gitignore inside PortfolioGenie
sub_gitignore_content = """node_modules/
dist/
dist-ssr/
*.local
.vscode/
.idea
.DS_Store
*.log
"""
sub_gitignore_path = os.path.join(subfolder, ".gitignore")
with open(sub_gitignore_path, "w") as f:
    f.write(sub_gitignore_content)
print("Created subfolder .gitignore")
