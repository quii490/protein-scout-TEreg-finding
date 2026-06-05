---
type: protein-evaluation
gene: "MGAT4B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MGAT4B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MGAT4B |
| 蛋白名称 | Alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase B |
| 蛋白大小 | 548 aa / 63.2 kDa |
| UniProt ID | Q9UQ53 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Golgi apparatus, Vesicles, Cytosol; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 548 aa / 63.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006759, IPR057279, IPR056576; Pfam: PF04666, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Vesicles, Cytosol | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)
- Golgi membrane (GO:0000139)
- Golgi stack (GO:0005795)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Regulation of intracellular activity of N-glycan branching enzymes in mammals.. *The Journal of biological chemistry*. PMID: 38879010
2. Gene purging and the evolution of Neoave metabolism and longevity.. *The Journal of biological chemistry*. PMID: 37918802
3. UDP-galactose (SLC35A2) and UDP-N-acetylglucosamine (SLC35A3) Transporters Form Glycosylation-related Complexes with Mannoside Acetylglucosaminyltransferases (Mgats).. *The Journal of biological chemistry*. PMID: 25944901
4. Identification of the gene signatures related to NK/T cell communication to evaluate the tumor microenvironment and prognostic outcomes of patients with prostate adenocarcinoma.. *Frontiers in immunology*. PMID: 40308606
5. Identification of novel proteins for coronary artery disease by integrating GWAS data and human plasma proteomes.. *Heliyon*. PMID: 39386869

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.8 |
| 高置信度残基 (pLDDT>90) 占比 | 56.4% |
| 置信残基 (pLDDT 70-90) 占比 | 25.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 8.0% |
| 有序区域 (pLDDT>70) 占比 | 81.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.8，有序区 81.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006759, IPR057279, IPR056576; Pfam: PF04666, PF23524 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MGAT5 | 0.992 | 0.000 | — |
| MGAT5B | 0.992 | 0.000 | — |
| MGAT3 | 0.969 | 0.000 | — |
| MGAT2 | 0.968 | 0.000 | — |
| FUT8 | 0.964 | 0.000 | — |
| MGAT4D | 0.910 | 0.000 | — |
| MGAT4A | 0.905 | 0.000 | — |
| POMGNT1 | 0.755 | 0.000 | — |
| GYPC | 0.635 | 0.000 | — |
| MGAT1 | 0.609 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRSAM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| bgaB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YIPF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLAUR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APPBP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NetB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| kat80 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Spn | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| dally | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.8 + PDB: 无 | pLDDT=83.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm; 额外: Golgi apparatus, Vesicles, Cytoso | 一致 |
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
1. MGAT4B — Alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小548 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UQ53
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161013-MGAT4B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MGAT4B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UQ53
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000161013-MGAT4B/subcellular

![](https://images.proteinatlas.org/12804/1864_A5_20_cr5afd99ae9df92_red_green.jpg)
![](https://images.proteinatlas.org/12804/1864_A5_28_cr5afd99ae9e666_red_green.jpg)
![](https://images.proteinatlas.org/12804/1907_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/12804/1907_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/12804/1943_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/12804/1943_G12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UQ53-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
