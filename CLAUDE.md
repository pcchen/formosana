# Formosana Project

## Overview
This project contains linguistic reference tables for Taiwanese Hokkien (台語), including the official Tai-lo (臺灣台語羅馬字拼音方案) syllable table with Taiwanese kana annotations.

## Key Files
- `臺灣台語羅馬字拼音方案音節表_table.md` — Tai-lo syllable table with Taiwanese kana (台灣語假名)

## Taiwanese Kana System

### Cell Format
Each non-empty cell: `romanization kana character` (e.g., `pa パア 巴`)

### Initial Consonant Kana
- Initials mapped to 5 vowel classes (a/i/u/e/o-dan)
- Aspirated consonants (ph, th, kh, tsh): combining dot below (◌̣), e.g., パ̣
- t-row vs ts-row: t uses overline (チ̅/ツ̅), ts does not (チ/ツ)
- g and ng share the same kana row (ガ行)

### Vowel Distinctions
- **o (ヲ) vs oo (オ)**: Two distinct o-vowels
- `-ok`, `-ong`, `-onn` are oo-simplified (use オ, not ヲ) per table footnote
- `-ua`, `-ue`, `-uai`, `-uan`, `-uat`, `-ueh` use o-dan (ヲ for zero initial)

### Special Final Rules
- **-ian, -iat**: Use small ェ (not ァ) — reflects [ɛ] quality
- **-iok, -iong**: Use small ォ (oo-type)
- **-io, -ioh**: Use ヲ (o-type)

### Codas
- Nasal: -m→ム, -n→ヌ, -ng→ン
- Stop: -p→ㇷ゚, -t→ッ, -k→ㇰ
- Glottal -h: small version of preceding vowel kana (ァ/ィ/ゥ/ェ/ォ)

### Syllabic Nasals
- m→ム, hm→フム, ng→ン
- Consonant + ng finals (png, tng, etc.): initial kana (a-dan) + ン

### Nasalization (-nn)
- Visually identical to non-nasalized form (no tone marks used)
