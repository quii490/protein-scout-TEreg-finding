---
type: protein-evaluation
gene: "ARFGEF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARFGEF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARFGEF1 / ARFGEP1, BIG1 |
| 蛋白名称 | Brefeldin A-inhibited guanine nucleotide-exchange protein 1 |
| 蛋白大小 | 1849 aa / 208.8 kDa |
| UniProt ID | Q9Y6D6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Golgi apparatus; G |
| 蛋白大小 | 5/10 | ×1 | 5 | 1849 aa / 208.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.4; PDB: 3LTL, 5EE5, 5J5C |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR032629, IPR015403, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Golgi apparatus; Golgi apparatus, trans-Golgi network memb... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nuclear matrix (GO:0016363)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)
- small nuclear ribonucleoprotein complex (GO:0030532)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARFGEP1, BIG1 |

**关键文献**:
1. The Novel KLF4/BIG1 Regulates LPS-mediated Neuro-inflammation and Migration in BV2 Cells via PI3K/Akt/NF-kB Signaling Pathway.. *Neuroscience*. PMID: 35090882
2. Haploinsufficiency of ARFGEF1 is associated with developmental delay, intellectual disability, and epilepsy with variable expressivity.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 34113008
3. Expanding the Phenotypic and Genotypic Spectrum of ARFGEF1-Related Neurodevelopmental Disorder.. *Frontiers in molecular neuroscience*. PMID: 35782386
4. Genetic Variants Associated with Breast Cancer Are Detected by Whole-Exome Sequencing in Vietnamese Patients.. *Diagnostics (Basel, Switzerland)*. PMID: 40941673
5. Zebrafish models of candidate human epilepsy-associated genes provide evidence of hyperexcitability.. *bioRxiv : the preprint server for biology*. PMID: 38370728

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 40.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 21.0% |
| 有序区域 (pLDDT>70) 占比 | 73.5% |
| 可用 PDB 条目 | 3LTL, 5EE5, 5J5C |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3LTL, 5EE5, 5J5C）+ AlphaFold高质量预测（pLDDT=75.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR032629, IPR015403, IPR032691; Pfam: PF20252, PF16213, PF01369 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARL1 | 0.940 | 0.910 | — |
| MYO9B | 0.901 | 0.330 | — |
| ARFGEF2 | 0.830 | 0.787 | — |
| NUP62 | 0.822 | 0.510 | — |
| NCL | 0.807 | 0.510 | — |
| UBR5 | 0.778 | 0.000 | — |
| KIF21A | 0.688 | 0.510 | — |
| PPP1CC | 0.673 | 0.292 | — |
| FBL | 0.668 | 0.292 | — |
| MYCBP | 0.664 | 0.627 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| vpu | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| SCHIP1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ENSP00000262215.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| arcB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| CSGALNACT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCL1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HNRNPU | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 3LTL, 5EE5, 5J5C | pLDDT=75.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Golgi ap / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ARFGEF1 — Brefeldin A-inhibited guanine nucleotide-exchange protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1849 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6D6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000066777-ARFGEF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARFGEF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6D6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
