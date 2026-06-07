---
type: protein-evaluation
gene: "STAT3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAT3 — REJECTED (研究热度过高 (PubMed strict=21537，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAT3 / APRF |
| 蛋白名称 | Signal transducer and activator of transcription 3 |
| 蛋白大小 | 770 aa / 88.1 kDa |
| UniProt ID | P40763 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 770 aa / 88.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=21537 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.9; PDB: 5AX3, 5U5S, 6NJS, 6NUQ, 6QHD, 6TLC |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- mitochondrial inner membrane (GO:0005743)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21537 |
| PubMed broad count | 44739 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APRF |

**关键文献**:
1. Nmi interacts with Hsp105β and enhances the Hsp105β-mediated Hsp70 expression.. *Experimental cell research*. PMID: 25088258
2. Targeting the JAK2-STAT3-UCHL3-ENO1 axis suppresses glycolysis and enhances the sensitivity to 5-FU chemotherapy in TP53-mutant colorectal cancer.. *Acta pharmaceutica Sinica. B*. PMID: 40487654
3. Stat3 and CCAAT enhancer-binding protein β (C/ebpβ) activate Fanconi C gene transcription during emergency granulopoiesis.. *The Journal of biological chemistry*. PMID: 29382715
4. Non-canonical STAT3 function reduces REDD1 transcription.. *The FEBS journal*. PMID: 36380685
5. Gene signature-guided isolation identifies cucurbitacins as STAT3 inhibitors from Picria fel-terrae Lour.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 40505486

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.9 |
| 高置信度残基 (pLDDT>90) 占比 | 67.7% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 10.4% |
| 有序区域 (pLDDT>70) 占比 | 82.9% |
| 可用 PDB 条目 | 5AX3, 5U5S, 6NJS, 6NUQ, 6QHD, 6TLC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5AX3, 5U5S, 6NJS, 6NUQ, 6QHD, 6TLC）+ AlphaFold极高置信度预测（pLDDT=84.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR035855; Pfam: PF00017, PF01017, PF02864 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JAK1 | 0.999 | 0.839 | — |
| JAK2 | 0.999 | 0.885 | — |
| STAT1 | 0.999 | 0.874 | — |
| PIAS3 | 0.999 | 0.808 | — |
| SRC | 0.999 | 0.841 | — |
| EP300 | 0.999 | 0.856 | — |
| EGFR | 0.998 | 0.925 | — |
| STAT5B | 0.998 | 0.387 | — |
| JAK3 | 0.998 | 0.472 | — |
| TYK2 | 0.997 | 0.285 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.9 + PDB: 5AX3, 5U5S, 6NJS, 6NUQ, 6QHD,  | pLDDT=84.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. STAT3 — Signal transducer and activator of transcription 3，研究基础较多，新颖性有限。
2. 蛋白大小770 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21537 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 21537 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P40763
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168610-STAT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P40763
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000168610-STAT3/subcellular

![](https://images.proteinatlas.org/1671/26_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1671/26_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1671/27_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1671/27_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1671/28_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1671/28_H3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P40763-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P40763 |
| SMART | SM00964; |
| UniProt Domain [FT] | DOMAIN 580..670; /note="SH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00191" |
| InterPro | IPR008967;IPR000980;IPR036860;IPR001217;IPR035855;IPR048988;IPR036535;IPR013800;IPR015988;IPR013801;IPR012345;IPR013799; |
| Pfam | PF00017;PF01017;PF02864;PF02865;PF21354; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168610-STAT3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCKDK | Intact, Biogrid | true |
| BICD1 | Intact, Biogrid | true |
| BMX | Intact, Biogrid | true |
| CAPN1 | Intact, Biogrid | true |
| CORO1A | Intact, Biogrid | true |
| ECH1 | Intact, Biogrid | true |
| EGFR | Intact, Biogrid | true |
| ERBB2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
