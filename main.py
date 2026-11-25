from pathlib import Path

ENTRY = "The market took your money, not your luck. Your luck is still here, hiding under the couch."

output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(ENTRY, encoding="utf-8")
