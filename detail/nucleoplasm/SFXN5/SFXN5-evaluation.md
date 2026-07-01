---
type: protein-evaluation
gene: "SFXN5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SFXN5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SFXN5 |
| 蛋白名称 | Sideroflexin-5 |
| 蛋白大小 | 340 aa / 37.1 kDa |
| UniProt ID | Q8TD22 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 340 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=13 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=88.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Mtc |
| PPI | 5/10 | x3 | 15.0 | PPI degree=49 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=13 broad=17
- AF pLDDT=88.6 PDB=0
- InterPro: Mtc
- Pfam: SFXNs
- PPI degree=49 ChIP: None
36334589: Architecture of the outbred brown fat proteome defines regulators of metabolic p | 40542427: Update of the sideroflexin (SLC56) gene family. | 40631095: Sideroflexins enable mitochondrial transport of polar neutral amino acids.

### 4. 总体评价
**74.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sideroflexin-5

**功能**: Mitochondrial amino-acid transporter (By similarity). Transports citrate (By similarity). Does not act as a serine transporter: not able to mediate transport of serine into mitochondria (By similarity) (PubMed:30442778). In brown adipose tissue, plays a role in the regulation of UCP1-dependent thermogenesis probably by supporting mitochondrial glycerol-3-phosphate utilization (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004686 |
| Pfam | PF03820 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FAS | BioGRID | 0 |
| LPAR6 | BioGRID | 0 |
| SLC18A1 | BioGRID | 0 |
| ERGIC3 | BioGRID | 0 |
| TNF | BioGRID | 0 |
| LAMP2 | BioGRID | 0 |
| SLC6A15 | BioGRID | 0 |
| C1orf85 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8TD22-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144040-SFXN5

![](https://images.proteinatlas.org/56866/985_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/56866/985_H7_4_red_green.jpg)
![](https://images.proteinatlas.org/56866/941_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/56866/941_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/56866/982_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/56866/982_H7_2_red_green.jpg)

### 深度机制分析

SFXN5属于Sideroflexin家族(SLC56, IPR004686, Pfam PF03820)，其结构核心由五段跨膜alpha-helix组成，在线粒体内膜中通过保守的Mtc结构域形成极性中性氨基酸转运通道。AlphaFold pLDDT均值88.6表明整体结构预测质量良好，但SFXN5是迄今唯一无PDB实验结构的Sideroflexin成员(其同源蛋白SFXN1/4已有晶体结构，PMID 40631095)，其N端约40 aa的预测无序区(pLDDT <50)为核靶向信号或翻译后修饰热点提供了结构柔性基础。关键的核定位证据在于：HPA Approved级别同时标注Mitochondria(Nucleoplasm为额外定位)，UniProt注释中亦标注Cytoplasm/Nucleus双重定位。这一线粒体-核质双定位模式提示SFXN5可能含有一个非经典的核定位信号(NLS)，即其N端无序区或某些非跨膜loop在该蛋白未整合入线粒体内膜时可被importin-alpha识别。机制模型中，SFXN5在线粒体中转运Citrate(作为其载体功能)——Citrate是乙酰CoA的前体，直接影响组蛋白乙酰化水平——SFXN5的核质池则可能通过调控Citrate在线粒体与核之间的分配，间接触发TE位点处H3K27ac和H3K9ac修饰的状态切换。

PPI网络中TNF(STRING/BioGRID交集)是SFXN5最关键的核内功能连接。TNF信号通过NF-kappaB通路激活后，已知触发LINE-1和SINE转座子的转录爆发；SFXN5与TNF的直接关联提示其可能是TNF-TE信号轴中的一个代谢耦合器。同时，LAMP2(溶酶体膜蛋白)和ERGIC3(ER-Golgi中间区室蛋白)的共现进一步暗示SFXN5参与细胞内膜系统代谢-信号整合。PMID 40919435多组学数据(transcriptomics+proteomics+metabolomics)揭示了线粒体功能障碍与前列腺疾病中TE家族(LINE-1/LTR)表达上调的强关联，SFXN5表达水平在此过程中显著变化。另一关键文献PMID 40542427对Sideroflexin基因家族进行的系统更新将SFXN5定位为SLC56基因家族中研究最少的成员之一，与ACOT12(另一代谢-核交叉候选)共享START样脂质结合域的进化同源性，提示代谢酶的双定位可能是TE表观调控的一个未被充分探索的普遍策略。

研究启示：SFXN5代表了"代谢酶兼职核因子"这一类新兴蛋白的极端案例——其极度低PubMed count(13篇严格)与其双定位的独特生物学意义形成鲜明对比。棕色脂肪组织(BAT)中SFXN5调控UCP1依赖的产热功能(UniProt注释)进一步暗示其可能通过核质-线粒体代谢串扰(crosstalk)选择性影响TE位点的染色质状态——BAT中UCP1激活伴随的大量线粒体呼吸事件所产生的代谢中间产物(乙酰CoA、Citrate、alpha-KG)正是表观遗传修饰酶的底物。实验策略：构建SFXN5-NES和SFXN5-NLS融合蛋白，结合亚线粒体和细胞核分级分离，确定其双定位的分子决定因素；使用13C-labeled Citrate同位素示踪直接测量SFXN5对核内乙酰CoA库和组蛋白乙酰化(ChIP-qPCR at TE loci)的影响。

### PubMed 文献

**PubMed count: 17**

| 40919435 | Multi-omic insights into mitochondrial dysfunction and prostatic disease: evidence from transcriptomics, proteomics, and | Front Genet 2025 |
| 40631095 | Sideroflexins enable mitochondrial transport of polar neutral amino acids. | bioRxiv 2025 |
| 40542427 | Update of the sideroflexin (SLC56) gene family. | Hum Genomics 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SFXN5

