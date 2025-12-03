import os
import re
import pandas as pd

ROOT = "data"

CONDITIONS = {
    "silence": "silence.txt",
    "whitenoise": "whitenoise.txt",
    "instrumental": "instrumental.txt",
    "pop": "pop.txt"
}

def parse_digit_span_from_file(filepath):
    """
    Extract the maximum correct sequence length ("digit span")
    from a PsyToolkit digit-span raw data file.
    """
    max_correct_length = 0

    with open(filepath, "r") as f:
        lines = f.readlines()

    # Look only at lines containing correctness info
    # Example: 2 4 5 0 // 10 2 4 // ...
    correctness_pattern = re.compile(r'^\s*\d+\s+(\d+)\s+(\d+)\s+(\d+)\s+//')

    for line in lines:
        match = correctness_pattern.match(line)
        if match:
            correct_count = int(match.group(1))
            total_digits = int(match.group(2))
            error_flag = int(match.group(3))

            if error_flag == 0:
                if total_digits > max_correct_length:
                    max_correct_length = total_digits

    return max_correct_length


def extract_all_data(root_folder):
    """
    Walk through all participant folders and extract digit spans for all 4 conditions.
    Returns a DataFrame with columns: participant, condition, digit_span
    """
    rows = []

    for participant in sorted(os.listdir(root_folder)):
        part_path = os.path.join(root_folder, participant)
        
        if not os.path.isdir(part_path) or not participant.startswith("participant_"):
            continue

        participant_id = participant.replace("participant_", "")

        for condition, filename in CONDITIONS.items():
            file_path = os.path.join(part_path, filename)

            if not os.path.exists(file_path):
                print(f"WARNING: Missing file {file_path}, skipping.")
                continue

            span = parse_digit_span_from_file(file_path)

            rows.append({
                "participant": int(participant_id),
                "condition": condition,
                "digit_span": span
            })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = extract_all_data(ROOT)

    df = df.sort_values(by=["participant", "condition"])

    df.to_csv("digit_span_clean.csv", index=False)

    print("\nExtraction complete!")
    print(df)
