---
type: protein-evaluation
gene: "GGT5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GGT5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GGT5 / GGTLA1 |
| 蛋白名称 | Glutathione hydrolase 5 proenzyme |
| 蛋白大小 | 586 aa / 62.3 kDa |
| UniProt ID | P36269 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 586 aa / 62.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR055262, IPR043138, IPR000101, IPR043137, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 76 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GGTLA1 |

**关键文献**:
1. GGT5 facilitates migration and invasion through the induction of epithelial-mesenchymal transformation in gastric cancer.. *BMC medical genomics*. PMID: 38581025
2. Generation of novel lipid metabolism-based signatures to predict prognosis and immunotherapy response for colorectal adenocarcinoma.. *Scientific reports*. PMID: 39060344
3. Multiomics insights into retinoic acid-mediated regulation of eosinophils in severe asthma.. *The Journal of allergy and clinical immunology*. PMID: 41207640
4. GGT5 Is an Independent Prognostic Biomarker in Stomach Adenocarcinoma.. *Canadian journal of gastroenterology & hepatology*. PMID: 35257007
5. GGT5 as a promising prognostic biomarker and its effects on tumor cell progression in gastric cancer.. *Translational cancer research*. PMID: 39262487

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 81.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 3.1% |
| 有序区域 (pLDDT>70) 占比 | 93.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.1，有序区 93.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055262, IPR043138, IPR000101, IPR043137, IPR029055; Pfam: PF01019 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB5 | 0.967 | 0.000 | — |
| GGT6 | 0.961 | 0.000 | — |
| GSS | 0.955 | 0.000 | — |
| OPLAH | 0.948 | 0.000 | — |
| ANPEP | 0.946 | 0.000 | — |
| GGT7 | 0.940 | 0.000 | — |
| GGCT | 0.938 | 0.000 | — |
| LAP3 | 0.932 | 0.000 | — |
| LTC4S | 0.930 | 0.000 | — |
| GGT1 | 0.923 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| POTEI | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC1A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MVK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC20A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 无 | pLDDT=92.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. GGT5 — Glutathione hydrolase 5 proenzyme，非常新颖，仅有少数基础研究。
2. 蛋白大小586 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P36269
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099998-GGT5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GGT5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P36269
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000099998-GGT5/subcellular

![](https://images.proteinatlas.org/8121/1293_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8121/1293_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8121/1656_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8121/1656_F7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/8121/1774_G4_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/8121/1774_G4_39_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P36269-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
