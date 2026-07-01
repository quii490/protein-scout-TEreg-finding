---
type: protein-evaluation
gene: "DKFZp686O111"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## DKFZp686O111 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DKFZp686O111 |
| 蛋白名称 | Uncharacterized protein DKFZp686O111 |
| 蛋白大小 | 392 aa / 45.5 kDa |
| UniProt ID | Q5CZB4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 392 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=67.4; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Zinc_finger; Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=67.4 PDB=0
- InterPro: Zinc_finger; Znf_C2H2_sf; Znf_C2H2_type
- Pfam: zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**66.7/100** | **nucleoplasm**
TE candidate: Zinc_finger; Znf_C2H2_sf; Znf_C2H2_type


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp686O111

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050331 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp686O111

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050331 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5CZB4-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：DKFZp686O111（Q5CZB4, Uncharacterized protein DKFZp686O111, 392 aa / 45.5 kDa）的主要结构域注释为Zinc_finger, Znf_C2H2_sf, Znf_C2H2_type。Pfam数据库进一步识别到zf-C2H2等保守域。AlphaFold pLDDT=67.4（中低置信度）——结构预测显示较大无序区域，可能含IDR（intrinsically disordered region）或需要结合伴侣才能有序折叠。该蛋白暂无实验PDB结构（PDB=0），当前结构信息完全依赖AlphaFold预测。PubMed=0（TrEMBL条目），该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=0）——当前已知互作伙伴数量有限。该蛋白的互作图谱近乎空白，future interactome studies will be critical for linking this protein to specific pathway context.

**结构解读**：InterPro注释到3个结构域条目——Zinc_finger、Znf_C2H2_sf、Znf_C2H2_type。Pfam域zf-C2H2的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=67.4提示存在显著的柔性区段，可能需要在蛋白互作伴侣存在的条件下才能完全折叠。

**机制模型**：DKFZp686O111含有C2H2-type锌指结构域——该类结构域典型地介导DNA结合或protein-protein互作。C2H2-ZF蛋白是最大的transcription factor family in metazoans。该蛋白可能以sequence-specific manner识别genomic DNA——潜在靶向TE region中的cis-regulatory element。

**TE调控展望**：该蛋白被标注为TE_REG_CANDIDATE——含Zinc_finger; Znf_C2H2_sf; Znf_C2H2_type结构域。TE调控关联性取决于以下几个方面：（1）DKFZp686O111是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）DKFZp686O111是否能够通过其结构域识别TE-derived DNA/RNA element；（3）DKFZp686O111的knockout/knockdown是否改变LINE-1或ERV family的expression level。DKFZp686O111的锌指architecture（DNA-binding domain + repressive KRAB）使其成为prime candidate for TE-targeting transcription factor。建议ChIP-seq+RNA-seq联合分析以确定其在TE region上的binding profile和transcriptional consequence。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DKFZp686O111
