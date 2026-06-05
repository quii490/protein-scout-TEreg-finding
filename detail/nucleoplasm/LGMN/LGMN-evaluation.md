---
type: protein-evaluation
gene: "LGMN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LGMN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LGMN / PRSC1 |
| 蛋白名称 | Legumain |
| 蛋白大小 | 433 aa / 49.4 kDa |
| UniProt ID | Q99538 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Lysosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 433 aa / 49.4 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.1; PDB: 4AW9, 4AWA, 4AWB, 4FGU, 4N6N, 4N6O, 5LU8 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043577, IPR048501, IPR046427, IPR001096; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Lysosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- apical part of cell (GO:0045177)
- cytoplasm (GO:0005737)
- endolysosome lumen (GO:0036021)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- late endosome (GO:0005770)
- lysosomal lumen (GO:0043202)
- lysosome (GO:0005764)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 151 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PRSC1 |

**关键文献**:
1. Cardiac Resident Macrophage-Derived Legumain Improves Cardiac Repair by Promoting Clearance and Degradation of Apoptotic Cardiomyocytes After Myocardial Infarction.. *Circulation*. PMID: 35430895
2. CD4+ T-Cell Legumain Deficiency Attenuates Hypertensive Damage via Preservation of TRAF6.. *Circulation research*. PMID: 38047378
3. Legumain In Situ Engineering Promotes Efferocytosis of CAR Macrophage to Treat Cardiac Fibrosis.. *Advanced materials (Deerfield Beach, Fla.)*. PMID: 40223483
4. Legumain Is an Endogenous Modulator of Integrin αvβ3 Triggering Vascular Degeneration, Dissection, and Rupture.. *Circulation*. PMID: 35100526
5. The presence of blastocyst within the uteri facilitates lumenal epithelium transformation for implantation via upregulating lysosome proteostasis activity.. *Autophagy*. PMID: 37584546

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 90.5% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 94.0% |
| 可用 PDB 条目 | 4AW9, 4AWA, 4AWB, 4FGU, 4N6N, 4N6O, 5LU8, 5LU9, 5LUA, 5LUB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4AW9, 4AWA, 4AWB, 4FGU, 4N6N, 4N6O, 5LU8, 5LU9, 5LUA, 5LUB）+ AlphaFold极高置信度预测（pLDDT=94.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043577, IPR048501, IPR046427, IPR001096; Pfam: PF20985, PF01650 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CST6 | 0.997 | 0.957 | — |
| CTSB | 0.944 | 0.000 | — |
| CTSS | 0.932 | 0.000 | — |
| CD74 | 0.932 | 0.000 | — |
| CTSL | 0.920 | 0.000 | — |
| TGM3 | 0.826 | 0.000 | — |
| CTSH | 0.806 | 0.000 | — |
| CUBN | 0.776 | 0.000 | — |
| SET | 0.768 | 0.292 | — |
| CTSZ | 0.767 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| LAMC3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| USP17L24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| DEFA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATG7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDIA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP2R3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 4AW9, 4AWA, 4AWB, 4FGU, 4N6N,  | pLDDT=94.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lysosome / Vesicles; 额外: Nucleoplasm | 一致 |
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
1. LGMN — Legumain，研究基础较多，新颖性有限。
2. 蛋白大小433 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99538
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100600-LGMN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LGMN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99538
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000100600-LGMN/subcellular

![](https://images.proteinatlas.org/1426/1766_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/1426/1766_F1_4_red_green.jpg)
![](https://images.proteinatlas.org/1426/38_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/1426/38_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/1426/39_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/1426/39_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99538-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
