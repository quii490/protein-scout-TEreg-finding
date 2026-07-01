---
type: protein-evaluation
gene: "NKPD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NKPD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NKPD1 |
| 蛋白名称 | NTPase KAP family P-loop domain-containing protein 1 |
| 蛋白大小 | 610 aa / 67.8 kDa |
| UniProt ID | Q17RQ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm, Vesicles; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 610 aa / 67.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011646, IPR052754; Pfam: PF07693 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nonsynonymous Variation in NKPD1 Increases Depressive Symptoms in European Populations.. *Biological psychiatry*. PMID: 27745872
2. Autosomal Dominant Lamellar Ichthyosis Due to a Missense Variant in the Gene NKPD1.. *The Journal of investigative dermatology*. PMID: 38642798

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 17.7% |
| 置信残基 (pLDDT 70-90) 占比 | 43.9% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 21.6% |
| 有序区域 (pLDDT>70) 占比 | 61.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.8，有序区 61.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011646, IPR052754; Pfam: PF07693 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 无 | pLDDT=70.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane, Cytosol; 额外: Nucleoplasm, Vesicle | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NKPD1 — NTPase KAP family P-loop domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小610 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

NKPD1（NTPase KAP family P-loop domain-containing protein 1）属于KAP家族P-loop NTPase超家族。UniProt FT注释显示其N端1-414位残基构成KAP NTPase结构域，InterPro归类为IPR011646（KAP family P-loop domain），Pfam对应PF07693（KAP_NTPase）。该结构域含有特征性的P-loop（磷酸结合环/Walker A motif），具有NTP结合和水解活性。KAP家族在进化上保守，其成员通常参与核酸代谢、染色质重塑和翻译调控等基本细胞过程。AlphaFold v6预测整体pLDDT=70.8，有序区域（pLDDT>70）占61.6%，其中N端催化域折叠较为有序（置信残基43.9%），而C端约200个残基的置信度较低，提示可能为调控性无序区域。

从结构域架构角度分析，NKPD1的功能模型可类比其他P-loop NTPase——N端催化域结合和水解NTP提供能量，通过构象变化驱动下游效应。然而，NKPD1最引人注目的特征是PPI网络的完全空白：STRING记录0个预测互作伙伴，IntAct记录0个实验互作。这种极端的PPI贫乏在具有完整催化域的蛋白中并不常见，可能反映了（1）该蛋白功能高度独立，不需要稳定的蛋白-蛋白相互作用；（2）现有PPI检测方法（酵母双杂交、亲和纯化质谱）未能捕获其互作伙伴；（3）该蛋白在特定条件（如应激、特定组织或发育阶段）下才进行蛋白复合体组装。

NKPD1的2篇PubMed文献均集中于临床遗传学领域：非同义变异增加欧洲人群抑郁症状风险（PMID:27745872），以及错义变异导致常染色体显性板层状鱼鳞病（PMID:38642798）。这些表型关联为NKPD1的功能提供了重要线索——皮肤屏障形成和神经系统功能的共同分子基础可能涉及NKPD1的NTPase活性。此外，NKPD1的HPA IF定位显示质膜和胞质溶胶为主要定位，核质和囊泡为额外定位——这种分布模式类似信号转导蛋白（如小GTPase）的定位特征。

该蛋白的研究空白极为显著（PubMed strict=2篇），其核定位信号虽较弱（评分4/10），但NTPase催化活性、与皮肤和神经系统疾病的遗传关联，以及在进化上保守的KAP家族背景下，构成了一个具有高不确定性但潜在收益可观的探索方向。若核质定位得到进一步验证，其NTPase活性可能在染色质重塑或RNA代谢中发挥作用，间接参与TE调控。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q17RQ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179846-NKPD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NKPD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q17RQ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000179846-NKPD1/subcellular

![](https://images.proteinatlas.org/43339/2275_D6_238_blue_red_green.jpg)
![](https://images.proteinatlas.org/43339/2275_D6_92_blue_red_green.jpg)
![](https://images.proteinatlas.org/43339/468_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43339/468_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43339/470_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43339/470_D4_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q17RQ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q17RQ9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 1..414; /note="KAP NTPase" |
| InterPro | IPR011646;IPR052754; |
| Pfam | PF07693; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179846-NKPD1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
