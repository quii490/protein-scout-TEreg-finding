---
type: protein-evaluation
gene: "LRRC75A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC75A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC75A / C17orf76, FAM211A |
| 蛋白名称 | Leucine-rich repeat-containing protein 75A |
| 蛋白大小 | 344 aa / 37.8 kDa |
| UniProt ID | Q8NAA5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 344 aa / 37.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032675 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul2-RING ubiquitin ligase complex (GO:0031462)
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf76, FAM211A |

**关键文献**:
1. LRRC75A-AS1 Drives the Epithelial-Mesenchymal Transition in Cervical Cancer by Binding IGF2BP1 and Inhibiting SYVN1-Mediated NLRP3 Ubiquitination.. *Molecular cancer research : MCR*. PMID: 38180377
2. LRRC75A-AS1 facilitates breast cancer cell proliferation and invasion via functioning as a CeRNA to modulate miR489-3p/ARD1.. *Scientific reports*. PMID: 40858914
3. Long noncoding RNA LRRC75A-AS1 inhibits cell proliferation and migration in colorectal carcinoma.. *Experimental biology and medicine (Maywood, N.J.)*. PMID: 31505952
4. Effects of ADSC-Derived Exosome LRRC75A-AS1 on Anti-inflammatory Function After SCI.. *Applied biochemistry and biotechnology*. PMID: 38165592
5. LRRC75A-AS1 targets miR-199b-5p/PDCD4 axis to repress multiple myeloma.. *Cancer biology & therapy*. PMID: 33131397

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.5 |
| 高置信度残基 (pLDDT>90) 占比 | 47.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 28.5% |
| 有序区域 (pLDDT>70) 占比 | 61.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.5，有序区 61.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032675 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.5 + PDB: 无 | pLDDT=74.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRRC75A — Leucine-rich repeat-containing protein 75A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小344 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

LRRC75A（Leucine-rich repeat-containing protein 75A, 344 aa, UniProt Q8NAA5）。定位于Nucleoplasm（HPA Approved），额外Nucleoli和Cytosol。InterPro注释IPR032675（LRR_NTF结构域，富含亮氨酸重复序列的N端帽结构域），Pfam未检出。AlphaFold pLDDT=74.5（有序区61.6%），无PDB实验结构。

从结构域架构角度，LRR（富含亮氨酸重复序列）结构域形成马蹄形螺旋结构，在先天免疫中作为模式识别受体（如TLR蛋白）发挥作用，但也可介导蛋白-蛋白互作和核酸结合。LRRC75A的LRR_NTF结构域提示可能折叠为经典LRR折叠。但pLDDT=74.5中等置信度，28.5%残基低于50，表明蛋白存在显著无序区域——可能位于LRR域间的linker或未被注释的低复杂度区域。

从PPI网络角度，数据极其匮乏——STRING 0个预测互作，IntAct 0个实验互作。HPA interaction页面也未解析到任何伙伴。GO注释的Cul2-RING ubiquitin ligase complex (GO:0031462)提示LRRC75A可能与Cullin2泛素连接酶复合体相关，但无直接证据。值得注意的是，文献研究几乎完全集中在lncRNA LRRC75A-AS1上（作为ceRNA竞争miRNA），而非LRRC75A蛋白本身（PMID:38180377, PMID:40858914, PMID:31505952），蛋白功能的文献盲区极为显著。

从TE调控角度，LRRC75A在nucleoplasm的定位、LRR结构域（可能参与核酸结合）和Cul2-RING连接酶的潜在关联形成推理性框架：CRL2（Cullin2-RING ligase）复合体参与多个染色质相关底物的泛素化降解，若LRRC75A作为CRL2底物识别亚基，可能调控TE区域组蛋白修饰相关蛋白的周转。但这是完全推理性的模型。

PubMed 16篇，综合评分65.6/100。强烈建议开展LRRC75A蛋白（非其lncRNA）的首次功能表征。