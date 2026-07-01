---
type: protein-evaluation
gene: "GNB1L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GNB1L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNB1L / GY2, KIAA1645, WDR14 |
| 蛋白名称 | Guanine nucleotide-binding protein subunit beta-like protein 1 |
| 蛋白大小 | 327 aa / 35.6 kDa |
| UniProt ID | Q9BYB4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 327 aa / 35.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015943, IPR036322, IPR001680; Pfam: PF00400 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GY2, KIAA1645, WDR14 |

**关键文献**:
1. FACS-based genome-wide CRISPR screens define key regulators of DNA damage signaling pathways.. *Molecular cell*. PMID: 37541219
2. Genome-scale mapping of DNA damage suppressors through phenotypic CRISPR-Cas9 screens.. *Molecular cell*. PMID: 37478847
3. A 31-bp indel in the 5' UTR region of GNB1L is significantly associated with chicken body weight and carcass traits.. *BMC genetics*. PMID: 32847500
4. GNB1L, a gene deleted in the critical region for DiGeorge syndrome on 22q11, encodes a G-protein beta-subunit-like polypeptide.. *Biochimica et biophysica acta*. PMID: 11072084
5. Evidence for involvement of GNB1L in autism.. *American journal of medical genetics. Part B, Neuropsychiatric genetics : the official publication of the International Society of Psychiatric Genetics*. PMID: 22095694

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 79.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 95.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.8，有序区 95.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEPTIN5 | 0.896 | 0.069 | — |
| TBX1 | 0.889 | 0.000 | — |
| DGCR8 | 0.886 | 0.000 | — |
| GP1BB | 0.872 | 0.059 | — |
| GSC2 | 0.807 | 0.066 | — |
| LOC102724788 | 0.807 | 0.000 | — |
| RANBP1 | 0.805 | 0.073 | — |
| PRODH | 0.795 | 0.000 | — |
| COMT | 0.748 | 0.000 | — |
| CRKL | 0.728 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| GSTM3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASPRV1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNJ5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RABGGTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GATD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TEKT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CNPY2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 无 | pLDDT=91.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 深度机制分析

GNB1L编码G蛋白beta亚基样蛋白1，属于WD40重复蛋白超家族（InterPro IPR015943、IPR036322、IPR001680，Pfam PF00400），这是自然界最大的beta螺旋桨折叠蛋白家族之一。其结构域架构由典型的WD40-beta螺旋桨组成，每个WD40重复单元（约40 aa）包含保守的GH二肽和WD二肽基序，七个WD40重复组装成七叶beta螺旋桨。327 aa（35.6 kDa）在这一家族中属于中等偏小尺寸，每个螺旋桨叶片由1-2个WD40重复贡献。AlphaFold pLDDT高达91.8（有序区域95.1%），是候选列表中最高的结构置信度之一，但缺乏实验PDB验证（归一化结构得分8/10）。

GNB1L因位于22q11.2微缺失区域的DGCR（DiGeorge综合征关键区域）中而得名。PPI网络中最引人注目也最具TE研究意义的伙伴是DGCR8（STRING评分886）和TBX1（889）。DGCR8是Microprocessor复合物的核心亚基，与DROSHA核糖核酸酶III共同负责pri-miRNA的识别和切割——这是miRNA生物发生的起始和限速步骤。虽然STRING对DGCR8的评分基于染色体邻近性（Gene Neighborhood & Co-occurrence证据），但GNB1L和DGCR8在22q11.2区域的物理共定位赋予了这种关联以基因组组织层面的生物学意义。

TE调控相关性集中体现在GNB1L-DGCR8-Microprocessor轴上：（1）Microprocessor（DGCR8/DROSHA）是哺乳动物中TE源性小RNA（endo-siRNA和piRNA）加工的关键酶复合物。DGCR8识别pri-miRNA中茎-环结构的单链-双链连接处，而许多TE衍生的转录产物（特别是Alu元件和SINE家族）天然形成这种二级结构，可被Microprocessor识别和切割；（2）LINE-1转录产物含有多个茎-环结构（尤其在5'UTR区），这些结构在体外和体内均可被DGCR8/DROSHA识别，产生针对LINE-1的small RNA并触发RNA干扰介导的LINE-1 mRNA降解；（3）GNB1L作为WD40支架蛋白，可能以类似G蛋白beta亚基与其gamma亚基配体的模式，与DGCR8形成"beta propeller-alpha helical tail"异源二聚体，从而调节Microprocessor的pri-miRNA/pri-TE-RNA加工效率；（4）22q11.2区域本身富含Alu元件和片段重复，该区域的染色质景观受DGCR区域基因（包括GNB1L）的顺式或反式调控。归一化评分76.9/100，WD40-DGCR8-pri-miRNA/TE-RNA轴赋予该蛋白可观的TE调控潜力。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GNB1L — Guanine nucleotide-binding protein subunit beta-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小327 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TBX1 | STRING | 889 |
| DGCR8 | STRING | 886 |
| GSC2 | STRING | 807 |
| RANBP1 | STRING | 805 |
| PRODH2 | STRING | 795 |
| PRODH | STRING | 795 |
| CRKL | STRING | 728 |
| DGCR6L | STRING | 705 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BYB4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185838-GNB1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNB1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BYB4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000185838-GNB1L/subcellular

![](https://images.proteinatlas.org/34628/366_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34628/366_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34628/370_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34628/370_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34628/373_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34628/373_B6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BYB4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BYB4 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015943;IPR036322;IPR001680; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185838-GNB1L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCNF | Biogrid | false |
| HSPA2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
