---
type: protein-evaluation
gene: "PHF13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHF13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHF13 |
| 蛋白名称 | PHD finger protein 13 |
| 蛋白大小 | 300 aa / 33.6 kDa |
| UniProt ID | Q86YI8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 300 aa / 33.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 3O70, 3O7A |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041947, IPR011011, IPR001965, IPR013083; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.5/180** | |
| **归一化总分** | | | **74.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic links between multimorbidity and human aging.. *GeroScience*. PMID: 41405793
2. Differential oligomerization regulates PHF13 chromatin affinity and function.. *Nucleic acids research*. PMID: 40598901
3. PHF13 epigenetically activates TGFβ driven epithelial to mesenchymal transition.. *Cell death & disease*. PMID: 35597793
4. PHF13 is a molecular reader and transcriptional co-regulator of H3K4me2/3.. *eLife*. PMID: 27223324
5. Dual role of the chromatin-binding factor PHF13 in the pre- and post-integration phases of HIV-1 replication.. *Open biology*. PMID: 29021215

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 21.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 36.7% |
| 低置信 (pLDDT<50) 占比 | 29.3% |
| 有序区域 (pLDDT>70) 占比 | 34.0% |
| 可用 PDB 条目 | 3O70, 3O7A |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 34.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041947, IPR011011, IPR001965, IPR013083; Pfam: PF20826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNASE1L2 | 0.824 | 0.822 | — |
| TBX20 | 0.814 | 0.814 | — |
| PHF1 | 0.681 | 0.000 | — |
| SIN3A | 0.632 | 0.582 | — |
| BLVRA | 0.607 | 0.607 | — |
| PHF21B | 0.586 | 0.448 | — |
| TRIM28 | 0.543 | 0.073 | — |
| ATM | 0.542 | 0.000 | — |
| PPIE | 0.519 | 0.494 | — |
| CDK5 | 0.499 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CPTP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| DNASE1L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TBX20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPIE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BLVRA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000377648 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 3O70, 3O7A | pLDDT=64.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PHF13 — PHD finger protein 13，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小300 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86YI8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116273-PHF13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHF13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86YI8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86YI8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
