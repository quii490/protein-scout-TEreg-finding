---
type: protein-evaluation
gene: "BEGAIN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BEGAIN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BEGAIN / KIAA1446 |
| 蛋白名称 | Brain-enriched guanylate kinase-associated protein |
| 蛋白大小 | 593 aa / 64.8 kDa |
| UniProt ID | Q9BUH8 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:33:49 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | x4 | 24 | HPA: Nucleoplasm; UniProt: Cytoplasm,... |
| 蛋白大小 | 10/10 | x1 | 10 | 593 aa / 64.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=19 篇 (<=20->10) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=55.9 |
| 调控结构域 | 3/10 | x2 | 6 | InterPro: 1; Pfam: 0; IPR043441 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **136.5/180** | |
| **归一化总分 (/1.83)** | | | **74.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Golgi apparatus, Cytosol | Approved |
| UniProt | Cytoplasm, Membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- postsynapse (GO:0098794)
- synapse (GO:0045202)

**结论**: 核定位证据较好，主要数据源支持核定位，但存在一定程度的其它亚细胞定位信号。

#### 3.2 蛋白大小评估

**评价**: 593 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1446 |

**关键文献**:
1. Effects of paternal and chronological age on BEGAIN methylation and its possible role in autism.. *Aging*. PMID: 38019471
2. Involvement of N4BP2L1, PLEKHA4, and BEGAIN genes in breast cancer and muscle cell development.. *Frontiers in cell and developmental biology*. PMID: 38859961
3. BEGAIN: a novel imprinted gene that generates paternally expressed transcripts in a tissue- and promoter-specific manner in sheep.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 16261422
4. Brain-enriched guanylate kinase-associated protein, a component of the post-synaptic density protein complexes, contributes to learning and memory.. *Scientific reports*. PMID: 38086879
5. Identification of Long Non-Coding RNA as Potential Biomarkers for the Diagnosis of Postmenopausal Osteoporosis.. *International journal of endocrinology*. PMID: 39619600

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.9 |
| 高置信度残基 (pLDDT>90) 占比 | 20.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.3% |
| 低置信 (pLDDT<50) 占比 | 61.7% |
| 有序区域 (pLDDT>70) 占比 | 26.0% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold低质量预测（pLDDT=55.9），大部分区域无序。三维结构评分 5/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043441; Pfam: 无 |

**染色质调控潜力分析**: 存在 1 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RTL1 | 0.602 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DTNB | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| FAM107A | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ZFP64 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| USP2 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ZNF417 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ABLIM1 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| BAHD1 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| DEF6 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ZNF250 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| CATSPER1 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=55.9 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 74.6/100

**核心优势**:
1. BEGAIN -- Brain-enriched guanylate kinase-associated protein，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小593 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 1 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. AlphaFold pLDDT 较低（55.9），存在显著无序区
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9BUH8
- Protein Atlas: https://www.proteinatlas.org/search/BEGAIN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BEGAIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BUH8
- STRING: https://string-db.org/network/9606.BEGAIN
- Packet data timestamp: 2026-06-03 03:33:49

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000183092-BEGAIN/subcellular

![](https://images.proteinatlas.org/2899/1054_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/2899/1054_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/2899/1_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/2899/1_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/2899/3_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/2899/3_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BUH8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
