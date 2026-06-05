---
type: protein-evaluation
gene: "MAFA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MAFA — REJECTED (研究热度过高 (PubMed strict=537，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAFA |
| 蛋白名称 | Transcription factor MafA |
| 蛋白大小 | 353 aa / 37.0 kDa |
| UniProt ID | Q8NHW3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 353 aa / 37.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=537 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.5; PDB: 4EOT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR004826, IPR046347, IPR013592, IPR008 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 537 |
| PubMed broad count | 998 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-cell transcriptomic analysis deciphers heterogenous cancer stem-like cells in colorectal cancer and their organ-specific metastasis.. *Gut*. PMID: 38050068
2. Molecular Pathogenesis of Multiple Myeloma: Clinical Implications.. *Hematology/oncology clinics of North America*. PMID: 38199896
3. Regulation of insulin synthesis and secretion and pancreatic Beta-cell dysfunction in diabetes.. *Current diabetes reviews*. PMID: 22974359
4. Insulinomatosis: new aspects.. *Endocrine-related cancer*. PMID: 36952647
5. Dapagliflozin mitigates cellular stress and inflammation through PI3K/AKT pathway modulation in cardiomyocytes, aortic endothelial cells, and stem cell-derived β cells.. *Cardiovascular diabetology*. PMID: 39472869

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.5 |
| 高置信度残基 (pLDDT>90) 占比 | 25.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 24.6% |
| 低置信 (pLDDT<50) 占比 | 45.0% |
| 有序区域 (pLDDT>70) 占比 | 30.3% |
| 可用 PDB 条目 | 4EOT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.5），有序残基占 30.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR004826, IPR046347, IPR013592, IPR008917; Pfam: PF03131, PF08383 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.5 + PDB: 4EOT | pLDDT=61.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MAFA — Transcription factor MafA，研究基础较多，新颖性有限。
2. 蛋白大小353 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 537 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 537 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHW3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182759-MAFA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAFA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHW3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NHW3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
