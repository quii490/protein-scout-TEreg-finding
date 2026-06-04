---
type: protein-evaluation
gene: "EME2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EME2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EME2 |
| 蛋白名称 | Structure-specific endonuclease subunit EME2 |
| 蛋白大小 | 379 aa / 41.2 kDa |
| UniProt ID | A4GXA9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 379 aa / 41.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=79.9; PDB: 7F6L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042530, IPR006166, IPR033310, IPR047523; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- endodeoxyribonuclease complex (GO:1905347)
- Holliday junction resolvase complex (GO:0048476)
- nuclear replication fork (GO:0043596)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The plasma peptides of Alzheimer's disease.. *Clinical proteomics*. PMID: 34182925
2. MUS81-EME2 promotes replication fork restart.. *Cell reports*. PMID: 24813886
3. Crystal structure of the human MUS81-EME2 complex.. *Structure (London, England : 1993)*. PMID: 35290797
4. A Novel Four Mitochondrial Respiration-Related Signature for Predicting Biochemical Recurrence of Prostate Cancer.. *Journal of clinical medicine*. PMID: 36675580
5. Investigation of the immunogenicity of Zika glycan loop.. *Virology journal*. PMID: 32234060

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 52.2% |
| 置信残基 (pLDDT 70-90) 占比 | 22.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 15.8% |
| 有序区域 (pLDDT>70) 占比 | 74.9% |
| 可用 PDB 条目 | 7F6L |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/EME2/EME2-PAE.png]]

**评价**: AlphaFold 高质量预测（pLDDT=79.9，有序区 74.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042530, IPR006166, IPR033310, IPR047523; Pfam: PF21292, PF02732 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MUS81 | 0.999 | 0.930 | — |
| EME1 | 0.985 | 0.000 | — |
| ERCC4 | 0.905 | 0.098 | — |
| FAAP24 | 0.825 | 0.292 | — |
| FANCM | 0.807 | 0.334 | — |
| SLX4 | 0.733 | 0.059 | — |
| EXO1 | 0.718 | 0.140 | — |
| DNA2 | 0.710 | 0.197 | — |
| PALB2 | 0.697 | 0.290 | — |
| SLX1A | 0.679 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MUS81 | psi-mi:"MI:0096"(pull down) | pubmed:17289582|imex:IM-25488 |
| ENSP00000457353.1 | psi-mi:"MI:1034"(nuclease assay) | pubmed:17289582|imex:IM-25488 |
| ENST00000568449 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 7F6L | pLDDT=79.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EME2 — Structure-specific endonuclease subunit EME2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小379 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A4GXA9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197774-EME2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EME2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A4GXA9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/EME2/EME2-PAE.png]]
