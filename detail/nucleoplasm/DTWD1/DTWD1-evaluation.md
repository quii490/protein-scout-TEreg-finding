---
type: protein-evaluation
gene: "DTWD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DTWD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTWD1 |
| 蛋白名称 | tRNA-uridine aminocarboxypropyltransferase 1 |
| 蛋白大小 | 304 aa / 35.2 kDa |
| UniProt ID | Q8N5C7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 304 aa / 35.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005636, IPR051521; Pfam: PF03942 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.0/180** | |
| **归一化总分** | | | **79.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome, Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Biogenesis and functions of aminocarboxypropyluridine in tRNA.. *Nature communications*. PMID: 31804502
2. tRNA-Uridine Aminocarboxypropyltransferase DTW Domain Containing 2 Suppresses Colon Adenocarcinoma Progression.. *International journal of genomics*. PMID: 37745798
3. Hypoxia-induced HIF1α targets in melanocytes reveal a molecular profile associated with poor melanoma prognosis.. *Pigment cell & melanoma research*. PMID: 28168807
4. Corticosterone-mediated regulation and functions of miR-218-5p in rat brain.. *Scientific reports*. PMID: 34996981
5. Efficient region-based test strategy uncovers genetic risk factors for functional outcome in bipolar disorder.. *European neuropsychopharmacology : the journal of the European College of Neuropsychopharmacology*. PMID: 30503783

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.4 |
| 高置信度残基 (pLDDT>90) 占比 | 62.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 20.7% |
| 有序区域 (pLDDT>70) 占比 | 75.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.4，有序区 75.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005636, IPR051521; Pfam: PF03942 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DTWD2 | 0.759 | 0.000 | — |
| TSR3 | 0.709 | 0.000 | — |
| FGF7 | 0.651 | 0.000 | — |
| ZNF98 | 0.567 | 0.000 | — |
| DUS4L | 0.543 | 0.000 | — |
| CCDC85C | 0.529 | 0.000 | — |
| DUS2 | 0.512 | 0.000 | — |
| MPHOSPH10 | 0.489 | 0.000 | — |
| ZNF653 | 0.480 | 0.000 | — |
| ZBTB39 | 0.475 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=80.4 + PDB: 无 | pLDDT=80.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome, | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DTWD1 — tRNA-uridine aminocarboxypropyltransferase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小304 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N5C7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104047-DTWD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTWD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N5C7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
