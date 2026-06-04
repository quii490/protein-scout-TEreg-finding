---
type: protein-evaluation
gene: "ITGB1BP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ITGB1BP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ITGB1BP1 / ICAP1 |
| 蛋白名称 | Integrin beta-1-binding protein 1 |
| 蛋白大小 | 200 aa / 21.8 kDa |
| UniProt ID | O14713 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton; Cell membrane;  |
| 蛋白大小 | 10/10 | ×1 | 10 | 200 aa / 21.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.8; PDB: 4DX8, 4DX9, 4JIF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019517, IPR006020; Pfam: PF10480 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton; Cell membrane; Cell projection, lamellipodium; Cell pro... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell periphery (GO:0071944)
- centriolar satellite (GO:0034451)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- lamellipodium (GO:0030027)
- membrane (GO:0016020)
- nuclear body (GO:0016604)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ICAP1 |

**关键文献**:
1. ITGB1BP1, a Novel Transcriptional Target of CD44-Downstream Signaling Promoting Cancer Cell Invasion.. *Breast cancer (Dove Medical Press)*. PMID: 37252376
2. Weighted single-step GWAS identified candidate genes associated with carcass traits in a Chinese yellow-feathered chicken population.. *Poultry science*. PMID: 38134459
3. Transcriptome-wide miRNA identification of Bacopa monnieri: a cross-kingdom approach.. *Plant signaling & behavior*. PMID: 31797719
4. Utility of an Untargeted Metabolomics Approach Using a 2D GC-GC-MS Platform to Distinguish Relapsing and Progressive Multiple Sclerosis.. *Metabolites*. PMID: 39330500
5. Neuronal expression of the Ccm2 gene in a new mouse model of cerebral cavernous malformations.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 16465592

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 60.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 15.0% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 67.5% |
| 可用 PDB 条目 | 4DX8, 4DX9, 4JIF |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4DX8, 4DX9, 4JIF）+ AlphaFold高质量预测（pLDDT=79.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019517, IPR006020; Pfam: PF10480 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRIT1 | 0.999 | 0.984 | — |
| ITGB1 | 0.998 | 0.971 | — |
| CCM2 | 0.991 | 0.784 | — |
| PDCD10 | 0.920 | 0.000 | — |
| ENSP00000498010 | 0.905 | 0.905 | — |
| RAP1A | 0.891 | 0.000 | — |
| NME2 | 0.878 | 0.292 | — |
| MAP3K3 | 0.834 | 0.000 | — |
| NME1 | 0.717 | 0.000 | — |
| SMURF1 | 0.655 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GSDME | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SLC35F5 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| UTRN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| NME2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11919189|imex:IM-20208 |
| ITGB1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11919189|imex:IM-20208 |
| DLD | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRIT1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| RHOH | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 4DX8, 4DX9, 4JIF | pLDDT=79.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton; Cell  / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
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
1. ITGB1BP1 — Integrin beta-1-binding protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小200 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14713
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119185-ITGB1BP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ITGB1BP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14713
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
