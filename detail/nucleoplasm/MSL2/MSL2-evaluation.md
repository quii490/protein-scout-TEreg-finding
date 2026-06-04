---
type: protein-evaluation
gene: "MSL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MSL2 — REJECTED (研究热度过高 (PubMed strict=121，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MSL2 / KIAA1585, MSL2L1, RNF184 |
| 蛋白名称 | E3 ubiquitin-protein ligase MSL2 |
| 蛋白大小 | 577 aa / 62.5 kDa |
| UniProt ID | Q9HCI7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 577 aa / 62.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=121 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.9; PDB: 4B7Y, 4B86 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037922, IPR032049, IPR032043, IPR033467, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- MSL complex (GO:0072487)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 121 |
| PubMed broad count | 200 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1585, MSL2L1, RNF184 |

**关键文献**:
1. MSL2 ensures biallelic gene expression in mammals.. *Nature*. PMID: 38030723
2. MSL2 variants lead to a neurodevelopmental syndrome with lack of coordination, epilepsy, specific dysmorphisms, and a distinct episignature.. *American journal of human genetics*. PMID: 38815585
3. The MDM2 gene family.. *Biomolecular concepts*. PMID: 25372739
4. Novel protein-truncating variants of a chromatin-modifying gene MSL2 in syndromic neurodevelopmental disorders.. *European journal of human genetics : EJHG*. PMID: 38702431
5. Physical interaction between MSL2 and CLAMP assures direct cooperativity and prevents competition at composite binding sites.. *Nucleic acids research*. PMID: 37602401

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.9 |
| 高置信度残基 (pLDDT>90) 占比 | 16.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 14.9% |
| 低置信 (pLDDT<50) 占比 | 57.2% |
| 有序区域 (pLDDT>70) 占比 | 27.9% |
| 可用 PDB 条目 | 4B7Y, 4B86 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.9），有序残基占 27.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037922, IPR032049, IPR032043, IPR033467, IPR001841; Pfam: PF16682, PF16685 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MSL3 | 0.999 | 0.930 | — |
| MSL1 | 0.999 | 0.950 | — |
| KAT8 | 0.995 | 0.869 | — |
| KAT5 | 0.951 | 0.239 | — |
| MORF4L1 | 0.930 | 0.141 | — |
| EPC1 | 0.909 | 0.000 | — |
| ACTB | 0.908 | 0.000 | — |
| TRRAP | 0.906 | 0.000 | — |
| MBTD1 | 0.906 | 0.000 | — |
| EP400 | 0.905 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A0F7RG51 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| YWHAE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| WNK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| Kat8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| A0A384L4Z3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TRIM8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| NHLRC2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| IGHG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.9 + PDB: 4B7Y, 4B86 | pLDDT=55.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MSL2 — E3 ubiquitin-protein ligase MSL2，研究基础较多，新颖性有限。
2. 蛋白大小577 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 121 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 121 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCI7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174579-MSL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCI7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
