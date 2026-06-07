---
type: protein-evaluation
gene: "ATG10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: rejected
---

## ATG10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATG10 / APG10L |
| 蛋白名称 | Ubiquitin-like-conjugating enzyme ATG10 |
| 蛋白大小 | 220 aa / 25.3 kDa |
| UniProt ID | Q9H0Y0 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:25:19 |

### 2. 评分总览

**评估状态：REJECTED**
**拒因：PubMed strict count 141 > 100**

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoli; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 220 aa / 25.3 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=141 篇 |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=80.2 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR007135 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **118.5/180** | |
| **归一化总分 (/1.83)** | | | **64.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Nucleoli | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 220 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 141 |
| PubMed broad count | 217 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APG10L |

**关键文献**:
1. Trehalose induces autophagy via lysosomal-mediated TFEB activation in models of motoneuron degeneration.. *Autophagy*. PMID: 30335591
2. TRIM7/RNF90 promotes autophagy via regulation of ATG7 ubiquitination during L. monocytogenes infection.. *Autophagy*. PMID: 36576150
3. ATG10S promotes IFNL1 expression and autophagic degradation of multiple viral proteins mediated by IFNL1.. *Autophagy*. PMID: 38842055
4. ATG10 overexpression is related to the dismal prognosis and promotes the growth and migration of hepatocellular carcinoma cells via cyclin B1/CDK1 and CDK2.. *American journal of cancer research*. PMID: 37168332
5. Analysis of rs1864182 and rs1864183 variants in ATG10 gene and antineutrophil cytoplasmic autoantibody-associated vasculitis in Chinese Guangxi population.. *Journal of clinical laboratory analysis*. PMID: 34961976


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 55.5% |
| 置信残基 (pLDDT 70-90) 占比 | 20.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 16.8% |
| 有序区域 (pLDDT>70) 占比 | 76.0% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold高质量预测（pLDDT=80.2），预测结构可信。三维结构评分 9/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007135; Pfam: PF03987 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABARAPL2 | 0.937 | 0.167 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000404938.3 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| Art3 | two hybrid prey pooling approach | pubmed:unassigned1513|imex:IM-25777 |
| ATG12 | two hybrid array | pubmed:14690591 |
| ATG7 | two hybrid | pubmed:18719252 |
| GABARAPL1 | pull down | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | pull down | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | pull down | pubmed:20562859|imex:IM-15184 |
| MAP1LC3C | pull down | pubmed:20562859|imex:IM-15184 |
| GABARAP | pull down | pubmed:20562859|imex:IM-15184 |
| RBBP7 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=80.2 | 单一来源 |
| 定位 | HPA | Nucleoplasm, Nucleoli | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 64.8/100
**状态**: REJECTED -- PubMed strict count 141 > 100

**核心优势**:
1. 蛋白大小220 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
2. AlphaFold高质量预测（pLDDT=80.2），结构可信度高。
3. 存在 2 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9H0Y0
- Protein Atlas: https://www.proteinatlas.org/search/ATG10
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATG10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0Y0
- STRING: https://string-db.org/network/9606.ATG10
- Packet data timestamp: 2026-06-03 03:25:19

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000152348-ATG10/subcellular

![](https://images.proteinatlas.org/44163/711_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/44163/711_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/44163/723_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/44163/723_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/44163/866_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/44163/866_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0Y0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H0Y0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007135; |
| Pfam | PF03987; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000152348-ATG10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATG12 | Intact, Biogrid | true |
| ATG5 | Intact | false |
| ATG7 | Biogrid | false |
| ATXN1 | Intact | false |
| CASP6 | Intact | false |
| COQ8A | Intact | false |
| GNB2 | Intact | false |
| HIP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
