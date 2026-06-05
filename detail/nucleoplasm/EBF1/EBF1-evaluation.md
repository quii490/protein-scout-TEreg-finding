---
type: protein-evaluation
gene: "EBF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EBF1 — REJECTED (研究热度过高 (PubMed strict=403，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EBF1 / COE1, EBF |
| 蛋白名称 | Transcription factor COE1 |
| 蛋白大小 | 591 aa / 64.5 kDa |
| UniProt ID | Q9UH73 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 591 aa / 64.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=403 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=70.8; PDB: 3LYR, 3MQI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032200, IPR038173, IPR032201, IPR038006, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 403 |
| PubMed broad count | 744 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COE1, EBF |

**关键文献**:
1. Single-cell dynamics of liver development in postnatal pigs.. *Science bulletin*. PMID: 37783617
2. Hedgehog signaling reprograms hair follicle niche fibroblasts to a hyper-activated state.. *Developmental cell*. PMID: 35777353
3. Transcriptional function of E2A, Ebf1, Pax5, Ikaros and Aiolos analyzed by in vivo acute protein degradation in early B cell development.. *Nature immunology*. PMID: 39179932
4. IKZF1(plus) Defines a New Minimal Residual Disease-Dependent Very-Poor Prognostic Profile in Pediatric B-Cell Precursor Acute Lymphoblastic Leukemia.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 29498923
5. Retraction.. *Journal of cellular biochemistry*. PMID: 34288063

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 45.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 36.7% |
| 有序区域 (pLDDT>70) 占比 | 58.5% |
| 可用 PDB 条目 | 3LYR, 3MQI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3LYR, 3MQI）+ AlphaFold高质量预测（pLDDT=70.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032200, IPR038173, IPR032201, IPR038006, IPR013783; Pfam: PF16422, PF16423, PF01833 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAX5 | 0.985 | 0.000 | — |
| ZNF423 | 0.978 | 0.314 | — |
| TET2 | 0.976 | 0.292 | — |
| TCF3 | 0.948 | 0.000 | — |
| LHX2 | 0.938 | 0.000 | — |
| IKZF1 | 0.931 | 0.071 | — |
| IKZF3 | 0.885 | 0.071 | — |
| CEBPA | 0.876 | 0.000 | — |
| TMTC1 | 0.852 | 0.000 | — |
| CEBPB | 0.852 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKP1A | psi-mi:"MI:0018"(two hybrid) | pubmed:14749489 |
| SKP1B | psi-mi:"MI:0018"(two hybrid) | pubmed:14749489 |
| ASK11 | psi-mi:"MI:0018"(two hybrid) | pubmed:14749489 |
| ASK12 | psi-mi:"MI:0018"(two hybrid) | pubmed:14749489 |
| ASK13 | psi-mi:"MI:0018"(two hybrid) | pubmed:12169662 |
| ASK18 | psi-mi:"MI:0018"(two hybrid) | pubmed:12169662 |
| EIN3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14675533 |
| EIL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14675533 |
| SRK2A | psi-mi:"MI:0096"(pull down) | pubmed:14675533 |
| CUL1 | psi-mi:"MI:0096"(pull down) | pubmed:14675533 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 3LYR, 3MQI | pLDDT=70.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EBF1 — Transcription factor COE1，研究基础较多，新颖性有限。
2. 蛋白大小591 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 403 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 403 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UH73
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164330-EBF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EBF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UH73
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000164330-EBF1/subcellular

![](https://images.proteinatlas.org/61169/1397_B3_4_red_green.jpg)
![](https://images.proteinatlas.org/61169/1397_B3_5_red_green.jpg)
![](https://images.proteinatlas.org/61169/1402_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/61169/1402_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/61169/1482_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/61169/1482_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UH73-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
