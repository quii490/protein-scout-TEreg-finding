---
type: protein-evaluation
gene: "L3MBTL3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## L3MBTL3 (Lethal(3)malignant brain tumor-like protein 3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | L3MBTL3 |
| 蛋白全称 | Lethal(3)malignant brain tumor-like protein 3 |
| UniProt ID | Q96JM7 |
| 蛋白大小 | 780 aa / 85.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 780 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR004092; InterPro:IPR050548; InterPro:IPR001660; InterPro:IPR013761; InterPro:IPR002515; Pfam:PF02820 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Is a negative regulator of Notch target genes expression, required for RBPJ-mediated transcriptional repression (PubMed:29030483). It recruits KDM1A to Notch-responsive elements and promotes KDM1A-mediated H3K4me demethylation (PubMed:29030483). Involved in the regulation of ubiquitin-dependent degradation of a set of methylated non-histone proteins, including SOX2, DNMT1 and E2F1. It acts as an a

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR004092 |
| InterPro | IPR050548 |
| InterPro | IPR001660 |
| InterPro | IPR013761 |
| InterPro | IPR002515 |
| Pfam | PF02820 |
| Pfam | PF00536 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。


### 深度机制分析

**MBT重复甲基赖氨酸阅读器与Notch/RBPJ共抑制的TE调控窗口**：L3MBTL3（Lethal(3)malignant brain tumor-like protein 3, 780 aa, UniProt Q96JM7）是MBT（恶性脑瘤）结构域蛋白家族成员，拥有3个串联MBT（恶性脑瘤）重复（IPR004092, Pfman: MBT PF02820），作为甲基化组蛋白的"阅读器"。MBT域以芳香笼（aromatic cage）识别单甲基化和二甲基化的赖氨酸（H3K20me1/2, H4K20me1/2），但不识别三甲基化（H3K20me3）——这种甲基化状态的选择性赋予L3MBTL3在"低甲基化"活跃染色质区域（如增强子和启动子）而非"高三甲基化"异染色质区域富集的独特能力。

**Notch/RBPJ共抑制与TE衍生Notch增强子的沉默**：L3MBTL3的核心生化功能是被RBPJ（CSL/CBF1）招募至Notch靶基因，作为转录共抑制因子（PMID:29030483）。该蛋白将KDM1A/LSD1组蛋白去甲基化酶（BioGRID score=1）招募到Notch应答元件上，通过去除H3K4me2/me1活化标记使染色质沉默。对于TE生物学，Notch/RBPJ信号通路通过SLP/CSL结合基序（RTGRGAR）直接调控多个TE家族：(1) HERV-K LTR中的Notch应答元件在胶质母细胞瘤干细胞中驱动TE表达；(2) hAT-Charlie DNA转座子衍生的Notch增强子调控神经发育；(3) MER130元件为多个Notch靶基因提供替代启动子。L3MBTL3通过其KDM1A招募活性可主动去甲基化这些Notch-TE增强子上的H3K4me，在不需要DNA甲基化或H3K9me3的情况下实现转录抑制——这是非经典（KRAB/TRIM28非依赖）的TE沉默模式的范例。

**SAMD1互作与CpG岛-TE甲基化调控**：PPI中SAMD1（STERILE ALPHA MOTIF DOMAIN-CONTAINING PROTEIN 1, STRING 854）的高互作评分提供了另一条TE调控线索——SAMD1通过其SAM域识别未甲基化的CpG岛并招募KDM1A/LSD1进行H3K4me去甲基化，形成DNA甲基化-组蛋白去甲基化的协同沉默。若L3MBTL3与SAMD1在TE CpG富集区域（如ERV-K LTR的CpG岛或IAP 5'LTR）协同作用，可驱动高效的DNA甲基化-组蛋白修饰双重沉默。KBF2/NFKB2（STRING 779）的互作则与炎症-TE激活的NF-κB通路连接。

**结构域与实验方向**：MBT-β-夹心折叠和SAM域的空间排列尚需结构解析。PubMed=47的中等文献量指示功能研究已有基础。建议实验：L3MBTL3 KO后进行H3K4me2、H3K20me1 ChIP-seq与TE转录组联合分析，验证"MBT-KDM1A双效TE沉默"假说。归一化得分67.8/100的调控结构域维度16/30突出其作为染色质"阅读器-修饰器"的独特优势。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SAMD1 | STRING | 854 |
| DCAF5 | STRING | 799 |
| KBF2 | STRING | 779 |
| RBPJ | STRING | 779 |
| BCLAF1 | STRING | 739 |
| LZTR1 | BioGRID | 1 |
| LRRK2 | BioGRID | 1 |
| KDM1A | BioGRID | 1 |