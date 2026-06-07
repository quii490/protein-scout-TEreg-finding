---
type: protein-evaluation
gene: "KANK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KANK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KANK1 / ANKRD15, KANK, KIAA0172 |
| 蛋白名称 | KN motif and ankyrin repeat domain-containing protein 1 |
| 蛋白大小 | 1352 aa / 147.3 kDa |
| UniProt ID | Q14678 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; UniProt: Cytoplasm, cell cortex; Cell projection, ruffle membrane; Cy |
| 蛋白大小 | 5/10 | ×1 | 5 | 1352 aa / 147.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.0; PDB: 5YBJ, 5YBU, 8AS9, 8IVZ, 8IW0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR047184, IPR021939; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.5/180** | |
| **归一化总分** | | | **48.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Supported |
| UniProt | Cytoplasm, cell cortex; Cell projection, ruffle membrane; Cytoplasm; Nucleus; Cytoplasm; Nucleus; Cy... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- ruffle membrane (GO:0032587)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 152 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANKRD15, KANK, KIAA0172 |

**关键文献**:
1. KANK family proteins in cancer.. *The international journal of biochemistry & cell biology*. PMID: 33309958
2. Genome-wide identification of the genetic basis of amyotrophic lateral sclerosis.. *Neuron*. PMID: 35045337
3. Potential involvement of KANK1 haploinsufficiency in centrosome aberrations.. *Biochimica et biophysica acta. General subjects*. PMID: 38830559
4. Identification of KANK1 as a tumor suppressor gene in pancreatic ductal adenocarcinoma.. *Biochemical and biophysical research communications*. PMID: 40288262
5. KANK1 shapes focal adhesions by orchestrating protein binding, mechanical force sensing, and phase separation.. *Cell reports*. PMID: 37874676

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.0 |
| 高置信度残基 (pLDDT>90) 占比 | 18.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 62.4% |
| 有序区域 (pLDDT>70) 占比 | 32.4% |
| 可用 PDB 条目 | 5YBJ, 5YBU, 8AS9, 8IVZ, 8IW0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.0），有序残基占 32.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR047184, IPR021939; Pfam: PF12796, PF12075 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KIF21A | 0.995 | 0.970 | — |
| TLN1 | 0.979 | 0.042 | — |
| TLN2 | 0.977 | 0.042 | — |
| DOCK8 | 0.935 | 0.000 | — |
| DMRT1 | 0.916 | 0.044 | — |
| EIF4A1 | 0.900 | 0.900 | — |
| PHLDB2 | 0.894 | 0.000 | — |
| ERC1 | 0.816 | 0.064 | — |
| AP4M1 | 0.796 | 0.000 | — |
| CXXC5 | 0.784 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| EPB41L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| H1-1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| PIP4K2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIF21A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PPFIBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLCD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.0 + PDB: 5YBJ, 5YBU, 8AS9, 8IVZ, 8IW0 | pLDDT=54.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cell cortex; Cell projection, ruffle me / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. KANK1 — KN motif and ankyrin repeat domain-containing protein 1，研究基础较多，新颖性有限。
2. 蛋白大小1352 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14678
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107104-KANK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KANK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14678
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000107104-KANK1/subcellular

![](https://images.proteinatlas.org/56090/1041_F1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/56090/1041_F1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/56090/1144_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/56090/1144_B2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/56090/996_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/56090/996_F1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14678-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14678 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770;IPR047184;IPR021939; |
| Pfam | PF12796;PF12075; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000107104-KANK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNLL1 | Biogrid, Opencell | true |
| DYNLL2 | Biogrid, Opencell | true |
| YWHAQ | Intact, Biogrid | true |
| ARFGEF1 | Intact | false |
| BAIAP2 | Intact | false |
| CA10 | Bioplex | false |
| EDC3 | Bioplex | false |
| KIF21A | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
