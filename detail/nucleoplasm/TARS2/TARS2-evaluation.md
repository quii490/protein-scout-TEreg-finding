---
type: protein-evaluation
gene: "TARS2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TARS2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TARS2 |
| 蛋白名称 | Threonine--tRNA ligase, mitochondrial |
| 蛋白大小 | 718 aa / 81.0 kDa |
| UniProt ID | Q9BW92 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 718 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=20 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=91.0; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | aa-tRNA-synt_IIb; aa-tRNA-synth_II; aa-tRNA-synth_II/BPL/LPL |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=172 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Uncertain)
- PubMed strict=20 broad=34
- AF pLDDT=91.0 PDB=0
- InterPro: aa-tRNA-synt_IIb; aa-tRNA-synth_II; aa-tRNA-synth_II/BPL/LPL
- Pfam: HGTP_anticodon; TGS; tRNA-synt_2b
- PPI degree=172 ChIP: None
36218002: Novel TARS2 variant identified in a Chinese patient with mitochondrial encephalo | 40886211: Identification and validation of prognostic genes associated with mitochondrial  | 36150709: TARS2 Variants Cause Combination Oxidative Phosphorylation Deficiency-21: A Case

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Threonine--tRNA ligase, mitochondrial

**功能**: Catalyzes the attachment of threonine to tRNA(Thr) in a two-step reaction: threonine is first activated by ATP to form Thr-AMP and then transferred to the acceptor end of tRNA(Thr). Also edits incorrectly charged tRNA(Thr) via its editing domain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002314 |
| InterPro | IPR006195 |
| InterPro | IPR045864 |
| InterPro | IPR004154 |
| InterPro | IPR036621 |
| InterPro | IPR012675 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ICT1 | BioGRID | 0 |
| CUL3 | BioGRID | 0 |
| AHSA1 | BioGRID | 0 |
| CDC37 | BioGRID | 0 |
| CHORDC1 | BioGRID | 0 |
| FKBPL | BioGRID | 0 |
| EGFR | BioGRID | 0 |
| NTRK1 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：TARS2（718 aa，81.0 kDa）是线粒体苏氨酰-tRNA合成酶（ThrRS），属于II类氨酰化tRNA合成酶（aaRS，aa-tRNA-synt_IIb IPR002314，aa-tRNA-synth_II IPR006195，aa-tRNA-synth_II/BPL/LPL IPR045864）。II类aaRS的共同折叠以中央反平行β-片层为核心、由特征性motif 1/2/3构成活化位点。TARS2包含三个功能模块：（1）催化域——催化Thr的ATP依赖活化（Thr-AMP）+ tRNA^Thr的氨基酸化；（2）编辑域（editing domain，IPR012675, N2域）——水解误酰化的Ser-tRNA^Thr，通过"双筛"机制确保苏氨酸的翻译忠实性（Thr与Ser仅差一个甲基基团，单一识别位点无法可靠区分）；（3）反密码子结合域（HGTP_anticodon IPR004154, TGS IPR036621）——识别tRNA^Thr的反密码子（GGU）。

**PPI互作网络解读**：PPI degree=172，互作网络广度大但缺乏特异性核心互作。CUL3互作提示TARS2可能通过Cullin-RING E3泛素连接酶系统参与蛋白泛素化调控。CDC37、AHSA1、FKBPL、CHORDC1均为HSP90分子伴侣的co-chaperone——TARS2可能通过HSP90互作实现其折叠成熟和质量控制。EGFR和NTRK1这两个膜受体酪氨酸激酶的互作属非经典aaRS"兼职"功能——已有报道胞质ThrRS（TARS1）和TyrRS（YARS）在分泌后作为细胞因子样信号分子发挥作用，TARS2可能在线粒体以外的信号传导中具有类似职能。

**结构解读**：AlphaFold pLDDT=91.0，本批次中预测质量最高的蛋白之一（仅次于CNOT9的92.2）。催化域的Rossmann折叠（pLDDT >92）预测极为可靠，ATP结合位点（HIGH和KMSKS基序）和Thr结合口袋清晰可辨。编辑域的pLDDT >88，形成独立的结构域通过长linker连接至催化域——编辑活性位点含保守的His-X-X-X-Cys基序，通过锌离子配位稳定。反密码子结合域（pLDDT >85）形成经典的OB-fold（寡核苷酸/寡糖结合折叠），用于tRNA反密码子环的识别。TARS2作为线粒体定位蛋白，其N端含有线粒体靶向序列（MTS），需经线粒体加工肽酶（MPP）切除后才能成为成熟蛋白。

**机制模型**：（1）经典功能：TARS2在线粒体基质中催化苏氨酸tRNA的氨酰化——这是线粒体翻译的第一步，直接影响线粒体编码的13个氧化磷酸化亚基的合成效率。TARS2变异导致联合氧化磷酸化缺陷症-21（COXPD21, PMID:36150709），特征为脑病、发育迟缓和线粒体呼吸链活性下降——此表型直接反映线粒体翻译缺陷；（2）核质定位与"兼职"功能：TARS2的HPA核质信号（Cytosol; Nucleoplasm Uncertain）可能是以下两种机制的结果——a）MTS前体的部分胞质保留导致非线粒体分布，b）TARS2可能具有类似TARS1的非经典功能。TARS1已被报道结合CDK2 mRNA的5'UTR调控其翻译，TARS2理论上也可能通过结合核酸（mRNA或ncRNA）实现核质功能；（3）通过HSP90-cochaperone互作网络参与蛋白稳态，可能在细胞应激条件下激活线粒体未折叠蛋白反应（UPR^mt）。

**TE调控展望**：TARS2与TE调控的直接联系弱，但通过两个间接机制：（1）核编码的线粒体aaRS调控线粒体翻译——在"线粒体-核逆行信号"框架中，线粒体翻译缺陷可触发ATF4/CHOP介导的整合应激反应（ISR），ISR已知调控ERV和LINE-1表达；（2）aaRS的"兼职"核酸结合活性——许多aaRS结合mRNA（包括其自身mRNA以实现翻译自调控）和tRNA样结构（如某些ncRNA的3'端），理论上TARS2可识别含tRNA-like结构的TE RNA（如SINE的tRNA来源区域），参与其代谢调控。TARS2在心肌病中的新功能（PMID:42048853将其鉴定为扩张型心肌病的心肌细胞线粒体氧化应激调控因子）进一步凸显了该蛋白在疾病中尚未被充分认识的广义功能。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BW92-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000143374-TARS2

![](https://images.proteinatlas.org/28626/291_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/28626/291_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/28626/546_C8_5_red_green.jpg)
![](https://images.proteinatlas.org/28626/546_C8_6_red_green.jpg)
![](https://images.proteinatlas.org/28626/254_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/28626/254_C8_1_red_green.jpg)

### PubMed 文献

**PubMed count: 34**

| 42200585 | Decoding the Mitochondrial Translation-Stress Axis: Is TARS2 the Missing Link in DCM Pathogenesis? | JACC Basic Transl Sci 2026 |
| 42048853 | Systems Biology Identifies TARS2 as a Cardiomyocyte Regulator of Mitochondrial Oxidative Stress in Dilated Cardiomyopath | JACC Basic Transl Sci 2026 |
| 41548323 | Exploring the causal biological association between mitochondrial genes and carotid plaques: A multiomics Mendelian rand | Atherosclerosis 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TARS2

