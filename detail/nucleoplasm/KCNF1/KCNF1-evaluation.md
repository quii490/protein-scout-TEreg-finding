---
type: protein-evaluation
gene: "KCNF1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## KCNF1 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KCNF1 |
| 蛋白名称 | Voltage-gated potassium channel regulatory subunit KCNF1 |
| 蛋白大小 | 494 aa / 55.6 kDa |
| UniProt ID | Q9H3M0 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm; Primary cilium trans (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 494 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=10 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=79.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ion_trans_dom; K_chnl_volt-dep_Kv; K_chnl_volt-dep_Kv5/Kv9 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=25 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +1 |
### 3. 分析
- HPA: Golgi apparatus; Nucleoplasm; Primary cilium transition zone; Vesicles (Approved)
- PubMed: strict=10, broad=21
- AF pLDDT: 79.6 / PDB: 0
- InterPro: Ion_trans_dom; K_chnl_volt-dep_Kv; K_chnl_volt-dep_Kv5/Kv9
- Pfam: BTB_2; Ion_trans
- PPI degree=25 / ChIP: None
36397112: The prognostic value of tumor mutational burden related 6-gene-based Risk Score  | 36627549: Intraperitoneal 5-Azacytidine Alleviates Nerve Injury-Induced Pain in Rats by Mo | 33083937: Causal Bayesian gene networks associated with bone, brain and lung metastasis of
### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Voltage-gated potassium channel regulatory subunit KCNF1

**功能**: Regulatory alpha-subunit of the voltage-gated potassium (Kv) channel which, when coassembled with KCNB1 or KCNB2, can modulate their expression and their gating kinetics by acting on deactivation upon repolarization and inactivation during maintained depolarization. Accelerates inactivation but has relatively little effect on deactivation. Coexpression with KCNB1 or KCNB2 markedly slows inactivation. Each modulatory subunit has its own specific properties of regulation, and can lead to extensive

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005821 |
| InterPro | IPR003968 |
| InterPro | IPR003971 |
| InterPro | IPR048010 |
| InterPro | IPR011333 |
| InterPro | IPR003131 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

KCNF1（Voltage-gated potassium channel regulatory subunit KCNF1）是Kv通道的调控性α亚基（Kv5.1），属于电沉默亚基家族。其结构域架构包括：Ion_trans_dom（IPR005821）、K_chnl_volt-dep_Kv（IPR003968）、K_chnl_volt-dep_Kv5/Kv9（IPR003971）以及N端的BTB/POZ域（IPR048010/IPR003131，Pfam BTB_2）。494个氨基酸（55.6 kDa）的分子量和pLDDT=79.6的结构分数提示一个中等大小的、折叠合理的蛋白。KCNF1不能单独形成功能性通道——它需要与KCNB1（Kv2.1）或KCNB2（Kv2.2）共组装形成异聚体，通过加速失活来调控通道门控动力学，对去活化的影响相对较小。每一亚基具有特异的调控特性，可导致广泛的通道功能多样性。

HPA免疫荧光揭示了KCNF1极具信息量的定位模式：Golgi apparatus; Nucleoplasm; Primary cilium transition zone; Vesicles (Approved)。高尔基体和囊泡的定位与其作为通道α亚基的膜运输过程一致。初级纤毛过渡区的定位与Kv通道在纤毛形成和信号传导中的新兴角色相符。而核质定位——与其同家族成员KCNH5类似——构成了Kv电沉默亚基中反复出现的现象。BTB/POZ域的N端存在是一个关键的线索：BTB（Bric-a-brac, Tramtrack, Broad Complex）域是已知的转录抑制因子招募结构域，在BTB-ZF转录因子中通过二聚化招募辅抑制因子（如NCoR、SMRT）。如果在核质中KCNF1的BTB域功能性地参与转录调控，这可能构成离子通道 moonlighting的新范式。

PPI网络揭示了KCNF1与KCNG3、KCNH1和KCNV2的同家族Kv通道互作，支持其作为异聚体调控亚基的角色。OPRM1（μ-阿片受体）、CLPTM1L（唇腭裂跨膜蛋白1样蛋白）、TSPO（转运蛋白/外周苯二氮卓受体）和SLC39A7（锌转运体ZIP7）的互作提供了信号转导相关的新连接。SERP1（应激相关内质网蛋白1）的互作提示了内质网应激相关的功能。这些互作需要在后续实验中验证其作为特异性生理互作（而非非特异性膜蛋白假阳性）。

PubMed strict=10篇文献覆盖了KCNF1在肿瘤突变负荷（PMID 36397112）、神经病理性疼痛中的DNA甲基化调控（PMID 36627549）和肿瘤转移基因网络（PMID 33083937）等关联研究，缺乏直接的分子机制研究。KCNF1在TE调控中的潜在角色取决于以下假设：（1）其BTB域在核质中是否功能性参与转录复合体；（2）其电压感应域（VSD）是否以非经典方式感知核内信号（如膜电位变化）；（3）锌离子信号（通过SLC39A7/ZIP7）是否调控其核质穿梭。这些问题的解答将决定KCNF1在TE调控研究中是否有探索价值。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KCNG3 | BioGRID | 0 |
| KCNH1 | BioGRID | 0 |
| KCNV2 | BioGRID | 0 |
| OPRM1 | BioGRID | 0 |
| CLPTM1L | BioGRID | 0 |
| TSPO | BioGRID | 0 |
| SLC39A7 | BioGRID | 0 |
| SERP1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H3M0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162975-KCNF1

![](https://images.proteinatlas.org/14738/2177_B6_84_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2177_B6_121_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2147_F11_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2147_F11_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2150_F4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2150_F4_66_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162975-KCNF1

![](https://images.proteinatlas.org/14738/2177_B6_84_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2177_B6_121_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2147_F11_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2147_F11_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2150_F4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2150_F4_66_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162975-KCNF1

![](https://images.proteinatlas.org/14738/2177_B6_84_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2177_B6_121_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2147_F11_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2147_F11_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2150_F4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/14738/2150_F4_66_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 21**

| 40423692 | A Kv2 inhibitor combination reveals native neuronal conductances consistent with Kv2/KvS heteromers. | Elife 2025 |
| 38352561 | A Kv2 inhibitor combination reveals native neuronal conductances consistent with Kv2/KvS heteromers. | bioRxiv 2025 |
| 38111060 | Risk factors analysis and survival prediction model establishment of patients with lung adenocarcinoma based on differen | Eur J Med Res 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KCNF1

