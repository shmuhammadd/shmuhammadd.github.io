// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-bio",
          title: "Bio",
          description: "Shamsuddeen Hassan Muhammad Bio.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/biography/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "publications by categories in reversed chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "news-joining-imperial-college-london-as-a-google-deepmind-academic-fellow",
          title: 'Joining Imperial College London as a Google DeepMind Academic Fellow',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/deepmind-academic-fellow/";
            },},{id: "news-co-organizing-semeval-2025-shared-task-on-emotion-detection",
          title: 'Co-Organizing SemEval-2025 Shared Task on Emotion Detection',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2024-06-01/";
            },},{id: "news-two-papers-accepted-at-naacl2025",
          title: 'Two papers accepted at NAACL2025',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2025-02-01/";
            },},{id: "news-",
          title: '',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2025-03-16/";
            },},{id: "news-i-will-be-attending-naccl-2025-in-albuquerque-new-mexico-april-30-may-7-2025-to-present-the-afrihate-paper",
          title: 'I will be attending NACCL 2025 in Albuquerque, New Mexico (April 30–May 7,...',
          description: "",
          section: "News",},{id: "news-outstanding-paper-award-naacl-2025-our-paper-irokobench-received-the-outstanding-paper-award-at-naacl-2025-in-albuquerque-new-mexico-april-30-may-7-2025",
          title: 'Outstanding Paper Award - NAACL 2025 Our paper IrokoBench received the Outstanding Paper...',
          description: "",
          section: "News",},{id: "news-four-papers-accepted-at-africanlp-2025",
          title: 'Four Papers Accepted at AfricaNLP 2025',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2025-05-05/";
            },},{id: "news-two-papers-accepted-at-acl2025",
          title: 'Two papers accepted at ACL2025',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2025-05-20/";
            },},{id: "news-i-will-be-teaching-natural-language-processing-nlp-in-the-ai-for-science-master-s-program-at-the-african-institute-for-mathematical-sciences-aims-in-south-africa-from-november-24-to-december-12-2025",
          title: 'I will be teaching Natural Language Processing (NLP) in the AI for Science...',
          description: "",
          section: "News",},{id: "news-i-will-be-teaching-natural-language-processing-nlp-at-the-african-institute-for-mathematical-sciences-aims-camerron-from-febuary-23-to-march-14-2025",
          title: 'I will be teaching Natural Language Processing (NLP) at the African Institute for...',
          description: "",
          section: "News",},{id: "news-i-will-be-giving-a-keynote-speech-at-the-york-st-john-university-on-19th-june-2025",
          title: 'I will be giving a keynote speech at the York St John University...',
          description: "",
          section: "News",},{id: "news-i-will-be-giving-a-keynote-speech-at-workshop-on-multilingual-and-equitable-language-technologies-melt-on-october-10-2025-at-palais-des-congrès-montreal-canada",
          title: 'I will be giving a keynote speech at Workshop on Multilingual and Equitable...',
          description: "",
          section: "News",},{id: "news-i-will-be-giving-a-keynote-speech-at-empowering-india-through-inclusive-generative-ai-workshop-on-5th-july-2025",
          title: 'I will be giving a keynote speech at Empowering India Through Inclusive Generative...',
          description: "",
          section: "News",},{id: "news-i-will-be-giving-a-keynote-speech-at-empowering-india-through-inclusive-generative-ai-workshop-on-5th-july-2025",
          title: 'I will be giving a keynote speech at Empowering India Through Inclusive Generative...',
          description: "",
          section: "News",},{id: "news-best-task-award-semeval-2025-our-semeval-task-semeval-2025-task-11-bridging-the-gap-in-text-based-emotion-detection-has-been-awarded-the-best-semeval2025-task-award-at-acl-2025",
          title: 'Best Task Award - SemEval 2025 Our SemEval task “SemEval-2025 Task 11: Bridging...',
          description: "",
          section: "News",},{id: "news-best-resource-award-acl-2025-our-paper-brighter-bridging-the-gap-in-human-annotated-textual-emotion-recognition-datasets-for-28-languages-has-been-awarded-the-best-resource-award-at-acl-2025-see-the-project-page-for-more-details",
          title: 'Best Resource Award - ACL 2025 Our paper “BRIGHTER: BRIdging the Gap in...',
          description: "",
          section: "News",},{id: "news-best-paper-award-deep-learning-indaba-2025-our-paper-the-state-of-large-language-models-for-african-languages-progress-and-challenges-has-been-awarded-the-best-paper-award-at-deep-learning-indaba-dli-2025-dli-is-the-largest-machine-learning-and-artificial-intelligence-ai-gathering-in-africa",
          title: 'Best Paper Award - Deep Learning Indaba 2025 Our paper, “The State of...',
          description: "",
          section: "News",},{id: "news-i-will-be-giving-a-talk-at-microsoft-research-lab-africa-nairobi-on-30th-october-2025",
          title: 'I will be giving a talk at Microsoft Research Lab - Africa, Nairobi...',
          description: "",
          section: "News",},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%73%68%61%6D%73%75%64%64%65%65%6E%32%30%30%34@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/shmuhammadd# your GitHub user name", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/shmuhammad", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=Ne1nt4gAAAAJ", "_blank");
        },
      },{
        id: 'social-whatsapp',
        title: 'whatsapp',
        section: 'Socials',
        handler: () => {
          window.open("https://wa.me/447707515926", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/shmuhammadd", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
