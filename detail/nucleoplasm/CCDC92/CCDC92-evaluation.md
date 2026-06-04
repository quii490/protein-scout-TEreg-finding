---
type: protein-evaluation
gene: "CCDC92"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC92 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC92 / CCDC92 |
| 蛋白大小 | 331 aa / ~36.4 kDa |
| UniProt ID | Q53HC0 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 5/10 | ×4 | 20 | UniProt Centrosome/centriole + GO nucleoplasm，centrosomal为主 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 331 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=23篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | 良好（pLDDT 73.3），49%有序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | 4/30调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Cytoplasm | — |
| GO Cellular Component | C:centriole; C:centrosome; C:cytoplasm; C:nucleoplasm | — |
| Protein Atlas (IF) | nucleoplasm+centrosome (Approved, A-431) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC92/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC92/IF_images/A-431_2.jpg|A-431]]

**结论**: UniProt Centrosome/centriole + GO nucleoplasm，centrosomal为主

#### 3.2 蛋白大小评估
**评价**: 331 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 23 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 23 篇。非常新颖，研究空间充足。

**关键文献**:
1. Zuo F et al. (2024). "CCDC92 deficiency ameliorates podocyte lipotoxicity in diabetic kidney disease". *Metabolism*. PMID: 37952690
2. Zuo FW et al. (2024). "CCDC92 promotes podocyte injury by regulating PA28α/ABCA1/cholesterol efflux axis in type 2 diabetic mice". *Acta Pharmacol Sin*. PMID: 38228909
3. Tang H et al. (2023). "Transcriptome-wide association study-derived genes as potential visceral adipose tissue-specific targets for type 2 diabetes". *Diabetologia*. PMID: 37540242
4. Huang LO et al. (2021). "Genome-wide discovery of genetic loci that uncouple excess adiposity from its comorbidities". *Nat Metab*. PMID: 33619380
5. Rezi CK et al. (2025). "KIF13B controls ciliary protein content by promoting endocytic retrieval and suppressing release of large extracellular vesicles from cilia". *Curr Biol*. PMID: 40930094
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 73.3 |
| 有序区域 (pLDDT>70) 占比 | 49.3% |
| pLDDT>90 占比 | 39.6% |
| pLDDT<50 占比 | 17.8% |
| 可用 PDB 条目 | 0 |


**评价**: AlphaFold中等质量（pLDDT 73.3，49%有序）。作为新颖蛋白（PubMed=23），此结构水平可接受（基线6分）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:ccd92_human(display_long)|uniprotkb:Limkain beta-2(gene name synonym)|uniprotkb:CCDC92(gene name)|psi-mi:CCDC92(display_short) | psi-mi:"MI:1356"(validated two | pubmed:32296183|imex:IM-25472 | 待分析 | 是 |
| psi-mi:ccd92_human(display_long)|uniprotkb:Limkain beta-2(gene name synonym)|uniprotkb:CCDC92(gene name)|psi-mi:CCDC92(display_short) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 是 |
| psi-mi:ccd92_human(display_long)|uniprotkb:Limkain beta-2(gene name synonym)|uniprotkb:CCDC92(gene name)|psi-mi:CCDC92(display_short) | psi-mi:"MI:1112"(two hybrid pr | pubmed:32296183|imex:IM-25472 | 待分析 | 是 |
| psi-mi:scg1_human(display_long)|uniprotkb:Secretogranin I(gene name synonym)|uniprotkb:Chromogranin-B(gene name synonym)|uniprotkb:CHGB(gene name)|psi-mi:CHGB(display_short)|uniprotkb:SCG1(gene name synonym) | psi-mi:"MI:0398"(two hybrid po | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | 待分析 | 否 |
| psi-mi:a0a6l8ppq8_bacan(display_long)|uniprotkb:GBAA_5256(locus name) | psi-mi:"MI:0398"(two hybrid po | imex:IM-13779|pubmed:20711500 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| PSMD8 | 0.875 | 待分析 | 否 |
| ADRM1 | 0.835 | 待分析 | 否 |
| PSMC1 | 0.832 | 待分析 | 否 |
| PSMD10 | 0.832 | 待分析 | 否 |
| PSMD14 | 0.829 | 待分析 | 否 |
| PSMD2 | 0.829 | 待分析 | 否 |
| PSMD13 | 0.825 | 待分析 | 否 |
| PSMC6 | 0.824 | 待分析 | 否 |
| PSMD12 | 0.823 | 待分析 | 否 |
| PSMC5 | 0.814 | 待分析 | 否 |


**已知复合体成员** (GO Cellular Component): C:centriole; C:centrosome; C:cytoplasm; C:nucleoplasm

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 30 个伙伴
- 调控相关比例: 4/30 (13%)

**评价**: PPI网络有部分调控关联（4/30），48个物理互作，功能关联中等。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 良好（pLDDT 73.3），49%有序 | 待验证 |
| 定位 | UniProt + GO | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Cytoplasm | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **67.2/100**

**核心优势**:
1. PubMed 23 篇，研究新颖性高
2. 蛋白大小 331 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53HC0
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53HC0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CCDC92%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CCDC92&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CCDC92


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC92/CCDC92-PAE.png]]




