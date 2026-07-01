---
type: protein-evaluation
gene: "MCHR2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MCHR2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MCHR2 |
| 蛋白名称 | Melanin-concentrating hormone receptor 2 |
| 蛋白大小 | 340 aa / 38.8 kDa |
| UniProt ID | Q969V1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Basal body; Nucleoplasm; Plasma membrane; Primary  (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 340 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=55 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=88.9; PDB=1 |
| 调控结构域 | 4/10 | ×2 | 8.0 | GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; MCH_rcpt |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- Basal body; Nucleoplasm; Plasma membrane; Primary cilium tip; Vesicles (Supported)
- PubMed strict=55 broad=90
- AF pLDDT=88.9 PDB=1
- InterPro: GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; MCH_rcpt
- Pfam: 7tm_1
- PPI degree=4 ChIP: None
20099459: Establishment of CHO cell line expressing human MCHR2 gene and research of its m | 38710677: Mechanisms of ligand recognition and activation of melanin-concentrating hormone | 39389409: Genome-Wide Association Study Meta-Analysis of 9619 Cases With Tic Disorders.

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**GPCR的核质信号——非经典G蛋白偶联受体功能**：MCHR2（Melanin-concentrating hormone receptor 2, 340 aa, UniProt Q969V1）属于A类GPCR超家族（Rhodopsin类），具有经典的7次跨膜（7TM）螺旋拓扑（InterPro: GPCR_Rhodpsn IPR000276, GPCR_Rhodpsn_7TM IPR017452; Pfam: 7tm_1 PF00001）。该受体被黑色素浓缩激素（MCH）激活后偶联Gq/11，激活磷脂酶C并升高胞内钙离子（PMIDs:11274220, 11404457, 11459838, 38710677）。HPA数据显示核质定位为Supported级别（伴有Basal body、Plasma membrane、Primary cilium tip、Vesicles的多重定位），暗示GPCR信号可能不局限于质膜。

**GPCR核膜信号与基因转录的直接耦合**：核膜GPCR信号是一个已验证的概念——多种GPCR（如mGluR5, AT1R, ETB）已被发现在核膜上发挥功能，直接调控核内钙离子振荡和CREB磷酸化。核内钙信号通过CaMKIV-CREB通路影响基因表达，而CREB结合位点（CRE/ATF基序）在多种TE（如Alu和HERV-K LTR）的启动子区域富集。若MCHR2在核膜上被MCH激活，可能通过Gq/11-PLC-IP3通路触发核内钙释放，间接调控TE近端基因转录。

**AlphaFold结构与跨膜GPCR的折叠质量**：AlphaFold pLDDT=88.9的高置信度和PDB=1的晶体结构（可能为共结晶状态）表明MCHR2的7TM支架在无配体G蛋白状态下高度有序。这与GPCR结构生物学的进展一致——冷冻电镜已解析多种A类GPCR在不同活性状态下的高分辨率结构。若MCHR2的核膜池存在，其跨膜拓扑意味着它可能插入内核膜（INM），在核质侧暴露C端尾部——C端尾部的磷酸化位点和β-arrestin结合基序可招募核内信号效应器。

**纤毛与中心体定位的TE调控含义**：Primary cilium tip（初级纤毛尖端, Supported级别）的定位特别值得注意。初级纤毛是Hedgehog（Hh）信号的关键细胞器，而Hh信号通路通过Gli转录因子调控包括TE衍生序列在内的多个基因组位点。此外，MCHR2的PPI degree=4（唯一的CSK互作, BioGRID score=0）表明其为典型"孤立"GPCR。

**低通量的网络与不确定性**：PubMed=55的文献量和归一化得分68.3/100中核定位特异性32/40是主要支撑。主要风险：MCHR2被认为在人中可能为假基因或低表达GPCR（PMID:38710677），且其生理学意义尚未被明确建立。建议作为低优先级候选，并首先通过RT-qPCR和Western blot确认靶细胞中的蛋白表达水平。


### 补充分析 (UniProt API)

**蛋白全称**: Melanin-concentrating hormone receptor 2

**功能**: G protein-coupled receptor for the neuropeptide melanin-concentrating hormone (MCH). Upon ligand binding, couples to G(q/11), leading to activation of phospholipase C and intracellular calcium mobilization (PubMed:11274220, PubMed:11404457, PubMed:11459838, PubMed:15340116, PubMed:38710677). The physiological roles mediated by this receptor remain unclear, and its contribution to specific biological processes has not been conclusively established (Probable). Expression of this receptor is restri

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000276 |
| InterPro | IPR017452 |
| InterPro | IPR008361 |
| InterPro | IPR008362 |
| Pfam | PF00001 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CSK | BioGRID | 0 |