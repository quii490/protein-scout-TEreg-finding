---
type: protein-evaluation
gene: "DUSP12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP12 |
| 蛋白名称 | Dual specificity protein phosphatase 12 |
| 蛋白大小 | 340 aa / 37.7 kDa |
| UniProt ID | Q9UNI6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 340 aa / 37.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.2; PDB: 4JNB, 4KI9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000340, IPR016278, IPR029021, IPR000387, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. RAB3B Dictates mTORC1/S6 Signaling in Chordoma and Predicts Response to mTORC1-Targeted Therapy.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40135815
2. MAP4K Family Kinases and DUSP Family Phosphatases in T-Cell Signaling and Systemic Lupus Erythematosus.. *Cells*. PMID: 31766293
3. DUSP12 regulates the tumorigenesis and prognosis of hepatocellular carcinoma.. *PeerJ*. PMID: 34414037
4. Dual-Specificity Phosphatase 12 Targets p38 MAP Kinase to Regulate Macrophage Response to Intracellular Bacterial Infection.. *Frontiers in immunology*. PMID: 29062315
5. Dual-specificity phosphatase 12 attenuates oxidative stress injury and apoptosis in diabetic cardiomyopathy via the ASK1-JNK/p38 signaling pathway.. *Free radical biology & medicine*. PMID: 36108935

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.2 |
| 高置信度残基 (pLDDT>90) 占比 | 67.6% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 10.3% |
| 有序区域 (pLDDT>70) 占比 | 81.7% |
| 可用 PDB 条目 | 4JNB, 4KI9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4JNB, 4KI9）+ AlphaFold高质量预测（pLDDT=85.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR016278, IPR029021, IPR000387, IPR020422; Pfam: PF00782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK1 | 0.812 | 0.308 | — |
| FOS | 0.791 | 0.104 | — |
| MAPK14 | 0.783 | 0.243 | — |
| MRTO4 | 0.779 | 0.113 | — |
| JUN | 0.763 | 0.093 | — |
| MAPK8 | 0.760 | 0.130 | — |
| ATF3 | 0.751 | 0.094 | — |
| FOSB | 0.728 | 0.094 | — |
| MAPK3 | 0.715 | 0.243 | — |
| HSD17B12 | 0.706 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=85.2 + PDB: 4JNB, 4KI9 | pLDDT=85.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol / Nucleoplasm | 一致 |
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
1. DUSP12 — Dual specificity protein phosphatase 12，非常新颖，仅有少数基础研究。
2. 蛋白大小340 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UNI6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000081721-DUSP12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UNI6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
