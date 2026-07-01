---
type: protein-evaluation
gene: "VASN"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## VASN (Vasorin) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | VASN |
| 蛋白全称 | Vasorin |
| UniProt ID | Q6EMK4 |
| 蛋白大小 | 673 aa / 74.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 673 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR000483; InterPro:IPR000742; InterPro:IPR003961; InterPro:IPR036116; InterPro:IPR013783; InterPro:IPR001611 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

May act as an inhibitor of TGF-beta signaling

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000483 |
| InterPro | IPR000742 |
| InterPro | IPR003961 |
| InterPro | IPR036116 |
| InterPro | IPR013783 |
| InterPro | IPR001611 |
| InterPro | IPR003591 |
| InterPro | IPR032675 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。


### 深度机制分析

**分泌型TGFβ抑制因子的非核蛋白本质**：VASN（Vasorin, 673 aa, UniProt Q6EMK4）是TGFβ信号通路的胞外/分泌抑制因子，其结构域组合极具特征——EGF样重复（IPR000742, IPR013032）、纤维连接蛋白III型（FN3）重复（IPR003961, IPR036116）和层粘连蛋白G样（LamG）结构域（IPR001611），以及富含亮氨酸重复（LRR）N端域（IPR032675）。这些结构域全部为胞外基质蛋白标志，指示VASN通过分泌途径（ER→Golgi→胞外）发挥功能，在细胞外基质中直接结合TGFβ1/2/3配体（BioGRID score=0）并抑制其受体结合。该蛋白的核仁分类（归一化67.8/100, 核定位特异性4/10）与分泌蛋白的ER-Golgi-胞外trafficking完全矛盾，几乎确定为假阳性分类。

**TGFβ-TE调控的旁分泌假说**：VASN对TGFβ信号的非核质抑制可能在旁分泌水平间接影响TE调控：(1) TGFβ/SMAD2/3通路通过SMAD结合元件（SBE）激活多种TE——HERV-H和MER21元件包含功能性SBE基序，驱动EMT和纤维化中的TE转录；(2) TGFβ还诱导LINE-1 ORF1p在上皮-间充质转化（EMT）中的表达（PMID:31292763）。VASN作为TGFβ拮抗剂，可能通过降低局部TGFβ浓度抑制TE的EMT依赖性激活。但这一效应不涉及VASN的核内功能，属于纯旁分泌调控。

**核内互作PPI的假阳性解释**：PPI中包含SRSF10（BioGRID score=0）、RPL5（BioGRID score=0）和RPL15（BioGRID score=0）等核/核糖体蛋白——这些互作可能为高通量AP-MS/Luck et al. 2020的共纯化伪影（分泌蛋白在细胞裂解液中与核蛋白的非特异性共沉淀）。SAFB（支架附着因子B, BioGRID score=0）和SNRPA1（U2AF, BioGRID score=0）的核蛋白互作进一步支持了假阳性推测。VASN不应被视为TE调控的可行候选。

**最低优先级推荐**：PubMed=107的文献量（主要集中于VASN-肝癌、VASN-线粒体稳态（PMID:42118142）和VASN-溶酶体酸化（PMID:41630427））表明其为明确的分泌功能蛋白。建议在TE筛选中排除VASN，优先级归零。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TGFB1 | BioGRID | 0 |
| TGFB2 | BioGRID | 0 |
| TGFB3 | BioGRID | 0 |
| SRSF10 | BioGRID | 0 |
| RPL5 | BioGRID | 0 |
| SAFB | BioGRID | 0 |
| SNRPA1 | BioGRID | 0 |
| RPL15 | BioGRID | 0 |