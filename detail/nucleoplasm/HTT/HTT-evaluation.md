---
type: protein-evaluation
gene: "HTT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HTT — REJECTED (研究热度过高 (PubMed strict=3519，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HTT / HTT, SERT |
| 蛋白名称 | Sodium-dependent serotonin transporter |
| 蛋白大小 | 630 aa / 70.3 kDa |
| UniProt ID | P31645 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cell membrane; Endomembrane system; Endosome membrane; Synap |
| 蛋白大小 | 10/10 | ×1 | 10 | 630 aa / 70.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3519 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.7; PDB: 5I6X, 5I6Z, 5I71, 5I73, 5I74, 5I75, 6AWN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000175, IPR013086, IPR037272; Pfam: PF03491, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cell membrane; Endomembrane system; Endosome membrane; Synapse; Cell junction, focal adhesion; Cell ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endomembrane system (GO:0012505)
- endosome membrane (GO:0010008)
- focal adhesion (GO:0005925)
- membrane raft (GO:0045121)
- neuron projection (GO:0043005)
- plasma membrane (GO:0005886)
- postsynaptic membrane (GO:0045211)
- presynaptic membrane (GO:0042734)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3519 |
| PubMed broad count | 6928 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HTT, SERT |

**关键文献**:
1. Huntington's Disease: Complex Pathogenesis and Therapeutic Strategies.. *International journal of molecular sciences*. PMID: 38612657
2. The Biology of Huntingtin.. *Neuron*. PMID: 26938440
3. Gene targeting techniques for Huntington's disease.. *Ageing research reviews*. PMID: 34098113
4. Huntington Disease.. **. PMID: 32644592
5. Polyglutamine-mediated ribotoxicity disrupts proteostasis and stress responses in Huntington's disease.. *Nature cell biology*. PMID: 38741019

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.7 |
| 高置信度残基 (pLDDT>90) 占比 | 74.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.1% |
| 低置信 (pLDDT<50) 占比 | 13.7% |
| 有序区域 (pLDDT>70) 占比 | 85.3% |
| 可用 PDB 条目 | 5I6X, 5I6Z, 5I71, 5I73, 5I74, 5I75, 6AWN, 6AWO, 6AWP, 6AWQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5I6X, 5I6Z, 5I71, 5I73, 5I74, 5I75, 6AWN, 6AWO, 6AWP, 6AWQ）+ AlphaFold极高置信度预测（pLDDT=84.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000175, IPR013086, IPR037272; Pfam: PF03491, PF00209 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HAP1 | 0.999 | 0.822 | — |
| TP53 | 0.998 | 0.307 | — |
| F8A2 | 0.998 | 0.960 | — |
| CREBBP | 0.997 | 0.832 | — |
| OPTN | 0.997 | 0.777 | — |
| ITPR1 | 0.995 | 0.297 | — |
| ZDHHC17 | 0.995 | 0.711 | — |
| TAF4 | 0.994 | 0.510 | — |
| GAPDH | 0.993 | 0.513 | — |
| REST | 0.991 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| N | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Usp10 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Ino80 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| sgg | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| sals | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| BNIP3 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| ENSP00000347184.5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-17394|pubmed:23275563 |
| SH3GL3 | psi-mi:"MI:0018"(two hybrid) | pubmed:16115810 |
| GIT1 | psi-mi:"MI:0428"(imaging technique) | pubmed:15383276|mint:MINT-5217 |
| MED31 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.7 + PDB: 5I6X, 5I6Z, 5I71, 5I73, 5I74,  | pLDDT=84.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Endomembrane system; Endosome membr / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HTT — Sodium-dependent serotonin transporter，研究基础较多，新颖性有限。
2. 蛋白大小630 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3519 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3519 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P31645
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197386-HTT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HTT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P31645
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000197386-HTT/subcellular

![](https://images.proteinatlas.org/26114/298_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/26114/298_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/26114/299_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/26114/299_A6_3_red_green.jpg)
![](https://images.proteinatlas.org/26114/300_A6_11_red_green.jpg)
![](https://images.proteinatlas.org/26114/300_A6_9_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P31645-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P31645 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000175;IPR013086;IPR037272; |
| Pfam | PF03491;PF00209; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197386-HTT/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHD3 | Intact, Biogrid | true |
| CREBBP | Intact, Biogrid | true |
| CRMP1 | Intact, Biogrid | true |
| DNAJA1 | Intact, Biogrid | true |
| ECH1 | Intact, Biogrid | true |
| ELP1 | Intact, Biogrid | true |
| F8A1 | Intact, Biogrid | true |
| FEZ1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
