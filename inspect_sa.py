import json

with open('parsed_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('sa_inspection.txt', 'w', encoding='utf-8') as out:
    out.write("=== SA QUESTIONS ===\n")
    for item in data['sa']:
        out.write(f"[{item['id']}] raw: {item['raw']}\n")
        if item['lines']:
            out.write(f"     lines: {item['lines']}\n")
        out.write("-" * 40 + "\n")

    out.write("\n=== ESSAY QUESTIONS ===\n")
    for item in data['essay']:
        out.write(f"[{item['id']}] q: {item['q']}\n")
        out.write("-" * 40 + "\n")
