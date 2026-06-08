# 1MS041 — Exam Reference Repository

Open-internet exam reference for the January 2026 exam.

## Structure

```
exam_repo/
├── cheatsheets/          # Formula summaries by topic
│   └── 01_probability_and_bayes.md
├── snippets/             # Reusable, copy-paste-ready functions
│   └── probability_utils.py
└── solutions/            # Solved practice exam problems
    └── 2022/
        └── problem1.py
```

## Cheat Sheets
| File | Topics covered |
|---|---|
| `01_probability_and_bayes.md` | Binomial PMF, conditional probability, Bayes, Hoeffding CI |

## Snippets
| File | Contains |
|---|---|
| `probability_utils.py` | `binomial`, `binom_pmf/cdf/sf/tail`, `hoeffding_interval/epsilon` |

## Solutions
| File | Problem | Key concepts |
|---|---|---|
| `2022/problem1.py` | Prob. warmup — threshold T | Compound binomial, law of total probability, conditional probability |
