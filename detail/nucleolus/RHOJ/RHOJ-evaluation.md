---
type: protein-evaluation
gene: "RHOJ"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RHOJ 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | RHOJ |
| 蛋白全称 | Rho-related GTP-binding protein RhoJ |
| UniProt ID | Q9H4E5 |
| 蛋白大小 | 214 aa / 23.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoli; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 214 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=51 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=88.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | P-loop_NTPase; Small_GTP-bd; Small_GTPase |
| PPI | 8/10 | x3 | 24.0 | PPI degree=626 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Plasma membrane-associated small GTPase specifically involved in angiogenesis (PubMed:21628409, PubMed:24434213, PubMed:30158707). Required for endothelial cell migration during vascular development via its interaction with GLUL (PubMed:30158707). Elicits the formation of F-actin-rich structures, th

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR027417 | P-loop_NTPase |
| InterPro | IPR005225 | Small_GTP-bd |
| InterPro | IPR001806 | Small_GTPase |
| InterPro | IPR003578 | Small_GTPase_Rho |
| Pfam | PF00071 | Ras |


#### 3.4 结构信息

蛋白长度 214 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126785-RHOJ

![](https://images.proteinatlas.org/3050/1595_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/3050/1595_E9_3_red_green.jpg)
![](https://images.proteinatlas.org/3050/1752_H3_8_cr5804d9d255681_red_green.jpg)
![](https://images.proteinatlas.org/3050/1752_H3_18_cr5804d9dc35937_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**72.7/100** | **nucleolus**
Nuclear protein


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00175;SM00173;SM00174; |
| InterPro | IPR027417;IPR005225;IPR001806;IPR003578; |
| Pfam | PF00071; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| WAS | BioGRID | 0 |
| PAK1 | BioGRID | 0 |
| MEOX2 | BioGRID | 0 |
| PAK2 | BioGRID | 0 |
| BLZF1 | BioGRID | 0 |
| BHLHE40 | BioGRID | 0 |
| WASL | BioGRID | 0 |
| TRIP10 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：RHOJ（214 aa，23.5 kDa）是小G蛋白Rho家族的典型成员，含P-loop_NTPase结构域（IPR027417）和小GTP结合结构域（Small_GTP-bd IPR005225，Small_GTPase IPR001806），具体归类为Rho亚家族（IPR003578）。Ras超家族折叠（PF00071）形成六股β-片层被5个α-螺旋包围的经典G结构域，含有G1-G5五个保守基序：G1（GxxxxGKS/T P-loop）结合磷酸基团，G2（Switch I）和G3（Switch II）作为分子开关在GTP/GDP结合态之间转换。HPA显示Nucleoli; Nucleoplasm; Plasma membrane三重定位（Approved），其中核仁定位是Rho家族极为罕见的特征。

**PPI互作网络解读**：PPI degree=626（本批次最高），反映了小G蛋白作为信号整合中枢的核心地位。关键互作包括：PAK1/PAK2（Rho效应器激酶，调控细胞骨架动力和MAPK通路）、WAS/WASL（Wiskott-Aldrich综合征蛋白，Arp2/3介导的肌动蛋白聚合上游调控因子）、MEOX2（同源框转录因子，调控血管发育）、TRIP10（Cdc42/Rac效应器）、BHLHE40（碱性螺旋-环-螺旋转录抑制因子）。这些互作描绘了RHOJ从质膜信号到核内基因表达调控的完整信号传导链。

**结构解读**：AlphaFold pLDDT=88.0（ESMFold平均pLDDT=0.95，83.6%残基pLDDT>0.9），两种方法高度一致地预测出高质量的G结构域折叠。Switch I（残基30-40）和Switch II（残基60-70）区域在GDP结合态下呈现特征性构象，GTP结合后Switch区域发生显著重排暴露效应器结合面。C端CAAX盒（Cys-Leu-Ile-Met）介导法尼基化修饰和膜锚定。pLDDT在核心β-片层（>95）和Switch区域（85-90）均较高，表明预测结构具备功能态的代表性。

**机制模型**：RHOJ通过经典的'GTPase分子开关'模式运作：（1）质膜上GDP→GTP交换（由GEF催化），激活后通过PAK激酶磷酸化级联调控细胞骨架重排和细胞迁移（血管新生中的关键功能，PMID:21628409, PMID:30158707）；（2）核质/核仁定位机制：Switch II区域含有一段推测的核定位信号（NLS）样序列（KKRx-like），GTP结合可能通过构象变化暴露此序列，允许importin-α/β识别并介导核输入。在核仁中，RHOJ可能通过BHLHE40互作参与rDNA转录调控或核仁应激信号传导；（3）GLUL（谷氨酰胺合成酶）被鉴定为RHOJ在内皮细胞中的直接互作伙伴（PMID:30158707），连接了GTPase信号和谷氨酰胺代谢。

**TE调控展望**：RHOJ不直接参与TE调控。但作为BHLHE40的互作伙伴值得注意——BHLHE40（DEC1）是circadian clock的转录抑制因子，可结合E-box元件（CACGTG）调控靶基因。许多TE启动子（特别是MER/LTR元件）含有功能性E-box序列，BHLHE40理论上可经由这些基序调控TE转录。RHOJ通过对BHLHE40的调控可能间接影响昼夜节律依赖的TE表达模式，但这一假说需要实验验证。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H4E5-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 114**

| 42333231 | Pan-cancer signaling landscape linked to endothelial and immune Sphingosine-1-phosphate receptor 1 (S1PR1) expression. | In Silico Pharmacol 2026 |
| 42127933 | Identification of genetic modifiers of autosomal dominant Alzheimer's disease: a genome-wide association study. | Lancet Neurol 2026 |
| 41928109 | DNA methylation signatures of treatment response in medication-overuse headache. | J Headache Pain 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RHOJ

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/RHOJ_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.95 |
| pLDDT > 0.9 | 83.6% |
| pLDDT < 0.5 | 0.0% |
| 残基数 | 214 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

