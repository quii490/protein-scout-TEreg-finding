---
type: protein-evaluation
gene: "DDX56"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX56 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX56 / DDX21, NOH61 |
| 蛋白名称 | Probable ATP-dependent RNA helicase DDX56 |
| 蛋白大小 | 547 aa / 61.6 kDa |
| UniProt ID | Q9NY93 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoli; 额外: Mitotic chromosome; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | x1 | 10 | 547 aa / 61.6 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.8; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR011545, IPR050079, IPR014001, IPR001650, IPR027 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Mitotic chromosome | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDX21, NOH61 |

**关键文献**:
1. Integrated Analysis of DEAD-Box Helicase 56: A Potential Oncogene in Osteosarcoma.. *Frontiers in bioengineering and biotechnology*. PMID: 32671031
2. Oncogenic splicing abnormalities induced by DEAD-Box Helicase 56 amplification in colorectal cancer.. *Cancer science*. PMID: 31390121
3. DExH/D-box helicases at the frontline of intrinsic and innate immunity against viral infections.. *The Journal of general virology*. PMID: 36006669
4. Human DDX56 protein interacts with influenza A virus NS1 protein and stimulates the virus replication.. *Genetics and molecular biology*. PMID: 33749700
5. DDX56 promotes EMT and cancer stemness via MELK-FOXM1 axis in hepatocellular carcinoma.. *iScience*. PMID: 38827395

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 36.4% |
| 置信残基 (pLDDT 70-90) 占比 | 43.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 79.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.8，有序区 79.4%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR050079, IPR014001, IPR001650, IPR027417; Pfam: PF00270, PF00271 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHX36 | 0.996 | 0.122 | — |
| DDX1 | 0.990 | 0.000 | — |
| RPF2 | 0.987 | 0.754 | — |
| CEBPZ | 0.979 | 0.698 | — |
| GTPBP4 | 0.978 | 0.707 | — |
| WDR74 | 0.975 | 0.278 | — |
| EBNA1BP2 | 0.971 | 0.594 | — |
| NOC2L | 0.971 | 0.583 | — |
| PES1 | 0.970 | 0.269 | — |
| WDR46 | 0.968 | 0.188 | — |

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
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 无 | pLDDT=79.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli; 额外: Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DDX56 -- Probable ATP-dependent RNA helicase DDX56，非常新颖，仅有少数基础研究。
2. 蛋白大小547 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NY93
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136271-DDX56/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX56
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NY93
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
