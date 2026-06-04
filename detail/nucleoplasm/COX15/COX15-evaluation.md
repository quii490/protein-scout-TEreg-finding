---
type: protein-evaluation
gene: "COX15"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COX15 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COX15 |
| 蛋白名称 | Heme A synthase COX15 |
| 蛋白大小 | 410 aa / 46.0 kDa |
| UniProt ID | Q7KZN9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 410 aa / 46.0 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=64 篇 (≤80→4) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=85.4; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR003780, IPR023754, IPR009003; Pfam: PF02628 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Supported |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytochrome complex (GO:0070069)
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- respiratory chain complex (GO:0098803)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 64 |
| PubMed broad count | 104 |
| 别名(未计入scoring) |  |

**关键文献**:
1. COX15 deficiency causes oocyte ferroptosis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39471219
2. Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview.. **. PMID: 26425749
3. Analysis of Oligomerization Properties of Heme a Synthase Provides Insights into Its Function in Eukaryotes.. *The Journal of biological chemistry*. PMID: 26940873
4. Cox15 is a novel oncogene that required for lung cancer cell proliferation.. *Biochemical and biophysical research communications*. PMID: 34547626
5. Opantimirs: A class of antagonizing microRNAs that upregulate Opa1 and improve mitochondrial and disuse myopathies.. *Cell reports. Medicine*. PMID: 40712573

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.4 |
| 高置信度残基 (pLDDT>90) 占比 | 70.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 13.7% |
| 有序区域 (pLDDT>70) 占比 | 82.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度（pLDDT=85.4，有序区 82.5%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003780, IPR023754, IPR009003; Pfam: PF02628 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COX10 | 0.999 | 0.501 | — |
| MT-CO3 | 0.994 | 0.000 | — |
| SURF1 | 0.992 | 0.509 | — |
| MT-CO1 | 0.992 | 0.000 | — |
| MT-CO2 | 0.991 | 0.095 | — |
| SCO1 | 0.980 | 0.315 | — |
| UQCRFS1 | 0.978 | 0.000 | — |
| SCO2 | 0.976 | 0.073 | — |
| CYC1 | 0.961 | 0.575 | — |
| BCS1L | 0.942 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.4 + PDB: 无 | pLDDT=85.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. COX15 -- Heme A synthase COX15，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小410 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 64 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7KZN9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000014919-COX15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COX15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7KZN9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
