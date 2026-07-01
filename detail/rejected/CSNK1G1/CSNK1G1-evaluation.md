---
type: protein-evaluation
gene: "CSNK1G1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CSNK1G1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSNK1G1 |
| 蛋白名称 | non-specific serine/threonine protein kinase |
| 蛋白大小 | 475 aa / 54.5 kDa |
| UniProt ID | U3KQB3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 475 aa / 54.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=71.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 24 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Cell-type-focused compound screen in human organoids reveals CK1 inhibition protects cone photoreceptors from death.. *Neuron*. PMID: 41916277
2. Stage-Resolved Phosphoproteomic Landscape of Mouse Spermiogenesis Reveals Key Kinase Signaling in Sperm Morphogenesis.. *Adv Sci (Weinh)*. PMID: 40903803
3. Differential analysis of testicular LncRNA in Kazakh horses of different ages.. *Int J Biol Macromol*. PMID: 40706934
4. Integration of multi-omics resources reveals genetic features associated with environmental adaptation in the Wuzhishan pig genome.. *J Therm Biol*. PMID: 40921116
5. Genome-wide analysis of genetic loci and candidate genes related to teat number traits in Dongliao black pigs.. *Front Genet*. PMID: 40438329

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 57.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 35.6% |
| 有序区域 (pLDDT>70) 占比 | 62.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.8，有序区 62.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSNK1G2 | 0.000 | 0.000 | — |
| CSNK1G3 | 0.000 | 0.000 | — |
| LRP6 | 0.000 | 0.000 | — |
| TMEM185A | 0.000 | 0.000 | — |
| AXIN1 | 0.000 | 0.000 | — |
| MTF1 | 0.000 | 0.000 | — |
| STK16 | 0.000 | 0.000 | — |
| CD59 | 0.000 | 0.000 | — |
| CTNNB1 | 0.000 | 0.000 | — |
| PPM1B | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9HCP0 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8BTH8 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9HCP0-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P78368 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q8TAP6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:P60409 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:P08754 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P13987 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P35613 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P55084 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 30
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 无 | pLDDT=71.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 深度机制分析

CSNK1G1（酪蛋白激酶1 gamma 1）的结构域架构属于CK1激酶家族的典型模式——N端Ser/Thr蛋白激酶催化域（包含保守的HRD和DFG基序）后接中央富含碱性残基的柔性区域，C端包含可能的自身抑制域。CK1家族特征性地识别pSer/pThr上游的酸性或磷酸化引导残基（S/T-X-X-S*/T*），这一底物选择性使CK1常作为"层级磷酸化"激酶——需要先前的磷酸化事件作为其底物结合的先决条件。

475 aa（54.5 kDa）的分子量在CK1家族中属于中等。AlphaFold v6 pLDDT为71.8，其中57.5%残基pLDDT>90的高置信区主要分布于激酶域，而低置信区（35.6%，pLDDT<50）集中在C端调控区，提示该区域具有天然无序特性——这是信号蛋白自抑制和多重互作的常见特征。PPI数据较为丰富：STRING鉴定15个预测互作（包含CSNK1G2/G3同工酶、LRP6、AXIN1、CTNNB1等Wnt通路核心组分），IntAct实验验证30个互作，17个来自pull down和抗标签共免疫沉淀的高置信实验方法。

TE调控相关性的机制推论集中于CSNK1G1在Wnt/beta-catenin和Hippo信号通路中的交叉角色：CSNK1G1通过磷酸化LRP6（共受体）和AXIN1（脚手架蛋白），调控beta-catenin的稳定化和核转位，影响TCF/LEF靶基因的转录。若TCF/LEF结合位点富集于特定TE家族的启动子区域（如MaLR/LTR中的TCF基序），CK1的磷酸化级联可能经Wnt信号传递至这些TE，实现信号依赖的TE激活。此外，CK1家族的广泛底物谱（包括哺乳动物昼夜节律蛋白PER、DNA损伤应答蛋白XRCC1/XRCC4等）暗示其可能通过多维度通路间接影响TE转录。

但CSNK1G1因**核定位得分2/10**被Rejected，HPA和UniProt均显示Cytosol/Cytoplasm定位，无核内集中分布证据。这一REJECTED判定是合理的——CK1蛋白主要在胞质中发挥信号转导功能，直接转录调控相关性较弱。归一化总分56.4/100。该蛋白不应作为TE调控靶标，建议作为Wnt通路信号细胞质部分的基础研究参考。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CSNK1G1 -- non-specific serine/threonine protein kinase，非常新颖，仅有少数基础研究。
2. 蛋白大小475 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/U3KQB3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169118-CSNK1G1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSNK1G1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/U3KQB3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-U3KQB3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
