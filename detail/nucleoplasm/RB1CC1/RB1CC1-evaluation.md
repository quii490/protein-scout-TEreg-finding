---
type: protein-evaluation
gene: "RB1CC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RB1CC1 — REJECTED (研究热度过高 (PubMed strict=176，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RB1CC1 / KIAA0203, RBICC |
| 蛋白名称 | RB1-inducible coiled-coil protein 1 |
| 蛋白大小 | 1594 aa / 183.1 kDa |
| UniProt ID | Q8TDY2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nuclear membrane; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytosol; Preautophagosomal st |
| 蛋白大小 | 5/10 | ×1 | 5 | 1594 aa / 183.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=176 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.5; PDB: 6DCE, 6GMA, 7CZG, 7CZM, 7D0E, 7EA2, 7EAA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040040, IPR019460; Pfam: PF10377 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear membrane | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytosol; Preautophagosomal structure; Lysosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Atg1/ULK1 kinase complex (GO:1990316)
- autophagosome membrane (GO:0000421)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- lysosome (GO:0005764)
- nuclear membrane (GO:0031965)
- phagophore assembly site (GO:0000407)
- phagophore assembly site membrane (GO:0034045)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 176 |
| PubMed broad count | 359 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0203, RBICC |

**关键文献**:
1. Acetylation in the regulation of autophagy.. *Autophagy*. PMID: 35435793
2. How autophagy controls the intestinal epithelial barrier.. *Autophagy*. PMID: 33906557
3. Multifaceted roles of TAX1BP1 in autophagy.. *Autophagy*. PMID: 35470757
4. Reticulophagy and viral infection.. *Autophagy*. PMID: 39394962
5. Autophagy in the physiological endometrium and cancer.. *Autophagy*. PMID: 32401642

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.5 |
| 高置信度残基 (pLDDT>90) 占比 | 22.1% |
| 置信残基 (pLDDT 70-90) 占比 | 50.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 19.8% |
| 有序区域 (pLDDT>70) 占比 | 72.7% |
| 可用 PDB 条目 | 6DCE, 6GMA, 7CZG, 7CZM, 7D0E, 7EA2, 7EAA, 8SOI, 8SQZ, 8SRM |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6DCE, 6GMA, 7CZG, 7CZM, 7D0E, 7EA2, 7EAA, 8SOI, 8SQZ, 8SRM）+ AlphaFold极高置信度预测（pLDDT=72.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040040, IPR019460; Pfam: PF10377 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BECN1 | 0.999 | 0.994 | — |
| ULK2 | 0.999 | 0.399 | — |
| ULK1 | 0.999 | 0.995 | — |
| CCPG1 | 0.999 | 0.910 | — |
| ATG16L1 | 0.999 | 0.825 | — |
| ATG14 | 0.999 | 0.994 | — |
| NRBF2 | 0.999 | 0.994 | — |
| CALCOCO2 | 0.999 | 0.933 | — |
| ATG101 | 0.999 | 0.840 | — |
| ATG13 | 0.999 | 0.859 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000025008.5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Stat1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ERCC6L | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| POLR1E | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MOB4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DBNL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATG12 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK19 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CALCOCO2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.5 + PDB: 6DCE, 6GMA, 7CZG, 7CZM, 7D0E,  | pLDDT=72.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytosol; Preautopha / Cytosol; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RB1CC1 — RB1-inducible coiled-coil protein 1，研究基础较多，新颖性有限。
2. 蛋白大小1594 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 176 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 176 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TDY2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000023287-RB1CC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RB1CC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TDY2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
