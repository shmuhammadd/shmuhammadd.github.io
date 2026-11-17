---
layout: post
inline: true
title: "Paper accepted to Findings of EACL 2027: The Illusion of Cross-Lingual Safety"
date: 2026-11-17 13:00:00-0400
categories: [news]
tags: [Paper, EACL, LLM Safety, Alignment, Africa]
---

📄 Our paper, **[The Illusion of Cross-Lingual Safety in Low-Resource Languages](https://arxiv.org/abs/2608.11146)**, has been accepted to Findings of EACL 2027! LLM safety alignment is mostly done in English, and we often assume it carries over to other languages. We tested that assumption in African languages. For most model–language pairs, harmful prompts kept less than 10% of the English refusal signal, and models failed to give a standard refusal in over 98% of cases. The models seem to understand the harmful request but do not route it to their safety mechanisms. We also release **LoDNA**, a dataset that pairs literal translations of harmful prompts with culturally localized versions. Safety has to be built and tested in each language, not assumed from English.
