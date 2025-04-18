---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

Please also find my publications on [Google Scholar](https://scholar.google.com/citations?user=yXOpclkAAAAJ) ( <a href='https://scholar.google.com/citations?user=yXOpclkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> ).

# Papers

- LDAformer: Predicting LncRNA-Disease Associations based on Topological Feature Extraction and Transformer Encoder [[PDF]](https://echochou990919.github.io/files/LDAformer.pdf) [[DOI]](https://doi.org/10.1093/bib/bbac370) [[GitHub]](https://github.com/EchoChou990919/LDAformer)  
**Yi Zhou**, Xinyi Wang, Lin Yao, Min Zhu  
Briefings in Bioinformatics (BIB), 2022 (JCR-Q1, IF: 13.994)  

- GBDT4CTRVis: Visual Analytics of Gradient Boosting Decision Tree for Advertisement Click-Through Rate Prediction [[PDF]](https://echochou990919.github.io/files/GBDT4CTRVis.pdf) [[DOI]](https://link.springer.com/article/10.1007/s12650-024-00984-0) [[Video]](https://www.bilibili.com/video/BV1Wm4y1E7Q1) [[Slide]](https://echochou990919.github.io/files/GBDT4CTRVis_Slides.pdf)  
Wenwen Gao, Shangsong Liu, **Yi Zhou**, Fengjie Wang, Feng Zhou, Min Zhu  
Journal of Visualization (JoV), 2024  

- Dowsing: A Task-Driven Approach for Multiple-View Visualizations Dynamic Recommendation [[PDF]](https://echochou990919.github.io/files/Dowsing.pdf) [[DOI]](https://link.springer.com/article/10.1007/s12650-024-00989-9) [[Webpage]](https://dowsing-machine.github.io/) [[Online Demo]](http://dowsing-machine.com/)  
Jiamin Zhu, Meixuan Wu, **Yi Zhou**, Haotian Zhu, Min Zhu  
Journal of Visualization (JoV), 2024  

- Timely-MDA: A Benchmark for Generalizable MiRNA-Disease Association Prediction [[PDF]](https://echochou990919.github.io/files/BIBM_Short_Paper_v2.pdf) [[DOI]](https://ieeexplore.ieee.org/abstract/document/10822171) [[Github]](https://github.com/EchoChou990919/Timely-MDA)  
**Yi Zhou**, Xian Guan, Meixuan Wu, Chengzhou Ouyang, Min Zhu  
International Conference on Bioinformatics and Biomedicine (BIBM), 2024

- Protein-binding RNA Prediction Based on Integrated Sequence-Structure-Function Pre-training [[PDF]](https://echochou990919.github.io/files/MTPRBP.pdf) [[DOI]](https://ieeexplore.ieee.org/abstract/document/10946866) [[Github]](https://github.com/TimmyGan/MTP-RBP)
Lin Gan, Xinyi Wang, **Yi Zhou**, Min Zhu
IEEE Transactions on Computational Biology and Bioinformatics (TCBB), 2025

# Preprints

- Computational Protein Science in the Era of Large Language Models (LLMs) [[PDF]](https://echochou990919.github.io/files/lm4protein_arxiv_v2.pdf) [[arXiv]](https://arxiv.org/abs/2501.10282)  
Wenqi Fan, **Yi Zhou**, Shijie Wang, Yuyao Yan, Hui Liu, Qian Zhao, Le Song, Qing Li  

# Patents

- A Visualization Method for Chromatin Hierarchy Analysis Based on Genetic Data  
Min Zhu, Fuqiu Chen, Chunlin Long, **Yi Zhou**, Xinyi Wang  
CN113946730A  
- An Analytical Task Perception Method that Integrates Deep Learning Models and Rules  
Min Zhu, Meixuan Wu, Jiamin Zhu, **Yi Zhou**, Haotian Zhu  
CN116303737A *(Under Substantial Examination)*  
- A Dynamic Visualization Recommendation Method Based on User Tasks  
Min Zhu, Jiamin Zhu, Meixuan Wu, **Yi Zhou**, Haotian Zhu  
CN116204704A *(Under Substantial Examination)*  
- Chromatin Topologically Associating Domains Boundary Prediction Method Based on Multimodal Fusion  
Min Zhu, Xiyao Li, Chunlin Long, **Yi Zhou**, Xinyi Wang  
CN115831217A *(Under Substantial Examination)*  
- Method and System for Long Non-coding RNA-Disease Association Prediction Based on Self-Attention Mechanism  
Min Zhu, **Yi Zhou**, Xinyi Wang, Lin Yao (**1st Student Author**)  
CN115171780A *(Under Substantial Examination)*  
<!-- - Method and System for Predicting Chromatin Topologically Associating Domains Based on Spectral Clustering  
Min Zhu, Chunlin Long, Mingyang Zhang, Xinyi Wang, **Yi Zhou**  
CN114444286A *(Under Substantial Examination)*   -->

<!-- [PDF](https://echochou990919.github.io/files/CN115171780A.pdf) -->
<!-- [PDF](https://echochou990919.github.io/files/CN116303737A.pdf) -->
<!-- [PDF](https://echochou990919.github.io/files/CN116204704A.pdf) -->
<!-- [PDF](https://echochou990919.github.io/files/CN115831217A.pdf) -->
<!-- [PDF](https://echochou990919.github.io/files/CN113946730A.pdf) -->
<!-- [PDF](https://echochou990919.github.io/files/CN114444286A.pdf) -->

# Other Available Works

- Sichuan University - Huawei MindSpore Application Case Implementation Project: Swin Transformer [[GitHub]](https://github.com/EchoChou990919/mindspore_swin_transformer)  
**Yi Zhou**, Xiyao Li, Wanjing Zhang  

- DLMV: A Visual Analytic System for LncRNA-Disease Association Prediction [[Poster]](https://echochou990919.github.io/files/DLMV_Poster.pdf) [[Online Demo]](https://rna-disease.pages.dev/)  
**Yi Zhou**, Jiamin Zhu, Meixuan Wu  


<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %} -->
