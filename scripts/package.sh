#!/usr/bin/env bash
# Validate the skill and build an uploadable zip in dist/ (for Customize > Skills > Upload a skill).
# Usage: ./scripts/package.sh
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/validate.py

SKILLS_DIR="plugins/ai-learning-coach/skills"
VERSION=$(python3 -c "import json; print(json.load(open('$SKILLS_DIR/ai-learning-coach/config.json'))['skill_version'])")
mkdir -p dist
OUT="dist/ai-learning-coach-${VERSION}.zip"
rm -f "$OUT"
(cd "$SKILLS_DIR" && zip -rq "../../../$OUT" ai-learning-coach -x '*.DS_Store')
echo "Built $OUT"
