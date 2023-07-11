import glob
import os
import yaml
from pprint import pprint


ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")

IGNORE_DIRS = [
    "assets",
    "_data",
    "_includes",
    "_layouts",
    "_site",
    ".github",
    ".git",
    "script",
]
IGNORE_EXTENSIONS = [".html", ".md", ".gitignore", ".gemspec"]
IGNORE_PATHS = ["_config.yaml", "LICENSE", "Gemfile"]

PATHS_FILE = "file_paths.yml"
CUSTOM_DIR_FILE = "custom_dirs.yml"
OUTPUT_DIR = os.path.join(ROOT_DIR, "_data")


def main():
    extensions = set()
    file_list = glob.glob(os.path.join(ROOT_DIR, "**"), recursive=True)
    filtered_file_data = {}
    custom_view_dirs = []
    for file_path in file_list:
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        if os.path.isdir(file_path):
            # find directories with a custom 'index.md' file
            if rel_path != "." and os.path.exists(os.path.join(file_path, "index.md")):
                custom_view_dirs.append(rel_path)
            continue

        # skip specified paths
        if rel_path in IGNORE_PATHS:
            continue

        # skip specified directories
        skip_dir = False
        for ignore_dir in IGNORE_DIRS:
            if rel_path.startswith(ignore_dir):
                skip_dir = True
                break
        if skip_dir:
            continue

        dir_name, file_name = os.path.split(rel_path)
        file_base_name, extension = os.path.splitext(file_name)

        # skip specified extensions
        if extension in IGNORE_EXTENSIONS:
            continue

        extensions.add(extension)

        # populate file data
        if dir_name not in filtered_file_data:
            filtered_file_data[dir_name] = []
        filtered_file_data[dir_name].append(
            {"path": rel_path, "name": file_name, "extension": extension[1:].upper()}
        )

    print("detected the following extensions:")
    pprint(extensions)
    print("directories with 'index.md':")
    pprint(custom_view_dirs)

    # write to files
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    with open(os.path.join(OUTPUT_DIR, PATHS_FILE), "w") as out_file:
        yaml.dump(filtered_file_data, out_file)
    with open(os.path.join(OUTPUT_DIR, CUSTOM_DIR_FILE), "w") as out_file:
        yaml.dump(custom_view_dirs, out_file)


if __name__ == "__main__":
    main()
