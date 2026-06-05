---
type: protein-evaluation
gene: "GON4L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GON4L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GON4L / GON4, KIAA1606, YARP |
| 蛋白名称 | GON-4-like protein |
| 蛋白大小 | 2241 aa / 248.6 kDa |
| UniProt ID | Q3T8J9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 2/10 | ×1 | 2 | 2241 aa / 248.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR049257, IPR009057, IPR003822, IPR036600, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Enhanced |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GON4, KIAA1606, YARP |

**关键文献**:
1. Newly identified Gon4l/Udu-interacting proteins implicate novel functions.. *Scientific reports*. PMID: 32848183
2. Distinct Control of histone H1 expression within the Histone Locus body by CRAMP1.. *bioRxiv : the preprint server for biology*. PMID: 39829857
3. The transcriptional regulator GON4L is required for viability and hematopoiesis in mice.. *Experimental hematology*. PMID: 33864850
4. Gon4l/Udu regulates cardiomyocyte proliferation and maintenance of ventricular chamber identity during zebrafish development.. *Developmental biology*. PMID: 32272116
5. Current insights into the molecular genetic basis of dwarfism in livestock.. *Veterinary journal (London, England : 1997)*. PMID: 28697878

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.7 |
| 高置信度残基 (pLDDT>90) 占比 | 9.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 67.3% |
| 有序区域 (pLDDT>70) 占比 | 23.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.7），有序残基占 23.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049257, IPR009057, IPR003822, IPR036600, IPR001005; Pfam: PF21227, PF02671 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASH1L | 0.959 | 0.076 | — |
| CRAMP1 | 0.872 | 0.783 | — |
| GIGYF2 | 0.791 | 0.044 | — |
| NPAT | 0.637 | 0.095 | — |
| SS18L2 | 0.618 | 0.618 | — |
| H2AX | 0.603 | 0.602 | — |
| ZNF692 | 0.600 | 0.068 | — |
| TTC24 | 0.575 | 0.045 | — |
| NCBP3 | 0.534 | 0.000 | — |
| ACIN1 | 0.525 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ITGB5 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| CRAMP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2BC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PNKD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SS18L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| H2AC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| H2BC26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.7 + PDB: 无 | pLDDT=47.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GON4L — GON-4-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2241 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=47.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3T8J9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116580-GON4L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GON4L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3T8J9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000116580-GON4L/subcellular

![](https://images.proteinatlas.org/57305/942_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/57305/942_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/57305/955_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/57305/955_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/57305/972_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/57305/972_C12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3T8J9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
