---
type: protein-evaluation
gene: "SDE2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SDE2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SDE2 / C1orf55 |
| 蛋白名称 | Splicing regulator SDE2 |
| 蛋白大小 | 451 aa / 49.7 kDa |
| UniProt ID | Q6IQ49 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Golgi apparatus, Plasma membrane, Cyto; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 451 aa / 49.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.2; PDB: 6QDV, 7N99, 8C6J, 8RO2, 9FMD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051421, IPR053822, IPR025086, IPR053821; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Golgi apparatus, Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- mitochondrion (GO:0005739)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf55 |

**关键文献**:
1. Intron specificity in pre-mRNA splicing.. *Current genetics*. PMID: 29299619
2. SDE2 integrates into the TIMELESS-TIPIN complex to protect stalled replication forks.. *Nature communications*. PMID: 33127907
3. SDE2 is an essential gene required for ribosome biogenesis and the regulation of alternative splicing.. *Nucleic acids research*. PMID: 34365507
4. Sde2: a novel nuclear protein essential for telomeric silencing and genomic stability in Schizosaccharomyces pombe.. *Biochemical and biophysical research communications*. PMID: 21333630
5. Sde2 is an intron-specific pre-mRNA splicing regulator activated by ubiquitin-like processing.. *The EMBO journal*. PMID: 28947618

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.2 |
| 高置信度残基 (pLDDT>90) 占比 | 20.0% |
| 置信残基 (pLDDT 70-90) 占比 | 29.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 41.7% |
| 有序区域 (pLDDT>70) 占比 | 49.9% |
| 可用 PDB 条目 | 6QDV, 7N99, 8C6J, 8RO2, 9FMD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.2），有序残基占 49.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051421, IPR053822, IPR025086, IPR053821; Pfam: PF22782, PF13297, PF22781 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC40 | 0.980 | 0.845 | — |
| SLU7 | 0.979 | 0.811 | — |
| SYF2 | 0.963 | 0.822 | — |
| PPIL1 | 0.958 | 0.800 | — |
| CDC5L | 0.940 | 0.822 | — |
| CACTIN | 0.915 | 0.800 | — |
| PRKRIP1 | 0.915 | 0.800 | — |
| FAM32A | 0.911 | 0.800 | — |
| PRPF19 | 0.900 | 0.856 | — |
| CWC15 | 0.897 | 0.824 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| PRKAA1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| Isy1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Wiz | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RBM8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| HNRNPA1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| SF3B4 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| GPKOW | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.2 + PDB: 6QDV, 7N99, 8C6J, 8RO2, 9FMD | pLDDT=65.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nuclear speckles; 额外: Golgi apparatus, Plasma memb | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SDE2 — Splicing regulator SDE2，非常新颖，仅有少数基础研究。
2. 蛋白大小451 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IQ49
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143751-SDE2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SDE2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IQ49
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000143751-SDE2/subcellular

![](https://images.proteinatlas.org/28467/254_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/28467/254_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/28467/291_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/28467/291_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/28467/546_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/28467/546_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6IQ49-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6IQ49 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 396..430; /note="SAP"; /evidence="ECO:0000305\|PubMed:27906959" |
| InterPro | IPR051421;IPR053822;IPR025086;IPR053821; |
| Pfam | PF22782;PF13297;PF22781; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143751-SDE2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HSPBAP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
