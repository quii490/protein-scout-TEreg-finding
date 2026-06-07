---
type: protein-evaluation
gene: "TFDP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TFDP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFDP2 / DP2 |
| 蛋白名称 | Transcription factor Dp-2 |
| 蛋白大小 | 446 aa / 49.2 kDa |
| UniProt ID | Q14188 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Mitotic spindle; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 446 aa / 49.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.2; PDB: 1CF7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037241, IPR003316, IPR038168, IPR014889, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Mitotic spindle | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- mitotic spindle (GO:0072686)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DP2 |

**关键文献**:
1. NetSig: network-based discovery from cancer genomes.. *Nature methods*. PMID: 29200198
2. Global analysis of induced transcription factors and cofactors identifies Tfdp2 as an essential coregulator during terminal erythropoiesis.. *Experimental hematology*. PMID: 24607859
3. The C/EBPβ-Dependent Induction of TFDP2 Facilitates Porcine Reproductive and Respiratory Syndrome Virus Proliferation.. *Virologica Sinica*. PMID: 34138404
4. The novel miR_146-Tfdp2 axis antagonizes METH induced neuron apoptosis and cell cycle abnormalities in tree shrew.. *Neuropharmacology*. PMID: 39793695
5. TFDP3 as E2F Unique Partner, Has Crucial Roles in Cancer Cells and Testis.. *Frontiers in oncology*. PMID: 34745961

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.2 |
| 高置信度残基 (pLDDT>90) 占比 | 38.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 43.5% |
| 有序区域 (pLDDT>70) 占比 | 49.5% |
| 可用 PDB 条目 | 1CF7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.2），有序残基占 49.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037241, IPR003316, IPR038168, IPR014889, IPR015648; Pfam: PF08781, PF02319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| E2F4 | 0.999 | 0.990 | — |
| E2F1 | 0.997 | 0.893 | — |
| E2F6 | 0.996 | 0.930 | — |
| E2F5 | 0.993 | 0.800 | — |
| RB1 | 0.987 | 0.834 | — |
| RBL2 | 0.983 | 0.768 | — |
| RBL1 | 0.982 | 0.771 | — |
| E2F2 | 0.982 | 0.835 | — |
| E2F3 | 0.976 | 0.687 | — |
| TFDP1 | 0.927 | 0.229 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| E2F6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RBL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17531812 |
| LIN9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| LIN37 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| LIN54 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| E2f4 | psi-mi:"MI:0096"(pull down) | pubmed:20946988|imex:IM-15160 |
| RB1 | psi-mi:"MI:0096"(pull down) | pubmed:16360038|imex:IM-20931 |
| PCGF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| E2F3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.2 + PDB: 1CF7 | pLDDT=65.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles, Mitotic spindle | 一致 |
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
1. TFDP2 — Transcription factor Dp-2，非常新颖，仅有少数基础研究。
2. 蛋白大小446 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14188
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114126-TFDP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFDP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14188
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000114126-TFDP2/subcellular

![](https://images.proteinatlas.org/18396/924_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/18396/924_A6_3_red_green.jpg)
![](https://images.proteinatlas.org/18396/932_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/18396/932_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/18396/971_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/18396/971_A6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14188-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14188 |
| SMART | SM01138;SM01372; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037241;IPR003316;IPR038168;IPR014889;IPR015648;IPR036388;IPR036390; |
| Pfam | PF08781;PF02319; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000114126-TFDP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| E2F4 | Intact, Biogrid | true |
| E2F6 | Intact, Biogrid | true |
| RB1 | Intact, Biogrid | true |
| E2F1 | Biogrid | false |
| L3MBTL2 | Biogrid | false |
| LIN37 | Biogrid | false |
| LIN54 | Biogrid | false |
| LIN9 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
