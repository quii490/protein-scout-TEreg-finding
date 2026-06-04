---
type: protein-evaluation
gene: "MACROD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MACROD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MACROD2 / C20orf133 |
| 蛋白名称 | ADP-ribose glycohydrolase MACROD2 |
| 蛋白大小 | 425 aa / 47.4 kDa |
| UniProt ID | A1Z1Q3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 425 aa / 47.4 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=83 篇 (≤100→2) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.6; PDB: 4IQY, 6Y4Y, 6Y4Z, 6Y73 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002589, IPR043472; Pfam: PF01661 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 83 |
| PubMed broad count | 136 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf133 |

**关键文献**:
1. Are PARPs promiscuous?. *Bioscience reports*. PMID: 35380161
2. ENPP1 processes protein ADP-ribosylation in vitro.. *The FEBS journal*. PMID: 27406238
3. Activity-Based Screening Assay for Mono-ADP-Ribosylhydrolases.. *SLAS discovery : advancing life sciences R & D*. PMID: 32527186
4. Comparative analysis of MACROD1, MACROD2 and TARG1 expression, localisation and interactome.. *Scientific reports*. PMID: 32427867
5. Behavioural Characterisation of Macrod1 and Macrod2 Knockout Mice.. *Cells*. PMID: 33578760

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.6 |
| 高置信度残基 (pLDDT>90) 占比 | 49.2% |
| 置信残基 (pLDDT 70-90) 占比 | 1.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 40.7% |
| 有序区域 (pLDDT>70) 占比 | 50.8% |
| 可用 PDB 条目 | 4IQY, 6Y4Y, 6Y4Z, 6Y73 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4IQY, 6Y4Y, 6Y4Z, 6Y73）+ AlphaFold高质量预测（pLDDT=71.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002589, IPR043472; Pfam: PF01661 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FLRT3 | 0.959 | 0.000 | — |
| OARD1 | 0.811 | 0.000 | — |
| ADPRHL2 | 0.800 | 0.000 | — |
| PARG | 0.778 | 0.000 | — |
| PARP10 | 0.750 | 0.292 | — |
| MACROH2A2 | 0.676 | 0.000 | — |
| NUDT16 | 0.610 | 0.000 | — |
| FLRT1 | 0.592 | 0.000 | — |
| FHIT | 0.583 | 0.000 | — |
| FLRT2 | 0.551 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=71.6 + PDB: 4IQY, 6Y4Y, 6Y4Z, 6Y73 | pLDDT=71.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MACROD2 — ADP-ribose glycohydrolase MACROD2，研究基础较多，新颖性有限。
2. 蛋白大小425 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 83 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A1Z1Q3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172264-MACROD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MACROD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A1Z1Q3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
