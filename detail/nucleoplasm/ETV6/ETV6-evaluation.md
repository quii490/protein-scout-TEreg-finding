---
type: protein-evaluation
gene: "ETV6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ETV6 — REJECTED (研究热度过高 (PubMed strict=1351，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETV6 / TEL, TEL1 |
| 蛋白名称 | Transcription factor ETV6 |
| 蛋白大小 | 452 aa / 53.0 kDa |
| UniProt ID | P41212 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 452 aa / 53.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1351 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.8; PDB: 1JI7, 1LKY, 2DAO, 2QAR, 2QB0, 2QB1, 5L0P |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1351 |
| PubMed broad count | 2223 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TEL, TEL1 |

**关键文献**:
1. Identification of ETV6-RUNX1-like and DUX4-rearranged subtypes in paediatric B-cell precursor acute lymphoblastic leukaemia.. *Nature communications*. PMID: 27265895
2. Updates on eosinophilic disorders.. *Virchows Archiv : an international journal of pathology*. PMID: 36068374
3. ETV6::ACSL6 translocation-driven super-enhancer activation leads to eosinophilia in acute lymphoblastic leukemia through IL-3 overexpression.. *Haematologica*. PMID: 38356460
4. Mechanism of ETV6-RUNX1 Leukemia.. *Advances in experimental medicine and biology*. PMID: 28299659
5. Translocations and Gene Fusions in Sinonasal Malignancies.. *Current oncology reports*. PMID: 36753024

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.8 |
| 高置信度残基 (pLDDT>90) 占比 | 19.5% |
| 置信残基 (pLDDT 70-90) 占比 | 19.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.3% |
| 低置信 (pLDDT<50) 占比 | 47.8% |
| 有序区域 (pLDDT>70) 占比 | 39.0% |
| 可用 PDB 条目 | 1JI7, 1LKY, 2DAO, 2QAR, 2QB0, 2QB1, 5L0P, 7JU2, 7N1O, 7N2B |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.8），有序残基占 39.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR036388; Pfam: PF00178, PF02198 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RUNX1 | 0.983 | 0.060 | — |
| NTRK3 | 0.972 | 0.074 | — |
| ETV7 | 0.971 | 0.679 | — |
| ABL1 | 0.932 | 0.074 | — |
| PDGFRB | 0.893 | 0.292 | — |
| ABL2 | 0.863 | 0.074 | — |
| CHIC2 | 0.853 | 0.000 | — |
| IKZF1 | 0.838 | 0.068 | — |
| NRAS | 0.838 | 0.091 | — |
| ASXL1 | 0.833 | 0.047 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| fldB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000379658.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HDAC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| ETV7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NID2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.8 + PDB: 1JI7, 1LKY, 2DAO, 2QAR, 2QB0,  | pLDDT=61.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ETV6 — Transcription factor ETV6，研究基础较多，新颖性有限。
2. 蛋白大小452 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1351 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1351 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P41212
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139083-ETV6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ETV6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P41212
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
