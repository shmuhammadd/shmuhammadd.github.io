---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  # - block: features
  #   content:
  #     title: Skills
  #     items:
  #       - name: R
  #         description: 90%
  #         icon: r-project
  #         icon_pack: fab
  #       - name: Statistics
  #         description: 100%
  #         icon: chart-line
  #         icon_pack: fas
  #       - name: Photography
  #         description: 10%
  #         icon: camera-retro
  #         icon_pack: fas
  - block: markdown
    id: news
    content:
       title: News
       text: |
              - [2023-09-04]: I will present our paper at EPIA2023 (Portuguese Conference on Artificial Intelligence)
              
              - [2023-07-04]: I will present our paper [SemEval-2023 Task 12: Sentiment Analysis for African Languages (AfriSenti-SemEval)](https://arxiv.org/pdf/2304.06845.pdf)) at SemEval2023 Workshop Co-located with ACL2023 Toronto Canada.
              
              - [2023-06-11]: I will attend Africa Arrtifical Intelligence Conference Rewanda
              
              - [2023-05-05]: Our paper: [Afrisenti:A Twitter Sentiment Analysis Benchmark for African Languages ](https://arxiv.org/pdf/2302.08956.pdf) won the best paper award at AfricaNLP2023
              - [2023-05-02]: Our project, [AfiHate](https://github.com/AfriHate/AfriHate), was selected as one of the [top 100 AI projects](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjmvNiZ8_D_AhVxTaQEHU0RCykQFnoECBoQAQ&url=https%3A%2F%2Fircai.org%2Fglobal-top-100-outstanding-projects%2Fresults%2F&usg=AOvVaw1wyZ7a53_wi2qDADuN4bFD&opi=89978449) that solve problems related to the 17 United Nations Sustainable Development Goals.
              - [2023-03-29]: I submitted my PhD thesis, waiting for defense.
    design:
       columns: '2'
  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      columns: '2'
      view: citation
  - block: collection
    id: posts
    content:
      title: Recent Posts
      subtitle: ''
      text: ''
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        folders:
          - post
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: compact
      columns: '2'
      
  # # - block: portfolio
  # #   id: projects
  # #   content:
  # #     title: Projects
  #     filters:
  #       folders:
  #         - project
  #     # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  #     default_button_index: 0
  #     # Filter toolbar (optional).
  #     # Add or remove as many filters (`filter_button` instances) as you like.
  #     # To show all items, set `tag` to "*".
  #     # To filter by a specific tag, set `tag` to an existing tag name.
  #     # To remove the toolbar, delete the entire `filter_button` block.
  #     buttons:
  #       - name: All
  #         tag: '*'
  #       - name: Deep Learning
  #         tag: Deep Learning
  #       - name: Other
  #         tag: Demo
  #   design:
  #     # Choose how many columns the section has. Valid values: '1' or '2'.
  #     columns: '1'
  #     view: showcase
  #     # For Showcase view, flip alternate rows?
  #     flip_alt_rows: false
  # - block: markdown
  #   id: new
  #   content:
  #      title: News
  #      subtitle: ''
  #      text: |-
  #        {{< news="news" >}}
  #   design:
  #      columns: '2'
  # - block: collection
  #   id: featured
  #   content:
  #     title: Featured Publications
  #     filters:
  #       folders:
  #         - publication
  #       featured_only: true
  #   design:
  #     columns: '2'
  #     view: card
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     columns: '2'
  #     view: compact
  # - block: tag_cloud
  #   content:
  #     title: Popular Topics
  #   design:
  #     columns: '2'
  #   2: formspree.io
  - block: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Doctoral Research Fellow
          company: Faculty of Science, University of Porto
          company_url: 'https://www.dcc.fc.up.pt/site'
          company_logo: logofcs
          location: Porto
          date_start: '2020-08-01'
          date_end: ''
          # description: |2-
          #     Responsibilities include:
          #     * Analysing
          #     * Modelling
          #     * Deploying
        - title: Researcher
          company: INESC TEC - Institute for Systems and Computer Engineering, Technology and Science
          company_url: 'https://www.inesctec.pt/en'
          company_logo: inesclogo
          location: Porto, Portugal
          date_start: '2019-05-01'
          date_end: ''
          # description: Taught electronic engineering and researched semiconductor physics.
        - title: Co-Founder
          company: HausaNLP
          company_url: 'https://hausanlp.github.io'
          company_logo: hausanlplogo
          location: Nigeria
          date_start: '2020-02-12'
        - title: Co-Founder
          company: Arewa Data Science Academy
          company_url: 'https://arewadatascience.org'
          company_logo: arewads
          location: Nigeria
          date_start: '2021-03-05'
        - title: Lecturer
          company: Bayero University , Kano
          company_url: 'https://www.buk.edu.ng/'
          company_logo: logobuk
          location: Kano, Nigeria
          date_start: '2012-04-12'
        # - title: Lecturer
        #   company: Saadatu Rimi College of Education
        #   company_url: ''
        #   company_logo: org-x
        #   location: Kano States
        #   date_start: '2010-10-01'
        #   date_end: '2012-04-02'
    design:
      columns: '2'
  - block: collection
    id: Publications
    content:
      title: Recent Publications
      text: |-
        {{% callout note %}}
        Quickly discover relevant content by [filtering publications](./publication/).
        {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text: |-
      # Contact (add or remove contact options as necessary)
      email: shamsuddeen2004@gmail.com
      phone: +351 934 673 685
      # appointment_url: 'https://calendly.com'
      # directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
      # office_hours:
      #   - 'Monday 10:00 to 13:00'
      #   - 'Wednesday 09:00 to 10:00'
      contact_links:
        - icon: twitter
          icon_pack: fab
          name: DM Me
          link: 'https://twitter.com/shmuhammadd'
      # Automatically link email and phone or display as text?
      autolink: true
      # Email form provider
      form:
        provider: 0
        # formspree:
        #   id:
        # netlify:
        #   # Enable CAPTCHA challenge to reduce spam?
        #   captcha: false
    design:
      columns: '2'
  # - block: Note
  #   id: notes
  #   content:
  #     title: Note
  #     subtitle:
  #     text: |-
---
