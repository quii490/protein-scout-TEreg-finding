---
type: protein-evaluation
gene: "GGA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GGA1 — REJECTED (研究热度过高 (PubMed strict=120，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GGA1 |
| 蛋白名称 | ADP-ribosylation factor-binding protein GGA1 |
| 蛋白大小 | 639 aa / 70.4 kDa |
| UniProt ID | Q9UJY5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Vesicles; 额外: Nucleoplasm; UniProt: Golgi apparatus, trans-Golgi network membrane; Endosome memb |
| 蛋白大小 | 10/10 | ×1 | 10 | 639 aa / 70.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=120 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.5; PDB: 1J2J, 1JWF, 1JWG, 1NA8, 1NAF, 1NWM, 1O3X |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008152, IPR013041, IPR008942, IPR008153, IPR004 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Nucleoplasm | Supported |
| UniProt | Golgi apparatus, trans-Golgi network membrane; Endosome membrane; Early endosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- early endosome (GO:0005769)
- early endosome membrane (GO:0031901)
- endosome membrane (GO:0010008)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 120 |
| PubMed broad count | 202 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Emerging roles of Golgi/endosome-localizing monomeric clathrin adaptors GGAs.. *Anatomical science international*. PMID: 31659673
2. GGA1 interacts with the endosomal Na+/H+ exchanger NHE6 governing localization to the endosome compartment.. *The Journal of biological chemistry*. PMID: 39002678
3. Induced oligomerization targets Golgi proteins for degradation in lysosomes.. *Molecular biology of the cell*. PMID: 26446839
4. Depletion of GGA1 and GGA3 mediates postinjury elevation of BACE1.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 22836275
5. GGA1 participates in spermatogenesis in mice under stress.. *PeerJ*. PMID: 37551344

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.5 |
| 高置信度残基 (pLDDT>90) 占比 | 44.6% |
| 置信残基 (pLDDT 70-90) 占比 | 19.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 28.6% |
| 有序区域 (pLDDT>70) 占比 | 64.2% |
| 可用 PDB 条目 | 1J2J, 1JWF, 1JWG, 1NA8, 1NAF, 1NWM, 1O3X, 1OM9, 1OXZ, 1PY1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1J2J, 1JWF, 1JWG, 1NA8, 1NAF, 1NWM, 1O3X, 1OM9, 1OXZ, 1PY1）+ AlphaFold极高置信度预测（pLDDT=73.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008152, IPR013041, IPR008942, IPR008153, IPR004152; Pfam: PF02883, PF03127, PF18308 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RABEP1 | 0.997 | 0.904 | — |
| ARF1 | 0.996 | 0.971 | — |
| IGF2R | 0.994 | 0.903 | — |
| CCDC91 | 0.989 | 0.977 | — |
| GGA2 | 0.987 | 0.765 | — |
| SORL1 | 0.986 | 0.956 | — |
| GGA3 | 0.983 | 0.626 | — |
| BACE1 | 0.979 | 0.876 | — |
| M6PR | 0.957 | 0.474 | — |
| SORT1 | 0.954 | 0.839 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RABEP1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15457209 |
| ARF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15143060 |
| TSG101 | psi-mi:"MI:0018"(two hybrid) | pubmed:15143060 |
| UBB | psi-mi:"MI:0018"(two hybrid) | pubmed:15143060 |
| RABGEF1 | psi-mi:"MI:0096"(pull down) | pubmed:12505986 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| Arf2 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12679809|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.5 + PDB: 1J2J, 1JWF, 1JWG, 1NA8, 1NAF,  | pLDDT=73.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network membrane; End / Golgi apparatus, Vesicles; 额外: Nucleoplasm | 一致 |
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
1. GGA1 — ADP-ribosylation factor-binding protein GGA1，研究基础较多，新颖性有限。
2. 蛋白大小639 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 120 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 120 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJY5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100083-GGA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GGA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJY5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000100083-GGA1/subcellular

![](https://images.proteinatlas.org/48280/693_B9_5_red_green.jpg)
![](https://images.proteinatlas.org/48280/693_B9_7_red_green.jpg)
![](https://images.proteinatlas.org/48280/712_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/48280/712_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/48280/804_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/48280/804_H8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJY5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UJY5 |
| SMART | SM00809;SM00288; |
| UniProt Domain [FT] | DOMAIN 17..147; /note="VHS"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00218"; DOMAIN 171..299; /note="GAT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00373"; DOMAIN 510..631; /note="GAE"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00093" |
| InterPro | IPR008152;IPR013041;IPR008942;IPR008153;IPR004152;IPR038425;IPR027422;IPR041198;IPR002014; |
| Pfam | PF02883;PF03127;PF18308;PF00790; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100083-GGA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BACE1 | Intact, Biogrid | true |
| GGA2 | Intact, Biogrid | true |
| GGA3 | Intact, Biogrid | true |
| IGF2R | Intact, Biogrid | true |
| RABEP1 | Intact, Biogrid | true |
| RNF11 | Intact, Biogrid | true |
| SORL1 | Intact, Biogrid | true |
| SORT1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
