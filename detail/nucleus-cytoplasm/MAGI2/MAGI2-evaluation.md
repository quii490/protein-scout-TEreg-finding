---
type: protein-evaluation
gene: "MAGI2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## MAGI2 (Membrane-associated guanylate kinase WW and PDZ 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | MAGI2 |
| 蛋白全称 | Membrane-associated guanylate kinase WW and PDZ 2 |
| UniProt ID | Q86UL8 |
| 蛋白大小 | 1455.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 1455 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR008145, IPR008144, IPR020590, IPR027417|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=46 |
| **加权总分** | | | **73/180** | |
| **归一化总分 (÷1.83)** | | | **39/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Tight junction + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: MAGI2 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Tight junction + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

synaptic scaffold, MAGUK family。

#### 3.3 PPI 网络

PPI degree=46。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

MAGI2 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR008145 |
| InterPro | IPR008144 |
| InterPro | IPR020590 |
| InterPro | IPR027417 |
| InterPro | IPR001478 |
| InterPro | IPR036034 |
| InterPro | IPR001202 |
| InterPro | IPR036020 |
| Pfam | PF00625 |
| Pfam | PF16663 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00072;SM00228;SM00456; |
| InterPro | IPR008145;IPR008144;IPR020590;IPR027417;IPR001478;IPR036034;IPR001202;IPR036020; |
| Pfam | PF00625;PF16663;PF00595;PF00397; |
| UniProt Domain | DOMAIN 17..101; /note="PDZ 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 109..283; /note="Guanylate kinase-like"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00100"; DOMAIN 302..335; /note="WW 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00224"; DOMAIN 348..381; /note="WW 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00224"; DOMAIN 426..510; /note="PDZ 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 605..683; /note="PDZ 3"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 778..860; /note="PDZ 4"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 920..1010; /note="PDZ 5"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143"; DOMAIN 1147..1229; /note="PDZ 6"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00143" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PTEN | STRING | 998 |
| TEP1 | STRING | 998 |
| CTNNB1 | STRING | 986 |
| BAP1 | STRING | 922 |
| MAGI1 | STRING | 922 |
| NLGN1 | STRING | 893 |
| KIDINS220 | STRING | 808 |
| TAMALIN | STRING | 796 |


### PubMed

**Count: 344**

| PMID | Title |
|---|---|
| 42331551 | [cfDNA sequencing reveals response heterogeneity to first-line camrelizumab plus chemotherapy in esophageal squamous cell carcinoma]. |
| 42310233 | Pan-cancer and single-cell analysis identifies MAGI2-AS3 as an immune regulator and prognostic biomarker with a focus on colorectal cancer. |
| 42166848 | The association of non-alcoholic fatty liver index, plasma metal levels, and genetic susceptibility using genome-wide type analysis. |
| 41870210 | Extended motif recognition tunes WW domain affinity in MAGI-IQSEC complexes. |
| 41840107 | Genetic basis of immunity in Indian cattle as revealed by comparative analysis of Bos genome. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q86UL8
- HPA: https://www.proteinatlas.org/

### 深度机制分析

MAGI2（Membrane-associated guanylate kinase WW and PDZ 2）是本次评估中结构域架构最为复杂的蛋白之一——其1455个氨基酸的序列上排列着6个PDZ结构域、2个WW结构域和1个Guanylate kinase-like (GuK)结构域，是MAGUK（膜相关鸟苷酸激酶）家族的典型成员。UniProt Domain注释精确定位了这些结构域的边界：PDZ1（17-101aa）、GuK（109-283aa）、WW1（302-335aa）、WW2（348-381aa）、PDZ2（426-510aa）、PDZ3（605-683aa）、PDZ4（778-860aa）、PDZ5（920-1010aa）和PDZ6（1147-1229aa）。SMART数据进一步确认了SM00072（PDZ）、SM00228（WW）和SM00456（GuK）的域架构。InterPro注释则扩展至11个条目（IPR008145/GK-like、IPR008144/Guanylate kinase、IPR020590/GuK N-terminal、IPR027417/P-loop NTPase、IPR001478/PDZ、IPR036034/PDZ superfamily、IPR001202/WW、IPR036020/WW superfamily），反映了其结构域的层级分类。

这种多模块域架构赋予了MAGI2独特的"分子支架"功能。PDZ结构域通常识别靶蛋白C端的三肽序列（如X-S/T-X-V/I-COOH），6个PDZ的串联排列使得MAGI2可以同时结合多个跨膜受体、离子通道或信号蛋白，形成信号复合体；WW结构域偏好结合富含脯氨酸的PPxY基序，介导与含PY基序蛋白（如HECT E3泛素连接酶）的互作；GuK结构域虽然与核苷酸激酶同源，但在MAGUK家族中已失去催化活性，转而作为蛋白-蛋白互作模块。三个模块的组合使MAGI2能够在突触后致密区（PSD）、紧密连接和粘附连接中搭建多蛋白信号复合体。

PPI互作网络直接验证了MAGI2的支架功能。STRING数据显示PTEN（磷酸酶-张力蛋白同源物, score=998）和CTNNB1（β-连环蛋白, score=986）是其最高置信度互作伙伴——PTEN通过与MAGI2的PDZ结构域结合被招募至质膜/细胞连接处，增强其肿瘤抑制功能；CTNNB1/Wnt信号的互作则反映了MAGI2在细胞粘附信号中的核心地位。TEP1（score=998）是PTEN的同源蛋白，进一步强化了这一互作模式的特异性。此外，MAGI1（score=922）作为家族同源蛋白可能形成异源二聚体，NLGN1（neuroligin-1, score=893）和KIDINS220（score=808）的互作则分别指向突触组织和神经营养因子信号。

在核定位方面，UniProt GO-CC列出了"Tight junction + Nucleus"的双重定位，但存在明显的主次关系——MAGI2在紧密连接中的定位和功能具有充分的实验支持，而核定位可能是条件性的或次要功能。HPA的明确结论（hpa_nuclear=False）进一步减弱了核定位的可信度。从结构域角度看，MAGI2缺乏经典NLS、DNA结合域（如锌指、同源框、bZIP等）或染色质调控域，其6个PDZ+2个WW+GuK的全部结构域功能均指向胞质/膜骨架蛋白的组装。PubMed文献（344篇）聚焦于MAGI2在突触功能（PMID 41870210报道WW结构域与IQSEC复合体的motif识别机制）、免疫调控（PMID 42310233发现MAGI2-AS3作为泛癌免疫调控因子）和GWAS关联（PMID 42166848）等方向，无任何TE调控相关研究。

综合来看，MAGI2的深度机制模型是一个典型的膜相关多模块支架蛋白：PDZ阵列→招募膜受体/通道；WW模块→招募PY基序蛋白；GuK→蛋白互作；PTEN→PDZ介导的肿瘤抑制信号；CTNNB1→Wnt/粘附信号。这一功能架构虽然精妙，但与核内TE调控完全不相关。推荐等级2/5（39/100）的极低归一化得分反映了其核定位证据薄弱（4/10）和PPI数据有限（2/10）的核心劣势。


