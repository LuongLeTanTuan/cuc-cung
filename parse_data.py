import docx
import json
import re

doc = docx.Document('81 CÂU HỎI MÔN LSĐCSVN - DÀNH CHO SV ÔN TẬP - 2024-2025.docx')
paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

p1_idx = paras.index('Phần 1: CÂU HỎI NHIỀU TÙY CHỌN')
p2_idx = paras.index('Phần 2: CÂU HỎI NGẮN')
p3_idx = paras.index('Phần 3: CÂU HỎI TỰ LUẬN')

p1_text = paras[p1_idx+1:p2_idx]
p2_text = paras[p2_idx+1:p3_idx]
p3_text = paras[p3_idx+1:]

# 1. Parse MCQ (Phần 1: Câu 1 - Câu 45)
mcq_list = []
curr_q = None

for line in p1_text:
    m_q = re.match(r'^Câu\s+(\d+)\.\s*(.*)', line)
    if m_q:
        if curr_q:
            mcq_list.append(curr_q)
        curr_q = {'id': int(m_q.group(1)), 'q': m_q.group(2).strip(), 'opts': []}
        continue
    
    m_opt = re.match(r'^([A-D])\.\s*(.*)', line)
    if m_opt and curr_q:
        curr_q['opts'].append(m_opt.group(2).strip())
    elif curr_q and not curr_q['opts']:
        curr_q['q'] += ' ' + line
    elif curr_q and curr_q['opts']:
        curr_q['opts'][-1] += ' ' + line

if curr_q:
    mcq_list.append(curr_q)

# 2. Parse Short Answer (Phần 2: Câu 46 - Câu 75)
sa_list = []
curr_sa = None

for line in p2_text:
    m_q = re.match(r'^Câu\s+(\d+)\.\s*(.*)', line)
    if m_q:
        if curr_sa:
            sa_list.append(curr_sa)
        content = m_q.group(2).strip()
        # Some lines in docx have both question and answer in one line, or question only
        curr_sa = {'id': int(m_q.group(1)), 'raw': content, 'lines': []}
    else:
        if curr_sa:
            curr_sa['lines'].append(line)

if curr_sa:
    sa_list.append(curr_sa)

# 3. Parse Essay (Phần 3: Câu 76 - Câu 81)
essay_list = []
for line in p3_text:
    m_q = re.match(r'^Câu\s+(\d+)\.\s*(.*)', line)
    if m_q:
        essay_list.append({'id': int(m_q.group(1)), 'q': m_q.group(2).strip()})
    elif essay_list:
        essay_list[-1]['q'] += ' ' + line

data = {
    'mcq': mcq_list,
    'sa': sa_list,
    'essay': essay_list
}

with open('parsed_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Parsed {len(mcq_list)} MCQs, {len(sa_list)} Short Answers, {len(essay_list)} Essays.")
