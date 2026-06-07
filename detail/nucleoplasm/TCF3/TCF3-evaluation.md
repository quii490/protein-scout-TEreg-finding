---
type: protein-evaluation
gene: "TCF3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TCF3 — REJECTED (研究热度过高 (PubMed strict=532，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCF3 / TCF3 |
| 蛋白名称 | Transcription factor 7-like 1 |
| 蛋白大小 | 588 aa / 62.6 kDa |
| UniProt ID | Q9HCS4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 588 aa / 62.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=532 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027397, IPR013558, IPR009071, IPR036910, IPR024 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- beta-catenin-TCF complex (GO:1990907)
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 532 |
| PubMed broad count | 1138 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCF3 |

**关键文献**:
1. Emerging molecular subtypes and therapies in acute lymphoblastic leukemia.. *Seminars in diagnostic pathology*. PMID: 37120350
2. Whole-transcriptome analysis in acute lymphoblastic leukemia: a report from the DFCI ALL Consortium Protocol 16-001.. *Blood advances*. PMID: 34933343
3. Burkitt lymphoma pathogenesis and therapeutic targets from structural and functional genomics.. *Nature*. PMID: 22885699
4. Mapping putative enhancers in mouse oocytes and early embryos reveals TCF3/12 as key folliculogenesis regulators.. *Nature cell biology*. PMID: 38839978
5. YBX1 as a therapeutic target to suppress the LRP1-β-catenin-RRM1 axis and overcome gemcitabine resistance in pancreatic cancer.. *Cancer letters*. PMID: 39216548

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.8 |
| 高置信度残基 (pLDDT>90) 占比 | 9.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 20.6% |
| 低置信 (pLDDT<50) 占比 | 64.8% |
| 有序区域 (pLDDT>70) 占比 | 14.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.8），有序残基占 14.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027397, IPR013558, IPR009071, IPR036910, IPR024940; Pfam: PF08347, PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TAL1 | 0.999 | 0.860 | — |
| LDB1 | 0.997 | 0.294 | — |
| LMO2 | 0.996 | 0.090 | — |
| LYL1 | 0.996 | 0.393 | — |
| GATA1 | 0.995 | 0.000 | — |
| MYOD1 | 0.993 | 0.795 | — |
| LDB2 | 0.992 | 0.045 | — |
| ID2 | 0.987 | 0.905 | — |
| RUNX1 | 0.975 | 0.292 | — |
| ID1 | 0.973 | 0.898 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000262965.5 | psi-mi:"MI:0096"(pull down) | pubmed:10915743|imex:IM-19434 |
| ENSP00000468487.1 | psi-mi:"MI:0096"(pull down) | pubmed:9409784 |
| Hand1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10924525 |
| Hand2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10924525 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| RPL37 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RUVBL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| RUVBL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| RUNX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12146|pubmed:18772112 |
| TAL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9824680 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.8 + PDB: 无 | pLDDT=51.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TCF3 — Transcription factor 7-like 1，研究基础较多，新颖性有限。
2. 蛋白大小588 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 532 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=51.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 532 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCS4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000071564-TCF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCS4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HCS4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000071564-TCF3/subcellular

![](https://images.proteinatlas.org/18351/962_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/18351/962_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/18351/970_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/18351/970_G4_3_red_green.jpg)
![](https://images.proteinatlas.org/62476/1106_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/62476/1106_B11_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HCS4 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027397;IPR013558;IPR009071;IPR036910;IPR024940; |
| Pfam | PF08347;PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000071564-TCF3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASCL1 | Intact, Biogrid | true |
| ID2 | Intact, Biogrid | true |
| ID3 | Intact, Biogrid | true |
| TAL1 | Intact, Biogrid | true |
| ASCL3 | Biogrid | false |
| BHLHE40 | Biogrid | false |
| CBFA2T3 | Biogrid | false |
| CREBBP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
