---
type: protein-evaluation
gene: "TMEM255A"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## TMEM255A (Transmembrane protein 255A) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | TMEM255A |
| 蛋白全称 | Transmembrane protein 255A |
| UniProt ID | Q5JRV8 |
| 蛋白大小 | 349 aa / 38.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 349 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 5/10 | x2 | 10.0 | InterPro:IPR028014; Pfam:PF14967 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **118/180** | |
| **归一化总分 (/1.83)** | | | **64.5/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR028014 |
| Pfam | PF14967 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 255A

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028014 |
| Pfam | PF14967 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 255A

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028014 |
| Pfam | PF14967 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE 调控潜力极低。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000125355-TMEM255A
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/48470/806_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/48470/806_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/48470/820_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/48470/820_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/48470/810_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/48470/810_D10_2_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR028014; |
| Pfam | PF14967; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 0 |
| SEC24B | BioGRID | 0 |
| WWP2 | BioGRID | 0 |
| ITCH | BioGRID | 0 |
| WWP1 | BioGRID | 0 |
| COLGALT2 | BioGRID | 0 |
| NEDD4 | BioGRID | 0 |
| KCTD2 | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM255A

### PubMed

**Count: 4**

| PMID | Title |
|---|---|
| 40207873 | Placental transcriptomic profiling in a mouse model of fetal growth restriction reveals disturbed inflammation and immunity regulation†. |
| 34782661 | Immune classification and identification of prognostic genes for uveal melanoma based on six immune cell signatures. |
| 32391621 | Fam70A binds Wnt5a to regulate meiosis and quality of mouse oocytes. |
| 31729179 | Alu-mediated Xq24 deletion encompassing CUL4B, LAMP2, ATP1B4, TMEM255A, and ZBTB33 genes causes Danon disease in a female patient. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/TMEM255A_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.69 |
| pLDDT > 0.9 占比 | 25.2% |
| pLDDT < 0.5 占比 | 22.3% |
| 建模残基数 | 349 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。

### 深度机制分析

TMEM255A（亦称FAM70A）是一个功能注释极不完整的跨膜蛋白，其唯一的已知结构域为DUF4487（Pfam:PF14967, InterPro:IPR028014），属于功能未知结构域家族。ESMFold预测的全局pLDDT仅0.69，且22.3%的残基pLDDT<0.5，提示该蛋白含有大量无序区域或未折叠区段，这对结构生物学研究构成显著挑战。其UniProt条目仍为TrEMBL状态（未审查），意味着该蛋白的序列和功能注释尚未经过专家审核，在蛋白命名、结构域边界和翻译后修饰方面存在较大的注释不确定性。值得注意的是，HPA定位数据显示TMEM255A存在于nucleoplasm和nuclear bodies，这与报告中"无已知核定位注释"的GO-CC分类形成了矛盾——HPA IF图像的核内信号提示该蛋白可能在特定条件下具有核质分布，但缺乏GO层面的实验验证。

PPI互作网络的BioGRID数据显示TMEM255A与8个蛋白存在互作（所有评分均为0的最低置信度），包括APP、SEC24B（COPII囊泡组分）、WWP2/HECT家族E3泛素连接酶）、ITCH（HECT E3连接酶）、WWP1、COLGALT2（胶原半乳糖基转移酶）、NEDD4（HECT E3连接酶）和KCTD2。这些互作伙伴以泛素化相关酶类为突出特征——WWP2、ITCH、WWP1和NEDD4均为含WW结构域的HECT型E3泛素连接酶，参与蛋白泛素化降解和内吞分选。尽管互作评分为0，这一功能聚集模式提示TMEM255A可能与膜蛋白泛素化降解通路存在关联。

在疾病关联方面，仅有的4篇PubMed文献提供了有限的信息。PMID 32391621报道Fam70A（小鼠TMEM255A同源物）通过与Wnt5a结合调控小鼠卵母细胞的减数分裂和质量，揭示了其在生殖生物学中的潜在功能。PMID 31729179报道一例包含TMEM255A在内的Xq24区域缺失导致的Danon病（一种X连锁显性遗传性溶酶体贮积症），但该缺失同时涵盖CUL4B、LAMP2、ATP1B4和ZBTB33等多个基因，无法将表型归因于TMEM255A单一基因缺失。综合而言，该蛋白的结构和功能信息极度匮乏，缺乏任何TE调控相关的领域证据。

TMEM255A推荐等级2/5（64.5/100），其得分主要由研究新颖性（10/10）驱动——PubMed仅4篇文献且无一直接功能研究。然而，DUF4487结构域功能完全未知、结构预测质量低下（22.3%低置信残基）、PPI数据质量极低（全部score=0）以及缺乏核定位GO注释等多项劣势，使其在TE调控领域的开发价值极为有限。目前的机制模型仅能推断其可能参与膜蛋白的泛素化调控（基于WW结构域E3连接酶互作富集），但缺乏任何核内功能的分子基础。

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q5JRV8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JRV8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMEM255A
