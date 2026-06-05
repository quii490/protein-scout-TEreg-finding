---
type: protein-evaluation
gene: "STEAP3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STEAP3 — REJECTED (研究热度过高 (PubMed strict=129，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STEAP3 / TSAP6 |
| 蛋白名称 | Metalloreductase STEAP3 |
| 蛋白大小 | 488 aa / 54.6 kDa |
| UniProt ID | Q658P3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoli; UniProt: Endosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 488 aa / 54.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=129 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=89.2; PDB: 2VNS, 2VQ3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013130, IPR036291, IPR028939, IPR051267; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Approved |
| UniProt | Endosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endosome (GO:0005768)
- endosome membrane (GO:0010008)
- multivesicular body (GO:0005771)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 129 |
| PubMed broad count | 226 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TSAP6 |

**关键文献**:
1. Hypoxia-induced lncRNA STEAP3-AS1 activates Wnt/β-catenin signaling to promote colorectal cancer progression by preventing m(6)A-mediated degradation of STEAP3 mRNA.. *Molecular cancer*. PMID: 35986274
2. Ferroptosis regulates hemolysis in stored murine and human red blood cells.. *Blood*. PMID: 39541586
3. The LncRNA STEAP3-AS1 promotes liver metastasis in colorectal cancer by regulating histone lactylation through chromatin remodelling.. *Journal of experimental & clinical cancer research : CR*. PMID: 40665344
4. Liver iron transport.. *World journal of gastroenterology*. PMID: 17729394
5. Silencing of STEAP3 suppresses cervical cancer cell proliferation and migration via JAK/STAT3 signaling pathway.. *Cancer & metabolism*. PMID: 39736751

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.2 |
| 高置信度残基 (pLDDT>90) 占比 | 81.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 8.6% |
| 有序区域 (pLDDT>70) 占比 | 89.2% |
| 可用 PDB 条目 | 2VNS, 2VQ3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2VNS, 2VQ3）+ AlphaFold高质量预测（pLDDT=89.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013130, IPR036291, IPR028939, IPR051267; Pfam: PF03807, PF01794 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BNIP3L | 0.983 | 0.292 | — |
| PKMYT1 | 0.933 | 0.292 | — |
| TPT1 | 0.891 | 0.000 | — |
| TP53 | 0.856 | 0.000 | — |
| TFRC | 0.832 | 0.000 | — |
| SLC11A2 | 0.804 | 0.000 | — |
| CYBRD1 | 0.783 | 0.000 | — |
| SLC40A1 | 0.690 | 0.000 | — |
| RPS6KB2 | 0.668 | 0.000 | — |
| ACO1 | 0.659 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SETD7 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| BAD | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TTC21A | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PGRMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27599036|imex:IM-25485 |
| PGRMC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27599036|imex:IM-25485 |
| DPEP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TIGD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.2 + PDB: 2VNS, 2VQ3 | pLDDT=89.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endosome membrane / Cytosol; 额外: Nucleoli | 一致 |
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
1. STEAP3 — Metalloreductase STEAP3，研究基础较多，新颖性有限。
2. 蛋白大小488 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 129 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 129 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q658P3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115107-STEAP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STEAP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q658P3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000115107-STEAP3/subcellular

![](https://images.proteinatlas.org/50510/771_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50510/771_G11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50510/979_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50510/979_E10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q658P3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
