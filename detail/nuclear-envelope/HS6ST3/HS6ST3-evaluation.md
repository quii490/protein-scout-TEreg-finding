---
type: protein-evaluation
gene: "HS6ST3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HS6ST3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HS6ST3 |
| 蛋白名称 | Heparan-sulfate 6-O-sulfotransferase 3 |
| 蛋白大小 | 471 aa / 54.8 kDa |
| UniProt ID | Q8IZP7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nuclear membrane; 额外: Plasma membrane, Actin fi; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 471 aa / 54.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010635, IPR027417, IPR005331; Pfam: PF03567 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Plasma membrane, Actin filaments | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Association of HS6ST3 gene polymorphisms with obesity and triglycerides: gene x gender interaction.. *Journal of genetics*. PMID: 24371161
2. Genome wide association study of clinical duration and age at onset of sporadic CJD.. *PloS one*. PMID: 39079175
3. Regulation of heparan sulfate 6-O-sulfation by beta-secretase activity.. *The Journal of biological chemistry*. PMID: 17363373
4. Silencing HS6ST3 inhibits growth and progression of breast cancer cells through suppressing IGF1R and inducing XAF1.. *Experimental cell research*. PMID: 28017727
5. Identification of a novel 43-bp insertion in the heparan sulfate 6-O-sulfotransferase 3 (HS6ST3) gene and its associations with growth and carcass traits in chickens.. *Animal biotechnology*. PMID: 30472903

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.4 |
| 高置信度残基 (pLDDT>90) 占比 | 61.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 21.2% |
| 有序区域 (pLDDT>70) 占比 | 70.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.4，有序区 70.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010635, IPR027417, IPR005331; Pfam: PF03567 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPC6 | 0.682 | 0.000 | — |
| HS2ST1 | 0.676 | 0.091 | — |
| GPC5 | 0.655 | 0.000 | — |
| GLCE | 0.651 | 0.125 | — |
| NDST4 | 0.635 | 0.000 | — |
| HS3ST6 | 0.634 | 0.000 | — |
| NDST2 | 0.626 | 0.000 | — |
| HS3ST5 | 0.623 | 0.000 | — |
| HS3ST1 | 0.619 | 0.000 | — |
| NDST3 | 0.582 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HS6ST1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IDE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DOCK3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EBI-25475894 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32838362|imex:IM-27901| |
| NOS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DEFB116 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.4 + PDB: 无 | pLDDT=80.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Nuclear membrane; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HS6ST3 — Heparan-sulfate 6-O-sulfotransferase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小471 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZP7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185352-HS6ST3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HS6ST3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZP7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000185352-HS6ST3/subcellular

![](https://images.proteinatlas.org/78257/1694_A11_13_cr57ceaee227b3d_red_green.jpg)
![](https://images.proteinatlas.org/78257/1694_A11_19_cr57ceaee8a40a5_red_green.jpg)
![](https://images.proteinatlas.org/78257/1704_B7_21_cr57d84c816c338_red_green.jpg)
![](https://images.proteinatlas.org/78257/1704_B7_7_cr57d84c79c1689_red_green.jpg)
![](https://images.proteinatlas.org/78257/1766_A1_3_red_green.jpg)
![](https://images.proteinatlas.org/78257/1766_A1_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZP7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
