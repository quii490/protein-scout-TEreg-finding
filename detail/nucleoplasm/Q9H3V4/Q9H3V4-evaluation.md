---
type: protein-evaluation
gene: "Q9H3V4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## Q9H3V4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | Q9H3V4 |
| 蛋白名称 | Ad4BP |
| 蛋白大小 | 34 aa / 3.9 kDa |
| UniProt ID | Q9H3V4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 34 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=82.8; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | NR5-like; Znf_hrmn_rcpt; Znf_NHR/GATA |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=82.8 PDB=0
- InterPro: NR5-like; Znf_hrmn_rcpt; Znf_NHR/GATA
- Pfam: zf-C4
- PPI degree=0 ChIP: None


### 4. 总体评价
**66.7/100** | **nucleoplasm**
TE candidate: NR5-like; Znf_hrmn_rcpt; Znf_NHR/GATA


### 补充分析 (UniProt API)

**蛋白全称**: Ad4BP

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR016355 |
| InterPro | IPR001628 |
| InterPro | IPR013088 |
| Pfam | PF00105 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Ad4BP

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR016355 |
| InterPro | IPR001628 |
| InterPro | IPR013088 |
| Pfam | PF00105 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H3V4-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：Q9H3V4（Q9H3V4, Ad4BP, 34 aa / 3.9 kDa）的主要结构域注释为NR5-like, Znf_hrmn_rcpt, Znf_NHR/GATA。Pfam数据库进一步识别到zf-C4等保守域。AlphaFold pLDDT=82.8（优质）——大部分区域折叠可信，个别loop区域可能为柔性无序。该蛋白暂无实验PDB结构（PDB=0），当前结构信息完全依赖AlphaFold预测。PubMed=0（TrEMBL条目），该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=0）——当前已知互作伙伴数量有限。该蛋白的互作图谱近乎空白，future interactome studies will be critical for linking this protein to specific pathway context.

**结构解读**：AlphaFold预测（pLDDT=82.8）整体折叠可信，NR5-like构成结构核心。Pfam域zf-C4的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=82.8的整体质量表明大部分残基（pLDDT>70）处于有序构象，适合X射线晶体学或冷冻电镜（cryo-EM）解析。

**机制模型**：Q9H3V4含有nuclear hormone receptor-type锌指结构域——该类domain介导DNA binding和ligand-dependent transcriptional activation。Nuclear receptor superfamily是metazoan中最大的转录调控家族之一。特定的NR成员（如NR2C1/TR2, NR2C2/TR4）已被报道与LTR retrotransposon的hormone-responsive element相互作用——暗示Q9H3V4可能通过类似的DNA识别机制调控TE活性。

**TE调控展望**：该蛋白被标注为TE_REG_CANDIDATE——含NR5-like; Znf_hrmn_rcpt; Znf_NHR/GATA结构域。TE调控关联性取决于以下几个方面：（1）Q9H3V4是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）Q9H3V4是否能够通过其结构域识别TE-derived DNA/RNA element；（3）Q9H3V4的knockout/knockdown是否改变LINE-1或ERV family的expression level。建议通过affinity purification-MS鉴定Q9H3V4在核内的完整interactome——尤其是chromatin reader/writer/eraser复合体的成员。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/Q9H3V4
