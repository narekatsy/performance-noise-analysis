# Digit Span & Background Sound Experiment

This repository contains the full workflow for a psychology experiment examining how different background sounds (silence, white noise, instrumental music, pop music) affect working memory performance, measured using a [Digit Span task from PsyToolkit](https://www.psytoolkit.org/experiment-library/rdigitspan.html).

Participants completed the task under four conditions, and the resulting data were saved in `.txt` format and processed with Python to extract accuracy scores and run statistical analyses (repeated-measures ANOVA + post-hoc tests).


## Repository Structure

```bash
performance-noise-analysis/
│
├── data/                       # Participants test results
│   ├── participant_1/
│   │   ├── silence.txt
│   │   ├── whitenoise.txt
│   │   ├── instrumental.txt
│   │   └── pop.txt
│   ├── participant_2/
│   └── ... participant_12/
│
├── extract_digit_span.py       # Script to parse PsyToolkit raw txt files
├── analysis.py                 # Statistical analysis (ANOVA, post-hoc, plots)
├── digit_span_clean.csv        # Cleaned dataset
├── digit_span_results.txt      # Final analysis results
└── README.md
```

## How to Use

1. Clone the repository

```
git clone https://github.com/narekatsy/performance-noise-analysis.git
cd performance-noise-analysis
```

2. Create a virtual environment (optional but recommended)

*On Windows*
```bash
python -m venv venv
venv\Scripts\activate
```

*On macOS/Linux*
```bash
python -m venv venv
source venv/bin/activate
```

3. Install required Python packages

```bash
pip install -r requirements.txt
```

4. Running Data Extraction

```bash
python extract_digit_span.py
```

This generates `digit_span_clean.csv`, contains test data in more structured format for analysis.

5. Running Analysis

```bash
python analysis.py
```

The script outputs:
- Descriptive statistics
- One-way repeated-measures ANOVA
- Holm-corrected pairwise comparisons
- Visualization plots


## Summary of Findings

- **Silence** produced the highest digit-span scores.
- **White noise** produced significantly lower performance than silence.
- Music conditions (pop, instrumental) showed intermediate performance but not significantly different after correction.
