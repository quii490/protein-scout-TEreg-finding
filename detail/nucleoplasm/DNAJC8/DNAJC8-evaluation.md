---
type: protein-evaluation
gene: "DNAJC8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC8 / SPF31 |
| 蛋白名称 | DnaJ homolog subfamily C member 8 |
| 蛋白大小 | 253 aa / 29.8 kDa |
| UniProt ID | O75937 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytokinetic bridge, Cytosol; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 253 aa / 29.8 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=83.7; PDB: 7VPX |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001623, IPR042858, IPR036869; Pfam: PF00226 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytokinetic bridge, Cytosol | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- intercellular bridge (GO:0045171)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPF31 |

**关键文献**:
1. DNAJC8: a prognostic marker and potential therapeutic target for hepatocellular carcinoma.. *Frontiers in immunology*. PMID: 38274804
2. Scouring the human Hsp70 network uncovers diverse chaperone safeguards buffering TDP-43 toxicity.. *bioRxiv : the preprint server for biology*. PMID: 40654997
3. A Chemotherapy Response-Related Gene Signature and DNAJC8 as Key Mediators of Hepatocellular Carcinoma Progression and Drug Resistance.. *Journal of hepatocellular carcinoma*. PMID: 40130083
4. Analyses of the function of DnaJ family proteins reveal an underlying regulatory mechanism of heat tolerance in honeybee.. *The Science of the total environment*. PMID: 32059293
5. A novel nuclear DnaJ protein, DNAJC8, can suppress the formation of spinocerebellar ataxia 3 polyglutamine aggregation in a J-domain independent manner.. *Biochemical and biophysical research communications*. PMID: 27133716

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.7 |
| 高置信度残基 (pLDDT>90) 占比 | 57.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 82.2% |
| 可用 PDB 条目 | 7VPX |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.7，有序区 82.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR042858, IPR036869; Pfam: PF00226 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHX9 | 0.894 | 0.314 | — |
| PRPF40A | 0.875 | 0.000 | — |
| SRRT | 0.874 | 0.000 | — |
| PPP1R8 | 0.873 | 0.000 | — |
| RBM39 | 0.868 | 0.189 | — |
| SRRM2 | 0.848 | 0.124 | — |
| SF3A2 | 0.842 | 0.830 | — |
| HTATSF1 | 0.836 | 0.000 | — |
| RBM25 | 0.835 | 0.000 | — |
| DDX5 | 0.833 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GH1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| HMGA1 | psi-mi:"MI:0049"(filter binding) | imex:IM-12160|pubmed:18850631 |
| Sf3a1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CTNNB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| HNRNPM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.7 + PDB: 7VPX | pLDDT=83.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytokinetic bridge, Cytosol | 一致 |
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
1. DNAJC8 — DnaJ homolog subfamily C member 8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小253 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75937
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126698-DNAJC8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75937
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:55

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000126698-DNAJC8/subcellular

![](https://images.proteinatlas.org/26275/1050_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/26275/1050_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/26275/2268_B5_110_red_green.jpg)
![](https://images.proteinatlas.org/26275/2268_B5_42_red_green.jpg)
![](https://images.proteinatlas.org/26275/917_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/26275/917_C1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75937-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75937 |
| SMART | SM00271; |
| UniProt Domain [FT] | DOMAIN 57..124; /note="J"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00286" |
| InterPro | IPR001623;IPR042858;IPR036869; |
| Pfam | PF00226; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000126698-DNAJC8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGTR1 | Intact, Biogrid | true |
| CCDC97 | Biogrid, Bioplex | true |
| GPATCH11 | Biogrid, Opencell | true |
| RAP1A | Biogrid, Bioplex | true |
| SF3A1 | Biogrid, Opencell | true |
| SF3A2 | Intact, Biogrid | true |
| SF3B1 | Biogrid, Opencell | true |
| SF3B2 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
