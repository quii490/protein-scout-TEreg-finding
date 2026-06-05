---
type: protein-evaluation
gene: "CLIC5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLIC5 — REJECTED (研究热度过高 (PubMed strict=104，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLIC5 |
| 蛋白名称 | Chloride intracellular channel protein 5 |
| 蛋白大小 | 410 aa / 46.5 kDa |
| UniProt ID | Q9NZA1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Plasma membrane; 额外: Nuclear speckles; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; Membrane; A |
| 蛋白大小 | 10/10 | x1 | 10 | 410 aa / 46.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=104 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=68.0; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 25 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.0/180** | |
| **归一化总分** | | | **35.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nuclear speckles | Supported |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; Membrane; Apical cell membrane; Cytoplasm; Mitochon... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 104 |
| PubMed broad count | 110 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CLIC5B attenuates pro-inflammatory fibroblast migration through inhibition of the CLIC1/CLIC4-PIP5K1 axis.. *Tissue Cell*. PMID: 41922125
2. Use of biomolecular emulator for characterizing flexible proteins by small-angle x-ray scattering.. *Protein Sci*. PMID: 42178622
3. Translocator protein in touch with mitochondrial chloride intracellular channel CLIC5.. *Biochem Biophys Res Commun*. PMID: 41764818
4. Human CLIC5 as a Recurrent Hotspot of HPV 16 Integration in Cervical Cancer.. *J Med Virol*. PMID: 41923498
5. Exclusion of CLIC5 as a Candidate Gene and Identification of NEFM as a Possible Novel Gene Correlated With Autosomal Recessive Pure Cerebellar Ataxia in a Highly Consanguineous Family.. *Mol Genet Genomic Med*. PMID: 41913087

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.0 |
| 高置信度残基 (pLDDT>90) 占比 | 47.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 42.0% |
| 有序区域 (pLDDT>70) 占比 | 55.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.0），有序残基占 55.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TPRN | 0.000 | 0.000 | — |
| EZR | 0.000 | 0.000 | — |
| RDX | 0.000 | 0.000 | — |
| GRXCR2 | 0.000 | 0.000 | — |
| MYO7A | 0.000 | 0.000 | — |
| PLS1 | 0.000 | 0.000 | — |
| CLIC4 | 0.000 | 0.000 | — |
| CLIC2 | 0.000 | 0.000 | — |
| RIPOR2 | 0.000 | 0.000 | — |
| MSN | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O43504 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |
| uniprotkb:Q8BXK9 | psi-mi:"MI:0276"(blue native page) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NZA1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P78362 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:- |
| uniprotkb:Q96SB4 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:- |
| uniprotkb:Q9NZA1-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O15247 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q4KMQ1-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q14651 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q4KMQ1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 25
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 25 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.0 + PDB: 无 | pLDDT=68.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; M / Plasma membrane; 额外: Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 25 + 25 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CLIC5 -- Chloride intracellular channel protein 5，研究基础较多，新颖性有限。
2. 蛋白大小410 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 104 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 104 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZA1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112782-CLIC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLIC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZA1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NZA1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
