---
type: protein-evaluation
gene: "NVL"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NVL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NVL / NVL2 |
| 蛋白名称 | Nuclear valosin-containing protein-like |
| 蛋白大小 | 856 aa / 95.1 kDa |
| UniProt ID | O15381 |
| 评估日期 | 2026-06-04 |

**功能简介** (UniProt): Participates in the assembly of the telomerase holoenzyme and effecting of telomerase activity via its interaction with TERT (PubMed:22226966). Involved in both early and late stages of the pre-rRNA processing pathways (PubMed:26166824). Spatiotemporally regulates 60S ribosomal subunit biogenesis in the nucleolus (PubMed:15469983, PubMed:16782053, PubMed:26456651, PubMed:29107693). Catalyzes the r...

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: Nucleus, nucleoplasm; Nucleus, nucleolus; Nucleus, nucleopla |
| 蛋白大小 | 8/10 | ×1 | 8 | 856 aa / 95.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=72.5; PDB: 2X8A, 6RO1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR050168, IPR041569, IPR003959, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Enhanced |
| UniProt | Nucleus, nucleoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- telomerase holoenzyme complex (GO:0005697)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 234 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NVL2 |

**关键文献**:
1. Identification of new telomere- and telomerase-associated autoantigens in systemic sclerosis.. *Journal of autoimmunity*. PMID: 36634459
2. Brucella effectors NyxA and NyxB target SENP3 to modulate the subcellular localisation of nucleolar proteins.. *Nature communications*. PMID: 36609656
3. Development of an enzyme-linked immunosorbent assay for the efficient detection of autoantibodies against nuclear valosin-containing protein-like protein (NVL) 2 using its manipulated cDNA.. *RMD open*. PMID: 40780730
4. The NVL gene confers risk for both major depressive disorder and schizophrenia in the Han Chinese population.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 25891250
5. Effects of hypertonic alkaline nasal irrigation on COVID-19.. *Laryngoscope investigative otolaryngology*. PMID: 34909468

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.5 |
| 高置信度残基 (pLDDT>90) 占比 | 19.0% |
| 置信残基 (pLDDT 70-90) 占比 | 49.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 22.1% |
| 有序区域 (pLDDT>70) 占比 | 68.9% |
| 可用 PDB 条目 | 2X8A, 6RO1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2X8A, 6RO1）+ AlphaFold高质量预测（pLDDT=72.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR050168, IPR041569, IPR003959, IPR003960; Pfam: PF00004, PF17862, PF16725 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTREX | 0.983 | 0.900 | — |
| TERT | 0.944 | 0.000 | — |
| GNL3L | 0.938 | 0.085 | — |
| DKC1 | 0.934 | 0.000 | — |
| NHP2 | 0.920 | 0.100 | — |
| GAR1 | 0.917 | 0.000 | — |
| NOP10 | 0.914 | 0.000 | — |
| TEP1 | 0.910 | 0.088 | — |
| NOM1 | 0.906 | 0.000 | — |
| WRAP53 | 0.906 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%，尚无实验验证互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.5 + PDB: 2X8A, 6RO1 | pLDDT=72.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, nucleolus; Nucleus, / Nucleoli | 一致 |
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
1. NVL — Nuclear valosin-containing protein-like，非常新颖，仅有少数基础研究。
2. 蛋白大小856 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15381
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143748-NVL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NVL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15381
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live via harvest pipeline; evaluated 2026-06-04

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000143748-NVL/subcellular

![](https://images.proteinatlas.org/28219/1176_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/28219/1176_B1_3_red_green.jpg)
![](https://images.proteinatlas.org/28219/1281_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/28219/1281_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/28219/1313_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/28219/1313_D12_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15381-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
