# NeoLex
Neology, Lexicology & Lexicography

(Funded by CNRS-CRLAO-EHESS)

## Overview

**NeoLex** is a computational lexicography project dedicated to the identification,
analysis, and modeling of neological units from **Chinese and Vietnamese corpora**.
The project combines **corpus linguistics**, **natural language processing (NLP)**,
and **lexical modeling**, with a particular focus on **terminology and neology studies**.

---

## Repository Contents

The repository includes:

- Corpus data (raw and cleaned)
- Jupyter notebooks documenting each processing step
- Python scripts for lexical exploration
- Structured JSON outputs for neological resources

---

## Repository Structure

```text
NeoLex/
│
├── Corpus_data/
│   └── Raw and cleaned corpora
│
├── Token/
│   └── Tokenized data and intermediate files
│
├── Scrapping_Corpus_Chinois.ipynb
│   └── Chinese corpus collection via web scraping
│
├── Step1_23-07_corpus.ipynb
│   └── Corpus preparation and preprocessing
│
├── Step2_07_08Tokenisation.ipynb
│   └── Tokenization and basic NLP processing
│
├── Step_3_Identification.ipynb
│   └── Identification of neological candidates
│
├── Step3_Version_amélioré_neolex.ipynb
│   └── Improved neology detection pipeline
│
├── Step4_evaluation.ipynb
│   └── Evaluation of extracted neological units
│
├── app_chi.py
│   └── Python application for Chinese lexical data
│
├── app_vi.py
│   └── Python application for Vietnamese lexical data
│
├── neo_chi.json
│   └── Structured neological resource (Chinese)
│
├── neo_vi.json
│   └── Structured neological resource (Vietnamese)
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
```

## Workflow

The project follows a step-by-step pipeline:

1. Corpus collection (web scraping, data selection)
2. Corpus preprocessing
3. Tokenization
4. Neological unit identification
5. Lexical structuring (JSON)
6. Evaluation

Each step is documented in a dedicated Jupyter notebook.

---

## Technologies

- Python 3
- Jupyter Notebook
- NLP libraries for Chinese and Vietnamese processing
- JSON for lexical resource representation

---

## Installation

Install dependencies with:

```bash
pip install -r requirements.txt
```
---


## Status

This project is **research-oriented** and currently **under active development**.

---

## Project Team

- **Project Lead**:  
  Huy-Linh DAO  
  (CRLAO, CNRS – INALCO)

- **Developer / Main Contributor**:  
  Lian CHEN 陈恋  
  (CRLAO, CNRS – EHESS - INALCO & LLL, University of Orléans)

- **Collaborator**:  
  Damien NOUVEL  
  (ERTIM, INALCO)

- **Technical Support**:  
  Alexandre DELAPORTE  
  (CNRS, CRLAO – EHESS)
