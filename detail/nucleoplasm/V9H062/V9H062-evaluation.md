---
type: protein-evaluation
gene: "V9H062"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## V9H062 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | V9H062 |
| 蛋白名称 | Mismatch repair protein (MSH2) mRNA, with a Q288stop mutation |
| 蛋白大小 | 287 aa / 31.7 kDa |
| UniProt ID | V9H062 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 287 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=87.6; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | DNA_mismatch_repair_MutS-lik_N; DNA_mismatch_repair_MutS_N; DNA_mmatch_repair_Mu |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=87.6 PDB=0
- InterPro: DNA_mismatch_repair_MutS-lik_N; DNA_mismatch_repair_MutS_N; DNA_mmatch_repair_MutS_con_dom
- Pfam: MutS_I; MutS_II
- PPI degree=0 ChIP: None


### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Mismatch repair protein (MSH2) mRNA, with a Q288stop mutation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007695 |
| InterPro | IPR016151 |
| InterPro | IPR007860 |
| InterPro | IPR036678 |
| Pfam | PF01624 |
| Pfam | PF05188 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Mismatch repair protein (MSH2) mRNA, with a Q288stop mutation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007695 |
| InterPro | IPR016151 |
| InterPro | IPR007860 |
| InterPro | IPR036678 |
| Pfam | PF01624 |
| Pfam | PF05188 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-V9H062-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：V9H062（V9H062, Mismatch repair protein MSH2 truncation, 287 aa / 31.7 kDa）的主要结构域注释为DNA_mismatch_repair_MutS-lik_N, DNA_mismatch_repair_MutS_N, DNA_mmatch_repair_MutS_con_dom。Pfam数据库进一步识别到MutS_I、MutS_II等保守域。AlphaFold pLDDT=87.6（优质）——大部分区域折叠可信，个别loop区域可能为柔性无序。该蛋白暂无实验PDB结构（PDB=0），当前结构信息完全依赖AlphaFold预测。PubMed=0（TrEMBL条目），该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=0）——当前已知互作伙伴数量有限。该蛋白的互作图谱近乎空白，future interactome studies will be critical for linking this protein to specific pathway context.

**结构解读**：AlphaFold预测（pLDDT=87.6）显示该蛋白具有明确的折叠结构域，其中DNA_mismatch_repair_MutS-lik_N为保守的催化/结合模块。Pfam域MutS_I、MutS_II的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=87.6的整体质量表明大部分残基（pLDDT>70）处于有序构象，适合X射线晶体学或冷冻电镜（cryo-EM）解析。

**机制模型**：V9H062（MSH2 truncation variant）为DNA mismatch repair（MMR）通路中MutS complex的部分片段——MutS识别mismatched bases和insertion/deletion loops during DNA replication。MMR通路的完整性对维持genome stability至关重要——MMR缺陷可能导致microsatellite instability（MSI）和TE element de-repression。

**TE调控展望**：V9H062的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于以下几个方面：（1）V9H062是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）V9H062是否能够通过其结构域识别TE-derived DNA/RNA element；（3）V9H062的knockout/knockdown是否改变LINE-1或ERV family的expression level。建议通过affinity purification-MS鉴定V9H062在核内的完整interactome——尤其是chromatin reader/writer/eraser复合体的成员。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/V9H062
