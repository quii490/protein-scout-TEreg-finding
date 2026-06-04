---
type: protein-evaluation
gene: "BACH2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BACH2 — REJECTED (研究热度过高 (PubMed strict=286，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BACH2 |
| 蛋白名称 | Transcription regulator protein BACH2 |
| 蛋白大小 | 841 aa / 92.5 kDa |
| UniProt ID | Q9BYV9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 841 aa / 92.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=286 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.6; PDB: 3OHU, 3OHV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000210, IPR004827, IPR043321, IPR004826, IPR046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 286 |
| PubMed broad count | 523 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The role of transcription factors in shaping regulatory T cell identity.. *Nature reviews. Immunology*. PMID: 37336954
2. Repurposing the CRISPR-Cas9 system for targeted DNA methylation.. *Nucleic acids research*. PMID: 26969735
3. Cannabinoid Receptor 2-Centric Molecular Feedback Loop Drives Necroptosis in Diabetic Heart Injuries.. *Circulation*. PMID: 36448459
4. BACH2 enforces the transcriptional and epigenetic programs of stem-like CD8(+) T cells.. *Nature immunology*. PMID: 33574619
5. TBL1XR1 Mutations Drive Extranodal Lymphoma by Inducing a Pro-tumorigenic Memory Fate.. *Cell*. PMID: 32619424

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.6 |
| 高置信度残基 (pLDDT>90) 占比 | 19.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 66.2% |
| 有序区域 (pLDDT>70) 占比 | 28.7% |
| 可用 PDB 条目 | 3OHU, 3OHV |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.6），有序残基占 28.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000210, IPR004827, IPR043321, IPR004826, IPR046347; Pfam: PF00651, PF03131 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAF | 0.993 | 0.184 | — |
| MAFG | 0.981 | 0.683 | — |
| MAFK | 0.980 | 0.681 | — |
| MAFF | 0.955 | 0.653 | — |
| NCOR1 | 0.890 | 0.168 | — |
| IRF4 | 0.853 | 0.000 | — |
| NCOR2 | 0.851 | 0.362 | — |
| PRDM1 | 0.809 | 0.088 | — |
| PAX5 | 0.803 | 0.065 | — |
| AICDA | 0.769 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Plcg2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ARRB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| sbcC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| COPS6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| TRIM42 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BATF3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MLX | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SCNM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ELOA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAFK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.6 + PDB: 3OHU, 3OHV | pLDDT=53.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. BACH2 — Transcription regulator protein BACH2，研究基础较多，新颖性有限。
2. 蛋白大小841 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 286 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 286 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BYV9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112182-BACH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BACH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BYV9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
