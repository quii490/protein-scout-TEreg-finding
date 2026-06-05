---
type: protein-evaluation
gene: "RTCB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RTCB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RTCB / C22orf28 |
| 蛋白名称 | RNA-splicing ligase RTCB |
| 蛋白大小 | 505 aa / 55.2 kDa |
| UniProt ID | Q9Y3I0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 505 aa / 55.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=61 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.4; PDB: 7P3B, 8BTT, 8ODO, 8ODP, 8ORJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001233, IPR036025, IPR027513; Pfam: PF01139 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- catalytic complex (GO:1902494)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- nuclear envelope (GO:0005635)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- tRNA-splicing ligase complex (GO:0072669)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed broad count | 112 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C22orf28 |

**关键文献**:
1. Highly efficient expression of circular RNA aptamers in cells using autocatalytic transcripts.. *Nature biotechnology*. PMID: 30962542
2. An RNA splicing system that excises DNA transposons from animal mRNAs.. *Nature*. PMID: 41372403
3. Insights into the structure and function of the RNA ligase RtcB.. *Cellular and molecular life sciences : CMLS*. PMID: 37935993
4. Robust genome and cell engineering via in vitro and in situ circularized RNAs.. *Nature biomedical engineering*. PMID: 39187662
5. Structural and biochemical characterization of the 3'-5' tRNA splicing ligases.. *The Journal of biological chemistry*. PMID: 40220997

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.4 |
| 高置信度残基 (pLDDT>90) 占比 | 88.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.8% |
| 可用 PDB 条目 | 7P3B, 8BTT, 8ODO, 8ODP, 8ORJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7P3B, 8BTT, 8ODO, 8ODP, 8ORJ）+ AlphaFold极高置信度预测（pLDDT=95.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001233, IPR036025, IPR027513; Pfam: PF01139 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RTRAF | 0.999 | 0.840 | — |
| DDX1 | 0.999 | 0.884 | — |
| FAM98B | 0.999 | 0.835 | — |
| ZBTB8OS | 0.997 | 0.292 | — |
| C2orf49 | 0.995 | 0.834 | — |
| RTCA | 0.945 | 0.000 | — |
| FAM98A | 0.895 | 0.209 | — |
| DRG1 | 0.781 | 0.000 | — |
| HNRNPM | 0.760 | 0.374 | — |
| RCL1 | 0.734 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| hdlbp.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| dati | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| hslR | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rplC | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rpsD | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| groEL | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rppH | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| ahpC | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.4 + PDB: 7P3B, 8BTT, 8ODO, 8ODP, 8ORJ | pLDDT=95.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RTCB — RNA-splicing ligase RTCB，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 61 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3I0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100220-RTCB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RTCB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3I0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000100220-RTCB/subcellular

![](https://images.proteinatlas.org/535/169_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/535/169_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/535/170_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/535/170_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/535/171_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/535/171_F2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3I0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
