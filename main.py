#!/usr/bin/env python3
"""Summarize field presence and type drift in JSON Lines data."""
import argparse
from collections import Counter, defaultdict
import json
import sys

def infer_type(value):
    if value is None: return "null"
    if isinstance(value, bool): return "boolean"
    if isinstance(value, int): return "integer"
    if isinstance(value, float): return "number"
    if isinstance(value, str): return "string"
    if isinstance(value, list): return "array"
    if isinstance(value, dict): return "object"
    return type(value).__name__

def summarize_lines(lines, error_limit=20):
    types, present, shapes = defaultdict(set), Counter(), Counter()
    errors, records = [], 0
    for line_number, raw in enumerate(lines, start=1):
        if not raw.strip(): continue
        try: value = json.loads(raw)
        except json.JSONDecodeError as exc:
            if len(errors) < error_limit: errors.append({"line":line_number,"error":exc.msg})
            continue
        if not isinstance(value, dict):
            if len(errors) < error_limit: errors.append({"line":line_number,"error":"record is not a JSON object"})
            continue
        records += 1
        shapes[tuple(sorted(value))] += 1
        for key, item in value.items():
            present[key] += 1
            types[key].add(infer_type(item))
    fields = {key:{"types":sorted(types[key]),"present":present[key],"missing":records-present[key]} for key in sorted(types)}
    return {"records":records,"fields":fields,"shapes":[{"keys":list(k),"count":v} for k,v in shapes.most_common()],"errors":errors}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",help="JSONL path or - for stdin")
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    try:
        if args.input=="-": result=summarize_lines(sys.stdin)
        else:
            with open(args.input,encoding="utf-8") as stream: result=summarize_lines(stream)
    except OSError as exc:
        print(f"jsonl-schema-drift: {exc}",file=sys.stderr); return 2
    if args.json: print(json.dumps(result,indent=2))
    else:
        print(f"Valid object records: {result['records']}")
        for key,details in result["fields"].items():
            print(f"- {key}: {', '.join(details['types'])}; missing in {details['missing']} records")
        print(f"Record shapes: {len(result['shapes'])}; malformed/non-object lines: {len(result['errors'])}")
        for error in result["errors"]: print(f"Line {error['line']}: {error['error']}",file=sys.stderr)
    return 1 if result["errors"] else 0

if __name__=="__main__": raise SystemExit(main())
