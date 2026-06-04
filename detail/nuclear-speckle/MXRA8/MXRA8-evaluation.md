---
type: protein-evaluation
gene: "MXRA8"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MXRA8 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MXRA8 |
| 别名 | — |
| 基因全称 | matrix remodeling associated 8 |
| 蛋白名称 | Matrix remodeling-associated protein 8 |
| 蛋白大小 | 442 aa |
| UniProt ID | Q9BRK3 |
| 评估日期 | 2026-01-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/MXRA8/IF_images/CACO_2_1.jpg|CACO_2]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/MXRA8/IF_images/Hep_G2_1.jpg|Hep_G2]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nuclear speckles |
| Size 蛋白大小 | 10/10 | x1 | 10 | 442 aa |
| Novelty 研究新颖性 | 6/10 | x5 | 30 | PubMed: 59 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=75.8 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 无已注释染色质调控结构域 |
| PPI Network PPI网络 | 2/10 | x3 | 6 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
| **原始总分** |  |  | **114/183** |  |
| **归一化总分** |  |  | **62.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | CACO-2, Hep-G2 | HPA validated |
| UniProt | Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IEA|NAS) | — |

#### 3.2 蛋白大小评估

442 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 59 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Kumar et al. (2021). "Chikungunya and arthritis: An overview.". *Travel Med Infect Dis*. PMID: 34563686
2. Zhang et al. (2025). "Associations of 2923 plasma proteins with incident inflammatory bowel disease in a prospective cohort study and genetic analysis.". *Nat Commun*. PMID: 40118817
3. Zhang et al. (2018). "Mxra8 is a receptor for multiple arthritogenic alphaviruses.". *Nature*. PMID: 29769725
4. Zimmerman et al. (2023). "Vertebrate-class-specific binding modes of the alphavirus receptor MXRA8.". *Cell*. PMID: 37804831
5. Qiu et al. (2021). "Single-cell RNA sequencing of human femoral head in vivo.". *Aging (Albany NY)*. PMID: 34111027
**评价**: PubMed 59 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 75.8 |
| pLDDT > 90 占比 | 46.6% |
| pLDDT 70-90 占比 | 18.1% |
| pLDDT 50-70 占比 | 14.3% |
| pLDDT < 50 占比 | 21.0% |
| 可用 PDB 条目 | 1 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/MXRA8/MXRA8-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=75.8, >90=47%, 70-90=18%, 50-70=14%, <50=21%. PDB entries: 6JO8)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 无已注释染色质调控结构域

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-915426|uniprotkb:P97900|ensembl:ENSRNOP00000023256.3 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:16396496|mint:MINT-5218203 | — | — |
| intact:EBI-948354|uniprotkb:Q7L3U8|uniprotkb:Q9NXB2|uniprotkb:A8MZ52|uniprotkb:B3KP62|uniprotkb:B4DN65|uniprotkb:Q9H6G3|uniprotkb:Q2M248|ensembl:ENSP00000261647.5 | MI:0397(two hybrid array) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-17183751|ensembl:ENSP00000496476.1 | MI:0397(two hybrid array) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-741158|uniprotkb:B4DE68|uniprotkb:Q9NW95|ensembl:ENSP00000287387.2 | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| intact:EBI-11721798|uniprotkb:B3KTR6|uniprotkb:B4DE34|uniprotkb:Q5TA39|uniprotkb:Q96KC3|ensembl:ENSP00000307887.6 | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| FAM20A | 0.0 | — | — |
| BACE1 | 0.0 | — | — |
| RHO | 0.0 | — | — |
| JAG2 | 0.0 | — | — |
| FAM20C | 0.0 | — | — |
| ADRB2 | 0.0 | — | — |
| MXRA7 | 0.0 | — | — |
| NAPSA | 0.0 | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 9
- 调控相关比例: 1/15 (7%)

**评价**: PPI 得分 2/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=75.8, PDB=1 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/9/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear speckles / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- PDB+AlphaFold 双源确认 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 有一定研究基础 (PubMed 59 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MXRA8
- Protein Atlas: https://www.proteinatlas.org/MXRA8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MXRA8
- UniProt: https://www.uniprot.org/uniprotkb/Q9BRK3
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRK3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MXRA8-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/MXRA8/MXRA8-PAE.png]]




