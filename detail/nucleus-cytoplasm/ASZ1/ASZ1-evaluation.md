---
type: protein-evaluation
gene: "ASZ1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASZ1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASZ1 / ALP1, ANKL1, C7orf7, GASZ |
| 蛋白名称 | Ankyrin repeat, SAM and basic leucine zipper domain-containing protein 1 |
| 蛋白大小 | 475 aa / 53.5 kDa |
| UniProt ID | Q8WWH4 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:24:52 |

**IF 图像**:
![](https://images.proteinatlas.org/20558/234_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20558/234_H6_2_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 475 aa / 53.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=18 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=67.2 |
| 调控结构域 | 10/10 | x2 | 20 | InterPro: 5; Pfam: 3; IPR002110, IPR036770... |
| PPI 网络 | 8/10 | x3 | 24 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **142.5/180** | |
| **归一化总分 (/1.83)** | | | **77.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- pi-body (GO:0071546)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 475 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALP1, ANKL1, C7orf7, GASZ |

**关键文献**:
1. Toward clinical exomes in diagnostics and management of male infertility.. *American journal of human genetics*. PMID: 38614076
2. PIWI proteins tether the piRNA biogenesis machinery to mitochondria during mammalian spermatogenesis.. *The EMBO journal*. PMID: 41023308
3. DNA methylation patterns in patients with asthenospermia and oligoasthenospermia.. *BMC genomics*. PMID: 38886667
4. Spatiotemporal control of PIWI compartmentalization by mitochondrial scaffolds defines pachytene piRNA pathway organization.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 42118831
5. Novel regulatory mechanisms for the CFTR gene.. *Biochemical Society transactions*. PMID: 19614605

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.2 |
| 高置信度残基 (pLDDT>90) 占比 | 32.4% |
| 置信残基 (pLDDT 70-90) 占比 | 16.6% |
| 中等置信 (pLDDT 50-70) 占比 | 16.8% |
| 低置信 (pLDDT<50) 占比 | 34.1% |
| 有序区域 (pLDDT>70) 占比 | 49.0% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=67.2），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR042650, IPR001660, IPR013761; Pfam: PF00023, PF12796, PF07647 |

**染色质调控潜力分析**: 存在 8 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAEL | 0.797 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NRAC | two hybrid array | pubmed:32296183|imex:IM-25472 |
| SMIM1 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| BET1 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| TMEM97 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| DEFB127 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| SLC35A1 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| TMEM218 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| TSPO2 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| LPAR3 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| TNFRSF10C | validated two hybrid | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11

**评价**: 互作网络中等：STRING 15 预测 + IntAct 11 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=67.2 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 77.9/100

**核心优势**:
1. ASZ1 -- Ankyrin repeat, SAM and basic leucine zipper domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小475 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 8 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8WWH4
- Protein Atlas: https://www.proteinatlas.org/search/ASZ1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASZ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WWH4
- STRING: https://string-db.org/network/9606.ASZ1
- Packet data timestamp: 2026-06-03 03:24:52

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WWH4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
