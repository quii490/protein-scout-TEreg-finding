---
type: protein-evaluation
gene: "RIMKLA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RIMKLA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RIMKLA / FAM80A |
| 蛋白名称 | N-acetylaspartylglutamate synthase A |
| 蛋白大小 | 391 aa / 42.9 kDa |
| UniProt ID | Q8IXN7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 391 aa / 42.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011761, IPR013651, IPR013815, IPR004666; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM80A |

**关键文献**:
1. Ribosomal modification protein rimK-like family member A activates betaine-homocysteine S-methyltransferase 1 to ameliorate hepatic steatosis.. *Signal transduction and targeted therapy*. PMID: 39117631
2. A novel diabetic foot ulcer diagnostic model: identification and analysis of genes related to glutamine metabolism and immune infiltration.. *BMC genomics*. PMID: 38287255
3. Mice deficient in the NAAG synthetase II gene Rimkla are impaired in a novel object recognition task.. *Journal of neurochemistry*. PMID: 33638175
4. NAAG synthetase deficiency has only low influence on pathogenesis in a Canavan disease mouse model.. *Journal of inherited metabolic disease*. PMID: 38011891
5. N-acetylaspartylglutamate synthetase II synthesizes N-acetylaspartylglutamylglutamate.. *The Journal of biological chemistry*. PMID: 21454531

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 63.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 18.9% |
| 有序区域 (pLDDT>70) 占比 | 76.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.2，有序区 76.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011761, IPR013651, IPR013815, IPR004666; Pfam: PF08443 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAT8L | 0.960 | 0.000 | — |
| FOLH1 | 0.932 | 0.000 | — |
| ASPA | 0.904 | 0.000 | — |
| RIMKLB | 0.903 | 0.000 | — |
| GATB | 0.761 | 0.000 | — |
| MOCOS | 0.618 | 0.500 | — |
| NAGS | 0.609 | 0.000 | — |
| C4orf47 | 0.537 | 0.000 | — |
| CCDC30 | 0.535 | 0.000 | — |
| ALDH18A1 | 0.481 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZNG1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MOCOS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DHTKD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| FGFR3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GSN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| HRAS | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| SFN | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| YWHAG | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| YWHAH | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 无 | pLDDT=80.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

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
1. RIMKLA — N-acetylaspartylglutamate synthase A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小391 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXN7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177181-RIMKLA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RIMKLA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXN7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (uncertain)。来源: https://www.proteinatlas.org/ENSG00000177181-RIMKLA/subcellular

![](https://images.proteinatlas.org/27826/1033_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/27826/1033_D3_3_red_green.jpg)
![](https://images.proteinatlas.org/27826/251_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/27826/251_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/27826/290_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/27826/290_A8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IXN7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
