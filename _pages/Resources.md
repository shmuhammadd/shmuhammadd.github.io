---
layout: page
permalink: /resources/
title: Resources & Tools
nav: true
nav_order: 6
---

Below is a collection of datasets, tools, software, and guides that I have developed or contributed to, all publicly available for the research community.

---

## Quick Navigation

Jump to any section:

- [Datasets](#datasets) — Research datasets for African languages
- [Tools & Software](#tools--software) — NLP tools and platforms
- [Writing NLP Papers](#writing-nlp-papers) — Guides and templates
- [Other Resources](#other-resources) — Tutorials, and more 

---

## Datasets

#### BRIGHTER: Multilingual Emotion Recognition Dataset
- **Description:** Human-annotated textual emotion recognition datasets for 28 languages
- **Languages:** 28 languages including African, Asian, and European languages
- **Task:** Emotion classification
- **Paper:** [ACL 2025 (Best Resource Paper Award)](https://aclanthology.org/2025.acl-long.436/)
- **Access:** [Website](https://brighter-dataset.github.io) • [HuggingFace](https://huggingface.co/brighter-dataset)

<!-- #### IrokoBench: African Languages LLM Benchmark
- **Description:** Comprehensive benchmark for evaluating Large Language Models on African languages
- **Languages:** Multiple African languages
- **Tasks:** Various NLP tasks tailored for African language contexts
- **Paper:** [NAACL 2025 (Outstanding Paper Award)](https://aclanthology.org/2025.naacl-long.139/)
- **Access:** [HuggingFace](https://huggingface.co/collections/masakhane/irokobench)  -->

#### AfriSenti: African Sentiment Analysis Dataset
- **Description:** Twitter sentiment analysis benchmark for African languages
- **Languages:** 14 African languages (Hausa, Yoruba, Igbo, Amharic, Swahili, and more)
- **Task:** Sentiment classification (positive, negative, neutral)
- **Paper:** [EMNLP 2023 (Best Non-archival Paper Award)](https://aclanthology.org/2023.emnlp-main.862.pdf)
- **Access:** [GitHub](https://github.com/afrisenti-semeval/afrisent-semeval-2023) • [HuggingFace](https://huggingface.co/datasets/HausaNLP/AfriSenti-Twitter) • [Leaderboard](https://codalab.lisn.upsaclay.fr/competitions/7320)

#### NaijaSenti: Nigerian Sentiment Analysis Dataset
- **Description:** Sentiment analysis dataset specifically for Nigerian languages and Nigerian Pidgin
- **Languages:** Hausa, Yoruba, Igbo, Nigerian Pidgin
- **Task:** Sentiment classification (positive, negative, neutral)
- **Paper:** [AfricaNLP Workshop](#)
- **Access:** [GitHub](https://github.com/hausanlp/NaijaSenti) • [HuggingFace](https://huggingface.co/datasets/HausaNLP/NaijaSenti-Twitter)

#### AfriHate: Hate Speech & Abusive Language Dataset
- **Description:** Multilingual collection of hate speech and abusive language datasets for African languages
- **Recognition:** IRCAI Global Top 100 AI Projects Award 2025
- **Languages:** Multiple African languages
- **Task:** Hate speech detection, abusive language classification
- **Paper:** [NAACL 2025](https://aclanthology.org/2025.naacl-long.92.pdf)
- **Access:** [GitHub](https://github.com/AfriHate/AfriHate) • [HuggingFace](https://huggingface.co/datasets/afrihate/afrihate)

#### MasakhaNER: Named Entity Recognition Dataset
- **Description:** Named entity recognition datasets for 21 African languages
- **Languages:** Amharic, Hausa, Igbo, Kinyarwanda, Luganda, Luo, Nigerian-Pidgin, Swahili, Wolof, Yoruba, and more
- **Task:** Named entity recognition (PER, LOC, ORG, DATE)
- **Paper:** [TACL 2021](https://aclanthology.org/2021.tacl-1.66.pdf)
- **Access:** [GitHub](https://github.com/masakhane-io/masakhane-ner) • [HuggingFace](https://huggingface.co/datasets/masakhane/masakhaner2) 

#### BLEnD: Everyday Knowledge Dataset
- **Description:** Everyday knowledge in diverse cultures and languages for evaluating cultural understanding in LLMs
- **Languages:** Multiple languages representing diverse cultures
- **Task:** Cultural knowledge understanding and reasoning
- **Paper:** [NeurIPS 2024 (Best Non-archival Paper Award)](https://arxiv.org/pdf/2406.09948)
- **Access:** [GitHub](https://github.com/nlee0212/BLEnD) • [HuggingFace](https://huggingface.co/datasets/nayeon212/BLEnD)

#### SemRel: Semantic Textual Relatedness Dataset
- **Description:** Semantic textual relatedness datasets for African and Asian languages
- **Languages:** 14 languages from Africa and Asia
- **Task:** Semantic similarity and relatedness measurement
- **Paper:** [SemEval 2024 (Honourable Mention)](https://arxiv.org/pdf/2403.18933)
- **Access:** [GitHub](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024) • [arXiv](https://arxiv.org/pdf/2402.08638)

#### AFRIDOC-MT: African Document-level Machine Translation
- **Description:** Document-level machine translation dataset for African languages with document context
- **Languages:** Multiple African languages
- **Task:** Document-level machine translation
- **Paper:** [EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1413.pdf)
- **Access:** [HuggingFace](https://huggingface.co/datasets/masakhane/AfriDocMT)

#### INJONGO: Multimodal Dataset for African Languages
- **Description:** Multimodal benchmark evaluating vision-language models on African cultural contexts
- **Languages:** Multiple African languages
- **Task:** Vision-language understanding and reasoning
- **Paper:** [ACL 2025](https://aclanthology.org/2025.acl-long.464/)
- **Access:** [GitHub](https://github.com/McGill-NLP/Injongo)

#### POLAR: Persuasive & Offensive Language in African Regional Languages
- **Description:** Dataset for detecting persuasive and offensive language in African regional contexts
- **Languages:** African regional languages
- **Task:** Persuasive language detection, offensive language identification
- **Paper:** [arXiv](https://arxiv.org/pdf/2505.20624)
- **Access:** [GitHub](https://github.com/Polar-SemEval/SemEval2026-task9)

#### UHURA: Unified Dataset for African Languages
- **Description:** Comprehensive unified dataset for multiple NLP tasks in African languages
- **Languages:** Multiple African languages
- **Tasks:** Multiple NLP tasks
- **Paper:** [arXiv](https://arxiv.org/pdf/2412.00948)
- **Access:** [GitHub](https://huggingface.co/datasets/masakhane/uhura-truthfulqa)

#### AfroXLMR-Social: African Social Media Dataset
- **Description:** Social media dataset for African languages covering diverse social contexts
- **Languages:** Multiple African languages
- **Task:** Social media text processing and understanding
- **Access:** [HuggingFace](https://huggingface.co/datasets/Tadesse/AfriSocial)

#### Who Wrote This: Hausa Authorship Attribution Dataset
- **Description:** Dataset for authorship attribution and text classification in Hausa
- **Language:** Hausa
- **Task:** Authorship attribution, text classification
- **Paper:** [arXiv](https://arxiv.org/pdf/2503.13101)
- **Access:** [GitHub](https://github.com/TheBangis/hausa_corpus)

#### HausaHate: Hausa Hate Speech Dataset
- **Description:** Hate speech detection dataset specifically for Hausa language
- **Language:** Hausa
- **Task:** Hate speech detection and classification
- **Paper:** [WOAH 2024](https://aclanthology.org/2024.woah-1.5.pdf)
- **Access:** [GitHub](https://github.com/franciellevargas/HausaHate)

#### AfriGSM: African Grade School Math Dataset
- **Description:** Grade school mathematics reasoning dataset for African languages
- **Languages:** Multiple African languages
- **Task:** Mathematical reasoning and problem solving
- **Access:** [HuggingFace](https://huggingface.co/datasets/masakhane/afrimgsm)

#### AfriMMLU: African Massive Multitask Language Understanding
- **Description:** Massive multitask language understanding benchmark for African languages
- **Languages:** Multiple African languages
- **Tasks:** Multiple choice question answering across various domains
- **Access:** [HuggingFace](https://huggingface.co/datasets/masakhane/afrimmlu)

#### AfriXNLI: African Cross-lingual Natural Language Inference
- **Description:** Cross-lingual natural language inference dataset for African languages
- **Languages:** Multiple African languages
- **Task:** Natural language inference (entailment, contradiction, neutral)
- **Access:** [HuggingFace](https://huggingface.co/datasets/masakhane/afrixnli)

#### AfriCOMET: African Machine Translation Evaluation Metric
- **Description:** Evaluation metric specifically designed for assessing machine translation quality in African languages
- **Languages:** Multiple African languages
- **Task:** Machine translation evaluation
- **Access:** [GitHub](https://github.com/masakhane-io/africomet)

#### MasakhaNEWS: African Language News Classification
- **Description:** News topic classification dataset for African languages
- **Languages:** Multiple African languages
- **Task:** News topic classification
- **Access:** [HuggingFace](https://huggingface.co/datasets/masakhane/masakhanews)

#### MasakhaPOS: African Language Part-of-Speech Tagging
- **Description:** Part-of-speech tagging dataset for African languages
- **Languages:** Multiple African languages
- **Task:** Part-of-speech tagging
- **Access:** [HuggingFace](https://huggingface.co/datasets/masakhane/masakhapos)

#### HaVQA: Hausa Visual Question Answering
- **Description:** Visual question answering dataset for Hausa language
- **Language:** Hausa
- **Task:** Visual question answering
- **Access:** [GitHub](https://github.com/shantipriyap/HausaVQA)

#### Hausa Visual Genome
- **Description:** Visual genome dataset with Hausa language annotations for image understanding
- **Language:** Hausa
- **Task:** Image captioning, visual understanding
- **Access:** [HuggingFace](https://huggingface.co/datasets/HausaNLP/HausaVG)

#### HERDPhobia: Hate Speech and Extreme Religious Discourse Dataset
- **Description:** Dataset focusing on hate speech and extreme religious discourse in Hausa
- **Language:** Hausa
- **Task:** Hate speech detection, religious discourse analysis
- **Access:** [GitHub](https://github.com/hausanlp/HERDPhobia)

#### MAFAND-MT: Machine Translation for African Languages
- **Description:** Machine translation dataset for African languages
- **Languages:** Multiple African languages
- **Task:** Machine translation
- **Access:** [GitHub](https://github.com/masakhane-io/lafand-mt)

#### FLORES Fix for Africa
- **Description:** Corrected and improved version of FLORES evaluation dataset for African languages
- **Languages:** African languages in FLORES
- **Task:** Machine translation evaluation
- **Access:** [GitHub](https://github.com/dsfsi/flores-fix-4-africa)

#### Nigerian Speech Corpus
- **Description:** Large-scale speech corpus for major Nigerian languages
- **Funding:** Lacuna Fund ($120,000)
- **Languages:** Hausa, Yoruba, Igbo, and Nigerian Pidgin
- **Tasks:** Automatic speech recognition, text-to-speech synthesis
- **Status:** In development
- **Access:** [Project Website](#)

---

## Tools & Software

<!-- #### HausaNLP Toolkit
- **Description:** Comprehensive NLP toolkit for Hausa language processing
- **Features:** Tokenization, POS tagging, lemmatization, sentiment analysis, named entity recognition
- **Installation:** `pip install hausanlp`
- **Documentation:** [Read the Docs](#)
- **Repository:** [GitHub](#) -->

#### Hausa Dictionary (Kamusun Hausa)
- **Description:** An online lexicon providing standardized Hausa definitions, examples, and usage
- **Features:** Comprehensive Hausa-English dictionary, example sentences, pronunciation guide, standardized definitions
- **Access:** [https://kamusunhausa.hausanlp.org/](https://kamusunhausa.hausanlp.org/)

#### Hausa Catalogue
- **Description:** A centralized repository indexing datasets, benchmarks, and resources for Hausa NLP research
- **Features:** Searchable database of datasets, research papers, models, and tools for Hausa language
- **Access:** [https://catalog.hausanlp.org](https://catalog.hausanlp.org)

#### Annotate Platform
- **Description:** A lightweight web-based annotation platform for text classification, translation, and sequence labeling
- **Features:** Multi-task annotation support, collaborative annotation, quality control, export to standard formats
- **Use Cases:** Text classification, machine translation, named entity recognition, sentiment labeling
- **Access:** [https://annotate.hausanlp.org](https://annotate.hausanlp.org)

#### NLPQuiz
- **Description:** Interactive quiz platform for learning and testing NLP concepts
- **Features:** Educational quizzes, progress tracking, concept reinforcement
- **Access:** [https://nlpquiz.hausanlp.org/auth/login](https://nlpquiz.hausanlp.org/auth/login)

#### Speech Annotation Bot
- **Description:** A Telegram-based tool for collecting speech data in low-connectivity environments; optimized for mobile users
- **Features:** Mobile-first design, works in low-bandwidth areas, Telegram integration, easy audio collection
- **Use Cases:** Speech corpus collection, crowdsourced pronunciation data, dialect documentation
- **Platform:** Telegram Bot
- **Languages:** Hausa and other low-resource languages

<!-- #### AfriNLP Tools Suite
- **Description:** Collection of NLP tools for processing 20+ African languages
- **Features:** Multi-language support, pre-trained models, easy-to-use API, integration with HuggingFace and spaCy
- **Repository:** [GitHub](#)
- **Documentation:** [Website](#) -->

<!-- #### MasakhaNER Model Zoo
- **Description:** Pre-trained named entity recognition models for African languages
- **Models Available:** BERT, RoBERTa, XLM-R, AfroXLMR-based models
- **Languages:** 21+ African languages
- **Repository:** [GitHub](#)
- **Models:** [HuggingFace Model Hub](#) -->
<!-- 
#### AfriSenti Models
- **Description:** Pre-trained sentiment analysis models for African languages
- **Models Available:** Multilingual and language-specific fine-tuned models
- **Languages:** 14 African languages
- **Repository:** [GitHub](#)
- **Models:** [HuggingFace Model Hub](#) -->

<!-- #### Open Data Collection Platform
- **Description:** Platform and playbook for ethical data collection in low-resource language contexts
- **Funding:** $430,000 grant (2025)
- **Features:** Web annotation interface, quality control mechanisms, participant management, data validation tools, multi-language support
- **Status:** In active development
- **Repository:** [GitHub](#)
- **Documentation:** [Website](#) -->

---

## Writing NLP Papers

#### Paper Templates & Examples
- **ACL Conference Templates:**
  - [ACL 2025 LaTeX Template (Overleaf)](#)
  - [NAACL Paper Template](#)
  - [EMNLP Submission Template](#)

- **Example Papers from My Work:**
  - [Dataset Paper Example](#) — BRIGHTER (ACL 2025)
  - [Shared Task Paper Example](#) — SemEval Task 11
  - [Benchmark Paper Example](#) — IrokoBench (NAACL 2025)
  - [System Description Example](#) — AfriSenti Shared Task

#### Writing Guides & Best Practices
- **Essential Reading:**
  - [ACL Author Guidelines](https://github.com/acl-org/acl-style-files)
  - [How to Write a Strong NLP Paper](#)
  - [Effective Abstract Writing for ML/NLP](#)
  - [Results & Analysis Section Guide](#)
  - [Common Pitfalls to Avoid in NLP Papers](#)

- **My Personal Recommendations:**
  - Start with a clear research question and contribution statement
  - Use active voice and concise language
  - Include comprehensive error analysis and ablation studies
  - Make your code and data publicly available
  - Get feedback early and often from colleagues
  - Address limitations and ethical considerations explicitly

#### LaTeX Tips & Resources
- **Useful LaTeX Packages:**
  - `booktabs` — Professional-looking tables
  - `algorithm2e` — Algorithm formatting
  - `tikz` — Diagrams and figures
  - `natbib` or `biblatex` — Bibliography management
  - `hyperref` — Cross-references and URLs

- **Helpful Tools:**
  - [Overleaf](https://www.overleaf.com/) — Online collaborative LaTeX editor
  - [Tables Generator](https://www.tablesgenerator.com/) — Quick table creation
  - [Detexify](https://detexify.kirelabs.org/classify.html) — Find LaTeX symbols by drawing

#### Understanding the Peer Review Process
- **Typical Timeline:**
  - Submission → Review assignment (2-3 weeks)
  - Review period (6-8 weeks)
  - Author response period (1 week)
  - Final decision (2-4 weeks after response)

- **Tips for Strong Author Responses:**
  - Be respectful and professional in all responses
  - Address each reviewer concern point-by-point
  - Provide specific line numbers for changes made
  - Acknowledge valid criticisms graciously
  - Clarify misunderstandings politely with evidence

- **Additional Resources:**
  - [How to Write an Effective Author Response](#)
  - [Dealing with Paper Rejection Constructively](#)
  - [Ethics in NLP Research](#)
  - [ACL Code of Ethics](https://www.aclweb.org/portal/content/acl-code-ethics)

---

## Tipsa and Resources

#### Tutorials & Workshop Materials
- **Video Tutorials:**
#### Community & Collaboration
- **Research Organizations:**
  - [HausaNLP](https://hausanlp.github.io/) — Hausa language NLP research group
  - [Arewa Data Science Academy](https://arewadatascience.github.io/) — Free AI/ML training for underserved students
  - [Masakhane](https://www.masakhane.io/) — Grassroots African NLP community


- **Tips for Successful Grant Applications:**
  - Clearly articulate the problem and potential impact
  - Demonstrate strong community involvement and partnerships
  - Include realistic budgets with detailed justifications
  - Highlight sustainability and scalability plans
  - Show evidence of preliminary work or pilot studies

## Acknowledgments

These resources were made possible through awosome collaborators  and generous funding support from:
- Google (DeepMind Academic Fellowship)
- Lacuna Fund
- Oracle Cloud Infrastructure (OCI)
- Nigerian TETFund
- Wikimedia Foundation
- University of Porto
- Imperial College London
- And countless volunteers and community members who contributed their time and expertise

---

*Last updated: December 2025*