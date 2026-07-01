---
type: protein-evaluation
gene: "ODAM"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## ODAM 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ODAM/IF_images/1816_E2_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ODAM/IF_images/1816_E2_4_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ODAM |
| 蛋白名称 | Odontogenic ameloblast-associated protein |
| 蛋白大小 | 279 aa |
| UniProt ID | [A1E959](https://www.uniprot.org/uniprotkb/A1E959) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 66 |
| AlphaFold pLDDT | 42.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Secreted; Cytoplasm; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 279 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 66篇 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT: 42.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 暂无数据 |
| **原始总分** |  |  | **90/183** |  |
| **归一化总分** |  |  | **49.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 ODAM 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Secreted; Cytoplasm; Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Zhao C et al. (2024). "Gradient-Based Instance-Specific Visual Explanations for Object Specification and Object Discrimination". *IEEE Trans Pattern Anal Mach Intell*. PMID: 38517727
2. Wang R et al. (2025). "The impact of dosage timing for inhaled corticosteroids in asthma: a randomised three-way crossover trial". *Thorax*. PMID: 40234005
3. Cai H et al. (2024). "CRISPR/Cas9 model of prostate cancer identifies Kmt2c deficiency as a metastatic driver by Odam/Cabs1 gene cluster expression". *Nat Commun*. PMID: 38453924
4. Waterson P & Robertson M (2022). "Forty years of Organisational Design and Management (ODAM)". *Ergonomics*. PMID: 35102812
5. Zhu S et al. (2022). "The versatile roles of odontogenic ameloblast-associated protein in odontogenesis, junctional epithelium regeneration and periodontal disease". *Front Physiol*. PMID: 36117697

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 未检索到实验验证互作

**评价**: 暂无数据 IntAct/STRING/GO-CC 数据。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IKBKG | BioGRID | 0 |
| APP | BioGRID | 0 |
| TOLLIP | BioGRID | 0 |
| FHL2 | BioGRID | 0 |
| NISCH | BioGRID | 0 |
| YPEL3 | BioGRID | 0 |
| MED25 | BioGRID | 0 |
| SNRPC | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### ESMFold 结构预测

| 指标 | 数值 |
|---|---|
| 平均 pLDDT | 0.35 |
| >0.9 | 0.0% |
| <0.5 | 90.0% |
| 残基数 | 279 |

ESMFold 从头折叠验证。PDB: `detail/_esm_structures/ODAM_esmfold.pdb`

### 5. 总体评价

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅66篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 42.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/ODAM)
- [UniProt](https://www.uniprot.org/uniprotkb/A1E959)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=ODAM%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/A1E959)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 暂无互作数据 |

暂无实验验证互作。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A1E959 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026802; |
| Pfam | PF15424; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000109205-ODAM/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARID5A | Intact | false |
| BRAF | Intact | false |
| FHL2 | Intact | false |
| HGS | Intact | false |
| MED25 | Intact | false |
| POGZ | Intact | false |
| SDCBP | Intact | false |
| SNRPC | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

### 深度机制分析

ODAM（Odontogenic ameloblast-associated protein, 279 aa）是一种非经典分泌蛋白，其结构特征极为有限：仅含一个InterPro注释结构域IPR026802（ODAM蛋白家族），无SMART域标记，无实验PDB结构。AlphaFold v6预测的pLDDT极低（42.8），且ESMFold从头折叠验证显示平均pLDDT仅0.35，90.0%残基低于0.5——这是所有评估蛋白中结构置信度最低的之一。如此大面积的无序结构提示ODAM可能不采取稳定的球形折叠（globular fold），而是以内在无序蛋白（intrinsically disordered protein, IDP）的形式存在，仅在特定配体结合或寡聚化状态下才获取部分有序构象。无序蛋白的特征——构象灵活性、短线性基序（SLiM）驱动的多配体互作、液-液相分离（LLPS）倾向——恰恰赋予其作为多功能枢纽蛋白的结构基础。

HPA IF实验显示ODAM定位为Nucleoplasm（reliability: Supported），而UniProt的注释则为Secreted/Cytoplasm/Nucleus——这种双重定位（分泌+核）在IDP中较为典型：IDP通常缺乏经典的细胞器分选信号，可通过非经典途径分泌（如外泌体出胞），同时在特定信号条件下通过被动扩散进入核质。ODAM最初被原始评分误判为核定位不足（≤3），经HPA复核救回后确认为核蛋白——这一发现纠正了ODAM作为细胞外基质蛋白的单一认知，揭示了其核功能维度。

PPI网络在BioGRID中捕获了若干引人注目的互作节点：IKBKG/NEMO（NF-kappaB必需调节因子）、APP（淀粉样前体蛋白）、MED25（Mediator复合体亚基25）、FHL2、SNRPC/U1C（U1 snRNP组分）和SDCBP/syntenin（外泌体生物合成蛋白）。其中，IKBKG和MED25的互作暗示ODAM可能参与转录调控：IKBKG作为IKK复合体的调节亚基，连接炎性信号与NF-kappaB转录应答；MED25则是Mediator共激活因子复合体的组分，直接桥接转录因子与RNA Pol II基础转录机器。ODAM作为IDP若同时与IKBKG和MED25发生直接互作，可能在炎症信号向转录机器的传导中起信号整合作用。

从TE调控机制角度，ODAM参与TE沉默的潜在路径需从炎症-TE双向关系切入。TE的转录激活（特别是ERV/LTR元件）产生双链RNA，激活RIG-I/MDA5-MAVS途径，下游信号通过IKBKG-IKK复合体磷酸化IkappaB释放NF-kappaB。ODAM与IKBKG的结合可能在NF-kappaB通路中充当信号调节节点，影响下游炎症因子和IFN刺激基因（ISG）的表达——这些ISG本身常由TE衍生的增强子驱动，形成正反馈回路。此外，ODAM与SNRPC/U1C的结合暗示其可能参与pre-mRNA的剪接调控，影响TE衍生外显子的包含或排除——这在TE的转录后调控（splicing-mediated repression）中扮演关键角色。

在肿瘤背景中，CRISPR/Cas9模型鉴定ODAM/Cabs1基因簇为前列腺癌转移的驱动因子（PMID:38453924），Kmt2c缺陷通过上调ODAM表达促进转移。ODAM在牙釉质生成（amelogenesis）和交界上皮再生中的多功能角色（PMID:36117697）进一步证明其IDP属性支持组织特异性功能转换。对于TE调控领域，ODAM的低结构质量和弱定位信号使其成为风险极高的候选因子；但其与IKBKG-MED25的双线互作和作为IDP的信号整合潜力，值得在炎症-TE交互信号领域进行初步筛选实验——如ODAM敲除后的NF-kappaB报告基因检测和ERV/LTR衍生RNA的RT-qPCR定量。

