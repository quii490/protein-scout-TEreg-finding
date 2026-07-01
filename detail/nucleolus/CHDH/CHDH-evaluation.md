---
type: protein-evaluation
gene: "CHDH"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## CHDH (Choline dehydrogenase, mitochondrial) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | CHDH |
| 蛋白全称 | Choline dehydrogenase, mitochondrial |
| UniProt ID | Q8NE62 |
| 蛋白大小 | 594 aa / 65.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 594 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR036188; InterPro:IPR012132; InterPro:IPR000172; InterPro:IPR007867; Pfam:PF05199; Pfam:PF00732 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Catalyzes the dehydrogenation of choline to betaine aldehyde in the mitochondria (By similarity). Involved in mitochondrial autophagy after mitochondrial damage (PubMed:25483962)

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR036188 |
| InterPro | IPR012132 |
| InterPro | IPR000172 |
| InterPro | IPR007867 |
| Pfam | PF05199 |
| Pfam | PF00732 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

CHDH（594 aa, UniProt Q8NE62）是线粒体胆碱脱氢酶，属于葡萄糖-甲醇-胆碱（GMC）氧化还原酶超家族。其结构域架构包含IPR036188（FAD/NAD(P)结合结构域超折叠）、IPR012132（GMC氧化还原酶）、IPR000172（GMC氧化还原酶N端）和IPR007867（葡萄糖-甲醇-胆碱氧化还原酶C端），Pfam条目PF05199（GMC_oxred_C）和PF00732（GMC_oxred_N）。该酶催化胆碱向甜菜碱醛的线粒体脱氢反应（By similarity）——这是胆碱代谢为甜菜碱的第一步，后者是重要的甲基供体。CHDH还参与线粒体损伤后的线粒体自噬（PubMed:25483962），通过维持线粒体功能完整性间接影响细胞代谢状态。

PPI数据显示RGN（钙结合蛋白, STRING评分859）、CEPT1（胆碱/乙醇胺磷酸转移酶1, 854）、PISD（磷脂酰丝氨酸脱羧酶, 843）和PLD3（磷脂酶D3, 809）为主要互作伙伴。这些互作共同指向磷脂代谢网络——CEPT1和PISD分别参与磷脂酰胆碱和磷脂酰乙醇胺的合成，而PLD3水解磷脂酰胆碱产生信号脂质磷脂酸。值得特别注意的是SQSTM1/p62（STRING评分781）的互作——p62是选择性自噬的关键受体蛋白，直接识别泛素化蛋白聚集体和受损线粒体以导向自噬降解，且p62已被证实直接结合LINE-1 ORF1p以抑制其核质积累。

从TE调控角度，CHDH通过两个代谢轴间接影响TE活性。第一，胆碱-甜菜碱-甲硫氨酸循环是S-腺苷甲硫氨酸（SAM）合成的关键通路——SAM是所有组蛋白甲基转移酶（HMT）和DNA甲基转移酶（DNMT）的唯一甲基供体。CHDH催化的胆碱脱氢决定甜菜碱可用性，进而影响肝脏和肾外组织中的同型半胱氨酸重甲基化，最终控制DNA和组蛋白甲基化所需SAM的整体供应。TE序列（尤其是IAP和LINE-1启动子）的CpG甲基化和H3K9me3/H4K20me3异染色质修饰完全依赖SAM依赖性甲基转移酶。因此CHDH作为胆碱代谢的限速酶可能通过甲基供体供应间接调节全局TE甲基化水平。第二，CHDH调控的线粒体自噬影响mtDNA应激信号——mtDNA释放至细胞质激活cGAS-STING通路可诱导IFN反应，进而通过ISRE（干扰素刺激应答元件）激活ERV/LTR启动子。

---

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000016391-CHDH

![](https://images.proteinatlas.org/36632/1239_H1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/36632/1239_H1_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/36632/1404_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36632/1404_B8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/36632/2192_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36632/2192_C2_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR036188;IPR012132;IPR000172;IPR007867; |
| Pfam | PF05199;PF00732; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RGN | STRING | 859 |
| CEPT1 | STRING | 854 |
| PISD | STRING | 843 |
| PLD3 | STRING | 809 |
| SQSTM1 | STRING | 781 |
| RPL8 | BioGRID | 1 |
| BPNT1 | BioGRID | 1 |
| TRMT1 | BioGRID | 1 |


### PubMed 文献

**PubMed count: 82**

| 42341503 | Global and mitochondrial choline dehydrogenase contribute to goose fatty liver formation by differentially regulating en | Poult Sci 2026 |
| 41684377 | Genetic variants in acetylcholine processing and significant improvement with pyridostigmine in a patient with postural  | Eur Heart J Case Rep 2026 |
| 41457117 | Tissue-Specific Transcriptomic Profiling of Vitamin-Dependent Mitochondrial Pathways in Female Buffalo. | Cell Biochem Biophys 2026 |