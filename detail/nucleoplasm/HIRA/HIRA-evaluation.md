---
type: protein-evaluation
gene: "HIRA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HIRA — REJECTED (研究热度过高 (PubMed strict=217，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HIRA / DGCR1, HIR, TUPLE1 |
| 蛋白名称 | Protein HIRA |
| 蛋白大小 | 1017 aa / 111.8 kDa |
| UniProt ID | P54198 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, PML body |
| 蛋白大小 | 8/10 | ×1 | 8 | 1017 aa / 111.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=217 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=74.4; PDB: 2I32, 5YJE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR055410, IPR031120, IPR011494, IPR015943, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- extracellular exosome (GO:0070062)
- HIR complex (GO:0000417)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 217 |
| PubMed broad count | 2483 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DGCR1, HIR, TUPLE1 |

**关键文献**:
1. Initiation of Parental Genome Reprogramming in Fertilized Oocyte by Splicing Kinase SRPK1-Catalyzed Protamine Phosphorylation.. *Cell*. PMID: 32169215
2. Histone chaperone HIRA, promyelocytic leukemia protein, and p62/SQSTM1 coordinate to regulate inflammation during cell senescence.. *Molecular cell*. PMID: 39178863
3. ATAD2 mediates chromatin-bound histone chaperone turnover.. *eLife*. PMID: 41557467
4. Multi-omics Analysis to Identify Key Immune Genes for Osteoporosis based on Machine Learning and Single-cell Analysis.. *Orthopaedic surgery*. PMID: 39238187
5. HIRA protects telomeres against R-loop-induced instability in ALT cancer cells.. *Cell reports*. PMID: 39509271

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.4 |
| 高置信度残基 (pLDDT>90) 占比 | 51.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 26.6% |
| 有序区域 (pLDDT>70) 占比 | 65.1% |
| 可用 PDB 条目 | 2I32, 5YJE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2I32, 5YJE）+ AlphaFold高质量预测（pLDDT=74.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055410, IPR031120, IPR011494, IPR015943, IPR036322; Pfam: PF24105, PF07569 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CABIN1 | 0.999 | 0.835 | — |
| ASF1A | 0.999 | 0.997 | — |
| UBN1 | 0.999 | 0.866 | — |
| ASF1B | 0.986 | 0.965 | — |
| H3-3B | 0.932 | 0.873 | — |
| UBN2 | 0.881 | 0.763 | — |
| HIRIP3 | 0.867 | 0.292 | — |
| DGCR2 | 0.863 | 0.000 | — |
| ZNF74 | 0.783 | 0.058 | — |
| SMTN | 0.763 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UPF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| ASF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14470|pubmed:16537536 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| H3-3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12180|pubmed:19410545 |
| Fas2 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| Pou5f1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20362542|imex:IM-16970 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| IRF2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PPIB | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.4 + PDB: 2I32, 5YJE | pLDDT=74.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HIRA — Protein HIRA，研究基础较多，新颖性有限。
2. 蛋白大小1017 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 217 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 217 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54198
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100084-HIRA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HIRA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54198
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000100084-HIRA/subcellular

![](https://images.proteinatlas.org/52902/2267_G11_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/52902/2267_G11_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/39243/651_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/39243/651_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/39243/652_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/39243/652_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P54198-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
