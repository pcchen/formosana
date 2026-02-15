import re

# Read the file
with open("/Users/pcchen/github/pcchen/Claude/formosana/臺灣台語羅馬字拼音方案音節表_1130826.md", "r") as f:
    content = f.read()

# Define initials (longer ones first for matching)
initials = ['tsh', 'ts', 'ph', 'th', 'kh', 'ng', 'p', 'b', 'm', 't', 'n', 'l', 'k', 'g', 's', 'j', 'h']
initial_labels = ['p', 'ph', 'm', 'b', 't', 'th', 'n', 'l', 'k', 'kh', 'g', 'ng', 'ts', 'tsh', 's', 'j', 'h', '-']

# Define finals
finals_list = [
    'a','ah','ai','ainn','ak','am','an','ang','ann','annh',
    'ap','at','au','auh','e','eh','enn','ennh',
    'i','ia','iah','iak','iam','ian','iang','iann','iannh',
    'iap','iat','iau','iauh','iaunn',
    'ih','ik','im','in','ing','inn','innh',
    'io','ioh','iok','iong','ip','it','iu','iuh','iunn',
    'm','mh','mng',  # added mng
    'ng','ngh','nng',  # added nng
    'o','oh','ok','om','ong','onn','oo','ooh','op',
    'u','ua','uah','uai','uainn','uan','uann','uat',
    'ue','ueh','uh','ui','un','ut',
    'png','tng','kng','sng',  # syllabic nasals with specific initials
]

# Build a dict: (initial, final) -> [characters]
grid = {}

# Parse syllable-character pairs from the content
# Pattern: a syllable (lowercase letters) optionally followed by a character
lines = content.split('\n')

def split_syllable(syl):
    """Split a syllable into (initial, final)"""
    for init in ['tsh', 'ts', 'ph', 'th', 'kh', 'ng', 'p', 'b', 'm', 't', 'n', 'l', 'k', 'g', 's', 'j', 'h']:
        if syl.startswith(init):
            final = syl[len(init):]
            if final:
                return (init, final)
    # Zero initial
    return ('-', syl)

# Collect all syllable-character entries
entries = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    # Skip header/metadata lines
    if line.startswith('臺灣') or line.startswith('960117') or line.startswith('1130826') or line.startswith('序號') or line.startswith('聲母') or line.startswith('韻母') or line.startswith('第') or line.startswith('備註'):
        continue
    # Skip numbered final definitions (like "01 a", "02 ah")
    if re.match(r'^\d+\s+\w+$', line):
        continue
    
    # Find all syllable-character pairs in the line
    # Pattern: word_of_lowercase_letters followed optionally by Chinese char(s)
    # Handle entries like "kang 江 khang 空" or "pa 巴" or "pah 百"
    tokens = re.findall(r'([a-z]+)\s*([\u4e00-\u9fff]*)', line)
    for syl, char in tokens:
        # Skip if it looks like a standalone initial label
        if syl in ['p','ph','m','b','t','th','n','l','k','kh','g','ng','ts','tsh','s','j','h'] and not char:
            # Check if this is just an initial header
            # But some are valid syllables like 'm 姆'
            if syl == 'm' and not char:
                continue
            if syl in ['ng'] and not char:
                continue
            continue
        
        initial, final = split_syllable(syl)
        if final:
            key = (initial, final)
            if key not in grid:
                grid[key] = []
            if char:
                grid[key].append(char)
            elif key not in grid:
                grid[key] = []

# Get all unique finals that appear
all_finals_used = sorted(set(f for (i, f) in grid.keys()), 
                          key=lambda x: finals_list.index(x) if x in finals_list else 999)

# For finals not in our predefined list, add them at the end
for f in sorted(set(f for (i, f) in grid.keys())):
    if f not in all_finals_used:
        all_finals_used.append(f)

# Generate the markdown table
header = '| 韻母 | ' + ' | '.join(initial_labels) + ' |'
separator = '|' + '|'.join(['---'] * (len(initial_labels) + 1)) + '|'

print(header)
print(separator)

for final in all_finals_used:
    row = [final]
    for init in initial_labels:
        init_key = init if init != '-' else '-'
        key = (init_key, final)
        if key in grid:
            chars = ''.join(grid[key])
            syl = (init if init != '-' else '') + final
            if chars:
                row.append(f'{syl} {chars}')
            else:
                row.append(f'{syl}')
        else:
            row.append('')
    print('| ' + ' | '.join(row) + ' |')

