"""Final checks for the DeepThink Markdown content.

Run from the repository root:   python3 tools/verify_content.py

1. Every local link and image in every .md file points to an existing file,
   and every #anchor exists (GitHub heading rules or <a id="...">).
2. Every Python program in Chapter 3 runs and prints exactly the
   "Expected output" block that follows it.
3. The Little Man Computer program of the Chapter 1 lab produces the
   memory contents and output given in the answer key.
4. Every Test Bank question Q1..Qn has exactly one answer.
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
failures = []


def gslug(text):
    t = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'[*`]', '', t).strip().lower()
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'[^\w\- ]', '', t, flags=re.U)
    return t.replace(' ', '-')


def anchors(path):
    used, out, code = {}, set(), False
    for line in open(path, encoding='utf-8'):
        if line.startswith('```'):
            code = not code
            continue
        if code:
            continue
        m = re.match(r'^(#{1,6}) (.*)$', line.rstrip('\n'))
        if m:
            b = gslug(m.group(2))
            n = used.get(b, 0)
            used[b] = n + 1
            out.add(b if n == 0 else f'{b}-{n}')
        out.update(re.findall(r'<a id="([^"]+)"', line))
    return out


# 1. links, images, anchors
checked = 0
for dp, dn, fn in os.walk(ROOT):
    if '.git' in dp:
        continue
    for f in fn:
        if not f.endswith('.md'):
            continue
        p = os.path.join(dp, f)
        txt = re.sub(r'```.*?```', '', open(p, encoding='utf-8').read(), flags=re.S)
        for target in re.findall(r'!?\[[^\]]*\]\(([^)\s]+)\)', txt) + re.findall(r'<img src="([^"]+)"', txt):
            if target.startswith(('http://', 'https://', 'mailto:')):
                continue
            checked += 1
            file_part, _, frag = target.partition('#')
            tp = os.path.normpath(os.path.join(dp, file_part)) if file_part else p
            if not os.path.exists(tp):
                failures.append(f'missing file: {os.path.relpath(p, ROOT)} -> {target}')
            elif frag and tp.endswith('.md') and frag not in anchors(tp):
                failures.append(f'missing anchor: {os.path.relpath(p, ROOT)} -> {target}')
print(f'[1] links and images checked: {checked}')

# 2. Python programs in Chapter 3
ch3 = open(os.path.join(ROOT, '03-Study-guide', '03-Behaviorist-AI.md'), encoding='utf-8').read()
blocks = list(re.finditer(r'```(\w*)\n(.*?)```', ch3, re.S))
n_py = 0
for i, m in enumerate(blocks):
    if m.group(1) != 'python':
        continue
    n_py += 1
    run = subprocess.run([sys.executable, '-I', '-c', m.group(2)], capture_output=True, text=True, timeout=30)
    expected = blocks[i + 1].group(2).strip() if i + 1 < len(blocks) else ''
    if run.returncode != 0 or run.stdout.strip() != expected:
        failures.append(f'Python program {n_py} in Chapter 3: output differs from the expected output')
print(f'[2] Python programs run: {n_py}')

# 3. Little Man Computer lab program (Chapter 1, Section 1.6)
OPS = {'ADD': 100, 'SUB': 200, 'STA': 300, 'LDA': 500, 'BRA': 600, 'BRZ': 700, 'BRP': 800, 'INP': 901, 'OUT': 902, 'HLT': 0}
ch1 = open(os.path.join(ROOT, '03-Study-guide', '01-Hardware.md'), encoding='utf-8').read()
lab = re.search(r'```text\n(\s+LDA FIVE.*?)```', ch1, re.S).group(1)
rows = [l.split('//')[0].split() for l in lab.splitlines() if l.strip()]
labels = {r[0]: i for i, r in enumerate(rows) if r[0] not in OPS and r[0] != 'DAT'}
mem = [0] * 100
for i, r in enumerate(rows):
    r = r[1:] if r[0] in labels else r
    mem[i] = int(r[1]) if r[0] == 'DAT' else OPS[r[0]] + (labels[r[1]] if len(r) > 1 else 0)
code = [f'{x:03d}' for x in mem[:8]]
pc = acc = 0
out = []
while mem[pc] != 0:
    ins = mem[pc]
    pc += 1
    op, a = divmod(ins, 100)
    if op == 1: acc += mem[a]
    elif op == 3: mem[a] = acc
    elif op == 5: acc = mem[a]
    elif ins == 902: out.append(acc)
if code != ['505', '106', '307', '902', '000', '005', '003', '000'] or out != [8] or mem[7] != 8:
    failures.append(f'LMC lab: got {code}, output {out}')
print(f'[3] LMC lab program: memory {", ".join(code)} -> output {out}')

# 4. Test Bank answers
tb = open(os.path.join(ROOT, '04-Test-bank', 'Test-Bank.md'), encoding='utf-8').read()
qs = [int(x) for x in re.findall(r'<a id="q(\d+)"></a>', tb)]
key = tb[tb.index('## Answer Key'):]
ans = [int(x) for x in re.findall(r'^\*\*(\d+)\.', key, re.M)]
if qs != list(range(1, len(qs) + 1)) or sorted(ans) != qs:
    failures.append('Test Bank: question numbers and answers do not match')
print(f'[4] Test Bank: {len(qs)} questions, {len(ans)} answers')

print('\nRESULT:', 'all checks passed' if not failures else f'{len(failures)} problem(s)')
for f in failures:
    print(' -', f)
sys.exit(1 if failures else 0)
