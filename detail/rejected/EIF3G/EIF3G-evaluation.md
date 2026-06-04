---
type: protein-evaluation
gene: "EIF3G"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF3G — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF3G |
| 蛋白名称 | Eukaryotic translation initiation factor 3 subunit G |
| 蛋白大小 | 320 aa / 35.6 kDa |
| UniProt ID | O75821 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 320 aa / 35.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=57 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.2; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 57 |
| PubMed broad count | 57 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Eukaryotic Initiation Factor 3F (eIF3F) Regulates the IRES-Mediated Translation of Bcl-xL via Its Interaction with Programmed Cell Death 4 (PDCD4) Protein.. *Int J Mol Sci*. PMID: 42123540
2. eIF3g binding to GUCG boxes located in mRNA coding regions enhances translation of mild heat shock response genes in the yeast Saccharomyces cerevisiae.. *Nucleic Acids Res*. PMID: 41556339
3. Yeast Eukaryotic Initiation Factor 4B Remodels the MRNA Entry Site on the Small Ribosomal Subunit.. *Biochemistry*. PMID: 39847343
4. N(6)-methyladenosine in 28S rRNA promotes oncogenic mRNA translation and tyrosine catabolism.. *Cell Rep*. PMID: 39739529
5. 40S ribosomal subunits scan mRNA for the start codon by one-dimensional diffusion.. *bioRxiv*. PMID: 39803544

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.2 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 34.7% |
| 中等置信 (pLDDT 50-70) 占比 | 25.9% |
| 低置信 (pLDDT<50) 占比 | 18.4% |
| 有序区域 (pLDDT>70) 占比 | 55.6% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=70.2，有序区 55.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF5 | 0.000 | 0.000 | — |
| EIF3B | 0.000 | 0.000 | — |
| EIF3A | 0.000 | 0.000 | — |
| EIF3L | 0.000 | 0.000 | — |
| EIF3F | 0.000 | 0.000 | — |
| EIF3E | 0.000 | 0.000 | — |
| EIF3M | 0.000 | 0.000 | — |
| EIF3H | 0.000 | 0.000 | — |
| EIF3K | 0.000 | 0.000 | — |
| EIF3C | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9SSJ0 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O75821 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Z1D1 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q96331 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.2 + PDB: 无 | pLDDT=70.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, perinuclear region / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EIF3G — Eukaryotic translation initiation factor 3 subunit G，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小320 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 57 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75821
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130811-EIF3G/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF3G
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75821
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
