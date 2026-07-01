---
type: protein-evaluation
gene: "HSPA14"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## HSPA14 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HSPA14 |
| 蛋白名称 | Heat shock 70 kDa protein 14 |
| 蛋白大小 | 509 aa / 54.8 kDa |
| UniProt ID | Q0VDF9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 509 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=27 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=91.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ATPase_NBD; Heat_shock_70_CS; HSP70_peptide-bd_sf |
| PPI | 7/10 | x3 | 21.0 | PPI degree=113 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=27 broad=61
- AF pLDDT=91.4 PDB=0
- InterPro: ATPase_NBD; Heat_shock_70_CS; HSP70_peptide-bd_sf
- Pfam: HSP70
- PPI degree=113 ChIP: None
39828281: The role of HSPA14 in breast cancer: implications for tumorigenesis, immune resp | 36845091: Expression of HSPA14 in patients with acute HIV-1 infection and its effect on HI | 34921435: Fatigue and expression of heat-shock protein genes in plaque psoriasis.

### 4. 总体评价
**68.9/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**核糖体相关分子伴侣复合物组分与核质功能的分离**：HSPA14（Heat shock 70 kDa protein 14, 509 aa, UniProt Q0VDF9）是核糖体相关复合物（Ribosome-associated complex, RAC）的核心Hsp70型组分。其结构域组合包括ATPase核苷酸结合域（InterPro: ATPase_NBD IPR043129）、热休克蛋白70保守位点（Heat_shock_70_CS IPR018181）和肽结合超折叠（HSP70_peptide-bd_sf IPR029047）。RAC定位于核糖体Exit隧道出口处，接收新生多肽链并辅助其折叠至天然构象——这一功能发生在胞质核糖体上，远离核质转录调控环境。

**高置信度pLDDT与核质定位的不解之谜**：AlphaFold pLDDT=91.4在HSP70家族中属于中上水平，表明NBD和SBD（底物结合域）在无配体状态下折叠良好。然而，该蛋白核定位证据为5/10（HPA n/a），即无任何直接核定位实验支持。其仅有的核功能线索来自PPI互作数据：DNAJC2（STRING score=998）既是RAC复合物的J-domain辅伴侣蛋白，也被报道在核内参与染色质重塑（DNAJC2/MPP11在酵母中定位核仁，与人Pes1/Bop1/WDR12复合物互作参与rRNA加工）。若HSPA14随DNAJC2一起穿梭入核，可能作为核内核糖体新生蛋白的折叠伴侣发挥功能。

**PPI与核蛋白功能的延展**：PPI degree=113（STRING/BioGRID）反映了HSPA14在HSP70超家族互作网络中的核心地位。其最强互作伙伴除了DNAJC2外，还包含HSP90AB1（STRING 822）、HSPA12B（STRING 803）、HSPA4（STRING 807）和DNAJB4（STRING 704），构成经典的热休克蛋白折叠网络。特别值得注意的共表达伙伴是DNAJB4——本次批次中DNAJB4（第30号）同为候选蛋白，若两者均在核质中被检测到，可能共同行使核内新生蛋白的质量控制功能，而这种功能可能间接涉及核内TE衍生蛋白的折叠监督。

**分子伴侣与TE调控的新兴概念**：近年文献已揭示分子伴侣系统深度参与TE调控：(1) HSP90通过稳定PIWI蛋白（piRNA通路核心Argonaut蛋白）直接影响TE的转录后沉默；(2) HSP70与HSP40协同促进L1 ORF1p蛋白的正确折叠和三聚化，若无此功能L1逆转座无法完成；(3) 分子伴侣作为蛋白质量传感器，可能优先降解错误表达的TE衍生蛋白，间接保护基因组不被TE干扰。HSPA14作为RAC组分，可能识别核糖体上正在合成的TE衍生异常蛋白并靶向降解。

**新颖性与实验策略**：PubMed=27的低文献量（归一化中新颖性45/50）和核定位空白使该蛋白符合探索型TE调控候选的条件。建议的实验路径：(1) 亚细胞分级+Western blot确定核定位存在与否；(2) 若核定位阳性，进行HSPA14-TE交联免疫沉淀+质谱鉴定（XL-IP-MS）寻找其核内互作伙伴；(3) CRISPR干扰HSPA14后通过RNA-seq检测TE转录组表达变化。


### 补充分析 (UniProt API)

**蛋白全称**: Heat shock 70 kDa protein 14

**功能**: Component of the ribosome-associated complex (RAC), a complex involved in folding or maintaining nascent polypeptides in a folding-competent state. In the RAC complex, binds to the nascent polypeptide chain, while DNAJC2 stimulates its ATPase activity

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR043129 |
| InterPro | IPR018181 |
| InterPro | IPR029047 |
| InterPro | IPR013126 |
| InterPro | IPR042049 |
| Pfam | PF00012 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DNAJC2 | STRING | 998 |
| HSP90AB1 | STRING | 822 |
| HSPA12A | STRING | 821 |
| HSPA4 | STRING | 807 |
| HSPA12B | STRING | 803 |
| HSPA13 | STRING | 746 |
| HSP90AA1 | STRING | 725 |
| DNAJB4 | STRING | 704 |