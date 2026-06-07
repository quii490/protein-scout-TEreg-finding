---
type: protein-evaluation
gene: "BICD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: rejected
---

## BICD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BICD2 / KIAA0699 |
| 蛋白名称 | Protein bicaudal D homolog 2 |
| 蛋白大小 | 824 aa / 93.5 kDa |
| UniProt ID | Q8TD16 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:36:34 |

**IF 图像**:
![](https://images.proteinatlas.org/23013/193_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23013/193_H4_2_blue_red_green.jpg)

### 2. 评分总览

**评估状态：REJECTED**
**拒因：PubMed strict count 116 > 100**

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Golgi apparatus, Plasma membrane... |
| 蛋白大小 | 7/10 | x1 | 7 | 824 aa / 93.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=116 篇 |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=78.0; PDB: 6OFP, 6PSE |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR018477 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **92.0/180** | |
| **归一化总分 (/1.83)** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Golgi apparatus, Plasma membrane, Cytosol | Supported |
| UniProt | Golgi apparatus, Cytoplasm, cytoskeleton, Cytoplasm, Nucleus envelope | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- annulate lamellae (GO:0005642)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nuclear envelope (GO:0005635)
- nuclear pore (GO:0005643)
- plasma membrane (GO:0005886)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 824 aa，蛋白偏大（> 800 aa），表达纯化有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 116 |
| PubMed broad count | 199 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0699 |

**关键文献**:
1. Distal hereditary motor neuropathies.. *Revue neurologique*. PMID: 38702287
2. Structure, Function, and Interactions of the HIV-1 Capsid Protein.. *Life (Basel, Switzerland)*. PMID: 33572761
3. Bicaudal D2 autoantibodies are highly specific for systemic sclerosis.. *Scandinavian journal of rheumatology*. PMID: 38913821
4. Role of Nesprin-2 and RanBP2 in BICD2-associated brain developmental disorders.. *PLoS genetics*. PMID: 36930595
5. Clinical spectrum of BICD2 mutations.. *European journal of neurology*. PMID: 32056343


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 50.1% |
| 置信残基 (pLDDT 70-90) 占比 | 21.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 20.1% |
| 有序区域 (pLDDT>70) 占比 | 71.9% |
| 可用 PDB 条目 | 6OFP, 6PSE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=78.0），结构可信度高。三维结构评分 9/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018477; Pfam: PF09730 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYNC1H1 | 0.999 | 0.994 | -- |
| DCTN2 | 0.999 | 0.994 | -- |
| DYNC1LI1 | 0.999 | 0.999 | -- |
| DCTN1 | 0.998 | 0.994 | -- |
| DYNC1I1 | 0.997 | 0.994 | -- |
| RANBP2 | 0.995 | 0.353 | -- |
| RAB6A | 0.991 | 0.721 | -- |
| NEK9 | 0.924 | 0.413 | -- |
| RGPD2 | 0.895 | 0.042 | -- |
| HOOK3 | 0.884 | 0.288 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORF | anti tag coimmunoprecipitation | imex:IM-17346|pubmed:22190034|psi-mi:"MI:0007" |
| PLK1 | anti tag coimmunoprecipitation | imex:IM-12200|pubmed:19596235 |
| ZRANB1 | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| Ranbp2 | tandem affinity purification | imex:IM-11719|pubmed:20360068 |
| Plk1 | tandem affinity purification | imex:IM-11719|pubmed:20360068 |
| deoR | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| spoT | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| Rgs1 | two hybrid | pubmed:15102471 |
| LRRK2 | anti tag coimmunoprecipitation | pubmed:31046837|imex:IM-26684 |
| NEK9 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 6OFP, 6PSE | pLDDT=78.0, v6 | 预测+实验 |
| 定位 | UniProt | Nucleus envelope, Nucleus, nuclear pore complex | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +2.0 / max +3

### 4. 总体评价

**归一化总分**: 50.3/100
**状态**: REJECTED -- PubMed strict count 116 > 100

**核心优势**:
1. AlphaFold高质量预测（pLDDT=78.0），结构可信度高。
2. 已有PDB实验结构：6OFP, 6PSE。
3. 存在 2 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8TD16
- Protein Atlas: https://www.proteinatlas.org/search/BICD2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BICD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TD16
- STRING: https://string-db.org/network/9606.BICD2
- Packet data timestamp: 2026-06-03 03:36:34

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TD16-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TD16 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018477; |
| Pfam | PF09730; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185963-BICD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNC1I1 | Intact, Biogrid | true |
| MAPRE1 | Biogrid, Opencell | true |
| RAB6A | Intact, Biogrid | true |
| ACTR1A | Biogrid | false |
| ALK | Biogrid | false |
| BICD1 | Biogrid | false |
| BORCS6 | Biogrid | false |
| CBR3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
