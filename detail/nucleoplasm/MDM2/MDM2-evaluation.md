---
type: protein-evaluation
gene: "MDM2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MDM2 — REJECTED (研究热度过高 (PubMed strict=7706，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MDM2 |
| 蛋白名称 | E3 ubiquitin-protein ligase Mdm2 |
| 蛋白大小 | 491 aa / 55.2 kDa |
| UniProt ID | Q00987 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Centriolar satellite, Mid piece, P; UniProt: Nucleus, nucleoplasm; Cytoplasm; Nucleus, nucleolus; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 491 aa / 55.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=7706 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 1RV1, 1T4E, 1T4F, 1YCR, 1Z1M, 2AXI, 2C6A |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028340, IPR044080, IPR016495, IPR036885, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Centriolar satellite, Mid piece, Principal piece, End piece | Supported |
| UniProt | Nucleus, nucleoplasm; Cytoplasm; Nucleus, nucleolus; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endocytic vesicle membrane (GO:0030666)
- glutamatergic synapse (GO:0098978)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7706 |
| PubMed broad count | 12965 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The MDM2 gene family.. *Biomolecular concepts*. PMID: 25372739
2. Induction of the Mdm2 gene and protein by kinase signaling pathways is repressed by the pVHL tumor suppressor.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39047034
3. Oncogenic Functions of Alternatively Spliced MDM2-ALT2 Isoform in Retroperitoneal Liposarcoma.. *International journal of molecular sciences*. PMID: 39769278
4. The mdm2 proto-oncogene.. *Leukemia & lymphoma*. PMID: 9322885
5. Structure and function of MDM2 and MDM4 in health and disease.. *The Biochemical journal*. PMID: 39960347

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 29.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 14.3% |
| 低置信 (pLDDT<50) 占比 | 47.7% |
| 有序区域 (pLDDT>70) 占比 | 38.1% |
| 可用 PDB 条目 | 1RV1, 1T4E, 1T4F, 1YCR, 1Z1M, 2AXI, 2C6A, 2C6B, 2F1Y, 2FOP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 38.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028340, IPR044080, IPR016495, IPR036885, IPR003121; Pfam: PF02201, PF13920, PF00641 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RB1 | 0.999 | 0.889 | — |
| AKT1 | 0.999 | 0.891 | — |
| UBE2D2 | 0.999 | 0.999 | — |
| USP7 | 0.999 | 0.925 | — |
| CDKN2A | 0.999 | 0.992 | — |
| MDM4 | 0.999 | 0.999 | — |
| EP300 | 0.999 | 0.820 | — |
| TP53 | 0.999 | 0.999 | — |
| RPL11 | 0.999 | 0.999 | — |
| RPL5 | 0.999 | 0.940 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000444430.2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12016|pubmed:17936559 |
| Arrb1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| TBP | psi-mi:"MI:0096"(pull down) | pubmed:9271120 |
| TP53 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:8875929|mint:MINT-52212 |
| DAXX | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14444|pubmed:16845383 |
| USP7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14444|pubmed:16845383 |
| PML | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:12915590|imex:IM-19268| |
| - | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12011|pubmed:17157790 |
| ESR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11178989|imex:IM-19898| |
| ATF4 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 1RV1, 1T4E, 1T4F, 1YCR, 1Z1M,  | pLDDT=62.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Cytoplasm; Nucleus, nucleolu / Nucleoplasm, Cytosol; 额外: Centriolar satellite, Mi | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MDM2 — E3 ubiquitin-protein ligase Mdm2，研究基础较多，新颖性有限。
2. 蛋白大小491 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7706 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 7706 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q00987
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135679-MDM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MDM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q00987
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000135679-MDM2/subcellular

![](https://images.proteinatlas.org/45159/2185_G12_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/45159/2185_G12_65_blue_red_green.jpg)
![](https://images.proteinatlas.org/45159/2199_F12_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/45159/2199_F12_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/16303/944_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/16303/944_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q00987-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
