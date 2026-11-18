<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=170&section=header&text=JSONL%20Schema%20Drift&fontColor=ffffff&fontSize=38&animation=fadeIn" alt="JSONL Schema Drift banner" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3000&pause=900&color=14B8A6&center=true&vCenter=true&width=820&lines=See%20how%20record%20keys%20and%20value%20types%20change%20across%20a%20JSONL%20file" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/jsonl-schema-drift)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/jsonl-schema-drift)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/jsonl-schema-drift?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/jsonl-schema-drift)

<img src="assets/illustration.svg" alt="JSONL Schema Drift illustration" width="92%"/>
</div>

## :compass: Overview

A JSON Lines profiler that summarizes field presence, observed value types, and recurring record shapes so data-pipeline changes are easy to spot.

## :sparkles: Features

- :white_check_mark: Reads JSONL one record at a time
- :white_check_mark: Reports missing fields and type changes
- :white_check_mark: Counts recurring record shapes and malformed lines
- :white_check_mark: Emits readable text or machine-friendly JSON

## :clapper: Demo

```bash
python main.py examples/events.jsonl
```

The example runs locally; no hosted service or upload is required.

## :rocket: Quick Start

```bash
python -m pip install -r requirements.txt
python main.py examples/events.jsonl
```

Run `python main.py --help` to see all supported options.

## :toolbox: Tech Stack

- Python 3.10+ standard library
- Automated tests: unittest
- Local-first processing

## :file_folder: Folder Structure

```text
jsonl-schema-drift/
├── main.py
├── requirements.txt
├── tests/test_core.py
├── examples/events.jsonl
└── assets/illustration.svg
```

## :world_map: Roadmap

- [x] Core workflow and CLI
- [x] Example input and tests
- [ ] Additional report formats
- [ ] Continuous integration on supported platforms

## :handshake: Contributing

Issues and pull requests are welcome. Keep changes focused, document behavior changes, and add tests for new features.

## :page_facing_up: License

MIT - see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated wave footer" width="100%"/></div>
