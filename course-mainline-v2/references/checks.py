"""Stage 2 output quality checks. Usage: python3 checks.py <path-to-output.md>"""
import re, sys

def check(path):
    with open(path) as f:
        content = f.read()
        lines = content.split('\n')

    issues = []

    # 1. Bold balance
    if content.count('**') % 2 != 0:
        issues.append("❌ Bold markers unbalanced")

    # 2. Heading hierarchy (no skips)
    prev = 0
    for i, line in enumerate(lines):
        m = re.match(r'^(#{1,6})\s', line)
        if m:
            lvl = len(m.group(1))
            if lvl > prev + 1 and prev > 0:
                issues.append(f"❌ L{i+1}: heading skip {'#'*prev} → {'#'*lvl}")
            prev = lvl

    # 3. Bold-period: Chinese punctuation inside ** markers
    # Only flag 。！？inside ** (period/exclamation/question are strong signals)
    bp = re.findall(r'\*\*[^*]*[。！？]\*\*', content)
    for b in bp:
        issues.append(f"❌ Bold-period: {b[:60]}")

    # 4. Module count (must be exactly 9)
    h2s = [l.strip()[:50] for l in lines if re.match(r'^## \d\.', l)]
    if len(h2s) != 9:
        issues.append(f"❌ Expected 9 modules, got {len(h2s)}: {h2s}")

    # 5. Section 5 existence
    if '## 5.' not in content:
        issues.append("❌ Missing Section 5 (判断标准)")

    # Summary
    if issues:
        print(f"❌ {len(issues)} issues found:")
        for issue in issues:
            print(f"  {issue}")
        return False
    else:
        print(f"✅ All checks passed ({len(lines)} lines, {len(h2s)} modules, {content.count('**')} bold)")
        return True

if __name__ == '__main__':
    check(sys.argv[1])
