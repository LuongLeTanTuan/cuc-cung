import json

with open('parsed_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('mcq_inspection.txt', 'w', encoding='utf-8') as out:
    for q in data['mcq']:
        out.write(f"Câu {q['id']}. {q['q']}\n")
        letters = ['A', 'B', 'C', 'D']
        for i, opt in enumerate(q['opts']):
            out.write(f"  {letters[i]}. {opt}\n")
        out.write("\n")

print(f"Wrote {len(data['mcq'])} MCQs to mcq_inspection.txt")
