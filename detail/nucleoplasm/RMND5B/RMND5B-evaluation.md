---
type: protein-evaluation
gene: "RMND5B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RMND5B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RMND5B |
| 蛋白名称 | E3 ubiquitin-protein transferase RMND5B |
| 蛋白大小 | 393 aa / 44.4 kDa |
| UniProt ID | Q96G75 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 393 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=90.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CRA_dom; CTLH/CRA; CTLH_C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=49 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=4 broad=5
- AF pLDDT=90.5 PDB=0
- InterPro: CRA_dom; CTLH/CRA; CTLH_C
- Pfam: CTLH; zf-RING_UBOX
- PPI degree=49 ChIP: None
31885576: The CTLH Complex in Cancer Cell Plasticity. | 38903709: Immune cell related signature predicts prognosis in esophageal squamous cell car | 37396042: The diagnostic significance of the ZNF gene family in pancreatic cancer: a bioin

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**CTLH泛素连接酶核心组分的转录因子降解功能**：RMND5B（393 aa, UniProt Q96G75）是CTLH（C-terminal to LisH）E3泛素连接酶复合物的核心催化组分。其结构域包括CTLH_C（IPR045098）和CRA（CT11-RanBPM）结构域（IPR013144），与RMND5A形成同源二聚体构成连接酶的底物识别模块。该复合物从UBE2H E2酶接受泛素，催化转录因子HBP1（HMG-box蛋白1）的多聚泛素化和蛋白酶体降解（PMID:29911972）。CTLH复合物的活性是正常细胞增殖所必需的，缺失会扰乱细胞周期调控。

**CTLH复合物在癌症和免疫中的TE调控关联**：RMND5B的PPI核心组分组为ARMC8（STRING 985）、WDR26（STRING 980）、GID8（STRING 959）和MAEA（STRING 866）。这组蛋白构成人类GID/CTLH E3复合物——在酵母中GID复合物通过泛素化果糖-1,6-双磷酸酶（FBPase）调控糖异生，而在人类中底物扩展至多个转录因子和信号蛋白。PMID:31885576（The CTLH Complex in Cancer Cell Plasticity）总结了该复合物在EMT和肿瘤干细胞可塑性中的角色——而EMT过程中TE（特别是HERV-H LTR和MER41）作为增强子被广泛激活以驱动间充质基因表达。若CTLH泛素化降解的是抑制TE活性的转录因子（如ZNFs或SETDB1），则RMND5B可能正向调控TE表达。

**RANBP9/10支架蛋白的细胞骨架-细胞核信号桥接**：RANBP10（STRING 854）和RANBP9（STRING 794）是CTLH复合物的两个支架伙伴，均含有SPRY、LisH和CTLH结构域。RANBP9/10定位于微管组织中心（MTOC）和细胞核，介导细胞骨架动力学与基因转录的耦合。ARMC8（Armadillo重复蛋白8, STRING 985）是具有α-超螺旋重复的支架，可能协调CTLH复合物的组装。YPEL5（STRING 832）是含Yippee样锌指基序的核蛋白，暗示DNA/染色质底物识别潜力。

**高结构置信度与有限的文献支持**：AlphaFold pLDDT=90.5为本批次中结构置信度最高的蛋白之一，CTLH域可能采用α/β Rossmann样折叠。PubMed=4的极低文献量（新颖性满分50/50）与归一化得分68.3/100耦合，使RMND5B成为泛素-蛋白酶体-TE调控交叉领域的高风险候选。实验上建议AP-MS鉴定CTLH复合物的泛素化底物组（ubiquitinome），并筛选其中是否包含已知TE调控因子。


### 补充分析 (UniProt API)

**蛋白全称**: E3 ubiquitin-protein transferase RMND5B

**功能**: Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. MAEA and RMND5A are both required for catalytic activity of the CTLH E3 ubiquitin-protein ligase complex (PubMed:29911972). Catalytic activity of the complex is required for normal cell proliferation (PubMed:29911972). The CTLH E3 ubiquitin-protein ligase complex is not required for the de

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR013144 |
| InterPro | IPR024964 |
| InterPro | IPR006595 |
| InterPro | IPR045098 |
| InterPro | IPR006594 |
| InterPro | IPR037681 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ARMC8 | STRING | 985 |
| WDR26 | STRING | 980 |
| GID8 | STRING | 959 |
| RMND5A | STRING | 901 |
| MAEA | STRING | 866 |
| RANBP10 | STRING | 854 |
| YPEL5 | STRING | 832 |
| RANBP9 | STRING | 794 |