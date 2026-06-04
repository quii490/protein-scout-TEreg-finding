---
type: protein-evaluation
gene: "DDX52"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX52 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX52 / ROK1 |
| 蛋白名称 | Probable ATP-dependent RNA helicase DDX52 |
| 蛋白大小 | 599 aa / 67.5 kDa |
| UniProt ID | Q9Y2R4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | x1 | 10 | 599 aa / 67.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=76.6; PDB: 3DKP |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR044764, IPR011545, IPR050079, IPR014001, IPR001 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ROK1 |

**关键文献**:
1. DDX52 gene expression in LUAD tissues indicates potential as a prognostic biomarker and therapeutic target.. *Scientific reports*. PMID: 37833424
2. The RNA helicase Ddx52 functions as a growth switch in juvenile zebrafish.. *Development (Cambridge, England)*. PMID: 34323273
3. The human DDX52 protein is a nucleic acid helicase and strand annealase that promotes cell migration.. *Bioscience reports*. PMID: 41510705
4. DDX52 knockdown inhibits the growth of prostate cancer cells by regulating c-Myc signaling.. *Cancer cell international*. PMID: 34399732
5. Expression and alternative splicing of folate pathway genes in HapMap lymphoblastoid cell lines.. *Pharmacogenomics*. PMID: 19374514

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.6 |
| 高置信度残基 (pLDDT>90) 占比 | 38.7% |
| 置信残基 (pLDDT 70-90) 占比 | 35.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 18.7% |
| 有序区域 (pLDDT>70) 占比 | 73.8% |
| 可用 PDB 条目 | 3DKP |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=76.6，有序区 73.8%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044764, IPR011545, IPR050079, IPR014001, IPR001650; Pfam: PF00270, PF00271 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP3 | 0.997 | 0.954 | — |
| PDCD11 | 0.995 | 0.562 | — |
| KRR1 | 0.992 | 0.397 | — |
| NOL6 | 0.992 | 0.954 | — |
| NOP14 | 0.978 | 0.000 | — |
| AATF | 0.972 | 0.497 | — |
| WDR46 | 0.971 | 0.000 | — |
| DDX47 | 0.954 | 0.053 | — |
| UTP20 | 0.954 | 0.000 | — |
| DDX49 | 0.948 | 0.053 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.6 + PDB: 3DKP | pLDDT=76.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DDX52 -- Probable ATP-dependent RNA helicase DDX52，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小599 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2R4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000278053-DDX52/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX52
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2R4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
