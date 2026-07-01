---
type: protein-evaluation
gene: "HEL-203"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## HEL-203 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HEL-203 |
| 蛋白名称 | Epididymis luminal protein 203 |
| 蛋白大小 | 586 aa / 68.5 kDa |
| UniProt ID | V9HVY7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 586 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=65.8; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | KRAB; KRAB_dom_sf; Znf_C2H2_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=65.8 PDB=0
- InterPro: KRAB; KRAB_dom_sf; Znf_C2H2_sf
- Pfam: KRAB; zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**66.7/100** | **nucleoplasm**
TE candidate: KRAB; KRAB_dom_sf; Znf_C2H2_sf


### 补充分析 (UniProt API)

**蛋白全称**: Epididymis luminal protein 203

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF01352 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Epididymis luminal protein 203

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF01352 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：HEL-203（V9HVY7, Epididymis luminal protein 203, 586 aa / 68.5 kDa）的主要结构域注释为KRAB, KRAB_dom_sf, Znf_C2H2_sf。Pfam数据库进一步识别到KRAB、zf-C2H2等保守域。AlphaFold pLDDT=65.8（中低置信度）——结构预测显示较大无序区域，可能含IDR（intrinsically disordered region）或需要结合伴侣才能有序折叠。该蛋白暂无实验PDB结构（PDB=0），当前结构信息完全依赖AlphaFold预测。PubMed=0（TrEMBL条目），该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=0）——该蛋白的已知互作伙伴数量有限，互作网络尚未充分建立。

**结构解读**：InterPro注释到3个结构域条目——KRAB、KRAB_dom_sf、Znf_C2H2_sf。Pfam域KRAB、zf-C2H2的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=65.8提示存在显著的柔性区段，可能需要在蛋白互作伴侣存在的条件下才能完全折叠。

**机制模型**：HEL-203含有C2H2-type锌指结构域——该类结构域典型地介导DNA结合或protein-protein互作。C2H2-ZF蛋白是最大的transcription factor family in metazoans。该蛋白可能以sequence-specific manner识别genomic DNA——潜在靶向TE region中的cis-regulatory element。

**TE调控展望**：该蛋白被标注为TE_REG_CANDIDATE——含KRAB; KRAB_dom_sf; Znf_C2H2_sf结构域。TE调控关联性取决于以下几个方面：（1）HEL-203是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）HEL-203是否能够通过其结构域识别TE-derived DNA/RNA element；（3）HEL-203的knockout/knockdown是否改变LINE-1或ERV family的expression level。HEL-203的锌指architecture（DNA-binding domain + repressive KRAB）使其成为prime candidate for TE-targeting transcription factor。建议ChIP-seq+RNA-seq联合分析以确定其在TE region上的binding profile和transcriptional consequence。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TACSTD2 | STRING | 725 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-V9HVY7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/HEL-203
