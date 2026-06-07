---
type: protein-evaluation
gene: "PDZRN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PDZRN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PDZRN3 / KIAA1095, LNX3, SEMCAP3 |
| 蛋白名称 | E3 ubiquitin-protein ligase PDZRN3 |
| 蛋白大小 | 1066 aa / 119.6 kDa |
| UniProt ID | Q9UPQ7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Synapse; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1066 aa / 119.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.1; PDB: 1UHP, 1WH1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051971, IPR001478, IPR036034, IPR001841, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.5/180** | |
| **归一化总分** | | | **59.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Synapse; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- neuromuscular junction (GO:0031594)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1095, LNX3, SEMCAP3 |

**关键文献**:
1. Identification and characterization of PDZRN3 and PDZRN4 genes in silico.. *International journal of molecular medicine*. PMID: 15010864
2. Decrease of Pdzrn3 is required for heart maturation and protects against heart failure.. *Scientific reports*. PMID: 34996942
3. PDZRN3 regulates adipogenesis of mesenchymal progenitors in muscle.. *Regenerative therapy*. PMID: 39980718
4. The RING finger- and PDZ domain-containing protein PDZRN3 controls localization of the Mg(2+) regulator claudin-16 in renal tube epithelial cells.. *The Journal of biological chemistry*. PMID: 28623232
5. Targeting Pdzrn3 maintains adult blood-brain barrier and central nervous system homeostasis.. *Journal of cerebral blood flow and metabolism : official journal of the International Society of Cerebral Blood Flow and Metabolism*. PMID: 34644209

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.1 |
| 高置信度残基 (pLDDT>90) 占比 | 22.4% |
| 置信残基 (pLDDT 70-90) 占比 | 26.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 39.2% |
| 有序区域 (pLDDT>70) 占比 | 49.0% |
| 可用 PDB 条目 | 1UHP, 1WH1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.1），有序残基占 49.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051971, IPR001478, IPR036034, IPR001841, IPR013083; Pfam: PF00595, PF13923 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MUSK | 0.756 | 0.328 | — |
| ANKRD20A2 | 0.617 | 0.614 | — |
| ANKRD20A1 | 0.601 | 0.597 | — |
| LNX1 | 0.566 | 0.254 | — |
| LNX2 | 0.558 | 0.254 | — |
| KIDINS220 | 0.557 | 0.091 | — |
| TAF3 | 0.512 | 0.000 | — |
| SHQ1 | 0.495 | 0.000 | — |
| SEMA4C | 0.477 | 0.000 | — |
| OIP5 | 0.468 | 0.468 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000263666.4 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| BMPR2 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| ZNF785 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POTEB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STX11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM13C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OIP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SDHA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| OFD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.1 + PDB: 1UHP, 1WH1 | pLDDT=63.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Synapse; Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PDZRN3 — E3 ubiquitin-protein ligase PDZRN3，非常新颖，仅有少数基础研究。
2. 蛋白大小1066 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPQ7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121440-PDZRN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PDZRN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPQ7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000121440-PDZRN3/subcellular

![](https://images.proteinatlas.org/38822/1927_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/38822/1927_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/38822/412_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/38822/412_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/38822/419_B2_4_red_green.jpg)
![](https://images.proteinatlas.org/38822/419_B2_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPQ7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPQ7 |
| SMART | SM00228;SM00184; |
| UniProt Domain [FT] | DOMAIN 249..339; /note="PDZ 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 419..503; /note="PDZ 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143" |
| InterPro | IPR051971;IPR001478;IPR036034;IPR001841;IPR013083;IPR017907;IPR001293; |
| Pfam | PF00595;PF13923; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000121440-PDZRN3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNLL1 | Biogrid, Opencell | true |
| DYNLL2 | Biogrid, Opencell | true |
| FZD4 | Biogrid | false |
| SLC5A8 | Biogrid | false |
| TBX20 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
