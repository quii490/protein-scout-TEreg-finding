---
type: protein-evaluation
gene: "KATNBL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KATNBL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KATNBL1 / C15orf29 |
| 蛋白名称 | KATNB1-like protein 1 |
| 蛋白大小 | 304 aa / 34.8 kDa |
| UniProt ID | Q9H079 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Midbody, Mitotic spindle; 额外: Nucleoplasm, Cleavage furrow; UniProt: Nucleus; Cytoplasm, cytoskeleton, spindle pole |
| 蛋白大小 | 10/10 | ×1 | 10 | 304 aa / 34.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028021, IPR042404; Pfam: PF13925 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Midbody, Mitotic spindle; 额外: Nucleoplasm, Cleavage furrow | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, spindle pole | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cleavage furrow (GO:0032154)
- katanin complex (GO:0008352)
- microtubule cytoskeleton (GO:0015630)
- midbody (GO:0030496)
- mitotic spindle (GO:0072686)
- mitotic spindle pole (GO:0097431)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf29 |

**关键文献**:
1. Proteomic Analysis of the Mammalian Katanin Family of Microtubule-severing Enzymes Defines Katanin p80 subunit B-like 1 (KATNBL1) as a Regulator of Mammalian Katanin Microtubule-severing.. *Molecular & cellular proteomics : MCP*. PMID: 26929214

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.1 |
| 高置信度残基 (pLDDT>90) 占比 | 45.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 40.1% |
| 有序区域 (pLDDT>70) 占比 | 52.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.1，有序区 52.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028021, IPR042404; Pfam: PF13925 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KATNA1 | 0.979 | 0.834 | — |
| KATNB1 | 0.964 | 0.831 | — |
| KATNAL1 | 0.954 | 0.780 | — |
| KATNAL2 | 0.631 | 0.000 | — |
| CCDC58 | 0.572 | 0.000 | — |
| ZZEF1 | 0.531 | 0.000 | — |
| ZNF805 | 0.509 | 0.000 | — |
| TIMM21 | 0.501 | 0.000 | — |
| NCAPD3 | 0.487 | 0.000 | — |
| WDR62 | 0.482 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000256544.3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| HAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KAT7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CA12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KATNAL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |
| TUBB4B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |
| TUBB2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |
| TUBB4A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |
| TUBB8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |
| TUBB6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.1 + PDB: 无 | pLDDT=70.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, spindle pole / Midbody, Mitotic spindle; 额外: Nucleoplasm, Cleavag | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KATNBL1 — KATNB1-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小304 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H079
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134152-KATNBL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KATNBL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H079
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
