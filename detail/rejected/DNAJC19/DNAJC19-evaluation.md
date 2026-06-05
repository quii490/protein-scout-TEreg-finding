---
type: protein-evaluation
gene: "DNAJC19"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC19 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC19 / TIM14, TIMM14 |
| 蛋白名称 | Mitochondrial import inner membrane translocase subunit TIM14 |
| 蛋白大小 | 116 aa / 12.5 kDa |
| UniProt ID | Q96DA6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion inner membrane |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 116 aa / 12.5 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.5; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001623, IPR036869; Pfam: PF00226 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- inner mitochondrial membrane protein complex (GO:0098800)
- matrix side of mitochondrial inner membrane (GO:0099617)
- membrane (GO:0016020)
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)
- PAM complex, Tim23 associated import motor (GO:0001405)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TIM14, TIMM14 |

**关键文献**:
1. Mutations in DNAJC19 cause altered mitochondrial structure and increased mitochondrial respiration in human iPSC-derived cardiomyocytes.. *Molecular metabolism*. PMID: 38142971
2. Mitochondrial Protein Homeostasis and Cardiomyopathy.. *International journal of molecular sciences*. PMID: 35328774
3. Generation of a homozygous DNAJC19 knockout human embryonic stem cell line by CRISPR/Cas9 system.. *Stem cell research*. PMID: 38696852
4. Targeting DNAJC19 overcomes tumor growth and lung metastasis in NSCLC by regulating PI3K/AKT signaling.. *Cancer cell international*. PMID: 34217321
5. Role of Magmas in protein transport and human mitochondria biogenesis.. *Human molecular genetics*. PMID: 20053669

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.5 |
| 高置信度残基 (pLDDT>90) 占比 | 56.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 87.9% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.5，有序区 87.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR036869; Pfam: PF00226 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAM16 | 0.999 | 0.899 | — |
| TIMM44 | 0.999 | 0.409 | — |
| HSPA9 | 0.998 | 0.732 | — |
| TIMM17A | 0.989 | 0.488 | — |
| TIMM50 | 0.973 | 0.162 | — |
| TIMM21 | 0.964 | 0.167 | — |
| TIMM17B | 0.921 | 0.307 | — |
| AUH | 0.910 | 0.000 | — |
| TIMM23 | 0.909 | 0.407 | — |
| HSPA4 | 0.900 | 0.149 | — |

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
| 三维结构 | AlphaFold pLDDT=87.5 + PDB: 无 | pLDDT=87.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAJC19 — Mitochondrial import inner membrane translocase subunit TIM14，非常新颖，仅有少数基础研究。
2. 蛋白大小116 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DA6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205981-DNAJC19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DA6
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:05

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96DA6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
