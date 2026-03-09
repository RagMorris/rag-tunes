#!/usr/bin/env python3

import json
import os

tunes = []

for entry in os.scandir("tunes"):
    if not entry.is_file():
        continue

    with open(entry.path) as abc_file:
        title = None
        group = None

        for line in abc_file.readlines():
            title_prefix = "T:"

            if line.startswith(title_prefix):
                if title is None:
                    title = line.removeprefix(title_prefix).strip()

            group_prefix = "G:"

            if line.startswith(group_prefix):
                if group is None:
                    group = line.removeprefix(group_prefix).strip()

        tunes.append({
            "id": entry.name.removesuffix(".abc"),
            "title": f"{title} ({group})"
        })

tunes.sort(key=lambda entry: entry["id"] )

with open("tunes.json", "w") as tunes_file:
    json.dump(tunes, tunes_file, indent=2)

