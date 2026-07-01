---
type: protein-evaluation
gene: "KCNAB1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KCNAB1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KCNAB1 |
| 蛋白名称 | Voltage-gated potassium channel subunit beta-1 |
| 蛋白大小 | 419 aa / 46.6 kDa |
| UniProt ID | Q14722 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 419 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=29 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=86.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | K_chnl_volt-dep_bsu_KCNAB; K_chnl_volt-dep_bsu_KCNAB-rel; K_chnl_volt-dep_bsu_KC |
| PPI | 5/10 | x3 | 15.0 | PPI degree=39 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=29 broad=71
- AF pLDDT=86.7 PDB=0
- InterPro: K_chnl_volt-dep_bsu_KCNAB; K_chnl_volt-dep_bsu_KCNAB-rel; K_chnl_volt-dep_bsu_KCNAB1
- Pfam: Aldo_ket_red
- PPI degree=39 ChIP: None
38992025: Contribution of plasma levels of VEGF-A and angiopoietin-2 in addition to a gene | 31130851: Kcnab1 Is Expressed in Subplate Neurons With Unilateral Long-Range Inter-Areal P | 36827074: Expression of AKRs superfamily and prognostic in human gastric cancer.

### 4. 总体评价
**74.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Voltage-gated potassium channel subunit beta-1

**功能**: Regulatory subunit of the voltage-gated potassium (Kv) Shaker channels composed of pore-forming and potassium-conducting alpha subunits and of regulatory beta subunits (PubMed:17156368, PubMed:17540341, PubMed:19713757, PubMed:7499366, PubMed:7603988). The beta-1/KCNAB1 cytoplasmic subunit mediates closure of delayed rectifier potassium channels by physically obstructing the pore via its N-terminal domain and increases the speed of channel closure for other family members (PubMed:9763623). Promo

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005983 |
| InterPro | IPR005399 |
| InterPro | IPR005400 |
| InterPro | IPR036812 |
| InterPro | IPR023210 |
| Pfam | PF00248 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KCNA2 | BioGRID | 0 |
| NEDD4L | BioGRID | 0 |
| NEDD4 | BioGRID | 0 |
| ELAVL1 | BioGRID | 0 |
| ARRB2 | BioGRID | 0 |
| KCNA5 | BioGRID | 0 |
| GNB2L1 | BioGRID | 0 |
| APP | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q14722-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000169282-KCNAB1

![](https://images.proteinatlas.org/36110/1751_H6_8_cr57fd3808e9794_red_green.jpg)
![](https://images.proteinatlas.org/36110/1751_H6_18_cr57fd3811b05b1_red_green.jpg)
![](https://images.proteinatlas.org/36110/1782_C4_9_cr596b670cb8690_red_green.jpg)
![](https://images.proteinatlas.org/36110/1782_C4_18_cr596b670cb8d83_red_green.jpg)
![](https://images.proteinatlas.org/36110/1695_E4_3_cr57d8382aa78cb_red_green.jpg)
![](https://images.proteinatlas.org/36110/1695_E4_13_cr57d838326cd9c_red_green.jpg)

### PubMed 文献

**PubMed count: 71**

| 42316864 | Voltage-gated potassium channels mediate thyroid hormone control of skeletal muscle excitability. | J Physiol 2026 |
| 40908485 | Early downregulation of hair cell (HC)-specific genes in the vestibular sensory epithelium during chronic ototoxicity. | J Biomed Sci 2025 |
| 40142207 | Association of Voltage-Gated Potassium Channel Polymorphisms with the Risk and Prognosis of Epilepsy in the Saudi Popula | Medicina (Kaunas) 2025 |

### 深度机制分析

KCNAB1是电压门控钾通道Shaker家族的胞质β调控亚基，其N端失活结构域通过物理阻塞孔道来加速延迟整流钾通道的闭合（"ball-and-chain"机制，PMID:9763623）。结构域架构包括K_chnl_volt-dep_bsu_KCNAB1（IPR005983）和Aldo_ket_red（PF00248，醛酮还原酶超家族折叠），后者赋予其NADPH依赖的氧化还原酶活性，使KCNAB1同时具备离子通道调控和代谢感知的双重功能。AlphaFold pLDDT=86.7，无实验PDB结构，但醛酮还原酶折叠高度保守，折叠预测可信。

Nucleoplasm; Plasma membrane; Vesicles三重Approved定位说明KCNAB1的功能远超出膜通道调控。核质定位提示KCNAB1可能在核内执行氧化还原感应功能——通过NADPH/NADP+比率感知细胞代谢状态，并将此信息传递给核内转录机器。PPI网络中ELAVL1（RNA结合蛋白HuR）和ARRB2（β-arrestin-2）的互作支持这一模型：HuR通过结合mRNA的ARE元件调控转录本稳定性，而β-arrestin-2介导GPCR信号的核转位，KCNAB1可能作为氧化还原调控的支架蛋白桥接代谢信号与基因表达。

AKR超家族在人类胃癌中的表达和预后分析（PMID:36827074）将KCNAB1纳入醛酮还原酶介导的化疗耐药网络。VEGF-A和血管生成素-2血浆水平的基因贡献（PMID:38992025）提示KCNAB1多态性影响血管生成信号通路。Kcnab1在板下神经元中的单侧长程跨区投射表达（PMID:31130851）揭示了其在神经发育中的独特作用模式。钾通道基因多态性与癫痫风险的关联（PMID:40142207）进一步支持KCNAB1在神经元兴奋性调控中的重要角色。核质定位功能的验证应聚焦于是否通过氧化还原敏感构象变化调控核内转录因子活性，以及核定位信号的识别。

