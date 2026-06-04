---
type: protein-evaluation
gene: "ARL6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARL6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARL6 / BBS3 |
| 蛋白名称 | ADP-ribosylation factor-like protein 6 |
| 蛋白大小 | 186 aa / 21.1 kDa |
| UniProt ID | Q9H0F7 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 02:32:09 |

**IF 图像**:
![](https://images.proteinatlas.org/19361/154_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19361/154_H6_2_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | HPA: Microtubules, Primary cilium; Un... |
| 蛋白大小 | 7/10 | x1 | 7 | 186 aa / 21.1 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=54 篇 (41-60->6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=94.7; PDB: 2H57 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: 5; Pfam: 1; IPR041839, IPR027417... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **135.0/180** | |
| **归一化总分 (/1.83)** | | | **73.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Nucleoplasm, Microtubules, Primary cilium, Primary cilium tip, Cytosol | Approved |
| UniProt | Cell projection, cilium membrane, Cytoplasm, cytoskeleton, cilium axoneme, Cytoplasm, cytoskeleton, cilium basal body | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- axonemal microtubule (GO:0005879)
- axoneme (GO:0005930)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- membrane coat (GO:0030117)
- microtubule cytoskeleton (GO:0015630)
- nucleoplasm (GO:0005654)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 186 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 85 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BBS3 |

**关键文献**:
1. Nonsyndromic Retinitis Pigmentosa Overview.. **. PMID: 20301590
2. Bardet-Biedl Syndrome Overview.. **. PMID: 20301537
3. Characterization, chromosomal localization, and expression during hematopoietic differentiation of the gene encoding Arl6ip, ADP-ribosylation-like factor-6 interacting protein (ARL6).. *Genomics*. PMID: 10995579
4. BBS1 is involved in retrograde trafficking of ciliary GPCRs in the context of the BBSome complex.. *PloS one*. PMID: 29590217
5. Novel homozygous mutations in the genes ARL6 and BBS10 underlying Bardet-Biedl syndrome.. *Gene*. PMID: 23219996

**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.7 |
| 高置信度残基 (pLDDT>90) 占比 | 87.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 95.1% |
| 可用 PDB 条目 | 2H57 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=94.7），结构可信度高。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041839, IPR027417, IPR005225, IPR024156, IPR006689; Pfam: PF00025 |

**染色质调控潜力分析**: 存在 6 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LZTFL1 | 0.676 | 0.102 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BBS4 | pull down | imex:IM-14958|pubmed:20603001 |
| BBS2 | pull down | imex:IM-14958|pubmed:20603001 |
| BBS5 | pull down | imex:IM-14958|pubmed:20603001 |
| ENSP00000419619.1 | pull down | imex:IM-14958|pubmed:20603001 |
| TTC8 | pull down | imex:IM-14958|pubmed:20603001 |
| BBS9 | pull down | imex:IM-14958|pubmed:20603001 |
| BBS7 | pull down | imex:IM-14958|pubmed:20603001 |
| BBS1 | pull down | imex:IM-14958|pubmed:20603001 |
| ACTL7B | pull down | imex:IM-14958|pubmed:20603001 |
| BBIP1 | fluorescence microscopy | imex:IM-14958|pubmed:20603001 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.7 + PDB: 2H57 | pLDDT=94.7, v6 | 预测+实验 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +2.0 / max +3

### 4. 总体评价

**归一化总分**: 73.8/100

**核心优势**:
1. AlphaFold高质量预测（pLDDT=94.7），结构可信度高。
2. 已有PDB实验结构：2H57。
3. 存在 6 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 5/10），需IF实验验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9H0F7
- Protein Atlas: https://www.proteinatlas.org/search/ARL6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARL6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0F7
- STRING: https://string-db.org/network/9606.ARL6
- Packet data timestamp: 2026-06-03 02:32:09
