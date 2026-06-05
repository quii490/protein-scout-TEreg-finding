---
type: protein-evaluation
gene: "PKN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PKN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PKN3 / PKNBETA |
| 蛋白名称 | Serine/threonine-protein kinase N3 |
| 蛋白大小 | 889 aa / 99.4 kDa |
| UniProt ID | Q6P5Z2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Nucleus; Cytoplasm, perinuclear region |
| 蛋白大小 | 8/10 | ×1 | 8 | 889 aa / 99.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000961, IPR035892, IPR011072, IPR036274, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 45 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PKNBETA |

**关键文献**:
1. PKN3 as a key regulator in cancer - From signaling pathways to targeted therapies.. *Bioorganic chemistry*. PMID: 40633483
2. Chemical proteomics reveals the target landscape of 1,000 kinase inhibitors.. *Nature chemical biology*. PMID: 37904048
3. Efficient delivery of PKN3 shRNA for the treatment of breast cancer via lipid nanoparticles.. *Bioorganic & medicinal chemistry*. PMID: 35752145
4. Regulation of osteoclast function via Rho-Pkn3-c-Src pathways.. *Journal of oral biosciences*. PMID: 31400545
5. Oral biosciences: The annual review 2019.. *Journal of oral biosciences*. PMID: 32109566

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.6 |
| 高置信度残基 (pLDDT>90) 占比 | 32.4% |
| 置信残基 (pLDDT 70-90) 占比 | 36.8% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 18.1% |
| 有序区域 (pLDDT>70) 占比 | 69.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.6，有序区 69.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000961, IPR035892, IPR011072, IPR036274, IPR011009; Pfam: PF02185, PF00069, PF00433 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARHGAP10 | 0.957 | 0.374 | — |
| ARHGAP26 | 0.937 | 0.433 | — |
| PDPK1 | 0.922 | 0.179 | — |
| PKN1 | 0.911 | 0.000 | — |
| RHOC | 0.907 | 0.311 | — |
| PKN2 | 0.906 | 0.000 | — |
| RHOA | 0.891 | 0.441 | — |
| RAC1 | 0.793 | 0.277 | — |
| RHOB | 0.751 | 0.372 | — |
| ARHGAP1 | 0.679 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380984 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| TGFBR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RABGAP1L | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| YEATS4 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| STRN | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CLOCK | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| OIP5 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CAVIN1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.6 + PDB: 无 | pLDDT=74.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, perinuclear region / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PKN3 — Serine/threonine-protein kinase N3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小889 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P5Z2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160447-PKN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PKN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P5Z2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000160447-PKN3/subcellular

![](https://images.proteinatlas.org/58305/1010_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58305/1010_A7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/58305/1014_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/58305/1014_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58305/1061_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/58305/1061_G10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P5Z2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
