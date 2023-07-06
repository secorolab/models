import glob
import os
import yaml


ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
SKIP_TOP_DIRS = ["assets", "_data", "script"]
EXTENSIONS = [
    ".json",
    ".provn",
    ".rosparams",
    ".yaml",
    ".svg",
    ".png",
    ".pgm",
    ".stl",
    ".floorplan",
    ".variation",
]
OUTPUT_FILE = "file_paths.yml"
OUTPUT_DIR = os.path.join(ROOT_DIR, "_data")


def main():
    file_list = glob.glob(os.path.join(ROOT_DIR, "**"), recursive=True)
    filtered_file_data = {}
    for file_path in file_list:
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        skip_dir = False
        for skip_top_dir in SKIP_TOP_DIRS:
            if rel_path.startswith(skip_top_dir):
                skip_dir = True
                break
        if skip_dir:
            continue

        dir_name, file_name = os.path.split(rel_path)
        if not dir_name:
            # skip top directory
            continue
        file_base_name, extension = os.path.splitext(file_name)
        if extension not in EXTENSIONS:
            continue

        top_dir = dir_name.split(os.sep)[0]
        if top_dir not in filtered_file_data:
            filtered_file_data[top_dir] = []
        filtered_file_data[top_dir].append(
            {"path": rel_path, "name": file_name, "extension": extension[1:].upper()}
        )

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(os.path.join(OUTPUT_DIR, OUTPUT_FILE), "w") as out_file:
        yaml.dump(filtered_file_data, out_file)


if __name__ == "__main__":
    main()
