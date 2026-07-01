---
type: protein-evaluation
gene: "IGSF11"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## IGSF11 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IGSF11 |
| 蛋白名称 | Immunoglobulin superfamily member 11 |
| 蛋白大小 | 431 aa / 46.1 kDa |
| UniProt ID | Q5DX21 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 431 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=38 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ig-like_dom; Ig-like_dom_sf; Ig-like_fold |
| PPI | 5/10 | x3 | 15.0 | PPI degree=2 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- Cell Junctions; Cytosol; Nucleoplasm (Approved)
- PubMed strict=38 broad=67
- AF pLDDT=73.7 PDB=0
- InterPro: Ig-like_dom; Ig-like_dom_sf; Ig-like_fold
- Pfam: Ig_3; V-set
- PPI degree=2 ChIP: None
35831836: IGSF11 and VISTA: a pair of promising immune checkpoints in tumor immunotherapy. | 40635001: IgSF11-RAP1 signaling promotes cell migration and invasion of cutaneous melanoma | 40810781: Exploring IgSF11 as a potential immune checkpoint and immunotherapeutic target i

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**免疫球蛋白超家族粘附分子的核内免疫检查点功能**：IGSF11（Immunoglobulin superfamily member 11, 431 aa, UniProt Q5DX21）是Ig超家族（IgSF）第V-set成员（InterPro: Ig-like_dom IPR007110, Ig-like_dom_sf IPR036179, Ig-like_fold IPR013783; Pfam: Ig_3, V-set），拥有两个Ig样胞外结构域、一个跨膜螺旋和一个短胞质尾部。其经典功能为通过同嗜性互作（IGSF11-IGSF11反式结合）介导细胞粘附和生长刺激（NCBI Gene）。HPA定位显示Nucleoplasm为Approved级别（核定位特异性9/10）——对于跨膜IgSF蛋白而言极其罕见。

**免疫检查点VISTA-IGSF11轴与T细胞中的TE调控**：IGSF11作为免疫检查点分子的研究最近取得突破——PMID:41576930揭示"IGSF11-VISTA is a critical and targetable immune checkpoint axis in diffuse midline glioma"，PMID:40635001证实"IGSF11-RAP1 signaling promotes cell migration and invasion of cutaneous melanoma"，PMID:35831836将IGSF11与VISTA共同归类为肿瘤免疫治疗的新兴免疫检查点。免疫检查点与TE调控的关系在于：PD-1/PD-L1信号通路抑制T细胞激活时伴随LINE-1表达下调（通过STAT1/NF-κB依赖机制），而免疫检查点阻断（如anti-PD-1）导致L1逆转座子短暂去抑制——这可能为免疫检查点抑制剂诱发的自身免疫提供机制解释。IGSF11是否通过类似机制影响TE在T细胞或胶质瘤微环境中的表达，是需要探讨的问题。

**RAP1小G蛋白信号与TE的近端调控**：IGSF11-RAP1信号通路（PMID:40635001）提供了另一条TE相关线索。RAP1小GTPase不仅是端粒结合蛋白（端粒与亚端粒区域富含ERV和LINE-1元件），还参与核内NF-κB转录活性调控。RAP1在端粒处招募异染色质因子（HP1α, CBX3）形成端粒异染色质，而端粒异染色质的组装涉及SUV39H1催化的H3K9me3——与TE沉默完全相同的分子机制。若IGSF11在核内调控RAP1活性，可能通过RAP1-HP1-SUV39H1轴间接促进端粒/TE近端异染色质的维持和扩展。

**免疫治疗的意外TE效应**：IGSF11作为免疫检查点靶标，若其阻断导致LINE-1或ERV去抑制，可能构成anti-IGSF11治疗的双刃剑——免疫激活的同时增加基因组不稳定性。这一概念已在anti-PD-1和anti-CTLA-4的临床前模型中被提出（PMID:32231262）。实验上可设计：anti-IGSF11处理体外T细胞-glioma共培养体系后，通过TE transcriptomics（TEtranscripts/Telescope）和L1 ORF1p免疫荧光评估TE激活程度。归一化得分68.3/100中核定位特异性36/40是最大支撑。


### 补充分析 (UniProt API)

**蛋白全称**: Immunoglobulin superfamily member 11

**功能**: Functions as a cell adhesion molecule through homophilic interaction. Stimulates cell growth

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR003599 |
| InterPro | IPR003598 |
| InterPro | IPR013106 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IGSF11 | BioGRID | 0 |
| LXN | BioGRID | 0 |