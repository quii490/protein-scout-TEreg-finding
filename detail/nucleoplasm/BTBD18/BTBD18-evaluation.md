---
type: protein-evaluation
gene: "BTBD18"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BTBD18 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTBD18 |
| 蛋白名称 | BTB/POZ domain-containing protein 18 |
| 蛋白大小 | 712 aa / 77.9 kDa |
| UniProt ID | B2RXH4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; 额外: Vesicles; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 712 aa / 77.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.3; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000210, IPR042915, IPR011333; Pfam: PF00651 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 1 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Testing Rare-Variant Association without Calling Genotypes Allows for Systematic Differences in Sequencing between Cases and Controls.. *PLoS genetics*. PMID: 27152526
2. BTBD18: A novel MLL partner gene in an infant with acute lymphoblastic leukemia and inv(11)(q13;q23).. *Leukemia research*. PMID: 20598370
3. BTBD18 Regulates a Subset of piRNA-Generating Loci through Transcription Elongation in Mice.. *Developmental cell*. PMID: 28292424
4. Sperm acrosome overgrowth and infertility in mice lacking chromosome 18 pachytene piRNA.. *PLoS genetics*. PMID: 33831001

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.3 |
| 高置信度残基 (pLDDT>90) 占比 | 15.4% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 73.9% |
| 有序区域 (pLDDT>70) 占比 | 18.5% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=49.3），有序残基占 18.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000210, IPR042915, IPR011333; Pfam: PF00651 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TDRD1 | 0.462 | 0.000 | — |
| NUP210L | 0.426 | 0.000 | — |
| SPDYC | 0.415 | 0.000 | — |
| AGFG1 | 0.413 | 0.000 | — |
| ADCY10 | 0.412 | 0.094 | — |
| CCDC155 | 0.405 | 0.094 | — |
| DDX50 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NXF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 1
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.3 + PDB: 无 | pLDDT=49.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Plasma membrane; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 7 + 1 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. BTBD18 — BTB/POZ domain-containing protein 18，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小712 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B2RXH4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000233436-BTBD18/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTBD18
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B2RXH4
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:17:49
