---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 6
description: Moments from conferences, talks, and academic life.
---

<!--
  HOW TO UPDATE THIS PAGE
  1. Drop a photo into  assets/img/gallery/  (e.g. assets/img/gallery/acl-2025.jpg)
  2. Add an entry to  _data/gallery.yml  with its path, event, and date.
  Newest photos (by date) appear first. No code changes needed here.
-->

<div class="gallery-grid">
  {% assign photos = site.data.gallery | sort: "date" | reverse %}
  {% for photo in photos %}
  <div class="gallery-item">
    {% include figure.liquid loading="lazy" path=photo.image class="img-fluid rounded z-depth-1 gallery-img" alt=photo.event %}
    <div class="gallery-cap">
      {% if photo.event %}<span class="gallery-event">{% if photo.link %}<a href="{{ photo.link }}" target="_blank" rel="noopener">{{ photo.event }}</a>{% else %}{{ photo.event }}{% endif %}</span>{% endif %}
      {% if photo.caption %}<span class="gallery-text">{{ photo.caption }}</span>{% endif %}
      {% if photo.location or photo.date %}
        <span class="gallery-meta">
          {{ photo.location }}{% if photo.location and photo.date %} &middot; {% endif %}{% if photo.date %}{{ photo.date | date: "%b %Y" }}{% endif %}
        </span>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>

<style>
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.gallery-item figure {
  margin: 0;
}

.gallery-img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
}

.gallery-cap {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  margin-top: 0.6rem;
}

.gallery-event {
  font-weight: 700;
  font-size: 0.98rem;
  line-height: 1.3;
  color: var(--global-text-color);
}

.gallery-text {
  font-size: 0.92rem;
  line-height: 1.45;
  color: var(--global-text-color);
}

.gallery-meta {
  font-size: 0.85rem;
  color: var(--global-text-color-light, var(--global-text-color));
}
</style>
