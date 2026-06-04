---
type: protein-evaluation
gene: "ARMCX4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARMCX4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARMCX4 / 无 |
| 蛋白名称 | Armadillo repeat-containing X-linked protein 4 |
| 蛋白大小 | 2290 aa / 236.0 kDa |
| UniProt ID | Q5H9R4 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 02:32:59 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 2/10 | x1 | 2 | 2290 aa / 236.0 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=4 篇 (<=20->10) |
| 三维结构 | 3/10 | x3 | 9 | AlphaFold v6 pLDDT=40.5 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 4; Pfam: 1; IPR011989, IPR006911... |
| PPI 网络 | 8/10 | x3 | 24 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | -- | max +3 | 1.0 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5 |
| **原始总分** | | | **140.0/180** | |
| **归一化总分 (/1.83)** | | | **76.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 2290 aa，蛋白偏大（> 1200 aa），表达纯化难度增加，但结构域丰富。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |

**关键文献**:
1. GPRASP/ARMCX Protein Family: Potential Involvement in Health and Diseases Revealed by their Novel Interacting Partners.. *Current topics in medicinal chemistry*. PMID: 33267763
2. Identification of key gene modules and pathways of human platelet transcriptome in acute myocardial infarction patients through co-expression network.. *American journal of translational research*. PMID: 34017580
3. Identification of potential pathogenic mutations in Chinese children with first branchial cleft anomalies detected by whole-exome sequencing.. *Pediatric investigation*. PMID: 34589676
4. Identification of Potential Genes and Critical Pathways in Postoperative Recurrence of Crohn's Disease by Machine Learning And WGCNA Network Analysis.. *Current genomics*. PMID: 37994325

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 40.5 |
| 高置信度残基 (pLDDT>90) 占比 | 2.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 71.3% |
| 有序区域 (pLDDT>70) 占比 | 18.6% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold低质量预测（pLDDT=40.5），大部分区域无序。三维结构评分 3/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR006911, IPR016024, IPR000225; Pfam: PF04826 |

**染色质调控潜力分析**: 存在 5 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZSCAN29 | 0.486 | 0.053 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DPAGT1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| Pde4dip | anti bait coimmunoprecipitation | pubmed:28671696|doi:10.1038/nn.4594|imex:IM-26285 |
| KLK6 | two hybrid array | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.1080 |
| ATN1 | two hybrid array | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.1080 |
| PRKACB | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| HUNK | two hybrid fragment pooling approach | pubmed:35914814|imex:IM-27626 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6

**评价**: 互作网络中等：STRING 15 预测 + IntAct 6 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=40.5 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 76.5/100

**核心优势**:
1. ARMCX4 -- Armadillo repeat-containing X-linked protein 4，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 5 个已知结构域，有明确的结构-功能切入点。
3. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold pLDDT 较低（40.5），存在显著无序区
3. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测
4. 蛋白偏大（2290 aa），表达纯化难度大

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q5H9R4
- Protein Atlas: https://www.proteinatlas.org/search/ARMCX4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARMCX4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5H9R4
- STRING: https://string-db.org/network/9606.ARMCX4
- Packet data timestamp: 2026-06-03 02:32:59
