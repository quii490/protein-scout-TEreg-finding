---
type: protein-evaluation
gene: "GPR65"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPR65 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR65 / TDAG8 |
| 蛋白名称 | G-protein coupled receptor 65 |
| 蛋白大小 | 337 aa / 39.3 kDa |
| UniProt ID | Q8IYL9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoli, Cytosol; UniProt: Cell membrane; Early endosome membrane; Late endosome membra |
| 蛋白大小 | 10/10 | ×1 | 10 | 337 aa / 39.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.6; PDB: 9BHL, 9JFT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000276, IPR017452, IPR005464; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoli, Cytosol | Approved |
| UniProt | Cell membrane; Early endosome membrane; Late endosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- early endosome membrane (GO:0031901)
- late endosome membrane (GO:0031902)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.6 |
| 高置信度残基 (pLDDT>90) 占比 | 46.6% |
| 置信残基 (pLDDT 70-90) 占比 | 30.3% |
| 中等置信 (pLDDT 50-70) 占比 | 19.0% |
| 低置信 (pLDDT<50) 占比 | 4.2% |
| 有序区域 (pLDDT>70) 占比 | 76.9% |
| 可用 PDB 条目 | 9BHL, 9JFT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（9BHL, 9JFT）+ AlphaFold高质量预测（pLDDT=82.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR005464; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD48 | 0.686 | 0.000 | — |
| ASIC3 | 0.608 | 0.000 | — |
| GPR132 | 0.603 | 0.000 | — |
| GPR39 | 0.573 | 0.000 | — |
| BTK | 0.566 | 0.000 | — |
| PLCB2 | 0.549 | 0.000 | — |
| SAMSN1 | 0.546 | 0.000 | — |
| GRK5 | 0.537 | 0.097 | — |
| TAGAP | 0.535 | 0.000 | — |
| PTAFR | 0.535 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000267549.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CYGB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.6 + PDB: 9BHL, 9JFT | pLDDT=82.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Early endosome membrane; Late endos / Vesicles; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GPR65 — G-protein coupled receptor 65，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小337 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYL9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140030-GPR65/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR65
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYL9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000140030-GPR65/subcellular

![](https://images.proteinatlas.org/77397/1806_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77397/1806_G7_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/77397/1846_A6_61_blue_red_green.jpg)
![](https://images.proteinatlas.org/77397/1846_A6_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/77397/1870_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77397/1870_E1_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IYL9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
