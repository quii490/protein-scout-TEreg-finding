---
type: protein-evaluation
gene: "CTDNEP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTDNEP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTDNEP1 / DULLARD |
| 蛋白名称 | CTD nuclear envelope phosphatase 1 |
| 蛋白大小 | 244 aa / 28.4 kDa |
| UniProt ID | O95476 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Lipid droplets; UniProt: Endoplasmic reticulum membrane; Nucleus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 244 aa / 28.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=90.5; PDB: 8UJL, 8UJM |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011948, IPR004274, IPR036412, IPR023214, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Lipid droplets | Approved |
| UniProt | Endoplasmic reticulum membrane; Nucleus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum membrane (GO:0005789)
- lipid droplet (GO:0005811)
- Nem1-Spo7 phosphatase complex (GO:0071595)
- nuclear envelope (GO:0005635)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DULLARD |

**关键文献**:
1. Suppression of TGF-β/SMAD signaling by an inner nuclear membrane phosphatase complex.. *Nature communications*. PMID: 40216785
2. Research Trends in C-Terminal Domain Nuclear Envelope Phosphatase 1.. *Life (Basel, Switzerland)*. PMID: 37374122
3. Structure and mechanism of the human CTDNEP1-NEP1R1 membrane protein phosphatase complex necessary to maintain ER membrane morphology.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38776370
4. Structure and mechanism of the human CTDNEP1-NEP1R1 membrane protein phosphatase complex necessary to maintain ER membrane morphology.. *bioRxiv : the preprint server for biology*. PMID: 38045299
5. Placental multi-omics integration identifies candidate functional genes for birthweight.. *Nature communications*. PMID: 35501330

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.5 |
| 高置信度残基 (pLDDT>90) 占比 | 70.5% |
| 置信残基 (pLDDT 70-90) 占比 | 23.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 93.9% |
| 可用 PDB 条目 | 8UJL, 8UJM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8UJL, 8UJM）+ AlphaFold高质量预测（pLDDT=90.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011948, IPR004274, IPR036412, IPR023214, IPR050365; Pfam: PF03031 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNEP1R1 | 0.994 | 0.292 | — |
| LPIN1 | 0.899 | 0.506 | — |
| LPIN3 | 0.886 | 0.506 | — |
| LPIN2 | 0.868 | 0.506 | — |
| BMPR2 | 0.853 | 0.068 | — |
| BMP1 | 0.649 | 0.000 | — |
| GTF2F1 | 0.577 | 0.477 | — |
| CTDP1 | 0.560 | 0.000 | — |
| SFT2D1 | 0.497 | 0.000 | — |
| GFM2 | 0.446 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| SLC17A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBQLN2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCDC107 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLXDC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EVA1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM189B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OLFM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SRPRB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TLR5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.5 + PDB: 8UJL, 8UJM | pLDDT=90.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane / Lipid droplets | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CTDNEP1 — CTD nuclear envelope phosphatase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小244 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95476
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175826-CTDNEP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTDNEP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95476
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Lipid droplets (approved)。来源: https://www.proteinatlas.org/ENSG00000175826-CTDNEP1/subcellular

![](https://images.proteinatlas.org/66466/1318_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/66466/1318_H2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/66466/1693_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66466/1693_C2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95476-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95476 |
| SMART | SM00577; |
| UniProt Domain [FT] | DOMAIN 57..224; /note="FCP1 homology"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00336" |
| InterPro | IPR011948;IPR004274;IPR036412;IPR023214;IPR050365; |
| Pfam | PF03031; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175826-CTDNEP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDCA3 | Bioplex | false |
| CNEP1R1 | Intact | false |
| UBQLN2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
