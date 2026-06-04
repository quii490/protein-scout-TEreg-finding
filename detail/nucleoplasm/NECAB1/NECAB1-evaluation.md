---
type: protein-evaluation
gene: "NECAB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NECAB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NECAB1 / EFCBP1 |
| 蛋白名称 | N-terminal EF-hand calcium-binding protein 1 |
| 蛋白大小 | 351 aa / 40.6 kDa |
| UniProt ID | Q8N987 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitotic spindle, Primary cilium, Primary ci; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 351 aa / 40.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007138, IPR011008, IPR011992, IPR018247, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic spindle, Primary cilium, Primary cilium tip, Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EFCBP1 |

**关键文献**:
1. Identification of hub genes and construction of diagnostic nomogram model in schizophrenia.. *Frontiers in aging neuroscience*. PMID: 36313022
2. Distribution of NECAB1-Positive Neurons in Normal and Epileptic Brain-Expression Changes in Temporal Lobe Epilepsy and Modulation by Levetiracetam and Brivaracetam.. *International journal of molecular sciences*. PMID: 40430045
3. EFCBP1/NECAB1, a brain-specifically expressed gene with highest abundance in temporal lobe, encodes a protein containing EF-hand and antibiotic biosynthesis monooxygenase domains.. *DNA sequence : the journal of DNA sequencing and mapping*. PMID: 17364817
4. Identification of diagnostic gene biomarkers related to immune infiltration in patients with idiopathic pulmonary fibrosis based on bioinformatics strategies.. *Frontiers in medicine*. PMID: 36507532
5. Insights Into the Antigenic Repertoire of Unclassified Synaptic Antibodies.. *Annals of clinical and translational neurology*. PMID: 41195642

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 57.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 17.7% |
| 有序区域 (pLDDT>70) 占比 | 73.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.1，有序区 73.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007138, IPR011008, IPR011992, IPR018247, IPR002048; Pfam: PF03992 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NECAB3 | 0.798 | 0.784 | — |
| NECAB2 | 0.792 | 0.773 | — |
| SYT1 | 0.573 | 0.053 | — |
| WDR90 | 0.566 | 0.298 | — |
| CALB1 | 0.457 | 0.109 | — |
| CALB2 | 0.445 | 0.109 | — |
| H3BUI4_HUMAN | 0.434 | 0.000 | — |
| KRTAP10-4 | 0.416 | 0.000 | — |
| EFCAB1 | 0.413 | 0.177 | — |
| KLHL32 | 0.410 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000387380.2 | psi-mi:"MI:0090"(protein complementation assay) | pubmed:32296183|imex:IM-25472 |
| CCDC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MPRIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NECAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF138 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UTP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCRS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NECAB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KANSL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAI14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 无 | pLDDT=79.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Mitotic spindle, Primary cilium,  | 一致 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NECAB1 — N-terminal EF-hand calcium-binding protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小351 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N987
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123119-NECAB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NECAB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N987
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
