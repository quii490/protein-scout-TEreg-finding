---
type: protein-evaluation
gene: "ANKS4B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKS4B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKS4B / HARP |
| 蛋白名称 | Ankyrin repeat and SAM domain-containing protein 4B |
| 蛋白大小 | 417 aa / 46.6 kDa |
| UniProt ID | Q8N8V4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cell projection, microvillus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 417 aa / 46.6 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.4; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037601, IPR002110, IPR036770, IPR001660, IPR013 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cell projection, microvillus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- brush border (GO:0005903)
- endoplasmic reticulum membrane (GO:0005789)
- microvillus (GO:0005902)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HARP |

**关键文献**:
1. Nuclear-Cytoplasmic Shuttling of the Usher Syndrome 1G Protein SANS Differs from Its Paralog ANKS4B.. *Cells*. PMID: 39594604
2. Anks4b, a novel target of HNF4α protein, interacts with GRP78 protein and regulates endoplasmic reticulum stress-induced apoptosis in pancreatic β-cells.. *The Journal of biological chemistry*. PMID: 22589549
3. ANKS4B Restricts Replication of Zika Virus by Downregulating the Autophagy.. *Frontiers in microbiology*. PMID: 32793175
4. A comprehensive understanding of ovarian carcinoma survival prognosis by novel biomarkers.. *European review for medical and pharmacological sciences*. PMID: 31646556
5. Roles of HNF1α and HNF4α in pancreatic β-cells: lessons from a monogenic form of diabetes (MODY).. *Vitamins and hormones*. PMID: 24559927

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.4 |
| 高置信度残基 (pLDDT>90) 占比 | 41.5% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 36.5% |
| 有序区域 (pLDDT>70) 占比 | 56.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.4，有序区 56.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037601, IPR002110, IPR036770, IPR001660, IPR013761; Pfam: PF12796, PF00536 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| USH1C | 0.995 | 0.955 | — |
| MYO7B | 0.980 | 0.797 | — |
| CDHR5 | 0.826 | 0.046 | — |
| CDHR2 | 0.815 | 0.046 | — |
| MYO7A | 0.686 | 0.487 | — |
| PLA2G12B | 0.606 | 0.000 | — |
| MYO10 | 0.567 | 0.414 | — |
| MYO15A | 0.553 | 0.414 | — |
| ABHD15 | 0.537 | 0.064 | — |
| MYO15B | 0.532 | 0.414 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| PLEC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MFHAS1 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| USH1C | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LRRK2 | psi-mi:"MI:0089"(protein array) | pubmed:24947832|imex:IM-22653 |
| MPP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BANP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.4 + PDB: 无 | pLDDT=70.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, microvillus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. ANKS4B — Ankyrin repeat and SAM domain-containing protein 4B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小417 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N8V4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175311-ANKS4B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKS4B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8V4
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:52:42

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000175311-ANKS4B/subcellular

![](https://images.proteinatlas.org/43523/1404_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/43523/1404_E9_3_red_green.jpg)
![](https://images.proteinatlas.org/43523/516_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/43523/516_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/43523/519_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/43523/519_D7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N8V4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
