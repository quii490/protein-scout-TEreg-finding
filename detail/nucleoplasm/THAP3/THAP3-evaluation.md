---
type: protein-evaluation
gene: "THAP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THAP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THAP3 |
| 蛋白名称 | THAP domain-containing protein 3 |
| 蛋白大小 | 239 aa / 27.1 kDa |
| UniProt ID | Q8WTV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 239 aa / 27.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026520, IPR006612; Pfam: PF05485 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CD45 inhibition in myeloid leukaemia cells sensitizes cellular responsiveness to chemotherapy.. *Annals of hematology*. PMID: 37917373
2. The THAP-zinc finger protein THAP1 associates with coactivator HCF-1 and O-GlcNAc transferase: a link between DYT6 and DYT3 dystonias.. *The Journal of biological chemistry*. PMID: 20200153
3. Network-based analysis of oligodendrogliomas predicts novel cancer gene candidates within the region of the 1p/19q co-deletion.. *Acta neuropathologica communications*. PMID: 29890994
4. THAP3 recruits SMYD3 to OXPHOS genes and epigenetically promotes mitochondrial respiration in hepatocellular carcinoma.. *FEBS letters*. PMID: 38664231
5. Two-stage Study of Familial Prostate Cancer by Whole-exome Sequencing and Custom Capture Identifies 10 Novel Genes Associated with the Risk of Prostate Cancer.. *European urology*. PMID: 32800727

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.3 |
| 高置信度残基 (pLDDT>90) 占比 | 35.1% |
| 置信残基 (pLDDT 70-90) 占比 | 18.0% |
| 中等置信 (pLDDT 50-70) 占比 | 17.6% |
| 低置信 (pLDDT<50) 占比 | 29.3% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.3，有序区 53.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026520, IPR006612; Pfam: PF05485 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| THAP11 | 0.889 | 0.129 | — |
| THAP12 | 0.882 | 0.000 | — |
| OGT | 0.660 | 0.399 | — |
| DNAJC11 | 0.628 | 0.000 | — |
| THAP6 | 0.624 | 0.000 | — |
| HCFC1 | 0.607 | 0.367 | — |
| THAP4 | 0.589 | 0.000 | — |
| THAP10 | 0.570 | 0.000 | — |
| RRM1 | 0.537 | 0.000 | — |
| THAP7 | 0.507 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NUTF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| UBL5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CASC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OGT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PABPC4L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YBX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZNF16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RPL17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| H1-6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RPS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.3 + PDB: 无 | pLDDT=70.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli, Mitochondria | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. THAP3 — THAP domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小239 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WTV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000041988-THAP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THAP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WTV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000041988-THAP3/subcellular

![](https://images.proteinatlas.org/67114/1263_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/67114/1263_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/67114/1270_A9_5_red_green.jpg)
![](https://images.proteinatlas.org/67114/1270_A9_6_red_green.jpg)
![](https://images.proteinatlas.org/67114/1284_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/67114/1284_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WTV1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
