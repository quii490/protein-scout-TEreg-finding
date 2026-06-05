---
type: protein-evaluation
gene: "CRIP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRIP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRIP2 / CRP2 |
| 蛋白名称 | Cysteine-rich protein 2 |
| 蛋白大小 | 208 aa / 22.5 kDa |
| UniProt ID | P52943 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm, Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 208 aa / 22.5 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=72.9; PDB: 2CU8 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 6 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell cortex (GO:0005938)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 69 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRP2 |

**关键文献**:
1. EAT-Lancet Diet Modifies the Risk of Rheumatoid Arthritis Through Metabolomic Signature.. *Arthritis & rheumatology (Hoboken, N.J.)*. PMID: 40546003
2. Screening and verification of potential gene targets in esophageal carcinoma by bioinformatics analysis and immunohistochemistry.. *Annals of translational medicine*. PMID: 35282073
3. Effect of miR-6767-5p on breast cancer cell phenotype and its regulatory mechanism.. *Scientific reports*. PMID: 40858742
4. Prognosis biomarker and potential therapeutic target CRIP2 associated with radiosensitivity in NSCLC cells.. *Biochemical and biophysical research communications*. PMID: 34773852
5. Omics integration identified CRIP2 as a key mediator of olaparib resistance in prostate cancer.. *Translational andrology and urology*. PMID: 41132344

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.9 |
| 高置信度残基 (pLDDT>90) 占比 | 4.8% |
| 置信残基 (pLDDT 70-90) 占比 | 55.8% |
| 中等置信 (pLDDT 50-70) 占比 | 27.9% |
| 低置信 (pLDDT<50) 占比 | 11.5% |
| 有序区域 (pLDDT>70) 占比 | 60.6% |
| 可用 PDB 条目 | 2CU8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=72.9，有序区 60.6%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRF | 0.664 | 0.000 | — |
| CXorf56 | 0.450 | 0.000 | — |
| AGO2 | 0.442 | 0.000 | — |
| SLC25A6 | 0.434 | 0.000 | — |
| CLBA1 | 0.430 | 0.000 | — |
| CNR1 | 0.429 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 6，IntAct interactions: 0
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.9 + PDB: 2CU8 | pLDDT=72.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 6 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CRIP2 -- Cysteine-rich protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小208 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52943
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182809-CRIP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52943
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000182809-CRIP2/subcellular

![](https://images.proteinatlas.org/42664/504_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/42664/504_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/42664/506_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/42664/506_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/42664/555_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/42664/555_A7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P52943-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
