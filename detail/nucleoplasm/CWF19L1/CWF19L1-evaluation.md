---
type: protein-evaluation
gene: "CWF19L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CWF19L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CWF19L1 |
| 蛋白名称 | CWF19-like protein 1 |
| 蛋白大小 | 538 aa / 60.6 kDa |
| UniProt ID | Q69YN2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 538 aa / 60.6 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=14 篇 (<=20->10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=83.4; PDB: 8RO2 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR040194, IPR006768, IPR006767, IPR036265; Pfam:  |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- post-mRNA release spliceosomal complex (GO:0071014)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 20 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The ERLIN1-CHUK-CWF19L1 gene cluster influences liver fat deposition and hepatic inflammation in the NHLBI Family Heart Study.. *Atherosclerosis*. PMID: 23477746
2. Expression patterns and functional analysis of porcine lnc-34015.. *Animal biotechnology*. PMID: 35714975
3. Heterozygous pathogenic variants in CWF19L1 in a Chinese family with spinocerebellar ataxia, autosomal recessive 17.. *Journal of clinical laboratory analysis*. PMID: 36357319
4. Identification of lncRNA-based regulatory mechanisms of Takifugu rubripes growth traits in fast and slow-growing family lines.. *Comparative biochemistry and physiology. Part D, Genomics & proteomics*. PMID: 37976965
5. A Novel Variant in CWF19L1 Gene in a Family with Late-Onset Autosomal Recessive Cerebellar Ataxia 17.. *Neurological research*. PMID: 33012273

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.4 |
| 高置信度残基 (pLDDT>90) 占比 | 51.1% |
| 置信残基 (pLDDT 70-90) 占比 | 36.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 87.3% |
| 可用 PDB 条目 | 8RO2 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.4，有序区 87.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040194, IPR006768, IPR006767, IPR036265; Pfam: PF04677, PF04676 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOM1L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| DBR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| H2BC15 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SMG7 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CWF19L2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SNRPE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.4 + PDB: 8RO2 | pLDDT=83.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CWF19L1 -- CWF19-like protein 1，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小538 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q69YN2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000095485-CWF19L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CWF19L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q69YN2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000095485-CWF19L1/subcellular

![](https://images.proteinatlas.org/36890/403_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/36890/403_C4_3_red_green.jpg)
![](https://images.proteinatlas.org/36890/406_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/36890/406_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/36890/408_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/36890/408_C4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q69YN2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q69YN2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040194;IPR006768;IPR006767;IPR036265; |
| Pfam | PF04677;PF04676; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000095485-CWF19L1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DNAJC17 | Biogrid, Opencell | true |
| CWF19L2 | Intact | false |
| METAP2 | Opencell | false |
| PRPF8 | Biogrid | false |
| PTGES3 | Opencell | false |
| SNRPB | Opencell | false |
| YWHAB | Opencell | false |
| YWHAE | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
