---
type: protein-evaluation
gene: "CTCF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTCF — REJECTED (研究热度过高 (PubMed strict=2536，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTCF |
| 蛋白名称 | Transcriptional repressor CTCF |
| 蛋白大小 | 727 aa / 82.8 kDa |
| UniProt ID | P49711 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, nucleoplasm; Chromosome; Chromosome, centromere |
| 蛋白大小 | 10/10 | ×1 | 10 | 727 aa / 82.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2536 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.8; PDB: 1X6H, 2CT1, 5K5H, 5K5I, 5K5J, 5K5L, 5KKQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050331, IPR056438, IPR036236, IPR013087; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus, nucleoplasm; Chromosome; Chromosome, centromere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, centromeric region (GO:0000775)
- condensed chromosome (GO:0000793)
- male germ cell nucleus (GO:0001673)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2536 |
| PubMed broad count | 3525 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. G-quadruplexes associated with R-loops promote CTCF binding.. *Molecular cell*. PMID: 37552993
2. YY1 Is a Structural Regulator of Enhancer-Promoter Loops.. *Cell*. PMID: 29224777
3. MYC reshapes CTCF-mediated chromatin architecture in prostate cancer.. *Nature communications*. PMID: 36997534
4. RNA-binding proteins mediate the maturation of chromatin topology during differentiation.. *Nature cell biology*. PMID: 40921733
5. Members of an array of zinc-finger proteins specify distinct Hox chromatin boundaries.. *Molecular cell*. PMID: 39173638

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.8% |
| 置信残基 (pLDDT 70-90) 占比 | 41.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 51.6% |
| 有序区域 (pLDDT>70) 占比 | 42.1% |
| 可用 PDB 条目 | 1X6H, 2CT1, 5K5H, 5K5I, 5K5J, 5K5L, 5KKQ, 5T00, 5T0U, 5UND |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.8），有序残基占 42.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050331, IPR056438, IPR036236, IPR013087; Pfam: PF00096, PF23611 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAD21 | 0.999 | 0.603 | — |
| YY1 | 0.991 | 0.299 | — |
| SMC3 | 0.989 | 0.310 | — |
| SUZ12 | 0.987 | 0.651 | — |
| STAG2 | 0.983 | 0.602 | — |
| NPM1 | 0.975 | 0.714 | — |
| SMC1A | 0.963 | 0.522 | — |
| EP300 | 0.959 | 0.330 | — |
| POU5F1 | 0.955 | 0.310 | — |
| CHD8 | 0.944 | 0.337 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-932806 | psi-mi:"MI:0096"(pull down) | pubmed:10734189|imex:IM-19405 |
| ENSMUSP00000005841.10 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| EBI-466743 | psi-mi:"MI:0809"(bimolecular fluorescence compleme | doi:10.1016/j.celrep.2019.03.0 |
| PGAP5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Orc4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| enok | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Vamp7 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Xpac | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Dmel\CG7236 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Dmel\CG13373 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.8 + PDB: 1X6H, 2CT1, 5K5H, 5K5I, 5K5J,  | pLDDT=58.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Chromosome; Chromosome, cent / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CTCF — Transcriptional repressor CTCF，研究基础较多，新颖性有限。
2. 蛋白大小727 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2536 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2536 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49711
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102974-CTCF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTCF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49711
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000102974-CTCF/subcellular

![](https://images.proteinatlas.org/4122/110_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/4122/110_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/4122/111_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/4122/111_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/4122/159_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/4122/159_A2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49711-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P49711 |
| SMART | SM00355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050331;IPR056438;IPR036236;IPR013087; |
| Pfam | PF00096;PF23611; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102974-CTCF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHD8 | Intact, Biogrid | true |
| DHX9 | Biogrid, Opencell | true |
| HDLBP | Intact, Biogrid | true |
| ILF3 | Biogrid, Opencell | true |
| MRPS22 | Biogrid, Opencell | true |
| MRPS27 | Biogrid, Opencell, Bioplex | true |
| MRPS34 | Biogrid, Opencell, Bioplex | true |
| NCL | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
