---
type: protein-evaluation
gene: "HMX3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HMX3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HMX3 / HMX3, MNAR |
| 蛋白名称 | Proline-, glutamic acid- and leucine-rich protein 1 |
| 蛋白大小 | 1130 aa / 119.7 kDa |
| UniProt ID | Q8IZL8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centriolar satellite; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm; Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1130 aa / 119.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 7UWF, 8FL2, 8FL3, 8FL4, 9DUM, 9DUO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR012980, IPR012583; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centriolar satellite | Approved |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- euchromatin (GO:0000791)
- membrane (GO:0016020)
- MLL1 complex (GO:0071339)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HMX3, MNAR |

**关键文献**:
1. Analyses of binding partners and functional domains for the developmentally essential protein Hmx3a/HMX3.. *Scientific reports*. PMID: 36670152
2. HMX3 is a critical vulnerability in MECOM-negative KMT2A::MLLT3 acute myelomonocytic leukemia.. *Leukemia*. PMID: 39633068
3. Hmx2 and Dmrt2 Coordinate the Differentiation of Intercalated Cell Subtypes in Kidney.. *Journal of the American Society of Nephrology : JASN*. PMID: 41051882
4. USP38 inhibits colorectal cancer cell proliferation and migration via downregulating HMX3 ubiquitylation.. *Cell cycle (Georgetown, Tex.)*. PMID: 36204976
5. Inner ear and maternal reproductive defects in mice lacking the Hmx3 homeobox gene.. *Development (Cambridge, England)*. PMID: 9435283

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 24.0% |
| 置信残基 (pLDDT 70-90) 占比 | 21.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 43.6% |
| 有序区域 (pLDDT>70) 占比 | 45.9% |
| 可用 PDB 条目 | 7UWF, 8FL2, 8FL3, 8FL4, 9DUM, 9DUO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 45.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR012980, IPR012583; Pfam: PF08166, PF08167 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP1R21 | 0.782 | 0.782 | — |
| HINFP | 0.782 | 0.782 | — |
| WNT7A | 0.751 | 0.000 | — |
| LHX6 | 0.682 | 0.134 | — |
| GAL | 0.668 | 0.000 | — |
| DTNA | 0.580 | 0.572 | — |
| DTNB | 0.580 | 0.572 | — |
| ISY1-RAB43 | 0.572 | 0.572 | — |
| ISY1 | 0.572 | 0.572 | — |
| WNT4 | 0.550 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NFKB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20195357|imex:IM-20475 |
| ESR1 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13780|pubmed:21182205 |
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| PELP1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| WDR18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OBI1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| NOL9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 7UWF, 8FL2, 8FL3, 8FL4, 9DUM,  | pLDDT=63.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm; Nucleus; / Nucleoplasm; 额外: Centriolar satellite | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HMX3 — Proline-, glutamic acid- and leucine-rich protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1130 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZL8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188620-HMX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HMX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZL8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000188620-HMX3/subcellular

![](https://images.proteinatlas.org/69659/1335_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/69659/1335_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/69659/1352_A9_5_red_green.jpg)
![](https://images.proteinatlas.org/69659/1352_A9_6_red_green.jpg)
![](https://images.proteinatlas.org/69659/1411_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/69659/1411_F12_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZL8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IZL8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR012980;IPR012583; |
| Pfam | PF08166;PF08167; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188620-HMX3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| USP38 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
