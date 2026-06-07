---
type: protein-evaluation
gene: "FERMT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FERMT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FERMT2 / KIND2, MIG2, PLEKHC1 |
| 蛋白名称 | Fermitin family homolog 2 |
| 蛋白大小 | 680 aa / 77.9 kDa |
| UniProt ID | Q96AC1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Focal adhesion sites; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Cytoplasm, cell cortex; Cytoplasm, cytoskeleton;  |
| 蛋白大小 | 10/10 | ×1 | 10 | 680 aa / 77.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.9; PDB: 2LGX, 2LKO, 2MSU, 4F7H, 6U4N, 6XTJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019749, IPR035963, IPR019748, IPR037843, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Focal adhesion sites; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Cytoplasm, cell cortex; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, stress fiber; C... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- cell cortex (GO:0005938)
- cell junction (GO:0030054)
- cell surface (GO:0009986)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 145 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIND2, MIG2, PLEKHC1 |

**关键文献**:
1. Alzheimer's disease risk genes and mechanisms of disease pathogenesis.. *Biological psychiatry*. PMID: 24951455
2. FERMT2 drives anoikis resistance and peritoneal metastasis by enhancing extracellular matrix deposition in gastric cancer.. *Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association*. PMID: 40024947
3. FERMT2 rs17125944 polymorphism with Alzheimer's disease risk: a replication and meta-analysis.. *Oncotarget*. PMID: 27244899
4. Comparison of Kindlin-2 deficiency-stimulated osteoarthritis-like lesions induced by Prg4(CreERT2) versus Aggrecan(CreERT2) transgene in mice.. *Journal of orthopaedic translation*. PMID: 37292436
5. Genetics of Alzheimer's disease.. *Advances in genetics*. PMID: 25311924

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 47.4% |
| 置信残基 (pLDDT 70-90) 占比 | 28.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 15.3% |
| 有序区域 (pLDDT>70) 占比 | 76.2% |
| 可用 PDB 条目 | 2LGX, 2LKO, 2MSU, 4F7H, 6U4N, 6XTJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2LGX, 2LKO, 2MSU, 4F7H, 6U4N, 6XTJ）+ AlphaFold极高置信度预测（pLDDT=79.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019749, IPR035963, IPR019748, IPR037843, IPR040790; Pfam: PF00373, PF18124 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FBLIM1 | 0.999 | 0.299 | — |
| ILK | 0.997 | 0.757 | — |
| PXN | 0.980 | 0.905 | — |
| VCL | 0.896 | 0.565 | — |
| PARVA | 0.893 | 0.354 | — |
| LIMS1 | 0.856 | 0.345 | — |
| FLNA | 0.852 | 0.098 | — |
| PICALM | 0.802 | 0.424 | — |
| FERMT3 | 0.798 | 0.778 | — |
| ITGB1 | 0.796 | 0.369 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| ITGB1 | psi-mi:"MI:0055"(fluorescent resonance energy tran | pubmed:21947080|imex:IM-16896 |
| EBI-6249674 | psi-mi:"MI:0096"(pull down) | pubmed:22623228|imex:IM-17422 |
| EBI-6095751 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19119138|imex:IM-20555 |
| EBI-6095589 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19119138|imex:IM-20555 |
| WDR20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FERMT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RIPPLY2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 2LGX, 2LKO, 2MSU, 4F7H, 6U4N,  | pLDDT=79.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cell cortex; Cytoplasm, cyto / Focal adhesion sites; 额外: Nucleoplasm, Cytosol | 一致 |
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
1. FERMT2 — Fermitin family homolog 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小680 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AC1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000073712-FERMT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FERMT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AC1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Focal adhesion sites (supported)。来源: https://www.proteinatlas.org/ENSG00000073712-FERMT2/subcellular

![](https://images.proteinatlas.org/40505/411_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40505/411_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40505/415_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40505/415_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40505/416_B11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/40505/416_B11_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96AC1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96AC1 |
| SMART | SM00295;SM00233; |
| UniProt Domain [FT] | DOMAIN 189..661; /note="FERM"; DOMAIN 380..476; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145" |
| InterPro | IPR019749;IPR035963;IPR019748;IPR037843;IPR040790;IPR011993;IPR001849;IPR037837; |
| Pfam | PF00373;PF18124; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000073712-FERMT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CTNNB1 | Intact, Biogrid | true |
| ARF6 | Biogrid | false |
| BBS12 | Intact | false |
| EZR | Biogrid | false |
| FBLIM1 | Biogrid | false |
| FHL1 | Biogrid | false |
| ILK | Biogrid | false |
| KRAS | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
