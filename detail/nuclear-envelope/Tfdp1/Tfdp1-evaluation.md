---
type: protein-evaluation
gene: "Tfdp1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Tfdp1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Tfdp1 / DP1 |
| 蛋白名称 | Transcription factor Dp-1 |
| 蛋白大小 | 410 aa / 45.1 kDa |
| UniProt ID | Q14186 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear membrane, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 410 aa / 45.1 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=96 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.8; PDB: 2AZE, 5GOW, 5TUU, 5TUV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037241, IPR003316, IPR038168, IPR014889, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear membrane, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- Rb-E2F complex (GO:0035189)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 96 |
| PubMed broad count | 252 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DP1 |

**关键文献**:
1. Transcriptional profiling of lung cell populations in idiopathic pulmonary arterial hypertension.. *Pulmonary circulation*. PMID: 32166015
2. Transcriptomic analysis of human pulmonary microvascular endothelial cells treated with LPS.. *Cellular signalling*. PMID: 37633475
3. Comprehensive Analysis Reveals the Potential Roles of Transcription Factor Dp-1 in Lung Adenocarcinoma.. *World journal of oncology*. PMID: 37350808
4. ZNF146 regulates cell cycle progression via TFDP1 and DEPDC1B in ovarian cancer cells.. *Reproduction (Cambridge, England)*. PMID: 38614125
5. Upregulation of TFDP1 and CDC27 Plays an Important Role in Bronchiectasis.. *Canadian respiratory journal*. PMID: 41458288

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.8 |
| 高置信度残基 (pLDDT>90) 占比 | 46.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 37.3% |
| 有序区域 (pLDDT>70) 占比 | 54.8% |
| 可用 PDB 条目 | 2AZE, 5GOW, 5TUU, 5TUV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.8），有序残基占 54.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037241, IPR003316, IPR038168, IPR014889, IPR015648; Pfam: PF08781, PF02319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RB1 | 0.999 | 0.985 | — |
| E2F4 | 0.999 | 0.991 | — |
| E2F5 | 0.999 | 0.982 | — |
| E2F6 | 0.999 | 0.943 | — |
| E2F1 | 0.999 | 0.994 | — |
| E2F3 | 0.996 | 0.843 | — |
| RBL1 | 0.996 | 0.954 | — |
| E2F2 | 0.989 | 0.879 | — |
| RBL2 | 0.983 | 0.566 | — |
| PCGF6 | 0.963 | 0.813 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| E2F6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SIAH1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| RBL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17531812 |
| LIN9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| LIN37 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| LIN54 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| Rnf2 | psi-mi:"MI:0096"(pull down) | pubmed:17296600 |
| E2F1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:16360038|imex:IM-20931 |
| RB1 | psi-mi:"MI:0096"(pull down) | pubmed:16360038|imex:IM-20931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.8 + PDB: 2AZE, 5GOW, 5TUU, 5TUV | pLDDT=69.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Nuclear membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. Tfdp1 — Transcription factor Dp-1，研究基础较多，新颖性有限。
2. 蛋白大小410 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 96 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14186
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198176-TFDP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Tfdp1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14186
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198176-TFDP1/subcellular

![](https://images.proteinatlas.org/44754/711_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/44754/711_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/44754/723_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/44754/723_H3_3_red_green.jpg)
![](https://images.proteinatlas.org/44754/866_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/44754/866_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14186-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14186 |
| SMART | SM01138;SM01372; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037241;IPR003316;IPR038168;IPR014889;IPR015648;IPR036388;IPR036390; |
| Pfam | PF08781;PF02319; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198176-TFDP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDK2 | Biogrid, Bioplex | true |
| COMMD1 | Biogrid, Bioplex | true |
| COMMD4 | Biogrid, Bioplex | true |
| COMMD8 | Biogrid, Bioplex | true |
| E2F1 | Intact, Biogrid | true |
| E2F2 | Intact, Biogrid | true |
| E2F4 | Intact, Biogrid | true |
| E2F6 | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
