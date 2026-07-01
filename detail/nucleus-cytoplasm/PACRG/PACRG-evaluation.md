---
type: protein-evaluation
gene: "PACRG"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## PACRG (Parkin coregulated gene protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PACRG |
| 蛋白全称 | Parkin coregulated gene protein |
| UniProt ID | Q96M98 |
| 蛋白大小 | 296.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 296 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | IPR019399, PF10274|
| 🔗 PPI | 3/10 | ×3 | 9.0 | PPI degree=63 |
| **加权总分** | | | **79/180** | |
| **归一化总分 (÷1.83)** | | | **43/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Axoneme + Nucleus + Manchette | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: PACRG 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Axoneme + Nucleus + Manchette。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

ciliary microtubule inner protein, Parkinson disease。

#### 3.3 PPI 网络

PPI degree=63。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

PACRG 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR019399 |
| Pfam | PF10274 |


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR019399; |
| Pfam | PF10274; |
| UniProt Domain | 未检出 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000112530-PACRG

![](https://images.proteinatlas.org/66293/1376_F8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/1376_F8_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/2148_D5_58_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/2148_D5_77_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/2160_F4_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/66293/2160_F4_43_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MEIG1 | STRING | 990 |
| CFAP20 | STRING | 915 |
| PRKN | STRING | 914 |
| TUBA1A | STRING | 895 |
| TEKT2 | STRING | 876 |
| TUBB4B | STRING | 868 |
| NME7 | STRING | 858 |
| PIERCE1 | STRING | 844 |


### PubMed

**Count: 101**

| PMID | Title |
|---|---|
| 41911957 | Transcriptome and alternative splicing analyses uncover immune-centric pathogenesis in periodontitis versus barrier-dysfunction-driven pathogenesis in |
| 41677459 | Correction: DNAH10 interacts with UCHL3-PACRG complex to coordinate sperm head and flagella development during spermiogenesis. |
| 41153639 | Tumour SNPs Associated with Immune-Related Hepatitis in Patients with Melanoma Receiving Immune Checkpoint Inhibitors. |
| 41058558 | DNAH10 interacts with UCHL3-PACRG complex to coordinate sperm head and flagella development during spermiogenesis. |
| 40265567 | In Silico Discovery of Potential Inhibitors Targeting the MEIG1-PACRG Complex for Male Contraceptive Development. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/PACRG_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.78 |
| pLDDT > 0.9 | 42.9% |
| pLDDT < 0.5 | 12.2% |
| 残基数 | 296 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。


### 深度机制分析

PACRG（Parkin coregulated gene protein）是一个与Parkinson病致病基因Parkin（PRKN）呈双向共调控的蛋白，其深度机制聚焦于纤毛/鞭毛轴丝结构和精子发生的生物学功能。该蛋白含有一个PACRG-specific结构域（InterPro:IPR019399, Pfam:PF10274），全长296个氨基酸，ESMFold预测的全局pLDDT=0.78且42.9%的残基pLDDT>0.9——这在本次评估的24个蛋白中属于中等偏上的结构置信度。然而12.2%的残基pLDDT<0.5提示N端或C端区域存在结构柔性，可能与互作伙伴结合时的诱导折叠相关。

PACRG的功能定位与微管系统密切相关。UniProt GO-CC将其定位为"Axoneme + Nucleus + Manchette"——其中Axoneme（轴丝）和Manchette是精子鞭毛和变形期临时性微管结构，这是其核心功能定位；Nucleus为次要或条件性定位。PACRG是纤毛/鞭毛轴丝中微管内部蛋白（MIP, microtubule inner protein）的组成部分，定位于微管双联体微管的内腔，可能作为微管稳定因子和/或纤毛跳动模式调控因子。在精子发生过程中，PACRG与MEIG1形成复合体定位于Manchette——一种由微管组成的精子头部塑形结构。这种"微管居民"（microtubule luminal resident）的定位模式极为独特——绝大多数微管相关蛋白（MAPs）定位于微管外表面，而PACRG进入微管管腔内部。

PPI互作网络完美支撑了这一功能模型。STRING数据显示MEIG1（Meiosis expressed gene 1, score=990）是最高置信度互作伙伴——MEIG1与PACRG形成1:1异源二聚体，两者共定位于轴丝和Manchette，其功能协同性在纤毛/鞭毛生物学中已被充分确立（PMID 40265567报道了靶向MEIG1-PACRG复合体的男性避孕药物虚拟筛选）。CFAP20（cilia and flagella associated protein 20, score=915）和PIERCE1（score=844）均为纤毛轴丝相关蛋白，扩展了PACRG的纤毛互作组。PRKN（Parkin, score=914）的互作反映了PACRG与Parkin在基因组层面的共调控——两者共享双向启动子，表达受共同调控。TUBA1A、TUBB4B、TEKT2和NME7等微管/纤毛蛋白的互作进一步将PACRG锚定于微管细胞骨架网络。

值得注意的是，PIERCE1（Pierce1）不仅是PACRG的STRING互作伙伴（score=844），同样也出现于本评估项目的核蛋白候选池中（nucleoplasm）。PIERCE1与PACRG在纤毛轴丝中的功能关联提示nucleoplasm候选池中可能存在一个微小的纤毛相关蛋白亚群，其核定位可能反映了这些蛋白在非纤毛细胞中的替代功能或储备状态。

PubMed文献分析聚焦于PACRG在纤毛/鞭毛和Parkinson病中的角色。PMID 41677459/41058558报道了DNAH10与UCHL3-PACRG复合体的互作以协调精子头尾发育——UCHL3是一种去泛素化酶，可能通过调控PACRG的泛素化状态影响其功能。PMID 40265567的MEIG1-PACRG虚拟筛选研究则直接将二者作为男性避孕靶标。PMID 41911957通过转录组分析揭示了免疫介导机制在牙周炎与屏障功能障碍中的差异，仅间接涉及PACRG。

核定位方面，尽管UniProt列出了Nucleus（GO-CC），HPA明确返回hpa_nuclear=False，且PACRG的功能结构域（PF10274）与DNA结合、染色质调控或转录调控无任何同源性。其在精子中的核定位可能与Manchette附着于精子核膜后的核传递有关，是一种间接的亚细胞关联而非功能性核定位。推荐等级2/5（43/100）。深度机制模型为：PACRG-MEIG1异源二聚体→微管管腔内部定位→轴丝稳定性维持→纤毛/鞭毛跳动调控→精子发育和男性生育。这一模型与TE调控无关，但PACRG在男性避孕药物开发中的靶标价值值得独立关注。



- UniProt: https://www.uniprot.org/uniprotkb/Q96M98
- HPA: https://www.proteinatlas.org/
