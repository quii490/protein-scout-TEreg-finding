---
type: protein-evaluation
gene: "MPO"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MPO — REJECTED (研究热度过高 (PubMed strict=6096，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MPO |
| 蛋白名称 | Myeloperoxidase |
| 蛋白大小 | 745 aa / 83.9 kDa |
| UniProt ID | P05164 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Lysosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 745 aa / 83.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=6096 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.0; PDB: 1CXP, 1D2V, 1D5L, 1D7W, 1DNU, 1DNW, 1MHL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019791, IPR010255, IPR037120; Pfam: PF03098 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Supported |
| UniProt | Lysosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- azurophil granule (GO:0042582)
- azurophil granule lumen (GO:0035578)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- lysosome (GO:0005764)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6096 |
| PubMed broad count | 19894 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Myeloperoxidase transforms chromatin into neutrophil extracellular traps.. *Nature*. PMID: 40963017
2. Myeloperoxidase Deficiency.. **. PMID: 29262241
3. Biosynthesis of human myeloperoxidase.. *Archives of biochemistry and biophysics*. PMID: 29408362
4. Myeloperoxidase-Associated Membranous Nephropathy in Antineutrophil Cytoplasmic Antibody-Associated Glomerulonephritis.. *Kidney international reports*. PMID: 39081744
5. Myeloperoxidase deficiency.. *Hematology/oncology clinics of North America*. PMID: 2831185

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.0 |
| 高置信度残基 (pLDDT>90) 占比 | 75.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 90.0% |
| 可用 PDB 条目 | 1CXP, 1D2V, 1D5L, 1D7W, 1DNU, 1DNW, 1MHL, 1MYP, 3F9P, 3ZS0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1CXP, 1D2V, 1D5L, 1D7W, 1DNU, 1DNW, 1MHL, 1MYP, 3F9P, 3ZS0）+ AlphaFold极高置信度预测（pLDDT=89.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019791, IPR010255, IPR037120; Pfam: PF03098 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AZU1 | 0.999 | 0.000 | — |
| PRTN3 | 0.999 | 0.331 | — |
| ELANE | 0.999 | 0.164 | — |
| CTSG | 0.999 | 0.044 | — |
| LTF | 0.998 | 0.228 | — |
| BPI | 0.995 | 0.000 | — |
| CAMP | 0.982 | 0.000 | — |
| MMP9 | 0.969 | 0.000 | — |
| CP | 0.965 | 0.900 | — |
| CTSS | 0.964 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRDX1 | psi-mi:"MI:0979"(oxidoreductase assay) | pubmed:23386615|imex:IM-23209 |
| GPX1 | psi-mi:"MI:0979"(oxidoreductase assay) | pubmed:25670081|imex:IM-24179 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| P/V/C | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CCDC47 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPK | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SLC4A1 | psi-mi:"MI:0047"(far western blotting) | pubmed:26714302|imex:IM-27606 |
| GYPB | psi-mi:"MI:0047"(far western blotting) | pubmed:26714302|imex:IM-27606 |
| GYPA | psi-mi:"MI:0047"(far western blotting) | pubmed:26714302|imex:IM-27606 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.0 + PDB: 1CXP, 1D2V, 1D5L, 1D7W, 1DNU,  | pLDDT=89.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lysosome / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. MPO — Myeloperoxidase，研究基础较多，新颖性有限。
2. 蛋白大小745 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6096 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 6096 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P05164
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005381-MPO/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MPO
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P05164
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000005381-MPO/subcellular

![](https://images.proteinatlas.org/61464/1398_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/61464/1398_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/61464/1403_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/61464/1403_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/61464/1487_B11_3_red_green.jpg)
![](https://images.proteinatlas.org/61464/1487_B11_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P05164-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P05164 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019791;IPR010255;IPR037120; |
| Pfam | PF03098; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000005381-MPO/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CALR | Intact | false |
| CFP | Intact | false |
| HNRNPK | Biogrid | false |
| STUB1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
