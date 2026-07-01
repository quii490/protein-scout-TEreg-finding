---
type: protein-evaluation
gene: "LACTB"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## LACTB (Serine beta-lactamase-like protein LACTB, mitochondrial) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | LACTB |
| 蛋白全称 | Serine beta-lactamase-like protein LACTB, mitochondrial |
| UniProt ID | P83111 |
| 蛋白大小 | 547 aa / 60.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 547 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 7/10 | x2 | 14.0 | InterPro:IPR001466; InterPro:IPR012338; InterPro:IPR052794; Pfam:PF00144 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Mitochondrial serine protease that acts as a regulator of mitochondrial lipid metabolism (PubMed:28329758). Acts by decreasing protein levels of PISD, a mitochondrial enzyme that converts phosphatidylserine (PtdSer) to phosphatidylethanolamine (PtdEtn), thereby affecting mitochondrial lipid metabolism (PubMed:28329758). It is unclear whether it acts directly by mediating proteolysis of PISD or by 

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR001466 |
| InterPro | IPR012338 |
| InterPro | IPR052794 |
| Pfam | PF00144 |

#### 3.3 核定位

无已知核定位注释

### 深度机制分析

LACTB（丝氨酸beta-内酰胺酶样蛋白）采用经典的青霉素结合蛋白/β-内酰胺酶折叠（IPR001466、IPR012338、Pfam PF00144），其活性位点Ser-X-X-Lys基序为催化丝氨酸蛋白酶水解反应所必需。IPR052794指向其在真核生物中特定的线粒体脂质代谢功能。547 aa（60.2 kDa）的分子量在丝氨酸蛋白酶家族中属中上水平。AlphaFold pLDDT数据可用但无实验PDB验证。

功能注释显示LACTB可降低PISD（磷脂酰丝氨酸脱羧酶）的蛋白水平，从而影响线粒体膜中磷脂酰丝氨酸（PtdSer）向磷脂酰乙醇胺（PtdEtn）的转化（PubMed:28329758）。PPI数据显示与CALM1（钙调蛋白）、ELAVL1（RNA结合蛋白HuR）、SPRTN（DNA修复蛋白酶）、PAXIP1（PAXIP1/PTIP，MLL3/4复合物亚基）、HERC2（E3泛素连接酶）、IBTK（BTB/Kelch蛋白）等多类功能因子的互作。其中PAXIP1的连接尤为值得注意——PAXIP1是COMPASS/MLL3-MLL4甲基转移酶复合物的组分，负责H3K4me1沉积在增强子区域。

TE调控相关性的机制推论：LACTB作为线粒体蛋白酶可能通过（1）PAXIP1-MLL3/4复合物连接间接影响H3K4me1标记在TE衍生增强子上的沉积模式；（2）调控线粒体脂质环境改变线粒体逆行信号（mitochondrial retrograde signaling）的输出强度，该信号影响核内的转录重编程和TE表达；（3）与ELAVL1/HuR互作间接参与TE衍生RNA的稳定性和翻译调控。然而，这些机制均为间接推论，LACTB在线粒体中的主要定位和功能使其与核内TE调控的距离较远。

无已知核定位注释（核定位特异性4/10），PubMed 79篇赋予了不错的新颖性（10/10）。归一化总分66.7/100。尽管LACTB的PAXIP互作暗示表观遗传调控的潜在链接，线粒体-核的通讯距离使得TE调控链条过长，不建议作为优先靶标。

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CALM1 | BioGRID | 0 |
| ELAVL1 | BioGRID | 0 |
| SPRTN | BioGRID | 0 |
| PAXIP1 | BioGRID | 0 |
| HERC2 | BioGRID | 0 |
| IBTK | BioGRID | 0 |
| ZNFX1 | BioGRID | 0 |
| FOXN1 | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LACTB


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103642-LACTB

![](https://images.proteinatlas.org/36362/571_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36362/571_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36362/544_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36362/544_A10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/36362/542_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36362/542_A10_2_blue_red_green.jpg)

### PubMed

**Count: 79**

| PMID | Title |
|---|---|
| 42366378 | Phenotyping of post-fertilization sperm mitophagy determinants discovered in a mammalian gamete-based cell-free system. |
| 42000972 | Fiber type-specific expression of LACTB leverages a function in oxidative metabolism. |
| 41929023 | Reduced LACTB expression in myeloid cells is associated with elevated succinylcarnitine levels and reduced Alzheimers disease risk. |
| 41775345 | LINC00852 inhibits colorectal cancer progression by regulating cell apoptosis, epithelial‒mesenchymal transition, invasion, and cuproptosis through mi |
| 41527692 | The depletion of serine beta-lactamase-like protein (LACTB) ameliorates metabolic dysfunction-associated steatotic liver disease by reducing ubiquitin |


