---
layout: page
permalink: /teaching/
title: Teaching & Supervision
description: Courses taught and student supervision.
nav: true
nav_order: 5
---

<h2>Teaching</h2>

<p style="font-size:1.05rem; text-align:justify;">
I teach and design courses across <strong>Imperial College London</strong>,
<strong>Bayero University Kano (BUK)</strong>, and the
<strong>African Institute for Mathematical Sciences (AIMS)</strong>.
My teaching emphasizes <strong>applied machine learning</strong>,
<strong>natural language processing (NLP)</strong>, and <strong>AI for Social Good</strong>,
with a focus on real-world, low-resource, and culturally grounded applications.
</p>

---

## Current Courses

<ul class="course-list">
  <li>
    <strong>Introduction to Python for Data Science</strong> — Arewa Data Science Academy  
    <em>Introductory programming and data manipulation using Python, NumPy, and Pandas.</em>
  </li>
  <li>
    <strong>Introduction to Machine Learning</strong> — Arewa Data Science Academy  
    <em>Foundations of Machine Learning, including supervised and unsupervised techniques.</em>
  </li>
  <li>
    <strong>Natural Language Processing & Large Language Models</strong> — AIMS South Africa and Cameroon  
    <em> Graduate-level course on natural language processing and large language models.</em>
  </li>
  <li>
    <strong>Machine Learning</strong> — Imperial College London (TA)  
    <em></em>
  </li>
</ul>

---

<h2>Supervision</h2>

<p style="font-size:1.05rem; text-align:justify;">
I supervise PhD, MSc, and undergraduate students working on topics in
<strong>NLP for low-resource languages</strong>, <strong>responsible AI</strong>,
and <strong>cross-cultural language technologies</strong>.
I also mentor research interns and early-career scholars across Africa through
the <a href="https://arewadatascience.github.io/" target="_blank">Arewa Data Science Academy</a>
and the <a href="https://hausanlp.github.io/" target="_blank">HausaNLP</a> community.
</p>

---

## Student Supervision

<details class="supervision-section" open>
<summary><span class="arrow"></span> <strong>PhD Students</strong></summary>
<ul class="student-list">
  <li>
    <a href="#" target="_blank"><strong>Hafiz Imam</strong></a> — Bayero University Kano  
    <em>Topic:</em> Automatic Speech Recognition for African Languages  
    <span class="role">Role:</span> Co-supervisor
  </li>
  <li>
    <a href="#" target="_blank"><strong>Murja Gadanya</strong></a> — Bayero University Kano  
    <em>Topic:</em> Emotion Recognition in Low-Resource Languages  
    <span class="role">Role:</span> Co-supervisor
  </li>
  <li>
    <a href="#" target="_blank"><strong>Saminu Aliyu</strong></a> — Modibbo Adama University of Technology  
    <em>Topic:</em> Hate Speech Detection in Low-Resource Languages  
    <span class="role">Role:</span> Co-supervisor
  </li>
  <li>
    <a href="#" target="_blank"><strong>Musa Adam</strong></a> — Bayero University Kano  
    <em>Topic:</em> LLM Adaptation for African Languages  
    <span class="role">Role:</span> Co-supervisor
  </li>
</ul>
</details>

<details class="supervision-section">
<summary><span class="arrow"></span> <strong>MSc Students</strong></summary>
<ul class="student-list">
  <li>
    <strong>Maryam Usman</strong> — MSc, Bayero University Kano  
    <em>Project:</em> Sentiment Analysis for Hausa Social Media Texts  
    <span class="role">Role:</span> Supervisor
  </li>
  <li>
    <strong>Abdulrahman Nuhu</strong> — MSc, AIMS South Africa  
    <em>Project:</em> Evaluating Large Language Models for African Dialogue Systems  
    <span class="role">Role:</span> Visiting Supervisor
  </li>
</ul>
</details>

<details class="supervision-section">
<summary><span class="arrow"></span> <strong>Undergraduate & Internship Supervision</strong></summary>
<ul class="student-list">
  <li>
    <strong>Hafsa Kabir</strong> — BSc, Bayero University Kano  
    <em>Project:</em> Dataset Creation for Hausa Text Summarization  
    <span class="role">Role:</span> Academic Supervisor
  </li>
  <li>
    <a href="https://arewadatascience.github.io/" target="_blank"><strong>Arewa Data Science Interns</strong></a> — Nigeria  
    <em>Focus:</em> Applied Data Science and Machine Learning  
    <span class="role">Role:</span> Research Mentor & Founder
  </li>
</ul>
</details>

---

## Alumni Highlights

<p style="font-size:1rem;">
Over <strong>40+</strong> students mentored across Africa.  
Alumni have advanced to <strong>PhD programs</strong> and <strong>research roles</strong> in Africa, and beyond.
</p>

<div class="alumni-banner">
 <strong>Empowering the next generation of African AI researchers.</strong>
</div>

---

<!-- ===== STYLING ===== -->
<style>
.course-list, .student-list {
  list-style-type: none;
  padding-left: 0;
}

.course-list li, .student-list li {
  background-color: var(--global-bg-color);
  border-left: 4px solid #0366d6;
  padding: 10px 15px;
  margin-bottom: 10px;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.25s ease;
}

.course-list li:hover, .student-list li:hover {
  background-color: rgba(3,102,214,0.08);
  transform: translateX(4px);
}

.student-list em, .course-list em {
  color: #666;
}

.role {
  color: #555;
  font-size: 0.9rem;
  font-style: italic;
}

/* ===== Collapsible styling with animation ===== */
.supervision-section {
  margin-bottom: 1.2rem;
  border: 1px solid rgba(3,102,214,0.25);
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.25, 0.1, 0.25, 1.0);
  box-shadow: 0 0 0 rgba(3,102,214,0);
}

.supervision-section:hover {
  box-shadow: 0 4px 12px rgba(3,102,214,0.15);
}

.supervision-section summary {
  cursor: pointer;
  font-size: 1.1rem;
  padding: 12px 16px;
  font-weight: 600;
  color: #0366d6;
  display: flex;
  align-items: center;
  gap: 8px;
  list-style: none;
  transition: all 0.3s ease;
}

.supervision-section summary:hover {
  background-color: rgba(3,102,214,0.06);
}

.supervision-section[open] summary {
  border-bottom: 2px solid rgba(3,102,214,0.15);
  background: linear-gradient(135deg, #e8f1ff, #f7fbff);
  box-shadow: inset 0 -2px 4px rgba(3,102,214,0.1);
}

/* Smooth arrow transition */
.arrow {
  display: inline-block;
  width: 0;
  height: 0;
  margin-right: 5px;
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-left: 6px solid #0366d6;
  transform: rotate(0deg);
  transition: transform 0.35s cubic-bezier(0.65, 0, 0.35, 1);
}

.supervision-section[open] .arrow {
  transform: rotate(90deg);
}

/* Smooth opening animation for the content */
.supervision-section[open] ul {
  animation: fadeSlide 0.4s ease-out;
}

@keyframes fadeSlide {
  from {
    opacity: 0;
    transform: translateY(-5px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ===== Dark Mode ===== */
html[data-theme="dark"] .supervision-section {
  background-color: #1a1a1a;
  border-color: rgba(27,142,242,0.25);
}
html[data-theme="dark"] .supervision-section summary {
  color: #66b0ff;
}
html[data-theme="dark"] .supervision-section summary:hover {
  background-color: rgba(27,142,242,0.15);
}
html[data-theme="dark"] .supervision-section[open] summary {
  background: linear-gradient(135deg, #1b1b1b, #242424);
  border-bottom: 2px solid rgba(27,142,242,0.25);
}
html[data-theme="dark"] .arrow {
  border-left-color: #66b0ff;
}

/* ===== Alumni banner ===== */
.alumni-banner {
  margin-top: 1.2rem;
  background: linear-gradient(135deg, #0366d6, #1b8ef2);
  color: white;
  text-align: center;
  padding: 14px 18px;
  border-radius: 10px;
  font-weight: 500;
  box-shadow: 0 3px 10px rgba(3,102,214,0.25);
}

html[data-theme="dark"] .alumni-banner {
  background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
  border-left: 4px solid #1b8ef2;
  color: #f0f0f0;
  box-shadow: 0 2px 8px rgba(27,142,242,0.2);
}
</style>
