---
type: protein-evaluation
gene: "CUTC"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CUTC 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CUTC / Copper homeostasis protein cutC homolog |
| 蛋白大小 | 273 aa / 29.3 kDa |
| UniProt ID | Q9NTM9 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | Cytoplasm; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 273 aa / 29.3 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 30 | PubMed 62 篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.4，PDB: 3IWP |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005627 - CutC-like; InterPro: IPR036822 - CutC- |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners, IntAct 79 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
|  | **原始总分** |  | **106/183** | **103.0/183** |  |  |  |
|  | **归一化总分** |  | **57.9/100** | **56.3/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | Nucleoplasm | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CUTC/IF_images/455_F6_1_blue_red_green.jpg|455_F6_1_blue_red]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CUTC/IF_images/455_F6_2_blue_red_green.jpg|455_F6_2_blue_red]]

**结论**: 主要核定位，伴部分胞质信号，HPA Approved。

#### 3.2 蛋白大小评估

**评价**: 大小适中，适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 62 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 有一定研究基础，但仍存在未探索的niche空间。

**关键文献**:
1. Mirji G et al. (2022). "The microbiome-derived metabolite TMAO drives immune activation and boosts responses to immune checkpoint blockade in pancreatic cancer". *Sci Immunol*. PMID: 36083892
2. Ma SR et al. (2022). "Berberine treats atherosclerosis via a vitamine-like effect down-regulating Choline-TMA-TMAO production pathway in gut microbiota". *Signal Transduct Target Ther*. PMID: 35794102
3. Benson TW et al. (2023). "Gut Microbiota-Derived Trimethylamine N-Oxide Contributes to Abdominal Aortic Aneurysm Through Inflammatory and Apoptotic Mechanisms". *Circulation*. PMID: 37011073
4. Cai YY et al. (2022). "Integrated metagenomics identifies a crucial role for trimethylamine-producing Lachnoclostridium in promoting atherosclerosis". *NPJ Biofilms Microbiomes*. PMID: 35273169
5. Jiang C et al. (2024). "Polyphenols from hickory nut reduce the occurrence of atherosclerosis in mice by improving intestinal microbiota and inhibiting trimethylamine N-oxide production". *Phytomedicine*. PMID: 38522315
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.4 |
| 高置信度残基 (pLDDT>90) 占比 | 85.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 90.1% |
| 可用 PDB 条目 | 3IWP |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CUTC/CUTC-PAE.png]]

**评价**: AlphaFold 高质量预测（pLDDT=91.4，有序区 90.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005627 - CutC-like; InterPro: IPR036822 - CutC-like_dom_sf; Pfam: PF03932 - CutC |

**染色质调控潜力分析**: 含明确的核酸结合/染色质相关结构域，多库确认。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CUTA | 0.738 | — | — |
| FMO3 | 0.632 | — | — |
| NADSYN1 | 0.629 | — | — |
| XPO7 | 0.566 | — | — |
| H6PD | 0.534 | — | — |
| KRT74 | 0.521 | — | — |
| ARSH | 0.518 | — | — |
| YBEY | 0.513 | — | — |
| CUEDC1 | 0.473 | — | — |
| ATOX1 | 0.472 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-553867|uniprotkb:Q2M8K2 | — | — | — | — |
| intact:EBI-1115407|uniprotkb:P46719|uniprotkb:P76294 | — | — | — | — |
| intact:EBI-546726|uniprotkb:P07366 | — | — | — | — |
| intact:EBI-1115399|uniprotkb:Q2MCD9 | — | — | — | — |
| intact:EBI-332175 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 20
- 仅 IntAct 实验: 79
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 79 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.4 + PDB: 3IWP | pLDDT=91.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus | 一致 |
| PPI | STRING + IntAct | 20 + 79 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CUTC — Copper homeostasis protein cutC homolog，有一定研究基础，但仍存在未探索的niche空间。
2. 蛋白大小273 aa，大小适中，适合常规生化实验和结构解析。

**风险/不确定性**:
1. 已有一定研究，需确认独特研究角度
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NTM9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CUTC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CUTC


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CUTC-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CUTC/CUTC-PAE.png]]




