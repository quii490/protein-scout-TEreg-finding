---
type: protein-evaluation
gene: "AP3B1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AP3B1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AP3B1 / ADTB3A |
| 蛋白名称 | AP-3 complex subunit beta-1 |
| 蛋白大小 | 1094 aa / 121.3 kDa |
| UniProt ID | O00203 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm, Nuclear membrane, Cytosol; UniProt: Cytoplasmic vesicle, clathrin-coated vesicle membrane; Golgi |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1094 aa / 121.3 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=78 篇 (≤80→4) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.3; PDB: 9C58, 9C59, 9C5A, 9C5B, 9C5C |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026740, IPR056314, IPR029394, IPR029390, IPR026 |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Nuclear membrane, Cytosol | Approved |
| UniProt | Cytoplasmic vesicle, clathrin-coated vesicle membrane; Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- AP-3 adaptor complex (GO:0030123)
- axon cytoplasm (GO:1904115)
- clathrin adaptor complex (GO:0030131)
- clathrin-coated vesicle membrane (GO:0030665)
- early endosome (GO:0005769)
- Golgi apparatus (GO:0005794)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 78 |
| PubMed broad count | 121 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ADTB3A |

**关键文献**:
1. AP3B1 facilitates PDIA3/ERP57 function to regulate rabies virus glycoprotein selective degradation and viral entry.. *Autophagy*. PMID: 39128851
2. AP3B1 Has Type I Interferon-Independent Antiviral Function against SARS-CoV-2.. *Viruses*. PMID: 39339853
3. Synergistic blood-based diagnostic value of AP3B1 and BMPR2 in Parkinson's disease.. *NPJ Parkinson's disease*. PMID: 41152257
4. Defective organellar membrane protein trafficking in Ap3b1-deficient cells.. *Journal of cell science*. PMID: 11058094
5. Reference gene selection for clinical chimeric antigen receptor T-cell product vector copy number assays.. *Cytotherapy*. PMID: 36935289

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 48.3% |
| 置信残基 (pLDDT 70-90) 占比 | 24.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 25.0% |
| 有序区域 (pLDDT>70) 占比 | 73.1% |
| 可用 PDB 条目 | 9C58, 9C59, 9C5A, 9C5B, 9C5C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（9C58, 9C59, 9C5A, 9C5B, 9C5C）+ AlphaFold预测（pLDDT=75.3），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026740, IPR056314, IPR029394, IPR029390, IPR026739; Pfam: PF01602, PF14796, PF24080 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Btk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Xpot | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ARRB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARRB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| pmbA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EPB41L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| Dynlt1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Cavin1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 9C58, 9C59, 9C5A, 9C5B, 9C5C | pLDDT=75.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, clathrin-coated vesicle membr / Vesicles; 额外: Nucleoplasm, Nuclear membrane, Cytos | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. AP3B1 — AP-3 complex subunit beta-1，有一定研究基础，但仍存在niche空间。
2. 蛋白大小1094 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 78 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00203
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132842-AP3B1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AP3B1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00203
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:56:15

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000132842-AP3B1/subcellular

![](https://images.proteinatlas.org/38347/1891_K12_28_cr5bbde0cd83d44_red_green.jpg)
![](https://images.proteinatlas.org/38347/1891_K12_5_cr5bbde0cd82b50_red_green.jpg)
![](https://images.proteinatlas.org/38347/2125_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/38347/2125_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/38347/2213_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/38347/2213_C7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00203-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
