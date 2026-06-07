---
type: protein-evaluation
gene: "TRIM35"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM35 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM35 / HLS5, KIAA1098 |
| 蛋白名称 | E3 ubiquitin-protein ligase TRIM35 |
| 蛋白大小 | 493 aa / 56.5 kDa |
| UniProt ID | Q9UPQ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 493 aa / 56.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 52 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HLS5, KIAA1098 |

**关键文献**:
1. TRIM35 triggers cardiac remodeling by regulating SLC7A5-mediated amino acid transport and mTORC1 activation in fibroblasts.. *Cell communication and signaling : CCS*. PMID: 39304904
2. TRIM35, a novel DNA-binding protein, epigenetically modifies H3 to promote HSPA6 transcription and suppress breast cancer progression.. *Cell death discovery*. PMID: 41136372
3. Inhibition of human adenovirus replication by TRIM35-mediated degradation of E1A.. *Journal of virology*. PMID: 37578239
4. TRIM35 Negatively Regulates the cGAS-STING-Mediated Signaling Pathway by Attenuating K63-Linked Ubiquitination of STING.. *Inflammation*. PMID: 39088122
5. The upregulation of miR-3945 in CD14+ monocytes is the risk factor for cardiovascular disease.. *Journal of biochemical and molecular toxicology*. PMID: 37702194

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.3 |
| 高置信度残基 (pLDDT>90) 占比 | 69.4% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 5.5% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.3，有序区 91.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006574; Pfam: PF13765, PF00622, PF00643 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| QARS1 | 0.619 | 0.614 | — |
| PIAS1 | 0.602 | 0.226 | — |
| TRIM10 | 0.597 | 0.563 | — |
| TRIM32 | 0.589 | 0.000 | — |
| CCDC27 | 0.581 | 0.000 | — |
| STAT1 | 0.537 | 0.000 | — |
| TRIM55 | 0.533 | 0.230 | — |
| PKM | 0.501 | 0.292 | — |
| TRIM66 | 0.471 | 0.000 | — |
| TRIM44 | 0.449 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBE2U | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| Ezh2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| HIP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| TSG101 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2W | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| Jarid2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12118|pubmed:20064376 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.3 + PDB: 无 | pLDDT=88.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRIM35 — E3 ubiquitin-protein ligase TRIM35，非常新颖，仅有少数基础研究。
2. 蛋白大小493 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPQ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104228-TRIM35/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM35
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPQ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104228-TRIM35/subcellular

![](https://images.proteinatlas.org/19647/183_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/19647/183_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/19647/185_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/19647/185_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/19647/242_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/19647/242_C5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPQ4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPQ4 |
| SMART | SM00336;SM00589;SM00184;SM00449; |
| UniProt Domain [FT] | DOMAIN 284..487; /note="B30.2/SPRY"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00548" |
| InterPro | IPR001870;IPR043136;IPR003879;IPR013320;IPR006574;IPR003877;IPR050143;IPR027370;IPR000315;IPR001841;IPR013083;IPR017907; |
| Pfam | PF13765;PF00622;PF00643;PF13445; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104228-TRIM35/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARAP3 | Bioplex | false |
| CDC42BPB | Bioplex | false |
| DIS3 | Bioplex | false |
| DNAAF5 | Bioplex | false |
| EIF2AK2 | Bioplex | false |
| NAB2 | Bioplex | false |
| OXSR1 | Bioplex | false |
| PDXDC1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
