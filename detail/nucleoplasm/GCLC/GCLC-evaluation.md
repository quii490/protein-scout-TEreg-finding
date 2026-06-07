---
type: protein-evaluation
gene: "GCLC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GCLC — REJECTED (研究热度过高 (PubMed strict=1090，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GCLC / GLCL, GLCLC |
| 蛋白名称 | Glutamate--cysteine ligase catalytic subunit |
| 蛋白大小 | 637 aa / 72.8 kDa |
| UniProt ID | P48506 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 637 aa / 72.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1090 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004308, IPR014746; Pfam: PF03074 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- glutamate-cysteine ligase complex (GO:0017109)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1090 |
| PubMed broad count | 1787 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GLCL, GLCLC |

**关键文献**:
1. Adipocyte-derived glutathione promotes obesity-related breast cancer by regulating the SCARB2-ARF1-mTORC1 complex.. *Cell metabolism*. PMID: 39442522
2. Histone lactylation enhances GCLC expression and thus promotes chemoresistance of colorectal cancer stem cells through inhibiting ferroptosis.. *Cell death & disease*. PMID: 40113760
3. NFE2L2 and SLC25A39 drive cuproptosis resistance through GSH metabolism.. *Scientific reports*. PMID: 39609608
4. Lymph node environment drives FSP1 targetability in metastasizing melanoma.. *Nature*. PMID: 41193799
5. ACTL6A protects gastric cancer cells against ferroptosis through induction of glutathione synthesis.. *Nature communications*. PMID: 37443154

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.2 |
| 高置信度残基 (pLDDT>90) 占比 | 91.2% |
| 置信残基 (pLDDT 70-90) 占比 | 2.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 93.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.2，有序区 93.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004308, IPR014746; Pfam: PF03074 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GCLM | 0.999 | 0.871 | — |
| GSS | 0.995 | 0.113 | — |
| NFE2L2 | 0.966 | 0.000 | — |
| OPLAH | 0.959 | 0.000 | — |
| GGT1 | 0.944 | 0.000 | — |
| GGT6 | 0.942 | 0.000 | — |
| ANPEP | 0.930 | 0.000 | — |
| GGT7 | 0.925 | 0.000 | — |
| GGT5 | 0.923 | 0.000 | — |
| GGCT | 0.922 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCL22 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ENSP00000497574.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TYW3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GCLM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NMD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NetB | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| anon-WO0153538.36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| EBI-25475894 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| PRR16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.2 + PDB: 无 | pLDDT=93.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GCLC — Glutamate--cysteine ligase catalytic subunit，研究基础较多，新颖性有限。
2. 蛋白大小637 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1090 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1090 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P48506
- Protein Atlas: https://www.proteinatlas.org/ENSG00000001084-GCLC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GCLC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48506
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000001084-GCLC/subcellular

![](https://images.proteinatlas.org/36360/430_C2_5_red_green.jpg)
![](https://images.proteinatlas.org/36360/430_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/36360/432_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/36360/432_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/36360/441_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/36360/441_C2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P48506-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P48506 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004308;IPR014746; |
| Pfam | PF03074; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000001084-GCLC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GCLM | Intact, Biogrid, Bioplex | true |
| PRKN | Biogrid | false |
| TYW3 | Bioplex | false |
| ZRANB1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
