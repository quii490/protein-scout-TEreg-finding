---
type: protein-evaluation
gene: "PDCD7"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PDCD7 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PDCD7 |
| 蛋白全称 | Programmed cell death protein 7 |
| UniProt ID | Q8N8D1 |
| 蛋白大小 | 485 aa / 53.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 485 aa|
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=7 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=76.4; PDB=5 |
| 🧬 调控结构域 | 7/10 | ×2 | 14.0 | IPR052831, IPR031974, PF16021|
| PPI | 6/10 | ×3 | 18.0 | PPI degree=71 |
| **加权总分** | | | **148/180** | |
| **归一化总分** | | | **82.0/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Promotes apoptosis when overexpressed

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR052831 | Apoptosis_promoter |
| InterPro | IPR031974 | PDCD7 |
| Pfam | PF16021 | PDCD7 |


#### 3.4 结构信息

蛋白长度 485 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
★★★★★  **82.0/100**  |  **nucleolus**
Nuclear protein


### 深度机制分析

**PDCD7并非真正的凋亡蛋白，而是U12型次要剪接体（minor spliceosome）的核心组分。** 这一结论来自PPI网络数据的决定性证据：PDCD7所有高置信度互作伙伴（STRING评分891-988）均为剪接体成分，且绝大多数特异性地属于U12型次要剪接体。SMART和UniProt Domain均未检出经典功能结构域（如死亡结构域、CARD、Bcl-2同源域等），说明PDCD7不依赖传统凋亡信号通路发挥功能。所谓"过表达促凋亡"的表型，极可能是剪接体组装异常导致U12型内含子加工失调的间接后果——这类内含子富集于DNA复制、转录调控和细胞周期相关基因中，其剪接缺陷会触发细胞周期停滞和程序性死亡。

**PPI网络提供了该蛋白功能归属的决定性证据。** 排名前八的互作伙伴中，SNRNP35（STRING 988）是U11 snRNP的35K组分，ZMAT5（STRING 954）是U11/U12 di-snRNP的20K锌指蛋白，ZRSR2（STRING 947）负责识别U12型内含子的3'剪接位点，SNRNP48（STRING 938）和SNRNP25（STRING 921）分别是U11/U12 snRNP的48K和25K蛋白，ZCRB1（STRING 913）是U12型剪接体的RNA结合组分。SNRPE（STRING 891）和SNRPF（STRING 890）则是Sm核心蛋白，为剪接体通用组分。这一完全的次要剪接体"朋友圈"——PPI degree达到71——强烈暗示PDCD7是U11/U12 di-snRNP复合物的结构性亚基，而非临时性调控因子。值得注意的是，2025年发表于*Molecular Cell*的论文"Structural basis of 5' splice site recognition by the minor spliceosome"（PMID: 39809272）正是通过冷冻电镜解析了该复合物的高分辨率结构，PDCD7在其中很可能扮演了支架性角色。

**AlphaFold结构预测数据与剪接体蛋白的典型行为一致。** pLDDT=76.4的全局置信度属于中等偏高区间，反映了部分折叠与部分无序共存的状态。这种"适度有序"恰是剪接体蛋白的结构特征：在游离态下存在大量柔性环区（intrinsically disordered regions, IDRs），而结合到snRNP复合物后会发生显著的折叠-结合偶联（folding-upon-binding）。PDB中有5个已解析结构条目，结合2025年*Molecular Cell*的次要剪接体冷冻电镜研究，这些结构很可能展示了PDCD7在U11/U12 di-snRNP内的构象状态——游离时高度动态，复合物中刚化固定。

**综合所有证据，PDCD7的分子机制可归纳如下：** PDCD7是U12型次要剪接体的组装支架蛋白，通过PDCD7保守结构域（IPR031974/PF16021）与U11/U12 snRNP的多个蛋白亚基（SNRNP35、ZMAT5、SNRNP48、SNRNP25等）形成界面，协同ZRSR2和ZCRB1完成对U12型内含子5'和3'剪接位点的识别与稳定。U12型内含子仅占人类基因组的约0.35%（~700-800个基因），但其宿主基因集中于DNA复制、染色质重塑、RNA加工和细胞骨架调控等基本过程。因此，PDCD7的功能异常——无论是表达量偏离（如过表达导致剪接失调）、突变失活还是复合物组装受阻——都会导致U12型内含子剪接障碍，进而触发细胞周期检查点激活和凋亡。这完美解释了PDCD7命名中"程序性细胞死亡"的由来：凋亡并非其直接功能，而是剪接体稳态被破坏后的细胞命运。

**研究和治疗意义：** ZRSR2（PDCD7的直接互作伙伴，STRING 947）在骨髓增生异常综合征（MDS）和急性髓系白血病（AML）中高频突变，其突变导致U12型剪接缺陷和染色质异常。PDCD7作为同一复合物的支架组分的地位使其成为理解ZRSR2突变致病机制的切入点，也是该剪接体模块的潜在协同靶点。此外，次要剪接体的U12型内含子基因偏向性为选择性剪接调控提供了理论窗口——干扰PDCD7-U11/U12复合物可特异性地调控少数关键基因的剪接模式而不影响全局基因表达。该蛋白目前PubMed仅15篇文献、归一化得分82分（研究新颖性满分10分），属于高度未被充分研究的靶点，其在剪接体生物学和疾病机制中的角色值得深入探索。

---

### 补充分析 (UniProt API)

**蛋白全称**: Programmed cell death protein 7

**功能**: Promotes apoptosis when overexpressed

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR052831 |
| InterPro | IPR031974 |
| Pfam | PF16021 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000090470-PDCD7

![](https://images.proteinatlas.org/49388/798_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/49388/798_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49388/791_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/49388/791_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49388/860_A10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/49388/860_A10_8_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR052831;IPR031974; |
| Pfam | PF16021; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SNRNP35 | STRING | 988 |
| ZMAT5 | STRING | 954 |
| ZRSR2 | STRING | 947 |
| SNRNP48 | STRING | 938 |
| SNRNP25 | STRING | 921 |
| ZCRB1 | STRING | 913 |
| SNRPE | STRING | 891 |
| SNRPF | STRING | 890 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N8D1-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 15**

| 40255485 | Transcriptomic signature can distinguish chronic neutrophilic leukemia from ambiguous neutrophilic leukemias. | Front Genet 2025 |
| 39809272 | Structural basis of 5' splice site recognition by the minor spliceosome. | Mol Cell 2025 |
| 35598413 | Exosomes Released from Bone-Marrow Stem Cells Ameliorate Hippocampal Neuronal Injury Through transferring miR-455-3p. | J Stroke Cerebrovasc Dis 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PDCD7

