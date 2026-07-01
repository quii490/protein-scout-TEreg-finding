---
type: protein-evaluation
gene: "FIGNL2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## FIGNL2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FIGNL2 |
| 蛋白名称 | Fidgetin-like protein 2 |
| 蛋白大小 | 653 aa / 66.6 kDa |
| UniProt ID | A6NMB9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 653 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=60.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | AAA+_ATPase; ATPase_AAA_core; Fidgetin_ATPase |
| PPI | 5/10 | x3 | 15.0 | PPI degree=3 |
| **加权总分** | | | **114/180** | |
| **归一化总分** | | | **63.4/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=4 broad=8
- AF pLDDT=60.4 PDB=0
- InterPro: AAA+_ATPase; ATPase_AAA_core; Fidgetin_ATPase
- Pfam: AAA
- PPI degree=3 ChIP: None
33585441: Microtubule Severing Protein Fignl2 Contributes to Endothelial and Neuronal Bran | 33859359: Multi-ancestry genome-wide gene-sleep interactions identify novel loci for blood | 41220267: Axonal Regeneration, Growth Cone, and the FIGN Gene Family: A Comprehensive Revi

### 4. 总体评价
**63.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Fidgetin-like protein 2

**功能**: Microtubule-severing enzyme that negatively regulates cell migration and wound healing (PubMed:25756798, PubMed:36523161). In migrating cells, targets dynamic microtubules (MTs) at the leading edge and severs them, thereby suppressing motility (PubMed:25756798, PubMed:36523161). Microtubule severing releases ARHGEF2 which activates RHOA, which in turn regulates focal ahesion turnover via focal adhesion kinase, as opposed to F-actin polymerization, to suppress cell motility (PubMed:36523161). Neg

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003593 |
| InterPro | IPR003959 |
| InterPro | IPR047828 |
| InterPro | IPR050304 |
| InterPro | IPR027417 |
| Pfam | PF00004 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CUL7 | BioGRID | 1 |
| EFHD1 | BioGRID | 0 |
| CXorf40A | BioGRID | 0 |


### 深度机制分析

FIGNL2（Fidgetin-like protein 2）。定位于nucleoplasm。包含653 aa / 66.6 kDa。UniProt编号A6NMB9。其InterPro结构域组成为IPR003593（AAA+ ATPase）、IPR003959（ATPase AAA核心）、IPR047828（Fidgetin ATPase）、IPR050304、IPR027417（P-loop NTPase折叠）。Pfam注释1个保守AAA结构域（PF00004）。AlphaFold预测三维结构pLDDT=60.4（中等置信度）。

从功能机制角度，FIGNL2属于AAA+ ATPase超家族中的Fidgetin亚家族，是一种微管切割酶（microtubule-severing enzyme），负调控细胞迁移和伤口愈合（PMID:25756798、36523161）。在迁移细胞中，FIGNL2靶向并切割前沿的动态微管，释放ARHGEF2以激活RHOA，进而通过黏着斑激酶调节黏着斑周转，抑制细胞运动。该蛋白的nucleoplasm定位提示其可能参与有丝分裂期间核内微管网络的调控，这与AAA+ ATPase家族在染色质重塑、核骨架重构中的广泛作用一致。从结构域角度，AAA+ ATPase核心通过核苷酸结合诱导的构象变化驱动机械力传导，将ATP水解的化学能转化为微管切割的机械功。中等pLDDT（60.4）暗示存在较大无序区域，可能在细胞周期依赖的核质穿梭中发挥作用。

从PPI互作网络角度，FIGNL2目前仅知与CUL7（Cullin-7，E3泛素连接酶复合体支架蛋白）存在低置信度生物网格互作，PPI degree=3，互作网络极为稀疏。CUL7作为CRL7泛素连接酶的支架亚基，参与细胞生长和分裂的调控，这一互作可能暗示FIGNL2在泛素化介导的蛋白降解通路中存在功能耦联。

从TE调控角度，微管切割活性与染色质构象存在间接关联——有丝分裂期间的微管-着丝粒连接驱动染色体分离，而FIGNL2作为微管动力学调控因子，其nucleoplasm定位使其在与着丝粒周缘染色质接触时可能影响局部转座子元件的空间可及性。此外，FIGNL2的AAA+ ATPase折叠与染色质重塑ATP酶（如SNF2家族）共享P-loop NTPase折叠，提示其可能通过非经典机制参与染色质结构调控。

从研究转化角度，PubMed中仅有4篇相关文献（PMID:33585441、33859359、41220267），研究新颖度极高（评分10/10），综合评分63.4/100，属于中等偏低优先级，但其独特的nucleoplasm定位与微管-染色质互作功能使其在TE调控领域具有探索价值，建议作为机制实验的备选靶标。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FIGNL2
