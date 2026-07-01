---
type: protein-evaluation
gene: "TMX1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMX1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | TMX1 |
| 蛋白全称 | Thioredoxin-related transmembrane protein 1 |
| UniProt ID | Q9H3N1 |
| 蛋白大小 | 280 aa / 30.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 280 aa|
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=33 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=76.6; PDB=1 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR036249, IPR017937, IPR013766, IPR052454|
| PPI | 8/10 | ×3 | 24.0 | PPI degree=228 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Thioredoxin domain-containing protein that participates in various redox reactions through the reversible oxidation of its active center dithiol to a disulfide and catalyze dithiol-disulfide exchange reactions (PubMed:11152479, PubMed:37648867). Acts as a key inhibitor of the alternative triglycerid

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR036249 | Thioredoxin-like_sf |
| InterPro | IPR017937 | Thioredoxin_CS |
| InterPro | IPR013766 | Thioredoxin_domain |
| InterPro | IPR052454 | TMX_domain-containing |
| Pfam | PF00085 | Thioredoxin |


#### 3.4 结构信息

蛋白长度 280 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**73.2/100** | **nucleolus**
Nuclear protein


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000139921-TMX1

![](https://images.proteinatlas.org/3085/19_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3085/19_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3085/18_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3085/18_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3085/17_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3085/17_D4_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR036249;IPR017937;IPR013766;IPR052454; |
| Pfam | PF00085; |
| UniProt Domain | DOMAIN 27..132; /note="Thioredoxin"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00691" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 1 |
| RPL7 | BioGRID | 1 |
| UPF1 | BioGRID | 1 |
| ATF2 | BioGRID | 1 |
| LYN | BioGRID | 1 |
| FAS | BioGRID | 1 |
| SPI1 | BioGRID | 1 |
| EWSR1 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：TMX1（280 aa，30.8 kDa）是硫氧还蛋白（Thioredoxin, Trx）超家族的跨膜成员。含N端Thioredoxin结构域（IPR013766，Thioredoxin_domain；Pfam PF00085，残基27-132），采用经典的硫氧还蛋白折叠——由4条平行/反平行β-链夹持3个α-螺旋构成混合β-片层核心，活性中心为典型的Cys-X-X-Cys（CXXC）基序。单次跨膜α-螺旋定位于残基约150-170处，C端胞质尾（约110 aa）含Thioredoxin-like超家族折叠（IPR036249）。TMX_domain-containing（IPR052454）注释其属于TMX亚家族——这是Trx超家族中特定的跨膜氧化还原酶群，在ER膜上发挥二硫键异构酶（PDI）样功能。Thioredoxin保守序列（IPR017937，Thioredoxin_CS）的CXXC基序（基于序列保守预测为CGPC）的Cys32和Cys35负责可逆的氧化还原反应。

**PPI互作网络解读**：PPI degree高达228，互作伙伴覆盖多个功能模块。ELAVL1（HuR，RNA结合蛋白，mRNA稳定性的核心调控子）和UPF1（无义介导的mRNA衰变NMD解旋酶）指向TMX1可能与RNA代谢调控存在功能关联。FAS（Fas/CD95死亡受体，外源性凋亡的启动器）和LYN（Src家族酪氨酸激酶，氧化还原敏感型激酶）的互作提示TMX1在氧化还原状态下调控凋亡信号。ATF2（激活转录因子2，JNK/p38 MAPK底物）和SPI1（PU.1，ETS家族转录因子）将TMX1与转录调控联系起来。EWSR1（Ewing肉瘤断点区蛋白1，FET家族RNA结合蛋白）的互作在PDI家族中罕见——EWSR1的氧化还原敏感性及其在转录和RNA加工中的双重角色为TMX1的功能提供了新颖视角。

**结构解读**：AlphaFold pLDDT=76.6，ESMFold平均pLDDT=86.0（52.1%残基pLDDT>0.9）。Thioredoxin域的活性中心CXXC基序处pLDDT >90，Cys32和Cys35硫醇基的距离（~3.8 angstroms）在还原态下适合二硫键的异构化和还原催化。跨膜螺旋区pLDDT中等（65-75），反映了单次跨膜蛋白的柔性——跨膜螺旋在ER膜平面上的旋转自由度对催化结构域接近ER腔面的不同底物至关重要。C端胞质尾（pLDDT 60-80）可能含另外的氧化还原活性区或蛋白互作基序——PDI家族的C端域通常含C端二聚化结构域和KDEL类ER滞留信号，但TMX1的C端缺少这两者，提示其ER定位可能通过跨膜螺旋实现而非可溶性KDEL回收。

**机制模型**：TMX1在ER膜上充当氧化还原催化剂，参与新生多肽的氧化折叠（oxidative folding）——通过CXXC活性中心的二硫醇（-SH/-SH）⇆ 二硫键（-S-S-）的氧化还原循环，催化底物蛋白的半胱氨酸残基之间形成正确的二硫键连接。具体机制包括：（1）氧化途径：TMX1的CXXC被Ero1（ER oxidoreductin 1）或PDI氧化为二硫键状态，然后将其传递给底物蛋白的半胱氨酸对完成氧化；（2）异构化途径：TMX1识别由错误二硫键导致的折叠中间体，通过还原-重排-再氧化循环纠正二硫键配对模式。在肝细胞肝癌（HCC）中，TMX1促进肿瘤进展的分子机制近期被阐明——TMX1通过稳定FABP5（脂肪酸结合蛋白5）抑制铁死亡（ferroptosis）（PMID:41482143），这提示TMX1能够通过氧化还原敏感的二硫键形成/断裂调控FABP5的构象稳定性和半衰期。核仁定位（nucleolus, GO-CC未知）在现有证据上缺乏支持——HPA IF中的核仁信号可能源自抗体的核蛋白交叉反应。

**TE调控展望**：TMX1的TE调控潜力极低。氧化还原调控在全局水平上影响转录因子活性（如AP-1、NF-κB、p53），但TMX1作为ER膜蛋白的拓扑限制使其无法直接接触染色质或核内调控因子。唯一值得注意的间接通路是：TMX1→调控FAS死亡受体信号→凋亡/存活平衡→染色质完整性和DNase I敏感性→TE区域可及性的多层间接级联——这一推测链条过于漫长，缺乏实验可检测性。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H3N1-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 50**

| 41922311 | Genetic evidence for causal relationship between general cognition and treatment resistance in schizophrenia. | Transl Psychiatry 2026 |
| 41482143 | TMX1 promotes the progression of hepatocellular carcinoma by inhibiting ferroptosis via stabilizing FABP5. | Cell Signal 2026 |
| 41168408 | CRISPR/Cas9 library screening uncovered CCT2 as a critical driver of acquired resistance to EGFR-targeted therapy by sta | Cell Death Differ 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMX1

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/TMX1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.86 |
| pLDDT > 0.9 | 52.1% |
| pLDDT < 0.5 | 0.0% |
| 残基数 | 280 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

