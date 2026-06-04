---
type: protein-evaluation
gene: "CLTB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLTB — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLTB |
| 蛋白名称 | Clathrin light chain B |
| 蛋白大小 | 229 aa / 25.2 kDa |
| UniProt ID | P09497 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; 额外: Plasma membrane, Cytosol; UniProt: Cytoplasmic vesicle membrane; Membrane, coated pit |
| 蛋白大小 | 10/10 | ×1 | 10 | 229 aa / 25.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000996; Pfam: PF01086 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasmic vesicle membrane; Membrane, coated pit | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary membrane (GO:0060170)
- clathrin coat (GO:0030118)
- clathrin coat of coated pit (GO:0030132)
- clathrin coat of trans-Golgi network vesicle (GO:0030130)
- clathrin vesicle coat (GO:0030125)
- clathrin-coated endocytic vesicle (GO:0045334)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Integrative single-cell RNA sequencing and mendelian randomization analysis reveal the potential role of synaptic vesicle cycling-related genes in Alzheimer's disease.. *The journal of prevention of Alzheimer's disease*. PMID: 40021385
2. Clathrin Light Chain B Drives Hepatocellular Carcinoma Progression Through Dual Mechanisms: Small Extracellular Vesicle-Mediated Angiogenesis and the NF-κB-PCLAF Signaling Axis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40820941
3. A Novel Proximity Biotinylation Assay Based on the Self-Associating Split GFP1-10/11.. *Proteomes*. PMID: 33276494
4. Cloning and sequence analysis of a low temperature-induced gene from trifoliate orange with unusual pre-mRNA processing.. *Plant cell reports*. PMID: 15138696
5. Chromosomal location and some structural features of human clathrin light-chain genes (CLTA and CLTB).. *Genomics*. PMID: 7713494

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.4 |
| 高置信度残基 (pLDDT>90) 占比 | 24.5% |
| 置信残基 (pLDDT 70-90) 占比 | 38.0% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 24.9% |
| 有序区域 (pLDDT>70) 占比 | 62.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.4，有序区 62.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000996; Pfam: PF01086 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLTCL1 | 0.999 | 0.928 | — |
| CLTC | 0.999 | 0.913 | — |
| AP2A1 | 0.992 | 0.637 | — |
| CLTA | 0.985 | 0.634 | — |
| AP2B1 | 0.979 | 0.697 | — |
| AP2A2 | 0.968 | 0.612 | — |
| HIP1 | 0.965 | 0.756 | — |
| HIP1R | 0.960 | 0.801 | — |
| AP2S1 | 0.960 | 0.163 | — |
| AP2M1 | 0.942 | 0.597 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PQBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| HSPA8 | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| ALYREF | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| APPL1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CAPZA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KIT | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.4 + PDB: 无 | pLDDT=72.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle membrane; Membrane, coated pit / Vesicles; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLTB — Clathrin light chain B，非常新颖，仅有少数基础研究。
2. 蛋白大小229 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09497
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175416-CLTB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLTB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09497
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
