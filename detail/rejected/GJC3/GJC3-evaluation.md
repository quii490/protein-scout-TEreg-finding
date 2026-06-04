---
type: protein-evaluation
gene: "GJC3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJC3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJC3 / GJE1 |
| 蛋白名称 | Gap junction gamma-3 protein |
| 蛋白大小 | 279 aa / 31.3 kDa |
| UniProt ID | Q8NFK1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 279 aa / 31.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.8; PDB: 6L3T, 6L3U, 6L3V |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000500, IPR019570, IPR017990, IPR013092, IPR038 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell junction, gap junction | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- connexin complex (GO:0005922)
- myelin sheath (GO:0043209)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GJE1 |

**关键文献**:
1. GJB4 and GJC3 variants in non-syndromic hearing impairment in Ghana.. *Experimental biology and medicine (Maywood, N.J.)*. PMID: 32524838
2. Exploring Differential Connexin Expression across Melanocytic Tumor Progression Involving the Tumor Microenvironment.. *Cancers*. PMID: 30717194
3. Conservation and divergence of myelin proteome and oligodendrocyte transcriptome profiles between humans and mice.. *eLife*. PMID: 35543322
4. Prospective variants screening of connexin genes in children with hearing impairment: genotype/phenotype correlation.. *Human genetics*. PMID: 20593197
5. Mechanism of two novel human GJC3 missense mutations in causing non-syndromic hearing loss.. *Cell biochemistry and biophysics*. PMID: 23179405

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.8 |
| 高置信度残基 (pLDDT>90) 占比 | 44.8% |
| 置信残基 (pLDDT 70-90) 占比 | 19.4% |
| 中等置信 (pLDDT 50-70) 占比 | 20.4% |
| 低置信 (pLDDT<50) 占比 | 15.4% |
| 有序区域 (pLDDT>70) 占比 | 64.2% |
| 可用 PDB 条目 | 6L3T, 6L3U, 6L3V |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6L3T, 6L3U, 6L3V）+ AlphaFold高质量预测（pLDDT=75.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR019570, IPR017990, IPR013092, IPR038359; Pfam: PF00029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KCNA2 | 0.827 | 0.000 | — |
| AP1S1 | 0.788 | 0.000 | — |
| GJC1 | 0.672 | 0.000 | — |
| GJA5 | 0.662 | 0.000 | — |
| GJB1 | 0.530 | 0.000 | — |
| GJC2 | 0.516 | 0.000 | — |
| GJB3 | 0.497 | 0.000 | — |
| GJB5 | 0.486 | 0.000 | — |
| GJB4 | 0.483 | 0.000 | — |
| GJE1 | 0.479 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STX7 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MS4A13 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.8 + PDB: 6L3T, 6L3U, 6L3V | pLDDT=75.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GJC3 — Gap junction gamma-3 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小279 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFK1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176402-GJC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFK1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
