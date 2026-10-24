#!/usr/bin/env python3
"""Check the skill before packaging: frontmatter, config, command table, reference files, version.

Usage: python3 scripts/validate.py
Exits non-zero and lists every problem found.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "plugins", "ai-learning-skill", "skills", "ai-learning-skill")
errors = []


def read(path):
    with open(os.path.join(SKILL, path), encoding="utf-8") as f:
        return f.read()


# --- SKILL.md frontmatter
skill_md = read("SKILL.md")
fm = re.match(r"^---\n(.*?)\n---\n", skill_md, re.S)
if not fm:
    errors.append("SKILL.md: missing YAML frontmatter")
    meta = {}
else:
    meta = dict(
        (k.strip(), v.strip()) for k, v in (line.split(":", 1) for line in fm.group(1).splitlines() if ":" in line)
    )
name = meta.get("name", "")
desc = meta.get("description", "")
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
    errors.append(f"SKILL.md: name '{name}' must be kebab-case, at most 64 characters")
if "claude" in name or "anthropic" in name:
    errors.append("SKILL.md: name must not contain 'claude' or 'anthropic'")
if os.path.basename(SKILL) != name:
    errors.append(f"SKILL.md: name '{name}' must match the folder name '{os.path.basename(SKILL)}'")
if not desc or len(desc) > 1024 or "<" in desc or ">" in desc:
    errors.append("SKILL.md: description must be 1-1024 characters with no angle brackets")

# --- command table
rows = []
for line in skill_md.splitlines():
    m = re.match(r"^\| `([a-z-]+)` \|(.*)\|$", line)
    if m:
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) != 5:
            errors.append(f"command table: row for '{m.group(1)}' needs 6 columns")
            continue
        rows.append((m.group(1), *cells))
if not rows:
    errors.append("SKILL.md: command table not found")
seen = set()
for cmd, group, status, what, example, ref in rows:
    status, ref = status.strip(), ref.strip()
    if cmd in seen:
        errors.append(f"command table: '{cmd}' listed twice")
    seen.add(cmd)
    if status not in ("v1", "coming soon"):
        errors.append(f"command table: '{cmd}' has unknown status '{status}'")
    if status == "v1":
        expected = f"references/{cmd}.md"
        if ref != expected:
            errors.append(f"command table: '{cmd}' should point to {expected}")
        elif not os.path.exists(os.path.join(SKILL, ref)):
            errors.append(f"missing reference file {ref}")
        else:
            body = read(ref)
            for field in ("**Summary:**", "**Options:**", "**Examples:**", "**Next:**"):
                if field not in body:
                    errors.append(f"{ref}: header is missing {field} (help reads it)")
for f in os.listdir(os.path.join(SKILL, "references")):
    if f.endswith(".md") and f[:-3] not in seen:
        errors.append(f"references/{f} has no row in the command table")

# --- config and version
try:
    cfg = json.loads(read("config.json"))
    for key in ("hub", "agent_index"):
        url = cfg.get("notion", {}).get(key, "")
        if not re.match(r"^https://(app\.notion\.com|www\.notion\.so|[a-z0-9-]+\.notion\.site)/", url):
            errors.append(f"config.json: notion.{key} is not a Notion URL")
    version = cfg.get("skill_version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("config.json: skill_version must look like 1.2.3")
    top = re.search(r"^## (\d+\.\d+\.\d+)", read("CHANGELOG.md"), re.M)
    if not top or top.group(1) != version:
        errors.append(f"CHANGELOG.md: newest entry must be version {version}")
except json.JSONDecodeError as e:
    errors.append(f"config.json: invalid JSON ({e})")

# --- plugin and marketplace manifests (for "Add marketplace" installs)
def load(path):
    try:
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f"{path}: missing or invalid JSON ({e})")
        return {}


plugin = load("plugins/ai-learning-skill/.claude-plugin/plugin.json")
market = load(".claude-plugin/marketplace.json")
if plugin.get("name") != name:
    errors.append(f"plugin.json: name must be '{name}'")
for key in ("name", "owner", "plugins"):
    if key not in market:
        errors.append(f"marketplace.json: missing '{key}'")
entries = [p for p in market.get("plugins", []) if p.get("name") == name]
if not entries:
    errors.append(f"marketplace.json: no plugin entry named '{name}'")
else:
    src = entries[0].get("source", "")
    if ".." in src or not os.path.isdir(os.path.join(ROOT, src)):
        errors.append(f"marketplace.json: source '{src}' must be an existing folder inside the repo")
    if "version" in entries[0] or "version" in plugin:
        errors.append("plugin.json / marketplace.json: leave 'version' out so installs track commits "
                      "(the display version lives in config.json)")

if errors:
    print("Validation failed:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"OK: {name} v{version}, {sum(1 for r in rows if r[2].strip() == 'v1')} v1 commands, "
      f"{sum(1 for r in rows if r[2].strip() == 'coming soon')} coming soon")
