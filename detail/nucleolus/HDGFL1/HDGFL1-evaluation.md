---
type: protein-evaluation
gene: "HDGFL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HDGFL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HDGFL1 / PWWP1 |
| 蛋白名称 | Hepatoma-derived growth factor-like protein 1 |
| 蛋白大小 | 251 aa / 27.2 kDa |
| UniProt ID | Q5TGJ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm, Nucleoli fibrillar center; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 251 aa / 27.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000313; Pfam: PF00855 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PWWP1 |

**关键文献**:
1. Genome-wide cross-trait analyses reveal shared genetic architecture and causal links between attention-deficit/hyperactivity disorder and cardiovascular diseases.. *Journal of affective disorders*. PMID: 41232685
2. Genome-wide association study of parity in Bangladeshi women.. *PloS one*. PMID: 25742292
3. Stem-Like Signature Predicting Disease Progression in Early Stage Bladder Cancer. The Role of E2F3 and SOX4.. *Biomedicines*. PMID: 30072631
4. [Prediction of immune-related genes associated with prognosis in patients with hepatocellular carcinoma by bioinformatics methods].. *Xi bao yu fen zi mian yi xue za zhi = Chinese journal of cellular and molecular immunology*. PMID: 36082705

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 27.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.0% |
| 中等置信 (pLDDT 50-70) 占比 | 31.5% |
| 低置信 (pLDDT<50) 占比 | 34.7% |
| 有序区域 (pLDDT>70) 占比 | 33.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 33.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000313; Pfam: PF00855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCL | 0.748 | 0.045 | — |
| NSD3 | 0.595 | 0.141 | — |
| IGF2BP3 | 0.529 | 0.000 | — |
| CTBP1 | 0.516 | 0.000 | — |
| DDX5 | 0.494 | 0.045 | — |
| CDK13 | 0.485 | 0.408 | — |
| CDK12 | 0.485 | 0.408 | — |
| CTBP2 | 0.475 | 0.000 | — |
| AGER | 0.439 | 0.000 | — |
| CCNQ | 0.439 | 0.302 | — |

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
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 无 | pLDDT=64.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HDGFL1 — Hepatoma-derived growth factor-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小251 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TGJ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112273-HDGFL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HDGFL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TGJ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
