#!/usr/bin/env bash
# Validate the skill and build an uploadable zip in dist/.
# Usage: ./scripts/package.sh
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/validate.py

VERSION=$(python3 -c "import json; print(json.load(open('skills/ai-learning-coach/config.json'))['skill_version'])")
mkdir -p dist
OUT="dist/ai-learning-coach-${VERSION}.zip"
rm -f "$OUT"
(cd skills && zip -rq "../$OUT" ai-learning-coach -x '*.DS_Store')
echo "Built $OUT"
