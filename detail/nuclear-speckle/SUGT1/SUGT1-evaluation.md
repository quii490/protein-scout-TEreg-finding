---
type: protein-evaluation
gene: "SUGT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUGT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUGT1 |
| 蛋白名称 | Protein SGT1 homolog |
| 蛋白大小 | 365 aa / 41.0 kDa |
| UniProt ID | Q9Y2Z0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Cytosol; 额外: Acrosome, Flagellar centriole, ; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 365 aa / 41.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.6; PDB: 1RL1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007052, IPR008978, IPR007699, IPR044563, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytosol; 额外: Acrosome, Flagellar centriole, Mid piece, Principal piece, End piece | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- centriole (GO:0005814)
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- nuclear body (GO:0016604)
- protein-containing complex (GO:0032991)
- sperm end piece (GO:0097229)
- sperm midpiece (GO:0097225)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Sugt1 loss in skeletal muscle stem cells impairs muscle regeneration and causes premature muscle aging.. *Life medicine*. PMID: 39872547
2. SUGT1 controls susceptibility to HIV-1 infection by stabilizing microtubule plus-ends.. *Cell death and differentiation*. PMID: 32514048
3. Overexpression of SUGT1 in human colorectal cancer and its clinicopathological significance.. *International journal of oncology*. PMID: 20126976
4. SUGT1 regulates the progression of ovarian cancer through the AKT/PI3K/mTOR signaling pathway.. *Translational oncology*. PMID: 39167956
5. Polycistronic baculovirus expression of SUGT1 enables high-yield production of recombinant leucine-rich repeat proteins and protein complexes.. *Protein expression and purification*. PMID: 35131438

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.6 |
| 高置信度残基 (pLDDT>90) 占比 | 22.5% |
| 置信残基 (pLDDT 70-90) 占比 | 50.7% |
| 中等置信 (pLDDT 50-70) 占比 | 14.5% |
| 低置信 (pLDDT<50) 占比 | 12.3% |
| 有序区域 (pLDDT>70) 占比 | 73.2% |
| 可用 PDB 条目 | 1RL1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=76.6，有序区 73.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007052, IPR008978, IPR007699, IPR044563, IPR011990; Pfam: PF04969, PF05002, PF13432 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSP90AA1 | 0.999 | 0.920 | — |
| HSP90AB1 | 0.998 | 0.748 | — |
| SKP1 | 0.993 | 0.900 | — |
| NOD1 | 0.973 | 0.625 | — |
| NLRP3 | 0.958 | 0.299 | — |
| PHLPP1 | 0.883 | 0.804 | — |
| HSP90B1 | 0.793 | 0.636 | — |
| DNAJC7 | 0.768 | 0.618 | — |
| CHORDC1 | 0.729 | 0.479 | — |
| E5RI56_HUMAN | 0.722 | 0.572 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| PARD6A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14676191 |
| BUB3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NR4A1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PHLPP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| HSP90AA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19875381 |
| recJ | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| LLGL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| EBI-6095589 | psi-mi:"MI:0096"(pull down) | pubmed:21712045|imex:IM-17900 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.6 + PDB: 1RL1 | pLDDT=76.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear bodies, Cytosol; 额外: Acrosome, Flagellar c | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SUGT1 — Protein SGT1 homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小365 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2Z0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165416-SUGT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUGT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2Z0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000165416-SUGT1/subcellular

![](https://images.proteinatlas.org/43949/2215_G10_29_blue_red_green.jpg)
![](https://images.proteinatlas.org/43949/2215_G10_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/43949/776_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/43949/776_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/43949/789_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/43949/899_D5_1_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2Z0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
