---
type: protein-evaluation
gene: "TMEM101"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM101 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM101 |
| 蛋白名称 | Transmembrane protein 101 |
| 蛋白大小 | 257 aa / 28.8 kDa |
| UniProt ID | Q96IK0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 257 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TMEM101 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=30 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=5 broad=6
- AF pLDDT=89.4 PDB=0
- InterPro: TMEM101
- Pfam: TMEM101
- PPI degree=30 ChIP: None
39738479: TMEM101 expression and its impact on immune cell infiltration and prognosis in h | 38858765: Genome-wide DNA methylation in relation to ARID1A deficiency in ovarian clear ce | 35334008: The early-stage triple-negative breast cancer landscape derives a novel prognost

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 101

**功能**: May activate NF-kappa-B signaling pathways

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029371 |
| Pfam | PF15111 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 101

**功能**: May activate NF-kappa-B signaling pathways

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029371 |
| Pfam | PF15111 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构与分子功能推断** TMEM101（257 aa, 28.8 kDa）属于IPR029371/PF15111家族，该家族在结构域数据库中尚无已知的酶活性或结合功能注释，在进化上属于保守但功能未鉴定的跨膜蛋白群。AlphaFold预测pLDDT均值高达89.4，表明该蛋白在单体状态下具有较好的整体折叠质量，但其预测结构中缺乏经典的DNA结合域、激酶域或染色质reader模块。值得注意的是，TMEM101不与任何已知的转录辅因子结构域（如Bromo、Chromo、PHD、SET等）共享结构特征，这意味着它若在核质中发挥功能，极可能是通过蛋白-蛋白互作而非直接结合核酸。这种"无注释结构域但高折叠置信度"的特征在孤儿核蛋白中常见，通常提示其作为接头蛋白（adaptor）或支架蛋白发挥作用。

**PPI网络中的关键生物学线索** 在30个互作伙伴中，ELAVL1、TRIM25和VAPB三个蛋白构成了最具信息量的功能三角形。ELAVL1（HuR）是经典的ARE结合蛋白，负责mRNA的核质穿梭与胞质稳定性调控——TMEM101与ELAVL1的互作强烈提示其参与RNA代谢或mRNA命运决定。TRIM25是RING型E3泛素连接酶，既是RLR抗病毒信号通路（RIG-I/MDA5）的核心激活因子，也参与转录因子（如p53、RORγt）的泛素化修饰调控。VAPB是内质网-线粒体膜接触位点（MAM）的支架蛋白，其核质定位较少被关注但已有报道。此外MAP4K1（HPK1）是JNK通路上游的STE20家族激酶，PKMYT1（Myt1）是G2/M检查点的关键负调控激酶（通过磷酸化CDK1 Thr14/Tyr15抑制有丝分裂进入）。该PPI网络暗示TMEM101可能作为NF-kB信号（其已知功能注释为"May activate NF-kappa-B signaling pathways"）、RNA稳定性以及细胞周期调控三条通路之间的空间协调因子。

**结构层面的功能含义** pLDDT=89.4属于"有信心中等折叠"区间，结合0个PDB实验结构的事实，TMEM101的三维结构信息完全依赖计算预测。PAE图能展示域间相对位置的置信度——若PAE显示多域间低误差（<5A），则表明TMEM101内部结构域相对位置较为确定，有利于形成稳定的互作界面；反之若PAE值高，则蛋白可能含有固有无序区（IDR），这与接头/支架蛋白的功能模式一致。鉴于TMEM101全长仅257aa且无已知催化域，高度可能通过其折叠的表面拓扑模式（而非序列线性模体）识别并结合多个伙伴蛋白，形成瞬时多蛋白信号复合体（signalosome-like assembly）。

**整合机制模型** 综合上述证据，我们提出TMEM101的机制假设如下：TMEM101在核质中作为NF-kB信号通路与RNA代谢之间的交叉调控节点蛋白。在免疫刺激（如TNFα、LPS）下，TMEM101通过TRIM25介导的泛素化修饰被激活，随后与ELAVL1协作调控一组含ARE元件的炎症相关mRNA的核保留/输出（核滞留→降解 vs. 胞质输出→翻译激活），从而在转录后水平精细调控NF-kB靶基因的表达幅度与持续时间。其与PKMYT1的潜在互作提示该机制可能在G2/M期受到细胞周期依赖的磷酸化调控，将免疫信号与细胞增殖耦合。已发表的文献支持其临床相关性：PMID:39738479显示TMEM101表达与肝细胞癌免疫浸润及预后显著关联；PMID:38858765将其鉴定为ARID1A缺陷型卵巢透明细胞癌的差异甲基化位点，提示其表达受染色质重塑复合物SWI/SNF的表观遗传调控。

**研究与转化意义** TMEM101的低PubMed计数（仅6篇）和缺乏已知催化结构域使其成为典型的高新颖性靶标。从转化角度看：（1）NF-kB通路是肿瘤炎症微环境与免疫治疗耐药的核心驱动力，TMEM101作为该通路的新型核内调控节点，可能成为抗炎或免疫增敏的干预靶点；（2）ELAVL1互作提示TMEM101可能控制一组免疫相关mRNA的命运——通过RIP-seq或CLIP-seq鉴定TMEM101结合的RNA群体将直接验证其RNA调控功能；（3）PKMYT1互作连接细胞周期检查点，暗示TMEM101可能协调"免疫信号-细胞周期"交叉对话，这在肿瘤免疫编辑（immunoediting）中具有潜在意义。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 0 |
| MAP4K1 | BioGRID | 0 |
| TRIM25 | BioGRID | 0 |
| STX10 | BioGRID | 0 |
| VAPB | BioGRID | 0 |
| PKMYT1 | BioGRID | 0 |
| TMEM243 | BioGRID | 0 |
| VAMP1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96IK0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000091947-TMEM101

![](https://images.proteinatlas.org/39739/1443_C4_4_red_green.jpg)
![](https://images.proteinatlas.org/39739/1443_C4_5_red_green.jpg)
![](https://images.proteinatlas.org/39739/1516_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/39739/1516_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/39739/1864_H5_94_red_green.jpg)
![](https://images.proteinatlas.org/39739/1864_H5_96_red_green.jpg)
![](https://images.proteinatlas.org/75651/1872_D10_15_cr5b505110ba9b0_red_green.jpg)
![](https://images.proteinatlas.org/75651/1872_D10_18_cr5b505110bad94_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 39738479 | TMEM101 expression and its impact on immune cell infiltration and prognosis in hepatocellular carcinoma. | Sci Rep 2024 |
| 38858765 | Genome-wide DNA methylation in relation to ARID1A deficiency in ovarian clear cell carcinoma. | J Transl Med 2024 |
| 38494731 | Differentiation of ovarian serous carcinoma from ovarian clear cell carcinoma using a 10-gene signature selected by comp | Fukushima J Med Sci 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM101

