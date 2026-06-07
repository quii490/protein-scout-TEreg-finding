---
type: protein-evaluation
gene: "TPPP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TPPP — REJECTED (研究热度过高 (PubMed strict=152，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TPPP / TPPP1 |
| 蛋白名称 | Tubulin polymerization-promoting protein |
| 蛋白大小 | 219 aa / 23.7 kDa |
| UniProt ID | O94811 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Golgi outpost; Cytoplasm, cytoskeleton, microtubule organizi |
| 蛋白大小 | 10/10 | ×1 | 10 | 219 aa / 23.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=152 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.1; PDB: 9J4D, 9J4E, 9J4F |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR008907; Pfam: PF05517 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Golgi outpost; Cytoplasm, cytoskeleton, microtubule organizing center; Cytoplasm, cytoskeleton; Nucl... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- microtubule organizing center (GO:0005815)
- mitochondrion (GO:0005739)
- mitotic spindle (GO:0072686)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 152 |
| PubMed broad count | 262 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TPPP1 |

**关键文献**:
1. Autophagy mediates the clearance of oligodendroglial SNCA/alpha-synuclein and TPPP/p25A in multiple system atrophy models.. *Autophagy*. PMID: 35000546
2. Tubulin Polymerization Promoting Protein (TPPP) gene methylation and corpus callosum measures in maltreated children.. *Psychiatry research. Neuroimaging*. PMID: 32120304
3. Alpha synuclein-mediated cytoskeletal dysfunction impairs myelination in human oligodendrocytes.. *Acta neuropathologica*. PMID: 40973885
4. Dual life of TPPP/p25 evolved in physiological and pathological conditions.. *Biochemical Society transactions*. PMID: 25399603
5. Role of the microtubule-associated TPPP/p25 in Parkinson's and related diseases and its therapeutic potential.. *Expert review of proteomics*. PMID: 28271739

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.1 |
| 高置信度残基 (pLDDT>90) 占比 | 40.2% |
| 置信残基 (pLDDT 70-90) 占比 | 34.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 18.3% |
| 有序区域 (pLDDT>70) 占比 | 74.4% |
| 可用 PDB 条目 | 9J4D, 9J4E, 9J4F |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（9J4D, 9J4E, 9J4F）+ AlphaFold高质量预测（pLDDT=78.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR008907; Pfam: PF05517 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCTN2 | 0.968 | 0.000 | — |
| DCTN1 | 0.959 | 0.000 | — |
| SNCA | 0.923 | 0.694 | — |
| CAPZA2 | 0.902 | 0.000 | — |
| CAPZA1 | 0.900 | 0.000 | — |
| ACTR10 | 0.858 | 0.000 | — |
| ACTR3C | 0.847 | 0.000 | — |
| ACTR3B | 0.844 | 0.000 | — |
| HDAC6 | 0.816 | 0.512 | — |
| DCTN4 | 0.806 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Invs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| CDK11B | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SNCA | psi-mi:"MI:0096"(pull down) | pubmed:18614564|imex:IM-19211 |
| H1-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HMGN2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DDB2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CDRT15P3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF114 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.1 + PDB: 9J4D, 9J4E, 9J4F | pLDDT=78.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi outpost; Cytoplasm, cytoskeleton, microtubul / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. TPPP — Tubulin polymerization-promoting protein，研究基础较多，新颖性有限。
2. 蛋白大小219 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 152 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 152 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94811
- Protein Atlas: https://www.proteinatlas.org/search/TPPP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TPPP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94811
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000171368-TPPP/subcellular

![](https://images.proteinatlas.org/36576/1682_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36576/1682_G7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/36576/1719_G6_13_cr5804b9c2eecf2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36576/1719_G6_18_cr5804b9cccd554_blue_red_green.jpg)
![](https://images.proteinatlas.org/36576/606_A5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36576/606_A5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94811-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94811 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011992;IPR008907; |
| Pfam | PF05517; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171368-TPPP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SNCA | Intact, Biogrid | true |
| DCAF10 | Bioplex | false |
| DYNLL2 | Biogrid | false |
| GNB2 | Bioplex | false |
| H1-1 | Intact | false |
| HDAC6 | Biogrid | false |
| LIN28A | Bioplex | false |
| MAGEB6 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
