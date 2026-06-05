---
type: protein-evaluation
gene: "Ahcy"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Ahcy — REJECTED (研究热度过高 (PubMed strict=169，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Ahcy / SAHH |
| 蛋白名称 | Adenosylhomocysteinase |
| 蛋白大小 | 432 aa / 47.7 kDa |
| UniProt ID | P23526 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Melanosome; Nucleus; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 432 aa / 47.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=169 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=98.2; PDB: 1A7A, 1LI4, 3NJ4, 4PFJ, 4PGF, 4YVF, 5W49 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR042172, IPR000043, IPR015878, IPR036291, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Melanosome; Nucleus; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- extracellular exosome (GO:0070062)
- melanosome (GO:0042470)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 169 |
| PubMed broad count | 215 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SAHH |

**关键文献**:
1. Ketogenesis impact on liver metabolism revealed by proteomics of lysine β-hydroxybutyrylation.. *Cell reports*. PMID: 34348140
2. Homocysitaconate controls inflammation through reshaping methionine metabolism and N-homocysteinylation.. *Cell metabolism*. PMID: 40876449
3. Towards frailty biomarkers: Candidates from genes and pathways regulated in aging and age-related diseases.. *Ageing research reviews*. PMID: 30071357
4. Functional and Pathological Roles of AHCY.. *Frontiers in cell and developmental biology*. PMID: 33869213
5. The role of S-adenosylhomocysteine hydrolase-like 1 in cancer.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 39154900

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 98.2 |
| 高置信度残基 (pLDDT>90) 占比 | 99.3% |
| 置信残基 (pLDDT 70-90) 占比 | 0.2% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.5% |
| 可用 PDB 条目 | 1A7A, 1LI4, 3NJ4, 4PFJ, 4PGF, 4YVF, 5W49, 5W4B |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1A7A, 1LI4, 3NJ4, 4PFJ, 4PGF, 4YVF, 5W49, 5W4B）+ AlphaFold极高置信度预测（pLDDT=98.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042172, IPR000043, IPR015878, IPR036291, IPR020082; Pfam: PF05221, PF00670 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTR | 0.992 | 0.000 | — |
| BHMT | 0.988 | 0.000 | — |
| CBS | 0.987 | 0.071 | — |
| CTH | 0.983 | 0.069 | — |
| BHMT2 | 0.979 | 0.000 | — |
| AHCYL1 | 0.968 | 0.457 | — |
| DNMT1 | 0.952 | 0.000 | — |
| DNMT3B | 0.950 | 0.000 | — |
| DNMT3A | 0.937 | 0.000 | — |
| KYAT1 | 0.925 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000217426.2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Arf6 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| AhcyL2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| BCAR3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PINX1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PAK2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=98.2 + PDB: 1A7A, 1LI4, 3NJ4, 4PFJ, 4PGF,  | pLDDT=98.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Melanosome; Nucleus; Endoplasmic reticu / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. Ahcy — Adenosylhomocysteinase，研究基础较多，新颖性有限。
2. 蛋白大小432 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 169 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 169 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23526
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101444-AHCY/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Ahcy
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23526
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000101444-AHCY/subcellular

![](https://images.proteinatlas.org/44675/2265_D9_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/44675/2265_D9_87_blue_red_green.jpg)
![](https://images.proteinatlas.org/44675/753_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44675/753_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44675/823_B4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44675/823_B4_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23526-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
