---
type: protein-evaluation
gene: "NGFR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NGFR — REJECTED (研究热度过高 (PubMed strict=513，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NGFR / TNFRSF16 |
| 蛋白名称 | Tumor necrosis factor receptor superfamily member 16 |
| 蛋白大小 | 427 aa / 45.2 kDa |
| UniProt ID | P08138 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; UniProt: Cell membrane; Cytoplasm; Perikaryon; Cell projection, growt |
| 蛋白大小 | 10/10 | ×1 | 10 | 427 aa / 45.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=513 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.9; PDB: 2N80, 2N83, 2N97, 3EWV, 5ZGG, 7CSQ, 8X8T |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011029, IPR000488, IPR052302, IPR001368, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | Cell membrane; Cytoplasm; Perikaryon; Cell projection, growth cone; Cell projection, dendritic spine | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cell-cell junction (GO:0005911)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- endosome (GO:0005768)
- extracellular region (GO:0005576)
- growth cone (GO:0030426)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 513 |
| PubMed broad count | 1980 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TNFRSF16 |

**关键文献**:
1. Comprehensive Molecular Characterization of Pheochromocytoma and Paraganglioma.. *Cancer cell*. PMID: 28162975
2. AP3B1 facilitates PDIA3/ERP57 function to regulate rabies virus glycoprotein selective degradation and viral entry.. *Autophagy*. PMID: 39128851
3. A human mucosal melanoma organoid platform for modeling tumor heterogeneity and exploring immunotherapy combination options.. *Science advances*. PMID: 37889972
4. NGFR Gene and Single Nucleotide Polymorphisms, rs2072446 and rs11466162, Playing Roles in Psychiatric Disorders.. *Brain sciences*. PMID: 36291307
5. Nerve growth factor receptor (Ngfr) induces neurogenic plasticity by suppressing reactive astroglial Lcn2/Slc22a17 signaling in Alzheimer's disease.. *NPJ Regenerative medicine*. PMID: 37429840

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.9 |
| 高置信度残基 (pLDDT>90) 占比 | 45.0% |
| 置信残基 (pLDDT 70-90) 占比 | 19.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.2% |
| 低置信 (pLDDT<50) 占比 | 24.4% |
| 有序区域 (pLDDT>70) 占比 | 64.4% |
| 可用 PDB 条目 | 2N80, 2N83, 2N97, 3EWV, 5ZGG, 7CSQ, 8X8T |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2N80, 2N83, 2N97, 3EWV, 5ZGG, 7CSQ, 8X8T）+ AlphaFold极高置信度预测（pLDDT=75.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011029, IPR000488, IPR052302, IPR001368, IPR041448; Pfam: PF00531, PF18422, PF00020 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BDNF | 0.999 | 0.095 | — |
| NTF3 | 0.999 | 0.625 | — |
| NGF | 0.999 | 0.863 | — |
| NTRK1 | 0.999 | 0.715 | — |
| LINGO1 | 0.999 | 0.625 | — |
| SORT1 | 0.999 | 0.688 | — |
| NTF4 | 0.999 | 0.000 | — |
| RTN4R | 0.998 | 0.518 | — |
| RIPK2 | 0.993 | 0.927 | — |
| ARHGDIA | 0.992 | 0.602 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1038810 | psi-mi:"MI:0030"(cross-linking study) | pubmed:11756426|imex:IM-20354 |
| ENSP00000172229.3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:11756426|imex:IM-20354 |
| NGF | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15131306 |
| EBI-4411191 | psi-mi:"MI:0096"(pull down) | pubmed:21541365|imex:IM-16842 |
| RIPK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21541365|imex:IM-16842 |
| ARHGDIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21541365|imex:IM-16842 |
| TRAF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21541365|imex:IM-16842 |
| TSC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17355907|imex:IM-19197 |
| BEX3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17355907|imex:IM-19197 |
| APP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:11756426|imex:IM-20354 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.9 + PDB: 2N80, 2N83, 2N97, 3EWV, 5ZGG,  | pLDDT=75.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasm; Perikaryon; Cell project / Nucleoplasm, Plasma membrane | 一致 |
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
1. NGFR — Tumor necrosis factor receptor superfamily member 16，研究基础较多，新颖性有限。
2. 蛋白大小427 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 513 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 513 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P08138
- Protein Atlas: https://www.proteinatlas.org/ENSG00000064300-NGFR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NGFR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P08138
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000064300-NGFR/subcellular

![](https://images.proteinatlas.org/4765/10_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4765/10_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/4765/11_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4765/11_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/4765/15_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4765/15_D1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P08138-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
