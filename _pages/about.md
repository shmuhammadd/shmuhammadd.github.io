---
layout: about
title: about
permalink: /
subtitle: "Imperial College London. Google DeepMind Academic Fellow. Co-founder of <a href='https://hausanlp.github.io/'>HausaNLP</a>. Founder of <a href='https://arewadatascience.github.io/'>Arewa Data Science Academy</a>."

# Hero header (rendered by _layouts/about.liquid)
role: Google DeepMind Academic Fellow
role_org: Imperial College London
role_url: https://www.imperial.ac.uk/
tagline: "I work on natural language processing for low-resource African languages — building open datasets and benchmarks, using NLP for computational social science, and making multilingual large language models better aligned and safer."

profile:
  align: right
  image: prof_picold.jpg
  image_circular: false
news: false  # Disable auto injection so we can control position
selected_papers: false
social: false
---

<div class="hiring-banner">
  <span class="hiring-badge">Hiring</span>
  <span class="hiring-text">I am hiring <strong>4 postdocs in LLM alignment</strong> at Imperial College London. Interested? <a href="mailto:shamsuddeen2004@gmail.com">Reach out via email</a>.</span>
</div>

<style>
.hiring-banner {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  flex-wrap: wrap;
  border: 1px solid var(--global-theme-color);
  border-left: 4px solid var(--global-theme-color);
  border-radius: 8px;
  padding: 0.8rem 1rem;
  margin: 0 0 1.6rem;
  background: var(--global-card-bg-color);
}

.hiring-badge {
  flex-shrink: 0;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #ffffff;
  background: var(--global-theme-color);
  border-radius: 999px;
  padding: 0.25rem 0.7rem;
}

.hiring-text {
  font-size: 0.97rem;
  line-height: 1.5;
  color: var(--global-text-color);
}

.hiring-text a {
  color: var(--global-theme-color);
  font-weight: 600;
}
</style>

I am a Google DeepMind Academic Fellow and an Advanced Research Fellow at Imperial College London. I also serve as a Senior Lecturer (Assistant Professor) at the Faculty of Computing, Bayero University, Kano, Nigeria, and as a Visiting Professor at the African Institute of Mathematical Sciences in Cameroon and South Africa, as well as at York St John University.

I received my PhD from the University of Porto, Portugal, under the supervision of Professor Pavel Brazdil and Professor Alipio Jorge. Prior to that, I earned an MS in Computer Science from the University of Manchester, UK, and a BSc in Computer Science from Bayero University, Kano, Nigeria.

My research focuses on Natural Language Processing (NLP) for low-resource African languages. I have published in top venues such as ACL, EMNLP, NAACL, ICLR, and NeurIPS. My work has received wide recognition and several best paper awards. I have served the research community in various leadership roles, including as Area Chair for ACL, NAACL, and EMNLP.

I am deeply passionate about diversity and inclusion. To further this cause, I co-founded the [HausaNLP](https://hausanlp.github.io/) research group, which aims to advance research and development in the Hausa language, one of the most widely spoken languages in Africa. Our work was recently featured by **Google Colab** — <a href="https://www.youtube.com/watch?v=kw0CZkFELi4" target="_blank">Bridging Language Gaps in AI</a>.


 I also founded the [Arewa Data Science Academy](https://arewadatascience.github.io/), which seeks to democratize data science and AI education by providing free data science and machine learning training to underserved students in Africa.
<p>If you have any questions regarding my research or want to collaborate, feel free to reach out.</p>

<h2>Research interests</h2>
<p>My research builds language technologies for the world's underrepresented languages and uses them to understand people, while keeping large models reliable and safe.</p>

<div class="interests-grid">
  <div class="interest-item">
    <h3 class="interest-title">NLP for African languages</h3>
    <p class="interest-desc">Speech and text technologies for Hausa and other African languages, spanning the full pipeline from data collection to deployable models.</p>
  </div>
  <div class="interest-item">
    <h3 class="interest-title">Datasets &amp; benchmarks</h3>
    <p class="interest-desc">Open, high-quality datasets and evaluation benchmarks that make progress on low-resource languages measurable and reproducible.</p>
  </div>
  <div class="interest-item">
    <h3 class="interest-title">Computational social science</h3>
    <p class="interest-desc">Using NLP to study sentiment, emotion, and online behaviour at scale across languages and cultures.</p>
  </div>
  <div class="interest-item">
    <h3 class="interest-title">Multilingual NLP</h3>
    <p class="interest-desc">Models and methods that transfer and generalise across many languages, with a focus on the long tail of low-resource settings.</p>
  </div>
  <div class="interest-item">
    <h3 class="interest-title">LLM alignment</h3>
    <p class="interest-desc">Aligning large language models with human preferences and values across diverse languages and cultural contexts.</p>
  </div>
  <div class="interest-item">
    <h3 class="interest-title">LLM safety</h3>
    <p class="interest-desc">Detecting and mitigating harmful content, such as hate speech and abuse, to make large language models safe in real, multilingual use.</p>
  </div>
</div>

<style>
.interests-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
  column-gap: 2.5rem;
  row-gap: 1.6rem;
  margin: 1.5rem 0 0.5rem;
}

.interest-item {
  padding-top: 0.9rem;
  border-top: 2px solid var(--global-text-color);
}

.interest-title {
  margin: 0 0 0.3rem;
  font-size: 1.02rem;
  font-weight: 700;
  line-height: 1.3;
  color: var(--global-text-color);
}

.interest-desc {
  margin: 0;
  font-size: 0.93rem;
  line-height: 1.55;
  color: var(--global-text-color-light, var(--global-text-color));
}
</style>

<h2>Recent papers</h2>
<p>A few recent and award-winning papers. See the <a href="{{ '/publications/' | relative_url }}">full list</a> for everything.</p>

{% include selected_papers.liquid %}

<p class="awards-more"><a href="{{ '/publications/' | relative_url }}">See all publications &rarr;</a></p>

<h2>Awards & recognitions</h2>
<p>Selected honours and best-paper awards recognising my research and community work in multilingual and African language technologies.</p>

<ol class="awards-list">
  <li class="award-row">
    <span class="award-year">2025</span>
    <span class="award-body">
      <span class="award-name">Best Resource Paper, ACL 2025</span>
      <a class="award-paper" href="https://aclanthology.org/2025.acl-long.436.pdf" target="_blank" rel="noopener">BRIGHTER: Textual Emotion Recognition Datasets for 28 Languages</a>
    </span>
  </li>
  <li class="award-row">
    <span class="award-year">2025</span>
    <span class="award-body">
      <span class="award-name">Best Task Award, SemEval 2025</span>
      <a class="award-paper" href="https://aclanthology.org/2025.semeval-1.327.pdf" target="_blank" rel="noopener">Task 11: Bridging the Gap in Text-Based Emotion Detection</a>
    </span>
  </li>
  <li class="award-row">
    <span class="award-year">2025</span>
    <span class="award-body">
      <span class="award-name">Outstanding Paper, NAACL 2025</span>
      <a class="award-paper" href="https://aclanthology.org/2025.naacl-long.139.pdf" target="_blank" rel="noopener">IrokoBench: A New Benchmark for African Languages in the Age of LLMs</a>
    </span>
  </li>
  <li class="award-row">
    <span class="award-year">2025</span>
    <span class="award-body">
      <span class="award-name">Best Paper, Deep Learning Indaba 2025</span>
      <a class="award-paper" href="https://arxiv.org/pdf/2506.02280" target="_blank" rel="noopener">The State of Large Language Models for African Languages</a>
    </span>
  </li>
  <li class="award-row">
    <span class="award-year">2024</span>
    <span class="award-body">
      <span class="award-name">Best Non-archival Paper, NeurIPS 2024</span>
      <a class="award-paper" href="https://proceedings.neurips.cc/paper_files/paper/2024/file/8eb88844dafefa92a26aaec9f3acad93-Paper-Datasets_and_Benchmarks_Track.pdf" target="_blank" rel="noopener">BLEnD: Everyday Knowledge in Diverse Cultures and Languages</a>
    </span>
  </li>
  <li class="award-row">
    <span class="award-year">2024</span>
    <span class="award-body">
      <span class="award-name">Honourable Mention, SemEval 2024</span>
      <a class="award-paper" href="https://arxiv.org/pdf/2403.18933" target="_blank" rel="noopener">Semantic Textual Relatedness for African and Asian Languages</a>
    </span>
  </li>
  <li class="award-row">
    <span class="award-year">2023</span>
    <span class="award-body">
      <span class="award-name">Best Non-archival Paper, AfricaNLP 2023</span>
      <a class="award-paper" href="https://aclanthology.org/2023.emnlp-main.862.pdf" target="_blank" rel="noopener">AfriSenti: A Twitter Sentiment Analysis Benchmark for African Languages</a>
    </span>
  </li>
  <li class="award-row">
    <span class="award-year">2023</span>
    <span class="award-body">
      <span class="award-name">Area Chair Award, IJCNLP–AACL 2023</span>
      <a class="award-paper" href="https://aclanthology.org/2021.tacl-1.66.pdf" target="_blank" rel="noopener">MasakhaNER: Named Entity Recognition for African Languages</a>
    </span>
  </li>
  <li class="award-row">
    <span class="award-year">2020</span>
    <span class="award-body">
      <span class="award-name">Wikimedia Research Award, EMNLP 2020</span>
      <a class="award-paper" href="https://aclanthology.org/2020.findings-emnlp.195.pdf" target="_blank" rel="noopener">Participatory Research for Low-Resourced Machine Translation</a>
    </span>
  </li>
</ol>

<p class="awards-more"><a href="/Awards & Recognitions/">View all awards and recognitions &rarr;</a></p>

<style>
.awards-list {
  list-style: none;
  margin: 1.5rem 0 0;
  padding: 0;
}

.award-row {
  display: grid;
  grid-template-columns: 64px 1fr;
  gap: 1.25rem;
  padding: 0.9rem 0;
  border-top: 1px solid var(--global-divider-color);
  align-items: baseline;
}

.award-row:last-child {
  border-bottom: 1px solid var(--global-divider-color);
}

.award-year {
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--global-text-color-light, var(--global-text-color));
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.02em;
}

.award-name {
  display: block;
  font-weight: 600;
  font-size: 1rem;
  line-height: 1.45;
  color: var(--global-text-color);
}

.award-paper {
  display: block;
  margin-top: 0.15rem;
  font-size: 0.95rem;
  line-height: 1.45;
  color: var(--global-theme-color);
  text-decoration: none;
}

.award-paper:hover {
  text-decoration: underline;
}

.awards-more {
  margin-top: 1.1rem;
  font-size: 0.95rem;
}

.awards-more a {
  color: var(--global-theme-color);
  font-weight: 500;
  text-decoration: none;
}

.awards-more a:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .award-row {
    grid-template-columns: 44px 1fr;
    gap: 0.85rem;
  }
}
</style>

<!-- ============================= -->
<!-- 🗞️ Media Coverage Section -->
<!-- ============================= -->
<h2 id="media-coverage">Media coverage</h2>
<p>
  Selected highlights from major outlets that have featured my research, datasets, and community initiatives.
</p>

<ul class="media-list">
  {% assign media_items = site.media | sort: 'date' | reverse %}
  {% for item in media_items %}
  <li class="media-row">
    {% if item.thumbnail %}
    <span class="media-logo"><img src="{{ '/assets/media/' | append: item.thumbnail | relative_url }}" alt="{{ item.source }}"></span>
    {% else %}
    <span class="media-logo media-logo--empty" aria-hidden="true"></span>
    {% endif %}
    <span class="media-body">
      <a class="media-title" href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a>
      <span class="media-meta">{{ item.source }} &middot; {{ item.date | date: "%b %Y" }}</span>
    </span>
  </li>
  {% endfor %}
</ul>

<style>
.media-list {
  list-style: none;
  margin: 1.5rem 0 0;
  padding: 0;
}

.media-row {
  display: grid;
  grid-template-columns: 56px 1fr;
  gap: 1.1rem;
  padding: 0.9rem 0;
  border-top: 1px solid var(--global-divider-color);
  align-items: center;
}

.media-row:last-child {
  border-bottom: 1px solid var(--global-divider-color);
}

.media-logo {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  border-radius: 8px;
  border: 1px solid var(--global-divider-color);
  background: #ffffff;
  overflow: hidden;
}

.media-logo img {
  max-width: 82%;
  max-height: 82%;
  object-fit: contain;
}

.media-logo--empty {
  background: var(--global-bg-color);
}

.media-body {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  min-width: 0;
}

.media-title {
  font-weight: 600;
  font-size: 1rem;
  line-height: 1.4;
  color: var(--global-theme-color);
  text-decoration: none;
}

.media-title:hover {
  text-decoration: underline;
}

.media-meta {
  font-size: 0.88rem;
  color: var(--global-text-color-light, var(--global-text-color));
}

@media (max-width: 480px) {
  .media-row {
    grid-template-columns: 44px 1fr;
    gap: 0.85rem;
  }
  .media-logo {
    width: 44px;
    height: 44px;
  }
}
</style>

---

## Latest Updates
{% include news.liquid %}

---

<div class="visitor-section">
  <p class="visitor-heading">Visitors</p>
  <a href="https://info.flagcounter.com/2a7q" target="_blank" rel="noopener" aria-label="Flag Counter detail">
    <img
      src="https://s01.flagcounter.com/count2/2a7q/bg_FFFFFF/txt_000000/border_0366d6/columns_5/maxflags_15/viewers_0/labels_1/pageviews_1/flags_0.png"
      alt="Flag Counter"
      class="flag-counter-img"
    >
  </a>
  <p class="visitor-caption">Tracking visitors since October 2025</p>
</div>

<style>
.visitor-section {
  text-align: center;
  border: 1px solid var(--global-divider-color);
  border-radius: 10px;
  padding: 1.1rem 1.2rem;
  margin: 2.5rem auto;
  max-width: 520px;
  background: var(--global-card-bg-color);
}

.visitor-heading {
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--global-text-color-light, var(--global-text-color));
  margin: 0 0 0.75rem;
}

.flag-counter-img {
  width: 100%;
  max-width: 420px;
  border-radius: 6px;
}

.visitor-caption {
  font-size: 0.8rem;
  color: var(--global-text-color-light, var(--global-text-color));
  margin: 0.75rem 0 0;
}

@media (max-width: 480px) {
  .visitor-section {
    padding: 0.9rem;
    max-width: 95%;
  }
  .flag-counter-img {
    max-width: 320px;
  }
}
</style>
