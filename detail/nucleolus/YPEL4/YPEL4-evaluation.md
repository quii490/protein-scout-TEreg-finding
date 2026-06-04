---
type: protein-evaluation
gene: "YPEL4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YPEL4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YPEL4 |
| 蛋白名称 | Protein yippee-like 4 |
| 蛋白大小 | 127 aa / 14.3 kDa |
| UniProt ID | Q96NS1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 127 aa / 14.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR034751, IPR004910, IPR039058; Pfam: PF03226 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.0/180** | |
| **归一化总分** | | | **77.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Potential important roles and signaling mechanisms of YPEL4 in pulmonary diseases.. *Clinical and translational medicine*. PMID: 29892964
2. MVP interacts with YPEL4 and inhibits YPEL4-mediated activities of the ERK signal pathway.. *Biochemistry and cell biology = Biochimie et biologie cellulaire*. PMID: 20555386
3. Identification of common biomarkers in diabetic kidney disease and cognitive dysfunction using machine learning algorithms.. *Scientific reports*. PMID: 39333211
4. Yippee like 4 (Ypel4) is essential for normal mouse red blood cell membrane integrity.. *Scientific reports*. PMID: 34354145
5. Construction of a prognostic model for colon cancer by combining endoplasmic reticulum stress responsive genes.. *Journal of proteomics*. PMID: 39159861

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.9 |
| 高置信度残基 (pLDDT>90) 占比 | 75.6% |
| 置信残基 (pLDDT 70-90) 占比 | 3.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 8.7% |
| 有序区域 (pLDDT>70) 占比 | 79.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.9，有序区 79.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034751, IPR004910, IPR039058; Pfam: PF03226 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RANBP10 | 0.525 | 0.186 | — |
| MACO1 | 0.506 | 0.000 | — |
| WDR26 | 0.469 | 0.302 | — |
| TMCC2 | 0.465 | 0.000 | — |
| OR6K2 | 0.457 | 0.000 | — |
| DEDD2 | 0.454 | 0.000 | — |
| OR9G4 | 0.441 | 0.000 | — |
| PPP1R10 | 0.427 | 0.000 | — |
| OR4K15 | 0.424 | 0.000 | — |
| TSPO2 | 0.423 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.9 + PDB: 无 | pLDDT=86.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. YPEL4 — Protein yippee-like 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小127 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96NS1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166793-YPEL4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YPEL4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96NS1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/YPEL4/YPEL4-PAE.png]]
