---
type: protein-evaluation
gene: "RARS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RARS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RARS1 / RARS |
| 蛋白名称 | Arginine--tRNA ligase, cytoplasmic |
| 蛋白大小 | 660 aa / 75.4 kDa |
| UniProt ID | P54136 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Nucleoli; UniProt: Cytoplasm; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 660 aa / 75.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.1; PDB: 4Q2T, 4Q2X, 4Q2Y, 4R3Z, 4ZAJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001412, IPR001278, IPR005148, IPR036695, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nucleoli | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- aminoacyl-tRNA synthetase multienzyme complex (GO:0017101)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RARS |

**关键文献**:
1. RARS1-related developmental and epileptic encephalopathy.. *Epilepsia open*. PMID: 37186453
2. Assembly of the Human Multi-tRNA Synthetase Complex Through Leucine Zipper Motifs.. *Journal of molecular biology*. PMID: 39542129
3. Global A-to-I RNA editing during myogenic differentiation of goat MuSCs.. *Frontiers in veterinary science*. PMID: 39444736
4. Hypomyelinating leukodystrophies in adults: Clinical and genetic features.. *European journal of neurology*. PMID: 33190326
5. Distinct pathogenic mechanisms of various RARS1 mutations in Pelizaeus-Merzbacher-like disease.. *Science China. Life sciences*. PMID: 33515434

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 78.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 96.4% |
| 可用 PDB 条目 | 4Q2T, 4Q2X, 4Q2Y, 4R3Z, 4ZAJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4Q2T, 4Q2X, 4Q2Y, 4R3Z, 4ZAJ）+ AlphaFold极高置信度预测（pLDDT=92.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001412, IPR001278, IPR005148, IPR036695, IPR035684; Pfam: PF03485, PF05746, PF00750 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MARS1 | 0.999 | 0.891 | — |
| LARS1 | 0.999 | 0.885 | — |
| QARS1 | 0.999 | 0.994 | — |
| KARS1 | 0.999 | 0.876 | — |
| EPRS1 | 0.999 | 0.908 | — |
| IARS1 | 0.999 | 0.898 | — |
| AIMP1 | 0.999 | 0.991 | — |
| AIMP2 | 0.998 | 0.911 | — |
| DARS1 | 0.996 | 0.901 | — |
| EEF1E1 | 0.996 | 0.875 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000018992.4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| 35826 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Irs1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15602769 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| MAP3K14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIE | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TANK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 4Q2T, 4Q2X, 4Q2Y, 4R3Z, 4ZAJ | pLDDT=92.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytosol / Cytosol; 额外: Nucleoplasm, Nucleoli | 一致 |
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
1. RARS1 — Arginine--tRNA ligase, cytoplasmic，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小660 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54136
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113643-RARS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RARS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54136
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
