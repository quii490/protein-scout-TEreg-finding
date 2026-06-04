---
type: protein-evaluation
gene: "ELP5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELP5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELP5 / C17orf81, DERP6 |
| 蛋白名称 | Elongator complex protein 5 |
| 蛋白大小 | 300 aa / 33.2 kDa |
| UniProt ID | Q8TE02 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 300 aa / 33.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019519; Pfam: PF10483 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- elongator holoenzyme complex (GO:0033588)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf81, DERP6 |

**关键文献**:
1. Structural insights into the function of Elongator.. *Cellular and molecular life sciences : CMLS*. PMID: 29332244
2. Evolutionary Conservation in Protein-Protein Interactions and Structures of the Elongator Sub-Complex ELP456 from Arabidopsis and Yeast.. *International journal of molecular sciences*. PMID: 38673955
3. A comprehensive meta-analysis of transcriptome data to identify signature genes associated with pancreatic ductal adenocarcinoma.. *PloS one*. PMID: 38324544
4. Shared genetic basis and causality between schizophrenia and inflammatory bowel disease: evidence from a comprehensive genetic analysis.. *Psychological medicine*. PMID: 38563283
5. Characterization of a six-subunit holo-elongator complex required for the regulated expression of a group of genes in Saccharomyces cerevisiae.. *Molecular and cellular biology*. PMID: 11689709

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 28.7% |
| 置信残基 (pLDDT 70-90) 占比 | 48.7% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 6.0% |
| 有序区域 (pLDDT>70) 占比 | 77.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.9，有序区 77.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019519; Pfam: PF10483 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELP1 | 0.999 | 0.972 | — |
| ELP4 | 0.999 | 0.987 | — |
| ELP3 | 0.999 | 0.976 | — |
| ELP6 | 0.999 | 0.854 | — |
| ELP2 | 0.998 | 0.099 | — |
| PIPOX | 0.842 | 0.836 | — |
| KTI12 | 0.752 | 0.413 | — |
| CTU1 | 0.739 | 0.166 | — |
| DPH3 | 0.647 | 0.095 | — |
| MOCS3 | 0.631 | 0.046 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ELP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ELP3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| IKI1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| Elp4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG17777 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| SPT7 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-15346|pubmed:21734642 |
| IKI3 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| ELP6 | psi-mi:"MI:0096"(pull down) | pubmed:15138274|imex:IM-19261 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 无 | pLDDT=78.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. ELP5 — Elongator complex protein 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小300 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TE02
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170291-ELP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TE02
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
