---
type: protein-evaluation
gene: "CENPB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CENPB — REJECTED (研究热度过高 (PubMed strict=299，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPB |
| 蛋白名称 | Major centromere autoantigen B |
| 蛋白大小 | 599 aa / 65.2 kDa |
| UniProt ID | P07199 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere |
| 蛋白大小 | 10/10 | ×1 | 10 | 599 aa / 65.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=299 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 1BW6, 1HLV, 1UFI, 6KDR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015115, IPR050863, IPR004875, IPR034882, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome, centromere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- chromosome, centromeric region (GO:0000775)
- condensed chromosome, centromeric region (GO:0000779)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- pericentric heterochromatin (GO:0005721)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 299 |
| PubMed broad count | 483 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Understanding and interpreting antinuclear antibody tests in systemic rheumatic diseases.. *Nature reviews. Rheumatology*. PMID: 33154583
2. FBXO38 is dispensable for PD-1 regulation.. *EMBO reports*. PMID: 39266770
3. PoxCbh, a novel CENPB-type HTH domain protein, regulates cellulase and xylanase gene expression in Penicillium oxalicum.. *Molecular microbiology*. PMID: 33561892
4. Vertebrate centromere architecture: from chromatin threads to functional structures.. *Chromosoma*. PMID: 38856923
5. CENPB promotes the proliferation of hepatocellular carcinoma and is directly regulated by miR-29a.. *Aging*. PMID: 37925172

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 19.7% |
| 置信残基 (pLDDT 70-90) 占比 | 33.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 34.6% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 1BW6, 1HLV, 1UFI, 6KDR |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 53.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015115, IPR050863, IPR004875, IPR034882, IPR009057; Pfam: PF09026, PF04218, PF03184 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPA | 0.994 | 0.510 | — |
| CENPC | 0.993 | 0.000 | — |
| CENPS | 0.973 | 0.000 | — |
| CENPH | 0.931 | 0.000 | — |
| CENPE | 0.901 | 0.000 | — |
| CENPI | 0.885 | 0.000 | — |
| CENPW | 0.866 | 0.322 | — |
| TRIM21 | 0.816 | 0.000 | — |
| CENPF | 0.812 | 0.000 | — |
| RO60 | 0.804 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GFI1B | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| TAF1D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| NR3C1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| OPTN | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| NR4A1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ETS1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| Rasd1 | psi-mi:"MI:0018"(two hybrid) | pubmed:21247419|imex:IM-16862 |
| MOV10 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PIP5K1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC59 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 1BW6, 1HLV, 1UFI, 6KDR | pLDDT=66.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere / Nuclear bodies; 额外: Nucleoplasm | 一致 |
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
1. CENPB — Major centromere autoantigen B，研究基础较多，新颖性有限。
2. 蛋白大小599 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 299 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 299 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P07199
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125817-CENPB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P07199
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (enhanced)。来源: https://www.proteinatlas.org/ENSG00000125817-CENPB/subcellular

![](https://images.proteinatlas.org/53507/1874_F11_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/53507/1874_F11_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/53507/819_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/53507/819_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/53507/826_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/53507/826_E10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P07199-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
