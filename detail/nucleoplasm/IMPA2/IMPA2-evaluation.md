---
type: protein-evaluation
gene: "IMPA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IMPA2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IMPA2 / IMP.18P |
| 蛋白名称 | Inositol monophosphatase 2 |
| 蛋白大小 | 288 aa / 31.3 kDa |
| UniProt ID | O14732 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Mitochondria; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 288 aa / 31.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.7; PDB: 2CZH, 2CZI, 2CZK, 2DDK, 2FVZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR033942, IPR020583, IPR020552, IPR000760, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitochondria | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IMP.18P |

**关键文献**:
1. IMPA2 blocks cervical cancer cell apoptosis and induces paclitaxel resistance through p53-mediated AIFM2 regulation.. *Acta biochimica et biophysica Sinica*. PMID: 37140233
2. Altered IMPA2 gene expression and calcium homeostasis in bipolar disorder.. *Molecular psychiatry*. PMID: 11673796
3. A novel function of IMPA2, plays a tumor-promoting role in cervical cancer.. *Cell death & disease*. PMID: 32409648
4. Identification of IMPA2 as the hub gene associated with colorectal cancer and liver metastasis by integrated bioinformatics analysis.. *Translational oncology*. PMID: 35483170
5. Association analysis between polymorphisms in the myo-inositol monophosphatase 2 (IMPA2) gene and bipolar disorder.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 20800640

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.7 |
| 高置信度残基 (pLDDT>90) 占比 | 91.0% |
| 置信残基 (pLDDT 70-90) 占比 | 4.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 2.1% |
| 有序区域 (pLDDT>70) 占比 | 95.9% |
| 可用 PDB 条目 | 2CZH, 2CZI, 2CZK, 2DDK, 2FVZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2CZH, 2CZI, 2CZK, 2DDK, 2FVZ）+ AlphaFold极高置信度预测（pLDDT=94.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033942, IPR020583, IPR020552, IPR000760, IPR020550; Pfam: PF00459 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ISYNA1 | 0.992 | 0.000 | — |
| IMPA1 | 0.987 | 0.796 | — |
| INPP1 | 0.972 | 0.000 | — |
| IMPAD1 | 0.958 | 0.000 | — |
| CDIPT | 0.948 | 0.000 | — |
| MIOX | 0.931 | 0.000 | — |
| INPP4A | 0.914 | 0.000 | — |
| INPP4B | 0.910 | 0.000 | — |
| MTM1 | 0.908 | 0.000 | — |
| TTF2 | 0.878 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000269159.3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| HERPUD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CDKA-1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CDKD-2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CKS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CYCA2-3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CYCD5-1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| E2FA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| KRP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| KRP4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.7 + PDB: 2CZH, 2CZI, 2CZK, 2DDK, 2FVZ | pLDDT=94.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. IMPA2 — Inositol monophosphatase 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小288 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14732
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141401-IMPA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IMPA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14732
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000141401-IMPA2/subcellular

![](https://images.proteinatlas.org/29561/322_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/29561/322_E8_3_red_green.jpg)
![](https://images.proteinatlas.org/29561/934_B1_4_red_green.jpg)
![](https://images.proteinatlas.org/29561/934_B1_7_red_green.jpg)
![](https://images.proteinatlas.org/29561/990_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/29561/990_F1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14732-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
