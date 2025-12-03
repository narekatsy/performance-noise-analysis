import pandas as pd
import pingouin as pg
import ptitprince as pt
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned digit-span dataset
df = pd.read_csv("digit_span_clean.csv")

print("===== Loaded Data =====")
print(df.head())

# ------------------------------------------------------------
# 1. Basic Descriptive Statistics
# ------------------------------------------------------------
print("\n===== Descriptive Statistics =====")
desc = df.groupby("condition")["digit_span"].describe()
print(desc)

# ------------------------------------------------------------
# 2. Repeated-Measures ANOVA (One-Way)
# ------------------------------------------------------------
print("\n===== Repeated-Measures ANOVA (One-Way) =====")

anova = pg.rm_anova(
    dv="digit_span",
    within="condition",
    subject="participant",
    data=df,
    detailed=True
)

print(anova)

# ------------------------------------------------------------
# 3. Post-Hoc Pairwise Comparisons (with Holm correction)
# ------------------------------------------------------------
print("\n===== Post-Hoc Pairwise Comparisons =====")

posthoc = pg.pairwise_ttests(
    dv="digit_span",
    within="condition",
    subject="participant",
    data=df,
    padjust="holm"
)

print(posthoc)

# ------------------------------------------------------------
# 4. Visualization
# ------------------------------------------------------------

# Raincloud plot for distribution of scores
plt.figure(figsize=(10, 6))
pt.RainCloud(
    x='condition',
    y='digit_span',
    data=df,
    palette='Set2',
    bw=.2,
    width_viol=.6,
    width_box=.3,
    orient='v'
)
plt.title("Digit Span Distribution Across Auditory Conditions")
plt.show()

# Violin plot for distribution of scores
plt.figure(figsize=(10, 6))
sns.violinplot(
    x="condition",
    y="digit_span",
    data=df,
    inner=None,
    palette="Set2"
)
sns.swarmplot(
    x="condition",
    y="digit_span",
    data=df,
    color="black",
    alpha=0.6
)
plt.title("Digit Span Performance Across Conditions")
plt.show()

# Bar plot for mean digit span with error bars
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df, 
    x='condition', 
    y='digit_span', 
    estimator='mean',     # computes mean per condition
    errorbar='sd',        # standard deviation (simple)
    palette='Set2'
)

plt.title("Mean Digit Span by Condition")
plt.ylabel("Digit Span")
plt.xlabel("Condition")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# SAVE RESULTS TO TXT FILE
# ------------------------------------------------------------
with open("digit_span_results.txt", "w") as f:
    f.write("===== Loaded Data (Head) =====\n")
    f.write(df.head().to_string())
    f.write("\n\n===== Descriptive Statistics =====\n")
    f.write(desc.to_string())
    f.write("\n\n===== Repeated-Measures ANOVA (One-Way) =====\n")
    f.write(anova.to_string())
    f.write("\n\n===== Post-Hoc Pairwise Comparisons =====\n")
    f.write(posthoc.to_string())

print("Results saved to digit_span_results.txt")


