---
type: protein-evaluation
gene: "DAP3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## DAP3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DAP3 |
| 蛋白名称 | Small ribosomal subunit protein mS29 |
| 蛋白大小 | 398 aa / 45.6 kDa |
| UniProt ID | P51398 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Mitochondria; Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 398 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=92 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=85.0; PDB=58 |
| 调控结构域 | 4/10 | ×2 | 8.0 | P-loop_NTPase; Ribosomal_mS29; Ribosomal_mS29_met |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=429 |
| **加权总分** | | | **138/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Enhanced)
- PubMed strict=92 broad=139
- AF pLDDT=85.0 PDB=58
- InterPro: P-loop_NTPase; Ribosomal_mS29; Ribosomal_mS29_met
- Pfam: DAP3
- PPI degree=429 ChIP: None
36769187: Identification of Anoikis-Related Subgroups and Prognosis Model in Liver Hepatoc | 25254289: Perrault Syndrome Overview. | 39080251: DAP3 promotes mitochondrial activity and tumour progression in hepatocellular ca

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Small ribosomal subunit protein mS29

**功能**: As a component of the mitochondrial small ribosomal subunit, it plays a role in the translation of mitochondrial mRNAs (PubMed:39701103). Involved in mediating interferon-gamma-induced cell death (PubMed:7499268). Displays GTPase activity in vitro (PubMed:39701103)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR019368 |
| InterPro | IPR008092 |
| Pfam | PF10236 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MRPS9 | STRING | 999 |
| MRPS5 | STRING | 999 |
| MRPS15 | STRING | 999 |
| MRPS18B | STRING | 998 |
| RPS12 | STRING | 998 |
| MRPS27 | STRING | 998 |
| MRPS14 | STRING | 998 |
| MRPS31 | STRING | 997 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P51398-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000132676-DAP3

![](https://images.proteinatlas.org/23687/237_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/23687/237_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/23687/236_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/23687/236_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/23687/268_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/23687/268_E11_2_red_green.jpg)

### 深度机制分析

DAP3编码**线粒体小核糖体亚基蛋白mS29**，是一个兼具线粒体翻译核心功能与核质凋亡信号双重角色的非典型蛋白。其域结构以IPR027417（P-loop NTPase超家族）和IPR019368（Ribosomal_mS29，对应Pfam PF10236/DAP3）为特征。P-loop NTPase域赋予DAP3内在GTPase活性（PubMed:39701103体外实验证实），这在核糖体蛋白中极为罕见——大多数核糖体蛋白为结构支架，不具备独立酶活性。mS29的同源物在细菌中不存在，是真核生物线粒体特异性获得，提示其在氧化磷酸化复合体翻译和线粒体-核逆行信号中演化出专门功能。IPR008092（Ribosomal_mS29_met，后生动物特异性）进一步表明该蛋白在高等真核生物中的功能复杂性。pLDDT=85.0和58个PDB条目提供了充足的实验结构支撑。

PPI网络以线粒体小亚基蛋白为核心构成近饱和的物理互作网络：MRPS9、MRPS5、MRPS15（均为999分）和MRPS18B、MRPS27、MRPS14、MRPS31（998-997分）直接反映了DAP3在28S小亚基中的固定位置，其与邻近亚基的紧密空间邻接是维持核糖体结构完整性所必需的跨界面互作。引人注目的是RPS12（胞质核糖体蛋白，998分）的高分互作——这不是典型的线粒体-胞质核糖体交叉互作，而可能反映DAP3在核质中的"月光"（moonlighting）功能，即脱离线粒体核糖体后定位于核质（HPA: Nucleoplasm Enhanced），通过与胞质翻译机器的非经典互作参与IFN-γ诱导的细胞死亡信号传导（PubMed:7499268首次鉴定了DAP3的促凋亡功能）。

结构-功能协同分析：GTBase活性（P-loop NTPase域）可能在线粒体翻译延伸或终止步骤中发挥校对功能——GTP水解的时间延迟为密码子-反密码子配对提供了动力学校对窗口。同时，该GTPase结构域在核质中可能转变为信号开关：GTP/GDP结合状态构象差异调节DAP3与凋亡效应蛋白（如FADD或caspase前体）的互作亲和力。PubMed:39080251揭示DAP3在肝细胞癌中促进线粒体活性和肿瘤进展，提示其促凋亡功能和促肿瘤代谢功能之间存在细胞环境依赖的平衡——高线粒体活性肿瘤可能通过DAP3过表达增强氧化磷酸化，同时以某种机制压制其凋亡信号臂。

综合机制模型：DAP3是一个**双定位双功能分子开关**。（1）在线粒体基质中，作为mS29亚基参与线粒体编码的13种氧化磷酸化蛋白的翻译，其GTPase活性提供翻译保真度的动力学控制，是线粒体呼吸链生物发生的必需因子——这与Perrault综合征的遗传关联（PubMed:25254289、42283975）一致，其中DAP3突变导致卵巢发育不全和感音神经性耳聋，与线粒体翻译缺陷的组织特异性表型完全吻合。（2）在核质中，DAP3响应IFN-γ等死亡信号后从线粒体释放并转位至核质，通过其P-loop域的GTP/GDP结合状态调控凋亡信号复合体的组装。92篇PubMed文献中仅少数探寻了核质功能，36769187（失巢凋亡相关亚群与肝癌预后）仅通过生物信息学间接关联，提示DAP3核质凋亡功能的直接生化验证仍是领域空白。鉴于该蛋白在癌症（促肿瘤代谢）和神经退行性疾病（线粒体功能障碍）中的双重角色，开发区分线粒体和核质功能池的变构调节剂——而非简单抑制——是实现治疗窗口的关键。

### PubMed 文献

**PubMed count: 139**

| 42283975 | Comprehensive Insights into Perrault Syndrome: Genetic Diversity and Clinical Implications. | Reprod Sci 2026 |
| 41757073 | Identification of target genes and regulatory networks for bone mineral density GWAS loci through systematic targeting a | bioRxiv 2026 |
| 41669898 | Osteoarthritis and chondrosarcoma: Bioinformatics analysis based on single-cell RNA sequencing and molecular docking. | Adv Clin Exp Med 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DAP3

